#include "stdio.h"
void increment(int* a)
{
	*a=*a+1;
	// return a;
}
int main(int argc, char const *argv[])
{
	int a=10;
	printf("%d\n",a);
	increment(&a);
	printf("%d\n",a);
	return 0;
}