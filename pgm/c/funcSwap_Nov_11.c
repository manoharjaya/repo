#include "stdio.h"
void swap(int*,int*);
void main()
{	
	int nid1=50,nid2=20;
	printf("%s\n","funcSwap_Nov_11 using call by reference.." );
	printf("%d\t%d\n",nid1,nid2 );
	swap(&nid1,&nid2);
}
void swap(int *sid1,int *sid2)
{
	printf("%s\n", "Im inside swap..");
	int temp=0;
	temp=*sid1;
	*sid1=*sid2;
	*sid2=temp;
	printf("%d\t%d\n",*sid1,*sid2);
}