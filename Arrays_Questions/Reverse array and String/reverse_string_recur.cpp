#include<stdio.h>

void reverse_string(int *str){
	if(*str){
		reverse_string(str +1);
		printf("%i ",*str );
	}
}

int main()
{
	int a[] = {1,2,3,4,5,6,'\0'};
	reverse_string(a);
	return 0;
}
