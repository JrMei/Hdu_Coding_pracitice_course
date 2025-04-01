#include <stdio.h>

int main() {
    double num;
    printf("请输入一个double类型的数: ");
    scanf("%lf", &num);
    printf("保留两位小数: %.2f\n", num);
    return 0;
}
