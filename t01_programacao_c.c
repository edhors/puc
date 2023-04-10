#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

int** matrix0(int row, int col) {
	int** m = (int**)malloc(row * sizeof(int**));
	for (int i = 0; i < row; i++) {
		m[i] = (int*)malloc(col * sizeof(int*));
		for (int j = 0; j < col; j++)
			m[i][j] = 0;
	}
	return m;
}

void diagonal(int** m, int n, int row, int col) {
	for (int i = 0; i < row; i++) 
		for (int j = 0; j < col; j++) 
			if (i == j)
				m[i][j] = n;
}

int check(int** m, int row, int col) {
	if (row != col)
		return FALSE;
	for (int i = 0; i < row; i++)
		for (int j = 0; j < col; j++)
			if (i != j && m[i][j] != 0)
				return FALSE;
	return TRUE;
}

void freematrix(int** m, int row, int col) {
	for (int i = 0; i < row; i++)
		for (int j = 0; j < col; j++)
			free(m[i][j]);
}

void printm(int** m, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) 
			printf("%d ", m[i][j]);
		printf("\n");
	}
}

int main(void) {
	int** a = matrix0(10, 10);
	diagonal(a, 5, 10, 10);
	printm(a, 10, 10);
	printf("%d", check(a, 10, 10));
	freematrix(a, 10, 10);
	printm(a, 10, 10);

	return 0;
}
