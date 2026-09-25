#!/usr/bin/env node
// Servidor MCP mínimo (stdio, sem dependências) que expõe a Obsidian CLI em modo leitura.
// Roda no Windows, ao lado do app do Obsidian. O app do Claude repassa estas ferramentas às sessões.
// Config: OBSIDIAN_BIN (caminho do Obsidian.com), OBSIDIAN_VAULT (cofre padrão, opcional).
"use strict";
const { execFile } = require("child_process");
const readline = require("readline");

const BIN = process.env.OBSIDIAN_BIN || (process.platform === "win32" ? "Obsidian.com" : "obsidian");
const VAULT = process.env.OBSIDIAN_VAULT || "";
const VERSAO = "1.0.0";

const vaultProp = { type: "string", description: 'Nome do cofre no Obsidian (ex.: "stonebid-vault" ou "Vault").' };
const TOOLS = [
  {
    name: "obsidian_search",
    description: "Busca no cofre pelo índice do Obsidian (acha por texto; use sinônimos e termos em inglês). Equivale a `obsidian search`.",
    inputSchema: {
      type: "object",
      properties: {
        vault: vaultProp,
        query: { type: "string", description: "Termo de busca." },
        limit: { type: "integer", description: "Máximo de resultados (padrão 10)." },
        path: { type: "string", description: "Limitar a uma pasta do cofre." },
        context: { type: "boolean", description: "true: devolve as linhas onde o termo aparece (search:context)." },
      },
      required: ["query"],
    },
  },
  {
    name: "obsidian_read",
    description: "Lê uma nota do cofre pelo nome (file) ou pelo caminho (path). Equivale a `obsidian read`.",
    inputSchema: {
      type: "object",
      properties: {
        vault: vaultProp,
        file: { type: "string", description: "Nome da nota, sem .md (resolve como wikilink)." },
        path: { type: "string", description: "Caminho a partir da raiz do cofre, com .md." },
      },
    },
  },
  {
    name: "obsidian_backlinks",
    description: "Lista as notas que apontam para uma nota. Equivale a `obsidian backlinks`.",
    inputSchema: {
      type: "object",
      properties: {
        vault: vaultProp,
        file: { type: "string", description: "Nome da nota, sem .md." },
        path: { type: "string", description: "Caminho a partir da raiz do cofre." },
      },
    },
  },
  {
    name: "obsidian_help",
    description: "Mostra a ajuda da Obsidian CLI (lista de comandos). Equivale a `obsidian help`.",
    inputSchema: { type: "object", properties: {} },
  },
];

function argsFor(name, a) {
  const out = [];
  const vault = a.vault || VAULT;
  if (vault && name !== "obsidian_help") out.push(`vault=${vault}`);
  const kv = (k) => { if (a[k] !== undefined && a[k] !== null && a[k] !== "") out.push(`${k}=${a[k]}`); };
  switch (name) {
    case "obsidian_search":
      if (!a.query) throw new Error("query é obrigatório");
      out.push(a.context ? "search:context" : "search");
      kv("query"); out.push(`limit=${a.limit || 10}`); kv("path");
      break;
    case "obsidian_read":
    case "obsidian_backlinks":
      if (!a.file && !a.path) throw new Error("informe file ou path");
      out.push(name === "obsidian_read" ? "read" : "backlinks");
      kv("file"); kv("path");
      break;
    case "obsidian_help":
      out.push("help");
      break;
    default:
      throw new Error(`ferramenta desconhecida: ${name}`);
  }
  return out;
}

function run(args) {
  return new Promise((resolve) => {
    execFile(BIN, args, { timeout: 30000, windowsHide: true, maxBuffer: 10 * 1024 * 1024, encoding: "utf8" },
      (err, stdout, stderr) => {
        const txt = [stdout, stderr].filter((s) => s && s.trim()).join("\n").trim();
        if (err) resolve({ ok: false, text: `Falha ao rodar "${BIN} ${args.join(" ")}": ${err.message}\n${txt}`.trim() });
        else resolve({ ok: true, text: txt || "(sem resultado)" });
      });
  });
}

function send(msg) { process.stdout.write(JSON.stringify(msg) + "\n"); }
const reply = (id, result) => send({ jsonrpc: "2.0", id, result });
const fail = (id, code, message) => send({ jsonrpc: "2.0", id, error: { code, message } });

async function handle(m) {
  const { id, method, params } = m;
  if (id === undefined || id === null) return; // notificação
  try {
    if (method === "initialize") {
      return reply(id, {
        protocolVersion: (params && params.protocolVersion) || "2025-06-18",
        capabilities: { tools: {} },
        serverInfo: { name: "obsidian-cli", version: VERSAO },
      });
    }
    if (method === "ping") return reply(id, {});
    if (method === "tools/list") return reply(id, { tools: TOOLS });
    if (method === "tools/call") {
      const name = params && params.name;
      let args;
      try { args = argsFor(name, (params && params.arguments) || {}); }
      catch (e) { return reply(id, { content: [{ type: "text", text: e.message }], isError: true }); }
      const r = await run(args);
      return reply(id, { content: [{ type: "text", text: r.text }], isError: !r.ok });
    }
    return fail(id, -32601, `método não suportado: ${method}`);
  } catch (e) {
    return fail(id, -32603, String(e && e.message || e));
  }
}

readline.createInterface({ input: process.stdin }).on("line", (line) => {
  if (!line.trim()) return;
  let m;
  try { m = JSON.parse(line); } catch { return fail(null, -32700, "JSON inválido"); }
  handle(m);
});
