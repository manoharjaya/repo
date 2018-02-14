#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	struct Node *next;
};

struct Node *head=NULL;

void Insert(int x)
{
	
	// struct Node *temp=(Node*)malloc(sizeof(struct Node));
	// temp->data=x;                 
	// temp->next=NULL;
	// if(head!=NULL)
	// 	temp->next=head;
	// head=temp;            

	
	struct Node *temp=(struct Node*)malloc(sizeof(struct Node));   // temp is created 
	temp->data=x;             //  dereference the temp
	temp->next=head; // Initially head is NULL   
	// MUST WRITE DIAGRAM
							     
	head=temp; // 


}
void Print()
{
	struct Node *temp=head;   // doubt for global
	printf("%s\n","list are:" );
	while(temp!=NULL)
	{
		printf("%d\t",temp->data);
		temp=temp->next;
	}
	printf("\n");
}
int main()
{
	int x,num,i;
	printf("How many num ?");
	scanf("%d",&num);
	for ( i = 0; i < num; ++i)
	{
		printf("%s\n", "enter the no ?");
		scanf("%d",&x);
		Insert(x);
		Print();

	}
	return 0;
}
	