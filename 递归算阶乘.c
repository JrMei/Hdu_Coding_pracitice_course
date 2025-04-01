#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int sumFactorials(int n) {
    if (n <= 0) return 0;
    return factorial(n) + sumFactorials(n - 2);
}

int main() {
    int n;
    printf("请输入一个正整数: ");
    scanf("%d", &n);
    printf("结果: %d\n", sumFactorials(n));
    return 0;
}
