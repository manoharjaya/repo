#include "stdio.h"
void main()
{
	int *nptr,nid=70;
	printf("%s\n", "pointerSimple_Nov_11");
	printf("%x\n",&nptr);
	printf("%x\n",&nid);
	printf("%d\n",nid );
	printf("%d\n",nptr );   // by default pointer is zero
	
	nptr=&nid;
	printf("%d\n",*nptr);

}