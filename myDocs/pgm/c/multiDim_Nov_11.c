#include "stdio.h"
void main()
{
	int narr[2][3]={15,15,45,78,87,65},i,j;
	printf("%s\n","multiDim_Nov_11" );
	for ( i = 0; i < 2; ++i)
	{
		for ( j = 0; j < 3; ++j)
		{
			printf("%d\n",narr[i][j]);
		}
	}
}