c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Shutting down...\n");
    sleep(5); // Simulate a 5-second delay
    system("shutdown -h now"); // Shutdown the computer immediately
    return 0;
}