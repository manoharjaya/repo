#include "stdio.h"
#include "string.h"
void Print(char *temp)
{
	int i=0;
	// while(temp[i]!='\0')    //1
	// {
	// 	printf("%c\n",temp[i]);
	// 	i++;	
	// }
	// while(*(temp+i)!='\0')  //2
	// {
	// 	printf("%c\n",*(temp+i));
	// 	i++;	
	// }
	while(*temp!='\0')  //3
	{
		printf("%c\n",*temp);
		temp++;	
	}

}
int main(int argc, char const *argv[])
{
	char carray[4];
	carray[0]='m';
	carray[1]='a';
	carray[2]='n';
	carray[3]='o';
	carray[4]='\0';
	printf("%s\n",carray);

	printf("%d\n",sizeof(carray) );

	char cstr[8]="manohar";    // string size is should be greater than the size of  an index ..	
								//  in this string string is manohar len is 7 eg:"manohar" when we declare as index is 7  eg: cstr[7] is should 
								// throw an error..
	printf("%d\n",sizeof(cstr) );
	printf("%d\n", strlen(cstr));

	char *cpointer;
	cpointer=cstr;

	printf("%d\n", cstr);

	printf("%d\n", (cpointer));


	printf("%c\n",*(cpointer+4));

	*(cpointer+4)='j';

	printf("%c\n",*(cpointer+4));

	printf("%s\n",cpointer);

	cpointer[4]='h';

	printf("%s\n", cpointer);

	Print(carray);

	return 0;
}