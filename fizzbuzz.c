#include <stdio.h>

int main(void)
{
	int i;
	for (i = 0; i < 100; i+=1) {
		if ((i % 3) == 0) printf("fizz\n");
		else if ((i%5) == 0) printf("buzz\n");
		else printf("%d\n", i);
	}

	return 0;
}

/*
	Test Plan for FizzBuzz
	
-
-
*/