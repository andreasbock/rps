file=stoch_cournot_capacity_penalty

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.svg
	rm *.pdf
	rm *.pdf_tex
	rm *.lst

v:
	vim -R $(file).lst

3d:
	./plot.py 3d

sli:
	./plot.py slices
	inkscape -z -D --file=foo.svg --export-pdf=foo.pdf --export-latex
	inkscape -z -D --file=fooprod.svg --export-pdf=fooprod.pdf --export-latex
	rm foo.svg
	rm fooprod.svg
	rm *pdf_tex
