#include <stdio.h>
#include <stdlib.h>

struct Node {
    int num;
    struct Node *next;
};

struct Node* createList() {
    struct Node *head = (struct Node*)malloc(sizeof(struct Node));
    struct Node *tail = head;
    tail->next = NULL;
    int num;
    printf("请输入节点的值 (输入-1结束): ");
    while (1) {
        scanf("%d", &num);
        if (num == -1) break;
        struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->num = num;
        newNode->next = NULL;
        tail->next = newNode;
        tail = newNode;
    }
    return head;
}

int countNodes(struct Node *head, int num) {
    int count = 0;
    struct Node *current = head->next;
    while (current != NULL) {
        if (current->num == num) count++;
        current = current->next;
    }
    return count;
}

int main() {
    struct Node *head = createList();
    int num;
    printf("请输入要统计的节点值: ");
    scanf("%d", &num);
    printf("值为%d的节点个数: %d\n", num, countNodes(head, num));
    return 0;
}
