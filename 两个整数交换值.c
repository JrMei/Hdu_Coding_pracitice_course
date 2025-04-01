#include <stdio.h>

int main() {
    int a, b, temp;
    printf("请输入两个整数: ");
    scanf("%d %d", &a, &b);
    printf("交换前: a = %d, b = %d\n", a, b);
    temp = a;
    a = b;
    b = temp;
    printf("交换后: a = %d, b = %d\n", a, b);
    return 0;
}
