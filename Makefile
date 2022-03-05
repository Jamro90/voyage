CC = python3
INS = pyinstaller
MAIN = main
LIBS = gui.py commands.py update.py document_maker.py 
MSG = echo "\n ----- COMPILATION COMPLETE! ----- \n"

default:
	${CC} ${MAIN}.py 

install:
	${INS} --onefile --windowed --icon="ico.ico" ${MAIN}.py ${LIBS}
	${MSG}

remove:
	mv dist/${MAIN} voyage
	rm -rf dist build ${MAIN}.spec __pycache__

done:
	make install
	make remove
	zip -r voyage.zip voyage
	${MSG}

req:
	pip install -r requiremnts.txt
