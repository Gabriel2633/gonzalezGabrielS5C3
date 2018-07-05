# include <iostream>

using namespace std;

int multiplicar(int x , int y);

int alcuadrado(int x);

int main ()
{
	int a=17;

	int b=31; 

	int O;
	int P;

	O = multiplicar(a,b);
	std::cout << "multiplicacion de a y b es igual a " << O << std::endl;	
	P = alcuadrado(a);
	std::cout << "a elevado al cuadrado es igual a " << P << std::endl;	
	
	return 0;
}

int multiplicar(int x, int y)
{
	int q;
	q = x*y;
	return q;
}

int alcuadrado(int x)
{
	int s;
	s = x*x;
	return s; 
}
