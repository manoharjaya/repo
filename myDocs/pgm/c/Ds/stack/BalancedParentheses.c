#include "stdio.h"
#include "stdlib.h"
struct Node
{
	char data;
	struct Node *next;
};
struct Node *head;
int Pop();
int CheckMatchValue();


void Push(char *Array,int no)
{
	int i;
	for ( i = 0; i < no; ++i)
	{

		if((Array[i]=='{') || (Array[i]=='[') || (Array[i]=='('))
		{
			struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
			temp->data=Array[i];
			temp->next=head;
			head=temp;
		}
		else if((Array[i]=='}') || (Array[i]==']') || (Array[i]==')'))
		{
			char c=Pop();
			
			printf("%c\n",c);

			int status=CheckMatchValue(c,Array[i]);
			if (status)
			{
				printf("%s\n", "balanced");
			}
			else
				 printf("%s\n", "Not balanced");

		}
		
	}
	
}

int CheckMatchValue(char c1,char c2)
{
	if((c1=='{') && (c2=='}'))
		return 1;
	else if((c1=='[') && (c2==']'))
		return 1;
	else if((c1=='(') && (c2==')'))
		return 1;
	else 
		return 0

}
int Pop()
{
	struct Node *temp=head;
	int c;

	if(temp==NULL){
		printf("Stack overflow n");
	     getchar();
	     exit(0);
	}
	else if(temp!=NULL){
		head=temp->next;
		c=temp->data;
		free(temp);
	}
	return c;
}

struct Node* Top()
{
	return head;
}

void Print()
{
	struct Node* temp=head;
	while(temp!=NULL)
	{
		printf("%c\t", temp->data);
		temp=temp->next;
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{

	head=NULL;
	printf("hello\n");

	// int Array[5]={1,2,3,4,5};
	char Array[7]="{[()]}";   // string should terminate with \0 atfer string 
	// char Array[6]={'{','[','(',')',']','}'};

	Push(Array,6);
	// Print();
	// Pop();
	// Pop();
	// Pop();
	// Print();
	// head=Top();
	// printf("%c\n",head->data);
	return 0;
}