file=wind_investment_stochastic_cournot

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

g:
	./new_get_data.py $(file).lst
