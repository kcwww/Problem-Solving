#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int n;

void Power(int x, int n, char arr[]) {
	int temp = 0, last = 0, cnt = 0;
	arr[0] = 1;

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= last; j++) {
			temp = arr[j] * x;
			if (temp >= 10) {
				arr[j] = temp % 10 + cnt;
				cnt = temp / 10;

				if (j == last) {
					arr[++last] = cnt;
					cnt = 0;
					break;
				}
			}
			else {
				arr[j] = temp + cnt;
				cnt = 0;
			}
		}
	}
	arr[0] -= 1;
	for (int i = last; i >= 0; i--) printf("%d", arr[i]);
	printf("\n");
}

void func(int n, int a, int b) {
	if (n == 1) {
		printf("%d %d\n", a, b);
		return;
	}

	func(n - 1, a, 6 - a- b);
	printf("%d %d\n", a, b);
	func(n - 1, 6 - a - b, b);
}

int main() {
	char result[35];

	scanf("%d", &n);
	Power(2, n, result);

	if (n > 20) return 0;
	func(n, 1, 3);

	return 0;
}
