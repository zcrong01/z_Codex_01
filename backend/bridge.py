#_Part_00100_imports  [주석단위]
import json
from pathlib import Path

from PySide6.QtCore import QObject, Slot

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

    @Slot(str, result=str)
    def save(self, code: str) -> str:
        path = self.build_dir / "sketch.ino"
        path.write_text(code, encoding="utf-8")
        return json.dumps({"ok": True, "path": str(path)})
