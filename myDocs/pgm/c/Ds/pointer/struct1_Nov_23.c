#include "stdio.h"
#include "string.h"


struct Employee
{
	int eno;
	char ename[20];
	char occu[20];

}emp1,emp2;

// void display(struct Employee emp);
void display(struct Employee *emp);
void  main(int argc, char const *argv[])
{
	printf("%d\n",sizeof(5.25));

	struct Employee emp3[5];

	emp3[0].eno=003;
	strcpy(emp3[0].ename,"jaya");
	strcpy(emp3[0].occu,"I can I will");

	emp1.eno=001;
	strcpy(emp1.ename,"Manohar");
	strcpy(emp1.occu,"Data Scientist");

	emp2.eno=002;
	strcpy(emp2.ename,"Mano");
	strcpy(emp2.occu,"Programmer..");


	// printf("%d\n",emp1.eno);
	// printf("%s\n",emp1.ename );
	// printf("%s\n",emp1.occu );

	// printf("%d\n",emp2.eno);
	// printf("%s\n",emp2.ename );
	// printf("%s\n",emp2.occu );
	printf("---------------------------------------------------\n");

	printf("%d\n",sizeof(emp1));

	printf("---------------------------------------------------\n");

	// display(emp1);
	display(&emp1);
	

	printf("---------------------------------------------------\n");


	// display(emp2);
	display(&emp2);
	printf("---------------------------------------------------\n");

	printf("---------------------------------------------------\n");


	// display(emp2);
	display(emp3);
	printf("---------------------------------------------------\n");

	return;
}


// void display(struct Employee emp)
// {
// 	printf("%d\n",emp.eno);
// 	printf("%s\n",emp.ename );
// 	printf("%s\n",emp.occu );

// }	

void display(struct Employee *emp)
{
	printf("%d\n",emp->eno);
	printf("%s\n",emp->ename );
	printf("%s\n",emp->occu );

}