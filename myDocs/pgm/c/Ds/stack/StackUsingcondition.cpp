#include "stdlib.h"
#include "iostream"
#include "stack"
#include "stdio.h"
using namespace std;

struct Node
{
	char data;
	Node *next;
};
struct Node* head;

stack<char> s;
void Insert(char data[],int n)
{
	char oper1,oper2;
	int oper3;
	int i;
	for (i = 0; i < n; ++i)
	{

		// if((data[i]!='*') && (data[i]!='+') && (data[i]!='-'))
		if((data[i]>='0') && (data[i]<='9'))
		{
			s.push(data[i]);
		}
		else if((data[i]=='*'))
		{

			oper2=s.top();     //
			s.pop();
			oper1=s.top();
			s.pop();
			oper3=(oper1-'0')*(oper2-'0');
			// printf("b=%c\n",oper3);
			oper3=oper3+'0';             // must have to convert into character 
			// printf("a=%c\n",oper3);
			s.push(oper3);
		}
		else if((data[i]=='-'))
		{
			oper2=s.top();
			s.pop();
			oper1=s.top();
			s.pop();
			oper3=(oper1-'0')-(oper2-'0');
			oper3=oper3+'0'; 
			s.push(oper3);
		}
		else
		{
			oper2=s.top();     //
			s.pop();
			oper1=s.top();
			s.pop();
			oper3=(oper1-'0')+(oper2-'0');
			oper3=oper3+'0'; 
			s.push(oper3);

		}
	}
}

char Top()
{
	return s.top();
}

char* HigherPrecedence(char top,char oper1)
{
	char tempCharArr[]="";
	if((top=='*'))
	{
		
		while(!s.empty())
		{

			tempCharArr=tempCharArr+s.top();
			s.pop();
		}
		return tempCharArr;
	}
	//s.push(oper1);
	return tempCharArr;
}

void InfixToPostfix(char Exp[],int n)
{
	char resArr[]="";
	for (int i = 0; i < n; ++i)
	{
		printf("%c\t",Exp[i]);
		
		if((Exp[i]>='A') && (Exp[i]<='Z'))     //{'A','+','B','*','C','-','D','*','E'};
		{
			resArr=resArr+Exp[i];
		}
		else if(!s.empty())
		{
			
			char resultArr[20]=HigherPrecedence(s.top(),Exp[i]);   // + , * 
			resArr=resArr+resultArr;
			s.push(Exp[i]);
		}
		else{
			s.push(Exp[i]); // insert operator in stack
		}
		
	}
	while(!s.empty())   // get remining element in stack
	{
		resArr=resArr+s.top();
		s.pop();
	}
	printf("\n");
	printf("%s\n",resArr);
}

int main(int argc, char const *argv[])
{

	/*char Arr[9]={'9','5','*','7','5','*','+','5','-'};   // 4 4 + 5 - // 8 5 - // 3 
	Insert(Arr,9);

	printf("%d",Top()-'0');
	printf("\n");*/


	char Exp[9]={'A','+','B','*','C','-','D','*','E'};

	InfixToPostfix(Exp,9);

	// for (int i = 0; i < 9; ++i)
	// {
	// 	if(i%2==1)	
	// 	{


	// 		printf("%c-----%d\n",Exp[i],Exp[i] );
	// 	}
	// }

	

	return 0;
}