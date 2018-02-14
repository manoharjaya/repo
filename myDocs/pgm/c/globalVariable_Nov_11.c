#include "stdio.h"
int bid=45;
void test();
int main()
{
	bid=500;
	printf("%s\t%d\n", "globalVariable_Nov_11",bid);
	test();
	return 0;
}
void test()
{
	printf("%d\n", bid);
}
