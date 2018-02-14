#include "stdio.h"
#ifndef Max
#define Max 10
#endif
int Arr[10];

void enQueue(int data)
{
	int rear=-1;
	if(rear==Max-1)
	{
		printf("%s\n","queue overflow");
		return;
	}
	Arr[++rear]=data;
}

void deQueue()
{
	int front=0;
	Arr[++front];
}
/*int IsOverFlow()
{
	if(Arr[Max-1]==rear)
	{
		return Arr[Max]
	}
}*/
int main(int argc, char const *argv[])
{
	
	enQueue(1);
	enQueue(2);
	enQueue(3);
	enQueue(4);
	
	printf("%s\n","hello manohar" );
	return 0;
}