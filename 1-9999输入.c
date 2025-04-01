#include <stdio.h>

int main() {
    int number;
    short position1, position2, position3, position4;
    printf("请输入1-9999之间的正整数: ");
    scanf("%d", &number);
    position1 = number / 1000;
    position2 = (number % 1000) / 100;
    position3 = (number % 100) / 10;
    position4 = number % 10;
    printf("千位: %d\n", position1);
    printf("百位: %d\n", position2);
    printf("十位: %d\n", position3);
    printf("个位: %d\n", position4);
    return 0;
}
