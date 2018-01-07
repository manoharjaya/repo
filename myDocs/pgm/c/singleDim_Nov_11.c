#include "stdio.h"
int main()
{
	int narr[20]={12,45,57,54,24};
	printf("%s\n", "singleDim_Nov_11");
	for (int i = 0; i < 5; ++i)
	{
		printf("arr[%d]=%d\n",i,narr[i]);
	}
	return 0;
}