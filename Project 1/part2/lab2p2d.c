#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/wait.h>

int main() {
    int fp_in = open("./file.txt", O_RDONLY);
    int fp_out = open("./talk.out", O_CREAT | O_WRONLY);

    if(fork() == 0) {
        dup2(fp_in, STDIN_FILENO);
        dup2(fp_out, STDOUT_FILENO);
        execlp("./talk", "talk", (char *) 0);
        close(fp_in);
        close(fp_out);
    }
    else
        wait(NULL);

}



