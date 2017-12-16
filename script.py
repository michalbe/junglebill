import bpy
import mathutils

DIST_DIR = "./dist/"

# print(dir(bpy))

def save_file(name):
	bpy.ops.wm.save_as_mainfile(filepath=DIST_DIR+name)

cube = bpy.data.objects["Cube"]
# one blender unit in x-direction
vec = mathutils.Vector((1.0, 5.0, 0.0))
inv = cube.matrix_world.copy()
inv.invert()
# vec aligned to local axis
vec_rot = vec * inv
cube.location = cube.location + vec_rot

save_file('test.blend')
