c
#include <stdio.h>
#include <unistd.h>

int main() {
 // Simulate a 10-second shutdown
    system("shutdown -h now"); // Execute the shutdown command
    return 0;
}
