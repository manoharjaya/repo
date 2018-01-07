#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	struct Node *next;
};

//head is global variable
struct Node *head;


//insert at begining of LL
struct Node* Insert(struct Node* head,int data)
{
	struct Node *temp=(struct Node*)malloc(sizeof(struct Node));
	temp->data=data;
	temp->next=NULL;
	if(head==NULL)   //initially temp is NULL  
		head=temp;       //assign the newly created address and thi is pointed to whole application
		//return;          // return back to main method
	else
	{
		struct Node* temp1=head;  
		while(temp1->next!=NULL) temp1=temp1->next;  // it goes until it reach NULL
		temp1->next=temp;    // assign the newly created address to previous node
	}
	return head;
}

void Print(struct Node* head)
{
	while(head!=NULL)
	{
		printf("%d\t",head->data);
		head=head->next;
	}
	printf("\n");
}

// using iterative method
struct Node* Reverse(struct Node* head)
{
	struct Node *current=head,*pre=NULL,*next;   // current = 100

	while(current!=NULL)   // 100 != null 
	{
		next=current->next;  // 2,100 -> 4,150 -> 6,200 -> 8,250 -> 10,300   // next = 150
		current->next=pre;  // pre = 0
		pre=current;         // current = 100
		current=next; 
	}
	head=pre;
	return head;
}

int main(int argc, char const *argv[])
{
	//printf("%s\n", "hello world");

	struct Node *head=NULL;

	head=Insert(head,1);
	head=Insert(head,2);
	head=Insert(head,3);
	head=Insert(head,4);
	head=Insert(head,5);

	Print(head);

	head=Reverse(head);

	Print(head);


	return 0;
}