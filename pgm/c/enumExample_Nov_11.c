#include "stdio.h"
void main()
{
	int nid=0;
	enum MONTH
	{
		jan=1,feb,mar,april,may,june,july,aug,sep,oct,nov,dec
	};
	enum MONTH month=july;
	if(month==7)
		printf("%d\n",month);
	// printf("%s\n","enumExample_Nov_11");
	
}