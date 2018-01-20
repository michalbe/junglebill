import bpy
import mathutils

class junglebill:
	def __init__(self):
		self.bpy = bpy
		self.mode = 'OBJECT'

		# Remove default cube from the scene
		self.bpy.ops.object.select_all(action='SELECT')
		self.bpy.data.objects['Cube'].select = True
		self.bpy.ops.object.delete()

	def get_object_from_file(self, file_path, object_name):
		with self.bpy.data.libraries.load(file_path) as (data_from, data_to):
			data_to.objects = [name for name in data_from.objects if name.startswith(object_name)]
		return data_to.objects[0]

	def copy(self, item):
		new_item = item.copy()
		new_item.data = item.data.copy()
		new_item.animation_data_clear()
		return new_item

	def add_object(self, item):
		self.bpy.context.scene.objects.link(item)

	def set_active(self, item):
		item.select = True
		self.bpy.context.scene.objects.active = item

	def edit_mode(self):
		self.bpy.ops.object.mode_set(mode='EDIT')
		self.mode = 'EDIT'

	def object_mode(self):
		self.bpy.ops.object.mode_set(mode='OBJECT')
		self.mode = 'OBJECT'

	def join(self, main_item):
		self.select_all()
		self.set_active(main_item)
		self.bpy.ops.object.join()

	def select_all(self):
		if self.mode == 'OBJECT':
			for item in bpy.data.objects:
				item.select = True
		else:
			self.bpy.ops.mesh.select_all(action='SELECT')

	def mirror(self, item, axis):
		self.set_active(item)
		self.edit_mode()
		self.select_all()
		bpy.ops.transform.mirror(
			'EXEC_DEFAULT',
			constraint_axis=axis,
			constraint_orientation='GLOBAL',
			proportional='DISABLED'
			)
		self.object_mode()

	def apply_modifiers(self, item):
		self.set_active(item)
		for modifier in item.modifiers:
			self.bpy.ops.object.modifier_apply(modifier=modifier.name)

	def save(self, path):
		self.bpy.ops.wm.save_as_mainfile(filepath=path)
