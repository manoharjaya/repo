#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int data;
	Node *next;
};
Node *head;
                                                                      // 100 ->  |7|0| ->   
void insert(int data,int n)
{
	Node *temp1=(Node*)malloc(sizeof(Node));  // 100         
	temp1->data=data; // 7
	temp1->next=head; // NULL
	if(n==1)
	{
		temp1->next=head;
		head=temp1;
		return;
	}
	Node* temp2=head;
	for (int i = 0; i <n-2; ++i)
	{
		temp2=temp2->next;
	}
	temp1->next=temp2->next;
	temp2->next=temp1;
}

void print()
{
	Node* temp=head;
	while(temp!=NULL)
	{
		printf("%d\n",temp->data);
		temp=temp->next;
	}
}
int main(int argc, char const *argv[])
{
	head=NULL;
	insert(7,1);   //7
	insert(10,2);  //7,10
	insert(15,3);  //15,7,10
	insert(22,4);  //15,22,7,10
	insert(77,5);  //77,15,22,7,10
	print();

	return 0;
}