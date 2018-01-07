#include "stdio.h"
int bid=45;
void test();
void main()
{
	int bid=50;
	printf("%s\n", "globalVariable_Nov_11");
	test();

}
void test()
{
	printf("%d\n", bid);
}
