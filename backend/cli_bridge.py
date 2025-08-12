#_Part_00100_imports  [주석단위]
import json
import subprocess
from pathlib import Path

#_Part_00200_cli_helpers  [주석단위]
def _run(cmd: list[str]) -> tuple[int, str, str]:
    """Run a command and return (returncode, stdout, stderr)."""
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, proc.stdout, proc.stderr

#_Part_00300_compile_upload  [주석단위]
def compile_and_upload(cli: str, project_dir: Path, fqbn: str, port: str) -> str:
    compile_cmd = [cli, "compile", "--fqbn", fqbn, str(project_dir)]
    upload_cmd = [cli, "upload", "-p", port, "--fqbn", fqbn, str(project_dir)]

    rc, c_out, c_err = _run(compile_cmd)
    if rc != 0:
        return json.dumps({
            "ok": False,
            "stage": "compile",
            "stdout": c_out,
            "stderr": c_err,
        }, ensure_ascii=False)

    rc, u_out, u_err = _run(upload_cmd)
    if rc != 0:
        return json.dumps({
            "ok": False,
            "stage": "upload",
            "stdout": u_out,
            "stderr": u_err,
        }, ensure_ascii=False)

    return json.dumps({
        "ok": True,
        "stage": "done",
        "stdout": c_out + "\n" + u_out,
    }, ensure_ascii=False)
