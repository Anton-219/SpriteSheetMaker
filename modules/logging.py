import bpy
from datetime import datetime


def log(message, show_popup=False, icon="INFO"):

    print(f"[Simplified SpriteSheetMaker {datetime.now()}] {message}")

    if not show_popup:
        return

    def draw_popup(self, context):
        lines = str(message).split("\n")
        for i, line in enumerate(lines):
            self.layout.label(
                text=line,
                icon=icon if i == 0 else 'BLANK1'
            )

    bpy.context.window_manager.popup_menu(
        draw_popup,
        title="Simplified SpriteSheetMaker",
        icon=icon
    )
