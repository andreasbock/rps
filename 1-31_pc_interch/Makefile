file=pc

all:
	gams $(file).gms

clean:
	rm $(file).lst
	rm *.lst

v:
	vim -R $(file).lst

g:
	../new_get_data.py $(file).lst
