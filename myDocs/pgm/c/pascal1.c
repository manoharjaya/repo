#include "stdio.h"
int main(int argc, char const *argv[])
{
	int i,j;
	// for ( i = 0; i < 4; ++i)
	// {
	// 	for ( j = 0; j <= i; ++j)
	// 	{
	// 		printf("%d\t",1);
	// 	}
	// 	printf("\n");
	// }

	for ( i = 4;i>=1; --i)
	{
		for ( j = 1; j <= i; ++j)
		{
			printf("%d\t",1);
		}
		printf("\n");
	}
	return 0;
}