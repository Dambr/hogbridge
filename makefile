all:
	pyinstaller main.spec

clean:
	python -c "import shutil; shutil.rmtree('build', ignore_errors=True)"
	python -c "import shutil; shutil.rmtree('dist', ignore_errors=True)"