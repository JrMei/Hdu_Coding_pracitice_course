#include <stdio.h>

struct Student {
    int id;
    char name[50];
    char gender[10];
    float score;
};

int main() {
    struct Student students[3];
    for (int i = 0; i < 3; i++) {
        printf("请输入第%d个学生的信息 (学号 姓名 性别 成绩):\n", i+1);
        scanf("%d %s %s %f", &students[i].id, students[i].name, students[i].gender, &students[i].score);
    }
    printf("学生信息:\n");
    for (int i = 0; i < 3; i++) {
        printf("学号: %d 姓名: %s 性别: %s 成绩: %.2f\n", students[i].id, students[i].name, students[i].gender, students[i].score);
    }
    return 0;
}
