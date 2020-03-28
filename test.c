#include<stdio.h>
#pragma warning(disable : 4996)
int main()
{
	printf("Welcome to use this calc\nPlease enter the first number!\n");
	int a,b,d;
	char c;
	c = "N";
	scanf("%d", &a);
	printf("Please enter the second number!\n");
	scanf("%d", &b);
	printf("Do you want to plus them?(Y/N)\n");
	scanf("%c", &c);
	if (c = "Y")
	{
		d = a + b;
		printf("%d+%d=%d",a,b,d);
	}
	else
	{
		printf("Sorry,something wrong was happened,The software will shutdown!\n");
	}
	getchar();
	return 0;
}