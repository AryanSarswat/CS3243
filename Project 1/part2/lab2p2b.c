#include <stdio.h>

int main(int ac, char **av, char **vp) {
    printf("ac = %d\n", ac);
    printf("Arguments:\n");

    int i;

    for(i=0; i<ac; i++)
        printf("Arg %d is %s\n", i, av[i]);

    i=0;
    while(vp[i] != NULL) {
        printf("Env %d is %s\n", i, vp[i]);
        i++;
    }
}
