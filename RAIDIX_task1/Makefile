PREFIX=/usr/local

all: hello

hello: hello.py
	python3 hello.py

install: all
	mkdir -p $(PREFIX)/bin
	install hello.py $(PREFIX)/bin/
