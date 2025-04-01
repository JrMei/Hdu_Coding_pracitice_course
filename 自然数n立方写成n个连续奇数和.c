#include <stdio.h>

void cubeSum(int n) {
    int sum = 0;
    printf("%d^3 = ", n);
    for (int i = 0; i < n; i++) {
        int num = n * n - n + 1 + 2 * i;
        sum += num;
        if (i != 0) printf(" + ");
        printf("%d", num);
    }
    printf(" = %d\n", sum);
}

int main() {
    int n;
    printf("请输入一个自然数: ");
    scanf("%d", &n);
    cubeSum(n);
    return 0;
}
