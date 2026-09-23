import bpy
from datetime import datetime


def log(message, show_popup = False, icon="INFO"):

    print(f"[Simplified SpriteSheetMaker {datetime.now()}] {message}")

    if(show_popup):
        bpy.ops.simplified_spritesheetmaker.message_popup('INVOKE_DEFAULT', **{ "message_heading": message,  "message_icon" : icon })
