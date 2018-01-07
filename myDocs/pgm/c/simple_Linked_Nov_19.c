#include "stdio.h"
#include "stdlib.h"

struct Node
{
	int data;
	Node *next;
};
void display(struct Node *n)
{
	while(n!=NULL)
	{
		printf("traverse=%d\n", n->data);
		n=n->next;	
		
	}
}
int main(int argc, char const *argv[])
{


	struct Node *head=NULL;
	struct Node *first=NULL;
	struct Node *second=NULL;
	
	
	head=(Node*)malloc(sizeof(Node));   
	first=(Node*)malloc(sizeof(Node));   
	second=(Node*)malloc(sizeof(Node));   
	
	printf("test=%d\n",head);

	head->data=2;
	head->next=first;


	first->data=4;
	first->next=second;

	second->data=6;
	second->next=NULL;

	display(head);
	                                                                                                                                                    

	// printf("%d\n",head->data);
	// printf("%d\n",first->data);
	// printf("%d\n",second->data);
	
	printf("%s\n","simple_nexted_Nov_19" );

	return 0;
}