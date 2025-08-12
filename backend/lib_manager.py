#_Part_00100_imports  [주석단위]
import json
import subprocess

#_Part_00200_list_helpers  [주석단위]
def list_cores(cli: str) -> str:
    cmd = [cli, "core", "list", "--format", "json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return proc.stdout


def list_libraries(cli: str) -> str:
    cmd = [cli, "lib", "list", "--format", "json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return proc.stdout


def summary(cli: str) -> str:
    cores = json.loads(list_cores(cli) or "[]")
    libs = json.loads(list_libraries(cli) or "[]")
    return json.dumps({"cores": cores, "libraries": libs}, ensure_ascii=False)
