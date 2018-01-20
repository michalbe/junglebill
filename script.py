import bpy
import mathutils

class junglebill:
	def __init__(self):
		self.bpy = bpy

		# Remove default cube from the scene
		self.bpy.ops.object.select_all(action='SELECT')
		self.bpy.data.objects['Cube'].select = True
		self.bpy.ops.object.delete()

	def get_object_from_file(self, file_path, object_name):
		with self.bpy.data.libraries.load(file_path) as (data_from, data_to):
			data_to.objects = [name for name in data_from.objects if name.startswith(object_name)]
		return data_to.objects[0]

	def add_object(self, object):
		self.bpy.context.scene.objects.link(object)

	def save(self, path):
		self.bpy.ops.wm.save_as_mainfile(filepath=path)
