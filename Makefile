#Time-stamp: <2016-12-31 00:52:19 hamada>

all:
	./generate.py ./short_quotes.txt > commit.py
	chmod 755 ./commit.py


push:
	git add .
	./commit.py |bash -


clean:
	rm -f commit.py *~ .*~

c: clean

