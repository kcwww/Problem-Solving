#define _CRT_SECURE_NO_WARNINGS
#include <stdio,h>

int main() {
	int num = 0, num2 = 0, count = 0, temp = 0; ans = 0;
	scanf("%d %d", &num, &num2);

	temp = num;

	while (temp) {
		if (temp % 10 == 8) count++;
		temp /= 10;
	}
	temp = count;
	count = 0;

	for(int i = num; i <= num2; i++) {
		ans = i;
		while(ans){
			if(ans % 10 == 8) count++;
			ans /= 10;
		}

		temp = temp > count ? count : temp;
		if(count == 0) break;
		count = 0;

	}

	printf("%d",temp);
	
	return 0;
}
