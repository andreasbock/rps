file=ndrf_stoch_miqcp

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

3d:
	./plot.py 3d

sli:
	./plot.py slices
	inkscape -z -D --file=foo.svg --export-pdf=foo.pdf --export-latex
	rm foo.svg
	rm *pdf_tex
