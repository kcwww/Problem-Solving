#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int num = 0;
	scanf("%d", &num);
	int* weight = (int*)malloc(sizeof(int) * num);
	int* tall = (int*)malloc(sizeof(int) * num);
	int* ans = (int*)malloc(sizeof(int) * num);
	
	for (int i = 0; i < num; i++) {
		scanf("%d %d", &weight[i], &tall[i]);
		ans[i] = 1;
	}
	


	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			if (i == j) continue;
			
			if (weight[i] < weight[j] && tall[i] < tall[j]) ans[i]++;
		}
	}


	for (int i = 0; i < num; i++) {
		printf("%d ", ans[i]);
	}

	free(weight);
	free(tall);
	free(ans);

	return 0;
}
