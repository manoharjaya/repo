#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	struct Node* next;
};
struct Node* top=NULL;


void Push(int data)
{
	struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
	temp->data=data;
	temp->next=top;
	top=temp;
}
void Pop()
{
	
	if(top==NULL) return;
	struct Node* temp=top;
	top=top->next;
	free(temp);
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
	

	Push(1);
	Push(2);
	Push(3);
	Push(4);
	Print();
	Pop();
	Pop();
	Print();

	return 0;
}