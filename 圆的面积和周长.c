#include <stdio.h>
#define PI 3.141592653589793

int main() {
    double r;
    int k;
    printf("请输入圆的半径: ");
    scanf("%lf", &r);
    printf("请输入一个整型数 (1: 面积, 2: 周长, 3: 面积和周长): ");
    scanf("%d", &k);
    switch (k) {
        case 1:
            printf("圆的面积: %.2f\n", PI * r * r);
            break;
        case 2:
            printf("圆的周长: %.2f\n", 2 * PI * r);
            break;
        case 3:
            printf("圆的面积: %.2f\n", PI * r * r);
            printf("圆的周长: %.2f\n", 2 * PI * r);
            break;
        default:
            printf("无效输入\n");
            break;
    }
    return 0;
}
