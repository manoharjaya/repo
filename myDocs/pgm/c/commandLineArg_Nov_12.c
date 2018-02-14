#include "stdio.h"
void main(int a, char *ds[])
{

  printf("%s\n", "verbose");


   printf("\n Program name  : %s \n", ds[0]);
   printf("1st arg  : %s \n", ds[1]);
   printf("2nd arg  : %s \n", ds[2]);
   printf("3rd arg  : %s \n", ds[3]);
   printf("4th arg  : %s \n", ds[4]);
   printf("5th arg  : %s \n", ds[5]);
   printf("%d\n",a);
 if(a>7)
  	{
  		printf("%s\n","greater than 7" );
  	}

}