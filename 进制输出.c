#include <stdio.h>

int main() {
    int num;
    printf("请输入一个整数: ");
    scanf("%d", &num);
    printf("无符号: %u\n", (unsigned int)num);
    printf("八进制: %o\n", num);
    printf("十六进制: %x\n", num);
    return 0;
}
