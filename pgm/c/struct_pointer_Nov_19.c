#include "stdio.h"
struct Employee
{
	
	char name[20];
	int age;
	char sub[20];

}emp={"Manohar jaya",23,"Data structure"};
int main(int argc, char const *argv[])
{
	struct Employee *empptr;
	printf("test=%d\n",sizeof(empptr));
	printf("%s\n","struct_pointer_Nov_19" );
	printf("%s\n",emp.name);
	printf("%d\n",emp.age);
	printf("%s\n",emp.sub);
	
	empptr=&emp;

	printf("--------------------------------------\n" );
	printf("%s\n",empptr->name);
	printf("%d\n",empptr->age);
	printf("%s\n",empptr->sub);
	
	printf("%d\n", sizeof(empptr));

	return 0;
}