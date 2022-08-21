#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n = 0;
	scanf("%d", &n);

	int start = 665;
	int val = 0;
	while (n) {
		start++;
		val = start;

		while (val >= 665) {

			if (val % 1000 == 666) {
				n--;
				break;
			}
			
			val /= 10;

		}
		
		

	}

	printf("%d", start);

}
