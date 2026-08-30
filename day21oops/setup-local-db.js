#!/usr/bin/env node
/**
 * Initialize a self-contained PostgreSQL cluster under .pgdata/ on port 5433.
 * Idempotent: re-running on an initialized cluster is safe (it just starts it).
 */
const { spawn, spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const os = require("os");

function isWindows() { return process.platform === "win32"; }

function findPgBin() {
  // Common locations
  const candidates = isWindows() ? [
    "C:\\Program Files\\PostgreSQL\\18\\bin",
    "C:\\Program Files\\PostgreSQL\\17\\bin",
    "C:\\Program Files\\PostgreSQL\\16\\bin",
    "C:\\Program Files\\PostgreSQL\\15\\bin",
  ] : ["/usr/lib/postgresql/18/bin", "/usr/lib/postgresql/17/bin", "/usr/lib/postgresql/16/bin", "/usr/bin"];
  for (const c of candidates) if (fs.existsSync(c)) return c;
  return null;
}

const bin = findPgBin();
if (!bin) {
  console.error("PostgreSQL binaries not found. Install PostgreSQL 14+ and ensure psql/createdb/pg_ctl are on PATH or in a standard location.");
  process.exit(1);
}
const dataDir = path.resolve(__dirname, "..", ".pgdata");
const port = "5433";
const logFile = path.join(dataDir, "pg.log");

if (!fs.existsSync(path.join(dataDir, "PG_VERSION"))) {
  console.log(`Initializing PostgreSQL cluster in ${dataDir}...`);
  fs.mkdirSync(dataDir, { recursive: true });
  const initdb = spawnSync(path.join(bin, isWindows() ? "initdb.exe" : "initdb"), [
    "-D", dataDir, "-U", "postgres", "-A", "trust", "-E", "UTF8", "--locale=C",
  ], { stdio: "inherit" });
  if (initdb.status !== 0) {
    console.error("initdb failed.");
    process.exit(1);
  }
}

console.log("Starting PostgreSQL...");
const startArgs = isWindows()
  ? [] // we'll run `postgres` directly to avoid pg_ctl's sandbox quirks
  : ["-D", dataDir, "-l", logFile, "-o", `-p ${port} -h 127.0.0.1`, "start"];
if (isWindows()) {
  const child = spawn(path.join(bin, "postgres.exe"), ["-D", dataDir, "-p", port, "-h", "127.0.0.1"], {
    detached: true, stdio: "ignore", windowsHide: true,
  });
  child.unref();
} else {
  const res = spawnSync(path.join(bin, "pg_ctl"), startArgs, { stdio: "inherit" });
  if (res.status !== 0) process.exit(1);
}

// Wait for socket
function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }
async function waitReady() {
  for (let i = 0; i < 30; i++) {
    await sleep(500);
    const probe = spawnSync(path.join(bin, "psql"), [
      "-h", "127.0.0.1", "-p", port, "-U", "postgres", "-t", "-c", "SELECT 1",
    ], { encoding: "utf8" });
    if (probe.status === 0) return true;
  }
  return false;
}

(async () => {
  const ready = await waitReady();
  if (!ready) { console.error("PostgreSQL did not become ready in time."); process.exit(1); }
  const exists = spawnSync(path.join(bin, "psql"), [
    "-h", "127.0.0.1", "-p", port, "-U", "postgres", "-t", "-c", "SELECT 1 FROM pg_database WHERE datname='airadar'",
  ], { encoding: "utf8" });
  if (!exists.stdout || !exists.stdout.includes("1")) {
    console.log("Creating database 'airadar'...");
    spawnSync(path.join(bin, "createdb"), [
      "-h", "127.0.0.1", "-p", port, "-U", "postgres", "airadar",
    ], { stdio: "inherit" });
  } else {
    console.log("Database 'airadar' already exists.");
  }
  console.log("\nPostgreSQL ready on 127.0.0.1:5433, database 'airadar'.");
  console.log("Next: cd backend && npx prisma db push && npx tsx prisma/seed.mts");
})();