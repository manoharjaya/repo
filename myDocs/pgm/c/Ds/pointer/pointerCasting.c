#include "stdio.h"
int main(int argc, char const *argv[])
{
	int a=1025	;
	int *ip;
	ip=&a;
	printf("%x\n", ip);
	printf("%d\n", *ip);
	printf("%d\n", a);
	printf("%x\n", &a);


	char* cp;

	cp=(char*)ip;   // typecasting
								//   0        0         4         1
	printf("%d\n",*cp );   //1025= 00000000 00000000 00000100 00000001   // it only displays last bytes because char 
							//store only one bytes rather than integer.	

	printf("%d\n",*(cp+1) );
	printf("%d\n",*(cp+2) );
	printf("%d\n",*(cp+3) );


	printf("%x\n",cp );
	

	void* vp=cp;

	printf("%d\n",*(int*)vp);

	
	return 0;
}