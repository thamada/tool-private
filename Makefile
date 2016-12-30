#Time-stamp: <2016-12-31 00:29:45 hamada>

all:
	./generate.py ./short_quotes.txt > commit.py
	chmod 755 ./commit.py


push:
	git add .
	./commit.py |bash -
