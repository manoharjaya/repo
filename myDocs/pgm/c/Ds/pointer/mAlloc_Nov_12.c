#include "stdio.h"
#include "stdlib.h"

int main(int argc, char const *argv[])
{
	
	int num=0,*nptr,sum=0,i;
	printf("%s\n", "Enter the no..");
	scanf("%d",&num);
	printf("%d\n",num );
	printf("sizeof num=%d\n",sizeof(num) );
	
	nptr=(int*)malloc(num*sizeof(int));

	printf("Allocated bytes is=%d\n",sizeof(nptr));	

	if (nptr==NULL)
	{
		printf("%s\n","null value is there..");
	}
	else
	{
		for ( i = 0; i < num; ++i)
		{
			scanf("%d",nptr+i);
			sum+=*(nptr+i);
		}
	}
	printf("%d\n",sum );
	free(nptr);
	return 0;
}