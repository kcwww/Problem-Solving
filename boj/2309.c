#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int main() {
	int dwerf[9] = { 0, };
	for (int i = 0; i < 9; i++) scanf("%d", &dwerf[i]);

	int sum = 0, ans = 0;
	for (int i = 0; i < 9; i++) sum += dwerf[i];
	sum = sum - 100;

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			ans = dwerf[i] + dwerf[j];
			if (ans == sum && i != j) {
				dwerf[i] = 0;
				dwerf[j] = 0;
				break;
			}
			ans = 0;
		}
		if (ans != 0) break;
	}
	for (int k = 0; k < 7; k++) {
		int min = 100;
		for (int i = 0; i < 9; i++) {
			if (dwerf[i] == 0) continue;
			else min = min > dwerf[i] ? dwerf[i] : min;
		}
		printf("%d\n", min);

		for (int i = 0; i < 9; i++) {
			
			if (dwerf[i] == min) dwerf[i] = 0;
		}
	}



	return 0;
}
