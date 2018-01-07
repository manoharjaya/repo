#include "stdio.h"
int main(int argc, char const *argv[])
{
	
	int *ptr;
	int **pptr;
	int no=27;
	ptr=&no;
	
	pptr=&ptr;
	printf("no=%d\n",no);
	printf("*ptr=%d\n",*ptr);
	printf("&no=%x\n",&no);
	printf("&ptr%x\n",&ptr);
    printf("ptr=%x\n", ptr);
    printf("&pptr=%x\n",&pptr);

    printf("**pptr=%d\n",**pptr);
    printf("pptr same as &ptr=%x\n",pptr);

	return 0;
}