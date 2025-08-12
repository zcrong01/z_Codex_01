#_Part_00100_imports  [주석단위]
import json
import shutil
from pathlib import Path

from PySide6.QtCore import QObject, Slot

from .cli_bridge import compile_and_upload

#_Part_00200_bridge_class  [주석단위]
class AppBridge(QObject):
    def __init__(self, root_dir: str):
        super().__init__()
        self.root_dir = Path(root_dir)
        self.build_dir = self.root_dir / "_build"
        self.build_dir.mkdir(exist_ok=True)

    @Slot(result=str)
    def ping(self) -> str:
        return "pong"

    # JS → Python: 코드 및 소스맵 저장
    @Slot(str, str, result=str)
    def saveSketch(self, code: str, source_map: str) -> str:
        ino_path = self.build_dir / "workspace.ino"
        map_path = self.build_dir / "workspace.sourcemap.json"
        try:
            ino_path.write_text(code, encoding="utf-8")
            map_path.write_text(source_map, encoding="utf-8")
            return json.dumps({
                "ok": True,
                "ino_path": str(ino_path),
                "map_path": str(map_path),
            })
        except Exception as e:
            return json.dumps({"ok": False, "message": str(e)})

    # JS → Python: Arduino CLI 컴파일/업로드
    @Slot(str, str, str, result=str)
    def compileAndUpload(self, ino_path: str, fqbn: str, port: str) -> str:
        cli = self._which_cli()
        if not cli:
            return json.dumps({
                "ok": False,
                "stage": "precheck",
                "message": "Arduino CLI not found"
            }, ensure_ascii=False)
        project_dir = Path(ino_path).parent
        return compile_and_upload(cli, project_dir, fqbn, port)

    #_Part_00300_helpers  [주석단위]
    def _which_cli(self) -> str | None:
        return shutil.which("arduino-cli")
