#include "stdio.h"
#include "stdlib.h"
struct Node
{
        int data;
        struct Node *next;
};

void Print(struct Node* head)
{
        printf("List are:\n");
        while(head!=NULL)
        {
                printf("%d\t",head->data);
                head=head->next;
        }
        printf("\n");
}

void Insert(Node** head,int x)
{
        struct Node *temp=(struct Node*)malloc(sizeof(struct Node));
        temp->data=x;
        temp->next=*head;
        head=temp;
}
void main()
{
	int num=0,i=0,x;
	struct Node* head=NULL; 
	printf("How many no?\n");
        scanf("%d",&num);
        for(i=0;i<num;i++)
        {
                printf("Enter the no:");
                scanf("%d",&x);
                Insert(&head,x);
                Print(head);
        }
}                                                                          