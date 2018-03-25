#include "stdio.h"
#define Max 11
int Arr[10];
int front=-1,rear=-1;

bool IsEmpty()
{
	if((front==-1)&&(rear==-1))
	{
		printf("%s\n","queue is Empty");
		return true;
	}
	return false;
}

bool IsFull()
{
	if(rear==Max-1)
	{
		printf("%s\n", "queue is full");
		return true;
	}
	return false;
}

int queuePeek()
{
	return Arr[rear];
}

int queueFront()
{
	return Arr[front];
}

void enQueue(int data)
{
	// if(IsFull())       // check if queue is full 
	if(((rear+1)%10)==front)
	{
		printf("%s\n","inside isfull" );
		return;
	}
	else if(IsEmpty())      // check if queue is empty
	{
		front=rear=0;
		// Arr[rear]=data;     |
	}						 //|
	else                     //|        use one line Arr[rear]=data  in line 47
	{                        //|
		rear=rear+1;         //|
		// rear=(rear+1)%(sizeof(Arr[10])/sizeof(int));   
		// Arr[rear]=data;   //|
	}
	Arr[rear]=data;    
	printf("arr=%d\n",Arr[rear]);
}

void deQueue()
{
	if (IsEmpty())   // queue is empty 
	{ 
		return;
	}
	else if(front==rear)   // when fornt and rear is equal check if 1==4   
	{
		// printf("inside front==rear%d\t%d\n",front,rear);
		front=rear=-1;
	}
	else
		front=front+1;   // 1 2 3 4
		// front=(front+1)%(sizeof(Arr[10])/sizeof(int));
}

int main(int argc, char const *argv[])
{

    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);
    enQueue(6);
    enQueue(7);
    enQueue(8);
    enQueue(9);
    enQueue(10);
    enQueue(11);  // queue if full when (rear+1)%10==0    if rear = 9 and front=0



 	/*printf("peek=%d\n",queuePeek());
    deQueue();
    printf("front afetr deQueue=%d\n",queueFront());
    deQueue();
    printf("frot after deQueue=%d\n",queueFront());
    deQueue();
    deQueue();
    deQueue();  // set front and rear is -1  

    deQueue();  // queue is empty
    deQueue();*/
    
	// printf("%s\n", "hello manohar");

	return 0;
}