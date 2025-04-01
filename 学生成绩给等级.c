#include <stdio.h>

char getGrade(int score) {
    if (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else if (score >= 70) return 'C';
    else if (score >= 60) return 'D';
    else return 'E';
}

int main() {
    int score;
    printf("请输入学生成绩: ");
    scanf("%d", &score);
    printf("等级: %c\n", getGrade(score));
    return 0;
}
