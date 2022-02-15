#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int slow(char *name, int time, int n) {
    for(int i=n; i<=n+4; i++) {
        printf("%s: i = %d\n", name, i);
        sleep(time);
    }
}

int main() {
    int id;

    if((id = fork()) != 0) {
        int stat;
        int my_id = getpid();
        int parent_id = getppid();
        printf("\nI am the parent.\n");
        printf("My ID is %d\n", my_id);
        printf("My parent's ID is %d\n", parent_id);
        printf("My child's ID is %d\n\n", id);
        slow("Parent", 1, 5);
        printf("\nWaiting for child to exit.\n");
        wait(&stat);
        printf("CHILD HAS EXITED WITH STATUS %d\n", WEXITSTATUS(stat));
    }
    else 
    {
        id = getpid();
        int parent_id = getppid();
        printf("\nI am the child.\n");
        printf("My ID is %d\n", id);
        printf("My parent's ID is %d\n\n", parent_id);
        slow("Child", 2, 10);
        exit(25);
    }
}


