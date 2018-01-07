#include "stdio.h"     // pre processive directive section
int total=0;          // global declaration
int add(int,int);     // function declaration
void main()           // main function
{
	printf("%s\n", "Addition");
	total=add(25,50);
	printf("sum=%d\n",total);
}
int add(int a,int b)
{
	return a+b;
}
