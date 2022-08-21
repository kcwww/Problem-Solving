#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

char chess[51][51];

int checkchess1(int i, int k) {
	int count = 0;


	for (int j = i; j < i + 8; j++) {
		for (int m = k; m < k + 8; m++) {
			if (j % 2 == 0) {
				if (m % 2 == 0) {
					if (chess[j][m] != 'B') count++;
				}
				else {
					if (chess[j][m] != 'W') count++;
				}
			}
			else {
				if (m % 2 == 0) {
					if (chess[j][m] != 'W') count++;
				}
				else {
					if (chess[j][m] != 'B') count++;
				}
			}

		}

	}

	return count;


}

int checkchess2(int i, int k) {
	int count = 0;


	for (int j = i; j < i + 8; j++) {
		for (int m = k; m < k + 8; m++) {
			if (j % 2 == 0) {
				if (m % 2 == 0) {
					if (chess[j][m] != 'W') count++;
				}
				else {
					if (chess[j][m] != 'B') count++;
				}
			}
			else {
				if (m % 2 == 0) {
					if (chess[j][m] != 'B') count++;
				}
				else {
					if (chess[j][m] != 'W') count++;
				}
			}

		}

	}

	return count;


}





int main() {

	int row = 0, col = 0;
	scanf("%d %d", &row, &col);
	
	for(int i = 0; i < row; i++) scanf("%s", &chess[i]);

	int count = 0;
	int min1 = 32, min2 = 32;
	
	//BW
	for (int k = 0; k <= col - 8; k++) {
		for (int i = 0; i <= row - 8; i++) {

		    count =	checkchess1(i, k);
			min1 = min1 < count ? min1 : count;



		}
	}

	//WB
	for (int k = 0; k <= col - 8; k++) {
		for (int i = 0; i <= row - 8; i++) {

			count = checkchess2(i, k);
			min2 = min2 < count ? min2 : count;



		}
	}
	printf("%d", min1 < min2 ? min1 : min2);
	
}
