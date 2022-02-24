CC = python3
INS = pyinstaller
MAIN = main
LIBS = gui.py commands.py update.py 
MSG = echo "\n ----- COMPILATION COMPLETE! ----- \n"

default:
	${CC} ${MAIN}.py 

install:
	${INS} --onefile --windowed ${MAIN}.py ${LIBS}
	${MSG}

remove:
	mv dist/${MAIN} voyage
	rm -rf dist build ${MAIN}.spec __pycache__

done:
	make install
	make remove
	${MSG}

req:
	pip install -r requiremnts.txt
