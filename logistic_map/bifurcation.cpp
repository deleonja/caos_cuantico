#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

// This script will generate the data used to create the bifurcation diagram of the defined map
// Plotting might be done using gnuplot. Maybe I'll add the script to do that, maybe I won't. Who's to say.
// Adding a Makefile would be a great idea too.

double map(const double growth, const double x)
{
  if ( x<=0.5)
    return ( growth*x );
  else
    return ( growth-growth*x );

}

int main()
{
  const double min_growth = 0.9;
  const double max_growth = 1.9;
  const int growth_intervals = 500;
  const int number_of_generations = 200;
  ofstream myfile;
  
  srand(time(NULL));

  double growth = min_growth;
  double x_n;
  
  myfile.open ("bifurcation_data");

  for(int i=0; i<growth_intervals; ++i){
    growth += (max_growth - min_growth)/growth_intervals; // Increase growth rate
    x_n = map(growth, ((double)rand())/RAND_MAX); // Run the map at random starting point
    for(int j=0; j<number_of_generations+growth_intervals; ++j) // Now do the following 
    {
      x_n = map(growth, x_n);
      if(j>=number_of_generations)
      {
        myfile << growth << ' ' << x_n << '\n';
      }
    }
  }
  myfile.close();
  
  return (0);
}