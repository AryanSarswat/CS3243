#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "utils.h"

#define MAX_STR_LEN 128

void strip(char *str) {
    while(*str) {
        if(*str == '\n')
            *str = '\0';
        str++;
    }
}

int main() {
    char str[MAX_STR_LEN];
    int nums[128];
    int count=0;
    int res = 0;

    while(!feof(stdin)) {
        char *res = fgets(str, MAX_STR_LEN, stdin);

        if(res){
            strip(str);
            int val = atoi(str);

            if(val){
                nums[count++] = val;
            }
        }
    }

    res = sum(nums, count);
    printf("Item count is %d\n", count);
    printf("The sum is %d\n", res);
    exit(res);
}

