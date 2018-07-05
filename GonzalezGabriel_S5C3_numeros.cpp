#include <iostream>
#include <cstdlib>


using std::cout;
using std::endl;


int main()
{
  int i, numeroal;
  for(i=0; i<1000; i++)
	{
    numeroal = rand() % 100 + 1;
    cout << i << " " << numeroal << endl;  	 	 
        }	

  return 0;
}

