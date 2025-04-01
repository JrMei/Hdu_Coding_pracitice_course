#include <stdio.h>

int main() {
    int stairs = 1;
    while (1) {
        if (stairs % 2 == 1 &&
            stairs % 3 == 2 &&
            stairs % 5 == 4 &&
            stairs % 6 == 5 &&
            stairs % 7 == 0) {
            break;
        }
        stairs++;
    }
    printf("共有%d阶梯\n", stairs);
    return 0;
}
