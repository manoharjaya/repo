#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	Node *next;
 
};
void display(struct Node*);
int main(int argc, char const *argv[])
{
	printf("%s\n", "hello test link ..");


	struct Node *head=NULL;
	struct Node *first=NULL;
	struct Node *second=NULL;


	head=(Node*)malloc(sizeof(Node));   
	first=(Node*)malloc(sizeof(Node));   
	second=(Node*)malloc(sizeof(Node));  


	head->data=2;
	head->next=first;


	first->data=4;
	first->next=second;

	second->data=6;
	second->next=NULL;



	printf("%d\n", sizeof(head));

	printf("%d\n",head->data);
	printf("%d\n",first->data);
	printf("%d\n",second->data);
	
	struct Node *newnode=NULL;
	newnode=(Node*)malloc(sizeof(Node));

	newnode->data=10;
	newnode->next=head;

	display(newnode);	
	return 0;
}

void display(struct Node *temp)
{
	while(temp!=NULL)
	{
		printf("%d\n", temp->data);
		temp=temp->next;
	}
	
}