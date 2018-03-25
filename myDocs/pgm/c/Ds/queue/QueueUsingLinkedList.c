#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	struct Node* next;
};
struct Node *front=NULL;
struct Node *rear=NULL;

void enQueue(int data)
{
	struct Node *temp=(struct Node*)malloc(sizeof(struct Node));
	temp->data=data;
	temp->next=NULL;
	if(front==NULL&&rear==NULL)     
	{
		front=rear=temp;
		return;
	}
	rear->next=temp;
	rear=temp;      // rear is updated every time
}


void deQueue()
{
	struct Node *temp=front;
	if(front==NULL)
		return;
	else if(front==rear)
	{
		front=rear=NULL;
	}
	else
	{
		front=front->next;   // front pointed to next to front node
	}
	free(temp);

}


void printQueue()
{
	struct Node *temp=front;
	while(temp!=NULL)
	{
		printf("%d\t",temp->data);
		temp=temp->next;
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	int no,Num,i;
	/*enQueue(1);
	enQueue(2);
	enQueue(3);
	enQueue(4);
	enQueue(5);*/

	printf("%s\n","How many no?");
	scanf("%d",&no);
	for ( i = 0; i < no; ++i)
	{
		printf("%s\n","Enter the elements");
		scanf("%d",&Num);
		enQueue(Num);
	}
	printQueue();	
	deQueue();
	deQueue();
	deQueue();
	printQueue();

	// printf("%s\n","hello manohar" );
	return 0;
}