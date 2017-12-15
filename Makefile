all:
	blender -b --python script.py 

clean:
	rm -rf dist/*.*
