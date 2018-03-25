#include "stdio.h"
int main(int argc, char const *argv[])
{
	int a=20;
	int* p;
	p=&a;
	printf("a=%d\n",a);
	printf("&a=%x\n",&a);
	printf("p=%d\n",p);
	printf("&p=%x\n",&p);
	printf("*p=%d\n",*p);
	printf("p+1=%d\n",p+1);
	

	printf("%d\n",*p);

	*(p+1)=75;
	printf("%d\n",*(p+1));

	return 0;
}