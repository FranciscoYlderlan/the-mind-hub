#!/usr/bin/env node
// Servidor MCP mínimo (sem dependências) que expõe a Obsidian CLI em modo leitura.
// Roda no Windows, ao lado do app do Obsidian. O app do Claude repassa estas ferramentas às sessões.
// Transportes:
//   - stdio (padrão, como o Claude desktop o inicia): uma mensagem JSON-RPC por linha.
//   - HTTP local (Streamable HTTP do MCP), com `--http`: só em 127.0.0.1, em POST /mcp.
//     Porta: `--port=N`, ou OBSIDIAN_MCP_PORT, ou 27180.
// Config: OBSIDIAN_BIN (caminho do Obsidian.com), OBSIDIAN_VAULT (cofre padrão, opcional).
"use strict";
const { execFile } = require("child_process");
const readline = require("readline");
const http = require("http");
const crypto = require("crypto");

const BIN = process.env.OBSIDIAN_BIN || (process.platform === "win32" ? "Obsidian.com" : "obsidian");
const VAULT = process.env.OBSIDIAN_VAULT || "";
const VERSAO = "1.1.0";
const PORTA_PADRAO = 27180;

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
    name: "obsidian_files",
    description: "Lista os arquivos do cofre ou, com total: true, devolve só a contagem. Equivale a `obsidian files` (ex.: ext: \"md\", total: true → número de notas).",
    inputSchema: {
      type: "object",
      properties: {
        vault: vaultProp,
        folder: { type: "string", description: "Limitar a uma pasta do cofre." },
        ext: { type: "string", description: 'Filtrar por extensão (ex.: "md").' },
        total: { type: "boolean", description: "true: devolve só o número de arquivos." },
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
    case "obsidian_files":
      out.push("files");
      kv("folder"); kv("ext");
      if (a.total === true) out.push("total");
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

// Resposta JSON-RPC de uma mensagem (ou null para notificação); o transporte a entrega.
const reply = (id, result) => ({ jsonrpc: "2.0", id, result });
const fail = (id, code, message) => ({ jsonrpc: "2.0", id, error: { code, message } });

async function handle(m) {
  const { id, method, params } = m || {};
  if (id === undefined || id === null) return null; // notificação
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

// ---- Transporte stdio (o de sempre) ----
function iniciarStdio() {
  const send = (msg) => { if (msg) process.stdout.write(JSON.stringify(msg) + "\n"); };
  readline.createInterface({ input: process.stdin }).on("line", (line) => {
    if (!line.trim()) return;
    let m;
    try { m = JSON.parse(line); } catch { return send(fail(null, -32700, "JSON inválido")); }
    handle(m).then(send);
  });
}

// ---- Transporte HTTP local (Streamable HTTP do MCP, respostas em JSON, sem fluxo SSE) ----
const LIMITE_CORPO = 1024 * 1024;
const HOSTS_ACEITOS = new Set(["127.0.0.1", "localhost", "[::1]", "host.docker.internal"]);
const sessoes = new Set();

function hostDe(valor) {
  if (!valor) return "";
  const v = String(valor).toLowerCase();
  if (v.startsWith("[")) return v.slice(0, v.indexOf("]") + 1);
  return v.split(":")[0];
}

function origemLocal(origin) {
  if (!origin) return true; // cliente fora do navegador não manda Origin
  try { return HOSTS_ACEITOS.has(hostDe(new URL(origin).host)); } catch { return false; }
}

function responder(res, status, corpo, cabecalhos = {}) {
  const texto = corpo === undefined ? "" : JSON.stringify(corpo);
  res.writeHead(status, {
    ...(texto ? { "Content-Type": "application/json; charset=utf-8" } : {}),
    "Content-Length": Buffer.byteLength(texto),
    ...cabecalhos,
  });
  res.end(texto);
}

async function atenderHttp(req, res) {
  // Defesa contra DNS rebinding (exigência da especificação): só Host e Origin locais.
  if (!HOSTS_ACEITOS.has(hostDe(req.headers.host)) || !origemLocal(req.headers.origin)) {
    return responder(res, 403, fail(null, -32000, "origem não permitida"));
  }
  const caminho = (req.url || "").split("?")[0];
  if (caminho !== "/mcp") return responder(res, 404, fail(null, -32000, "use o caminho /mcp"));

  const idSessao = req.headers["mcp-session-id"];
  if (req.method === "DELETE") {
    if (!idSessao || !sessoes.delete(idSessao)) return responder(res, 404, fail(null, -32001, "sessão não encontrada"));
    return responder(res, 204);
  }
  if (req.method !== "POST") {
    // Sem fluxo SSE do servidor para o cliente: GET não é oferecido.
    return responder(res, 405, fail(null, -32000, "método HTTP não suportado"), { Allow: "POST, DELETE" });
  }

  let tamanho = 0;
  const partes = [];
  for await (const p of req) {
    tamanho += p.length;
    if (tamanho > LIMITE_CORPO) return responder(res, 413, fail(null, -32000, "corpo grande demais"));
    partes.push(p);
  }
  let corpo;
  try { corpo = JSON.parse(Buffer.concat(partes).toString("utf8")); }
  catch { return responder(res, 400, fail(null, -32700, "JSON inválido")); }

  const mensagens = Array.isArray(corpo) ? corpo : [corpo];
  const inicia = mensagens.some((m) => m && m.method === "initialize");
  const cabecalhos = {};
  if (inicia) {
    const nova = crypto.randomUUID();
    sessoes.add(nova);
    cabecalhos["Mcp-Session-Id"] = nova;
  } else if (!idSessao) {
    return responder(res, 400, fail(null, -32000, "falta o cabeçalho Mcp-Session-Id"));
  } else if (!sessoes.has(idSessao)) {
    return responder(res, 404, fail(null, -32001, "sessão não encontrada; inicie outra com initialize"));
  }

  const respostas = (await Promise.all(mensagens.map(handle))).filter(Boolean);
  if (!respostas.length) return responder(res, 202, undefined, cabecalhos); // só notificações
  return responder(res, 200, Array.isArray(corpo) ? respostas : respostas[0], cabecalhos);
}

function iniciarHttp(porta) {
  const servidor = http.createServer((req, res) => {
    atenderHttp(req, res).catch((e) => {
      if (!res.headersSent) responder(res, 500, fail(null, -32603, String(e && e.message || e)));
      else res.end();
    });
  });
  servidor.on("error", (e) => {
    process.stderr.write(`obsidian-cli-mcp: não foi possível abrir 127.0.0.1:${porta} (${e.code || e.message})\n`);
    process.exit(1);
  });
  servidor.listen(porta, "127.0.0.1", () => {
    process.stderr.write(`obsidian-cli-mcp ${VERSAO}: HTTP em http://127.0.0.1:${porta}/mcp (OBSIDIAN_BIN=${BIN})\n`);
  });
  return servidor;
}

// ---- Escolha do transporte ----
const argv = process.argv.slice(2);
if (argv.includes("--http")) {
  const arg = argv.find((a) => a.startsWith("--port="));
  const bruto = arg ? arg.slice("--port=".length) : (process.env.OBSIDIAN_MCP_PORT || String(PORTA_PADRAO));
  const porta = Number(bruto);
  if (!Number.isInteger(porta) || porta < 1 || porta > 65535) {
    process.stderr.write(`obsidian-cli-mcp: porta inválida: ${bruto}\n`);
    process.exit(1);
  }
  iniciarHttp(porta);
} else {
  iniciarStdio();
}
