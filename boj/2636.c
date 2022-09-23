#include <stdio.h>

int n, m;
int map[101][101] = { 0, };

int row[4] = { -1,1,0,0 };
int col[4] = { 0,0,-1,1 };

void airOut(int ac[][101], int sero, int garo) {
	ac[sero][garo] = 1;

	for (int i = 0; i < 4; i++) {
		int ny = sero + row[i];
		int nx = garo + col[i];

		if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
			if (map[ny][nx] == 0 && ac[ny][nx] == 0)
				airOut(ac, ny, nx);
		}
	}
}

int main(void) {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			scanf("%d", &map[i][j]);
	}

	int time = 0;
    int pre_rcn = 0;

	while (1) {
		int air_check[101][101] = { 0, };
		airOut(air_check, 0, 0);
		int remove_ch[10000][2] = { 0, };
		int remove_ch_num = 0;

		for (int i = 1; i < n - 1; i++) {
			for (int j = 1; j < m - 1; j++) {
				if (map[i][j] == 1) {
					for (int d = 0; d < 4; d++) {
						int cy = i + row[d];
						int cx = j + col[d];

						if (cy >= 0 && cy < n && cx >= 0 && cx < m) {
							if (air_check[cy][cx] == 1) {
								remove_ch[remove_ch_num][0] = i;
								remove_ch[remove_ch_num++][1] = j;
								break;
							}
						}
					}
				}
			}
		}

		if (remove_ch_num == 0) break;
		pre_rcn = remove_ch_num;

		for (int r = 0; r < remove_ch_num; r++)
			map[remove_ch[r][0]][remove_ch[r][1]] = 0;

		time++;
	}
	printf("%d\n%d", time, pre_rcn);
	return 0;
}
