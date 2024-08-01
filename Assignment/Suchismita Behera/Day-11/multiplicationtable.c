#include<stdio.h>
#include<conio.h>
int main()
{
	int a,b,r;
	for(a=2;a<=10;a++)
	{
		for(b=1;b<=10;b++)
		{
			r = a*b;
			printf("%dx%d=%d\t",a,b,r);
		}
		printf("\n");
	}
	return(0);
 } 

