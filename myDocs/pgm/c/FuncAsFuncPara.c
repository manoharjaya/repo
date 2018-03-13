    #include "stdio.h"
    int f(int g()) {
    	printf("f\n");
        return 2*g();
    }
    int x() {
    	printf("x\n");
       return 12;
    }
    int main() {
       int n = f(x);
       printf("%d\n",n );
    }



manoharjaya

!@12QWqw


