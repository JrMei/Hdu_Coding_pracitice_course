#include <stdio.h>

int main() {
    int scores[10];
    int sum = 0;
    float average;
    printf("请输入10位学生的成绩:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &scores[i]);
        sum += scores[i];
    }
    average = sum / 10.0;
    printf("平均分: %.2f\n", average);
    printf("高于平均分的成绩:\n");
    for (int i = 0; i < 10; i++) {
        if (scores[i] > average) {
            printf("%d ", scores[i]);
        }
    }
    return 0;
}
