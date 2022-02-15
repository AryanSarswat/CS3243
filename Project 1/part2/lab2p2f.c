#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h>

int main() {

    printf("Be patient, the program will take around 7 seconds to run.\n");
    printf("At the end you can do \"cat results.out\" to see the result.\n");

    //
    // Add code here to pipe from ./slow 5 to ./talk and redirect
    // output of ./talk to results.out
    // I.e. your program should do the equivalent of ./slow 5 | talk > results.out
    // WITHOUT using | and > from the shell.
    //
    int p[2];
    int fp_out = open("./results.out", O_CREAT | O_WRONLY);

    if(pipe(p) < 0) 
        perror("lab2p2e: ");

    if(fork() == 0) {
        close(p[0]); // Close the reading end
        dup2(p[1], 1); // Redirect stdout to the writing end of the pipe
        execlp("./slow", "slow", "5", NULL);
        close(p[1]);
    }
    else {
        close(p[1]); // Close the writing end
        wait(NULL); // Wait for child to send the string

        dup2(p[0], STDIN_FILENO); // Redirect stdin to the reading end of the pipe
        dup2(fp_out, STDOUT_FILENO); // Redirect stdout to the file
        
        execlp("./talk", "talk", (char *) 0);

        close(p[0]);
        close(fp_out);
    }
}

