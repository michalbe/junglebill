all: clean
	blender -b --python script.py

clean:
	rm -rf dist/*.*
