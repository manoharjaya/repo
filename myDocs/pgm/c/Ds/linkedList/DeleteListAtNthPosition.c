#include "stdio.h"
#include "stdlib.h"

struct Node 
{
	int data;
	struct Node *next;
};
struct Node *head;

void deleteList(int n)
{
	struct Node *temp1=head;
	int i=0;
	if (n==1)
	{
		head = temp1->next; // head now pointed to next node of head 
		free(temp1);
		return;
	}

	for (i = 0; i <n-2; ++i)
	{
		temp1=temp1->next; // go to n-1 address position

		struct Node *temp2 = temp1->next; // point to deleted node positions

		temp1->next = temp2->next; // pointed to n+1 node 

		free(temp2);                                             
	}
}

void insert(int data)
{
	struct Node *temp1=(struct Node*)malloc(sizeof(struct Node));  // 100      
	 
	temp1->data=data; // 7
	temp1->next=head->next; // NULL
	head=temp1;  
}
void print()
{
	struct Node* temp=head;
	while(temp!=NULL)
	{
		printf("%d\n",temp->data);
		temp=temp->next;
	}
}


int main(int argc, char const *argv[])
{
	int Position;
	head=NULL;
	insert(7);   //7
	insert(10);  //7,10
	insert(15);  //15,7,10
	insert(22);  //15,22,7,10
	insert(77);  //77,15,22,7,10
	print();


	// printf("%s\n","Enter the Position:" );
	// scanf("%d");

	// deleteList(Position);
	// print();
	return 0;
}