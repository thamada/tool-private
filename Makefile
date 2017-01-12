#Time-stamp: <2017-01-12 01:19:59 hamada>

target := mit.py
source = ./short_quotes_HeartSutra.txt
source = ./short_quotes.txt


all: 
	./generate.py ${source} > $(target)
	chmod 755 $(target)


push:
	git add .
	./$(target) |bash -


clean:
	rm -f $(target) *~ .*~ *.db.bz2

c: clean

