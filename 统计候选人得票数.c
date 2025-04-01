#include <stdio.h>
#include <string.h>

struct Candidate {
    char name[20];
    int votes;
};

int main() {
    struct Candidate candidates[5] = {{"zhang", 0}, {"wang", 0}, {"li", 0}, {"zhao", 0}, {"liu", 0}};
    char vote[20];
    int numVotes;
    numVotes = 0;
    printf("请输入投票结果 (输入'结束'停止):\n");
    while (1) {
        scanf("%s", vote);
        if (strcmp(vote, "结束") == 0) break;
        for (int i = 0; i < 5; i++) {
            if (strcmp(vote, candidates[i].name) == 0) {
                candidates[i].votes++;
                numVotes++;
                break;
            }
        }
    }
    
    printf("投票统计结果:\n");
    for (int i = 0; i < 5; i++) {
        printf("%s: %d 票\n", candidates[i].name, candidates[i].votes);
    }
    return 0;
}
