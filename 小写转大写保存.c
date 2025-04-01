#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    FILE *file;
    printf("请输入一个字符串 (以'!'结束): ");
    scanf("%[^!]s", str);
    file = fopen("test.txt", "w");
    if (file == NULL) {
        printf("无法打开文件!\n");
        return 1;
    }
    for (int i = 0; str[i] != '\0'; i++) {
        fputc(toupper(str[i]), file);
    }
    fclose(file);
    printf("字符串已保存到文件 'test.txt'\n");
    return 0;
}
