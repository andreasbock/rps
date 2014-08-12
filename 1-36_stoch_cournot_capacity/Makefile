file=stoch_cournot_capacity

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

g:
	./plt.py $(file).lst
