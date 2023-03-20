plot :: bifurcation_data.dat
	gnuplot plot.p
	make clean

bifurcation_data.dat :: bifurcation.cpp bifurcation.o
	./bifurcation.o

bifurcation.o :: bifurcation.cpp
	gcc bifurcation.cpp -lstdc++ -lm -o bifurcation.o

clean:
	-rm -f *.o output

