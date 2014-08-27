file=stoch_cournot_capacity

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
