#include "stdio.h"

// void SumofElements(int* s)
// {
// 	int sum=0;

// 	for (int i = 0; i < 5; ++i)
// 	{
// 		sum=sum+(*(s+i));
// 		//printf("%d\n",*(s+i) );
// 	}
// 	printf("%d\n",sum);
// }
// int main(int argc, char const *argv[])
// {

// 	int a[]={45,78,1,5,2};

// 	SumofElements(a);
// 	return 0;
// }







void SumofElements(int a[])
{
	printf("%d\n",a);
	printf("%d\t%d\n",sizeof(a),sizeof(a)/sizeof(a[0]));
	int sum=0;
	for (int i = 0; i < 5; ++i)
	{
		// printf("%d\n",a[i]);
		sum=sum+a[i];
	}
	printf("%d\n",sum );
}
int main(int argc, char const *argv[])
{
	int a[]={45,88,7,5,990};
	printf("%d\n",a); //address

	// printf("%d\n", sizeof(a));

	printf("%d\t%d\n",sizeof(a),sizeof(a)/sizeof(a[0]));

	SumofElements(a);


	return 0;
}

