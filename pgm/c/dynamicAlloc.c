#include "stdio.h"
#include "stdlib.h"
void main()
{
	 int i,n,*nptr;
	 printf("%s\n","dynamic m/y allocation" );
	 printf("%s\n", "Enter the no:");
	 scanf("%d",&n);

	 nptr=(int*)malloc(n*sizeof(int));

	 printf("%d\n",nptr);

	 printf("%s\n","Enter the Array:" );
	 // scanf("%d",nptr);

	 for ( i = 0; i < n; ++i)
	 {
	 	scanf("%d",(nptr+i));
	 }
	 printf("\n");

	
	 for ( i = 0; i < n; ++i)
	 {
	 	printf("%d\n",*(nptr+i));
	 }
}
