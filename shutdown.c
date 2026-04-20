c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Shutting down the computer...\n");
    sleep(10); // Simulate a 10-second shutdown
    system("shutdown -h now"); // Execute the shutdown command
    return 0;
}