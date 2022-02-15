#include <stdio.h>

// For the sleep functiopn
#include <unistd.h>

// For the atoi function that converts
// strings to integers
#include <stdlib.h>

int main(int ac, char **av) {
    if(ac != 2) {
        printf("\nCounts from specified integer n to n + 5\n");
        printf("Usage: %s <integer>\n\n", av[0]);
        exit(-1);
    }

    int n = atoi(av[1]);
    int i;
    for(i=n; i<=n+5; i++) {
        printf("%d\n", i);
        sleep(1);
    }

    printf("\nFinal value of i is %d\n\n", i);

    exit(i);
}


