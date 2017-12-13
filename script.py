import bpy

directory = "./dist/"

# print(dir(bpy))

def save_file(name):
	bpy.ops.wm.save_as_mainfile(filepath=directory+name)

save_file('test.blend')
