#include "stdio.h"
#define MAX_SIZE 101
int A[MAX_SIZE];
int top=-1;

void Push(int value)
{
	if(top==MAX_SIZE-1)
	{
		printf("%s\n","stack overflow.." );
		return;
	}	
	top++;
	A[top]=value;
}
void Pop()
{
	if (top==-1)
	{
		printf("%s\n","No element to pop.." );
		return;
	}
	top--;
}

int Top()
{
	return A[top];
}


void Print()
{
	int i=0;
	
	if(top==-1)
	{
		printf("%s\n","stack is empty.." );
		return;
	}
	printf("%s\n", "stack are..");
	for ( i = 0; i <= top; ++i)
		printf("%d\n",A[i]);
	printf("\n");
}

int main(int argc, char const *argv[])
{
	// printf("%s\n","hello" );
	// printf("top value are=%d\n",Top() );
	Print();
	Push(1);
	Push(2);
	Push(3);
	Print();
	printf("top value are=%d\n",Top() );
	Pop();
	Push(4);
	Print();
	Pop();
	// Top();
	printf("top value are=%d\n",Top() );
	Print();
	return 0;
}