#include "stdio.h"
int main(int argc, char const *argv[])
{

	int a;
	printf("--Check odd or even--\n");
	printf("Enter your input..\n");
	scanf("%d",&a);
	if (a%2==0)
		printf("a=%d is even\n",a);
	else
		printf("a=%d is odd\n",a);
	return 0;
}