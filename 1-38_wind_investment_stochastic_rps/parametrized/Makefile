file=wind

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

g:
	./plot.py
