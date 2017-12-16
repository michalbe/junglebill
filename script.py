import bpy
import mathutils

DIST_DIR = "./dist/"

def save_file(name):
	bpy.ops.wm.save_as_mainfile(filepath=DIST_DIR+name)

# Remove cube from the scene
bpy.ops.object.select_all(action='SELECT')
bpy.data.objects['Cube'].select = True
bpy.ops.object.delete()

save_file('test.blend')
