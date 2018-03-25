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


//  recursion 
void Print(struct Node* head)
{
	if (head==NULL) retur;   // finally head is NULL  then it return back to main function   
	printf("%d\t",head->data);
	Print(head->next);  //  recursion call
}

//
void ReversePrint(struct Node* head)
{
	if(head==NULL) return;
	ReversePrint(head->next);   // it will goes until its getting null
	printf("%d\t",head->data);
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
	printf("\n");
	ReversePrint(head);
	printf("\n");

	return 0;
}