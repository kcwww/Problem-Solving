#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int count = 0;
int n;
int board[15];


int promising(int row) {

	
	for (int i = 0; i < row; i++) {
		if (board[row] == board[i] || row - i == abs(board[row] - board[i])) {
			return 0;
		}
	}
	return 1;
}


void n_queens(int row) {

	
	if (row == n) {
		count++;
		return;
	}

	for (int i = 0; i < n; i++) {
		board[row] = i; 	
		
		if (promising(row)) { 
			n_queens(row + 1); 
		}
	}
}

int main() {

	scanf("%d", &n);
	n_queens(0);
	printf("%d", count);

}
