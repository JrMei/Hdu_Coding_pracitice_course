#include <stdio.h>

int main() {
    float R1, R2;
    printf("请输入两个电阻值: ");
    scanf("%f %f", &R1, &R2);
    printf("串联电阻值: %.2f\n", R1 + R2);
    printf("并联电阻值: %.2f\n", (R1 * R2) / (R1 + R2));
    return 0;
}
