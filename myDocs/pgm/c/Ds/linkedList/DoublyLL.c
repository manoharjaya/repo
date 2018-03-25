
/*Dobuly linked list implementation */

#include "stdio.h"
#include "stdlib.h"

struct Node
{
	int data;
	struct Node *next;
	struct Node *pre;
};

struct Node* head;   // global declaration ..


struct Node *getNode(int data)
{
	struct Node* newNode=(struct Node*)malloc(sizeof(struct Node));
	newNode->data=data;
	newNode->pre=NULL;
	newNode->next=NULL;

	return newNode;
}


void InsertAtHead(int data)
{
	struct Node* newNode=getNode(data);

	if(head==NULL)
	{
		head=newNode;
		return;
	}
	head->pre=newNode;      
	newNode->next=head;
	head=newNode;
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


void reversePrint()
{
	struct Node* temp=head;
	while(temp->next!=NULL)   //iterate upto last
 	{
 		temp=temp->next;
	}


	while(temp!=NULL)
	{
		printf("%d\t",temp->data);
		temp=temp->pre;
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	
	head=NULL;
	InsertAtHead(1);
	InsertAtHead(2);
	InsertAtHead(3);
	InsertAtHead(4);
	InsertAtHead(5);
	
	Print();

	reversePrint();
	return 0;
}