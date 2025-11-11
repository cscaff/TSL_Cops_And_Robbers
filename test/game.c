#include <stdio.h>
#include <stdlib.h>

#define main controller_main
#include "../src/controller/controller.c"
#undef main

int main(void) {
    printf("=== Controller test harness ===\n");

    controller_main();

    return 0;
}