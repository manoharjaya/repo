#include "stdio.h"
int main(int argc, char const *argv[])
{
	int a=10;
	printf("%s\n","hello world" );
	printf("%d\n",a++);
	printf("%d\n",++a + ++a + a++);
	return 0;
}