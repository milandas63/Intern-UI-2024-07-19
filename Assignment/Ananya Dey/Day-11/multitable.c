#include<stdio.h>
#include<conio.h>
int main()
{
	int i,j,m;
	for(i=2;i<=10;i++)
	{
		for(j=1;j<=10;j++)
		{
			m = i*j;
			printf("%dx%d=%d\t",i,j,m);
		}
		printf("\n");
	}
	return(0);
 } 
