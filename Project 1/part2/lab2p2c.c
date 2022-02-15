#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    if(fork() ==  0) {
        char *args[] = {"cat", "file.txt", NULL};
        execvp("cat", args);
    }
    else
        wait(NULL);
}