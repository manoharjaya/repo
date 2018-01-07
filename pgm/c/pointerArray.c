#include "stdio.h"
int main(int argc, char const *argv[])
{
	int a[5]={2,5,7,8,10};

	printf("%d\n",a);   // address of first elements in an array

	printf("%d\n",*a );

	int *pa;

	pa=a;   // a should return base address of an array
	



	printf("%x\n",pa);
	printf("%d\n",*pa );

	printf("%x\n",&a);
	printf("%d\n",a[0]);


	for (int i = 0; i < 5; ++i)
	{
		printf("a[%d]=%d\n", i,*(pa+i));
	}

	printf("%d\n",a+1);
	printf("%d\n", &a[1]);

	printf("%d\n",*a);
	printf("%d\n",*(a+0) );

	return 0;
}