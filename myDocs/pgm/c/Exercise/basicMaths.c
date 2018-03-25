#include "stdio.h"
int main(int argc, char const *argv[])
{
	int num1,num2,choice;
	printf("Basic Maths\n");
	printf("Enter the num1\n");
	scanf("%d",&num1);
	printf("Enter the num2\n");
	scanf("%d",&num2);
	printf("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n");
	printf("Enter your choice\n");
	scanf("%d",&choice);
	/*if (choice==1)
		printf("Addition=%d\n",num1+num2);
	else if (choice==2)
		printf("Subtraction=%d\n",num1-num2);
	else if (choice==3)
		printf("Multiplication=%d\n",num1*num2);
	else if (choice==4)
		printf("Division=%d\n",num1/num2);
	else
		printf("Modulus=%d\n",num1%num2);*/
	switch(choice)
	{
		case 1: printf("Addition=%d\n",num1+num2);
				break;
		case 2: printf("Subtraction=%d\n",num1-num2);
				break;
		case 3: printf("Multiplication=%d\n",num1*num2);
				break;
		case 4: printf("Division=%d\n",num1/num2);
				break;
		case 5: printf("Modulus=%d\n",num1%num2);
				break;
		default: printf("No Operation\n");
				 break;
	}
	return 0;
}