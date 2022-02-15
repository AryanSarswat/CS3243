#include <stdio.h>

#define BUF_SIZE    128

int main() {
    char input[128];
    char *ret;
    while(!feof(stdin)) {
        ret = fgets(input, BUF_SIZE - 1, stdin);
        if(ret != NULL)
            printf("This is what I read: %s\n", input);
    }
}
