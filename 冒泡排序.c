#include <stdio.h>

void bubble_Sort(int arr[], int n) {
    int temp;
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[10];
    printf("请输入10个整型数:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }
    bubble_Sort(arr, 10);
    printf("排序后的数组: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
