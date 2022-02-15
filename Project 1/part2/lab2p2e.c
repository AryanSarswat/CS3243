#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>

int main() {
    int p[2];
    char str[] = "Hello this is the parent."

    // This creates a pipe. p[0] is the reading end,
    // p[1] is the writing end.

    if(pipe(p) < 0) 
        perror("lab2p2e: ");

    // We will send a message from father to child
    if(fork() != 0) {
        close(p[0]); // The the end we are not using.
        write(p[1], str, strlen(str));
        close(p[1]);
        wait(NULL);
    }
    else
    {
        char buffer[128];

        close(p[1]); // Close the writing end
        read(p[0], buffer, 127);
        printf("Child got the message \"%s\"\n", buffer);
        close(p[0]);
    }
}

