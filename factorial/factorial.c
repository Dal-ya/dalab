#include <stdio.h>
 
int GetFactorial(int num)
{
	int result = 1;
	int check = 1;

	if (num < 1 || num >10)
	{
		puts("ERROR: 1~10 값만 입력하세요");
		check = 0;
	}
	if (check = 1)
	{
		for (int i = 1; i <= num; ++i)
			result *= i;	
	}
 
	return result;
}
 
 
int main(void)
{
	printf("Factoral : %d\n", GetFactorial(1));
	printf("Factoral : %d\n", GetFactorial(5));
	printf("Factoral : %d\n", GetFactorial(11));
	printf("Factoral : %d\n", GetFactorial(10));
	
  return 0;
}

/*
---출력---
Factoral : 1
Factoral : 120
ERROR: 1~10 값만 입력하세요 
Factoral : 39916800
Factoral : 3628800
 */
