#include "stdio.h"
#include "stdlib.h"

struct Node
{
	int data;
	struct Node *next;
};

struct Node* head;

void  Insert(int data)
{

	struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
	temp->data=data;
	temp->next=NULL;
	
	if(head==NULL) 
		head=temp;
	else
	{

		struct Node* temp1=head;
		while(temp1->next!=NULL) temp1=temp1->next;
		temp1->next=temp;
	}
}


void Print()
{
	struct Node* temp=head;
	while(temp!=NULL)
	{
		printf("%d\t",temp->data);
		temp=temp->next;
	}
	printf("\n");
}


void reversePrint(struct Node* p)
{
	
	if(p->next==NULL)
	{
		head=p;
		return;
	}

	reversePrint(p->next);   // very important to understand lecture no 12   
	struct Node *q=p->next;  
	q->next=p;
	p->next=NULL;
	//printf("%d\t", p->data);
}

int main(int argc, char const *argv[])
{
	
	head=NULL;

	Insert(2);
	Insert(4);
	Insert(6);
	Insert(8);
	Insert(10);
	
	Print();

	reversePrint(head);

	Print();


	return 0;
}