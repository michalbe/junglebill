import bpy
import mathutils

class junglebill:
	def __init__(self):
		self.bpy = bpy

		# Remove default cube from the scene
		self.bpy.ops.object.select_all(action='SELECT')
		self.bpy.data.objects['Cube'].select = True
		self.bpy.ops.object.delete()

	def save(self, path):
		self.bpy.ops.wm.save_as_mainfile(filepath=path)
