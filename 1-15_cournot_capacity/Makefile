file=cournot_capacity

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

g:
	../new_get_data.py $(file).lst
	inkscape -z -D --file=foo.svg --export-pdf=foo.pdf --export-latex
	rm foo.svg
