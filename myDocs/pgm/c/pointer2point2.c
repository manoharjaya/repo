#include "stdio.h"
int main(int argc, char const *argv[])
{
	int a=200;
	int *ip;
	ip=&a;
	printf("%d\n",*ip);

	int **dip;
	dip=&ip;

	printf("%d\n", **dip);

	printf("%d\n",ip);

	printf("%d\n",*dip);

	int ***tip=&dip;

	printf("%d\n",***tip);
	return 0;
}