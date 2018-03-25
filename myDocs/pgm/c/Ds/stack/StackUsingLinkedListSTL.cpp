#include "iostream"
#include "stack"
#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	struct Node *next;
};
struct Node* top;
stack<struct Node*> s;
void Push(int data)
{
	struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
	s.push(temp);
	temp->data=data;
	temp->next=top;
	top=temp;
}
void Pop()
{
	struct Node* temp=top;
	while(temp!=NULL)
	{
		temp=s.top();
		
	}
}

void Print()
{
	struct Node* temp=top;
	while(temp!=NULL)
	{
		printf("%d\t",temp->data);
		temp=temp->next;
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{

	top=NULL;
	printf("%s\n","hello world" );
	Push(1);
	Push(2);
	Push(3);
	Push(4);
	Push(5);
	Print();
	// Pop();
	// Pop();
	// Print();
	return 0;
}