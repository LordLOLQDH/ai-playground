c
#include <windows.h>

void shutdown() {
    // Implement your shutdown logic here
    MessageBox(NULL, "Shutdown initiated", "Shutdown", MB_OK);
}

int main() {
    // Register the shutdown function as a system event handler
    SetConsoleCtrlHandler((PHANDLER_ROUTINE)shutdown, TRUE);

    // Wait for the system to be shut down
    WaitForSingleObject(INFINITE, NULL);

    return 0;
}