#Time-stamp: <2016-12-31 11:00:33 hamada>

target := mit.py

all:
	./generate.py ./short_quotes.txt > $(target)
	chmod 755 $(target)


push:
	git add .
	./$(target) |bash -


clean:
	rm -f $(target) *~ .*~

c: clean

