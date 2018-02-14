#include "stdio.h"
#include "iostream"
#include "stack"
using namespace std;


void Insert(char c[],int n)
{
	stack<char> s;
	//pushing element into stacks
	for (int i = 0; i < n; ++i)
	{
		s.push(c[i]);

	}
	// poping element into stack
	for (int i = 0; i < n; ++i)
	{
		/* code */
		c[i]=s.top();
		s.pop();
	}
}


int main(int argc, char const *argv[])
{

	char name[8]="manohar";
	// printf("%s\n",name );
	for (int i = 0; i < 7; ++i)
	{
		/* code */
		printf("%c", name[i]);
	}
	printf("\n");
	Insert(name,7);
	printf("%s\n",name);
	return 0;
}