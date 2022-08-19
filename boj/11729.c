#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

void move(int num, int start, int end) {
	int temp = start;

	printf("%d %d\n", start, end);

}


void hanoi(int N, int start, int end, char via) {

	if (N == 1) {
		move(1, start, end);
		return 0;
	}
	else {
		hanoi(N - 1, start, via, end);
		move(N, start, end);
		hanoi(N - 1, via, end, start);
	}


}



int main() {

	int num = 0, k = 0;
	scanf("%d", &num);
	k = pow(2, num) - 1;
	printf("%d\n",k);
	hanoi(num, 1, 3, 2);






	return 0;
}
