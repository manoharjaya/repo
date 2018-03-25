#include "stdio.h"
void main()
{
	char ch;
	char str[25];
	float f=142.123456789;
	double d=142.123456789;
	unsigned  int nid=-152;
	printf("%s\n","readFromKeyBoard");
	printf("%s\n", "Enter the single key from keyboard");
	scanf("%c",&ch);
	printf("%s\n","Enter the sentence from keyboard.." );
	scanf("%s\n",&str);
	printf("%s\n","Your value is..");
	printf("ch=%c\tstr=%s\n",ch,str);

	printf("%d\n", sizeof(10));
	printf("%d\n", sizeof(float));
	printf("%d\n", sizeof(double));
	printf("%d\n", sizeof(char));
	printf("%f\n",f);
	printf("%lf\n",d );
	printf("%d\n",nid);



}