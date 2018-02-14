#include "stdio.h"
void test();
int main(){

	extern int id;
	printf("%s\n", "Storage specifier");
	test();
	test();
	test();
	test();
	test();
	printf("%d\n", id);
	return 0;	
}
int id=7;  // extern variable
void test()
{
	// auto int nid=0;  // it is stored in cpu main m/y  and local scope
	static int nid=	0;   // 
	register int rid=50;   // stored in register
	printf("%d\n", nid);
	printf("%d\n",rid);
	nid++;
}