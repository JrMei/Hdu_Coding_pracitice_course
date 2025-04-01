#include <stdio.h>

int main() {
    int count = 0;
    printf("2000年到3000年的闰年:\n");
    for (int year = 2000; year <= 3000; year++) {
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            printf("%d ", year);
            count++;
            if (count % 10 == 0) printf("\n");
        }
    }
    printf("\n总共 %d 个闰年\n", count);
    return 0;
}
