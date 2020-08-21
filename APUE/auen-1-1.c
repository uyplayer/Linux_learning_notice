#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    putchar('a');
    write(1, "b", 1);
    putchar('a');
    write(1, "b", 1);
    putchar('a');
    write(1, "b", 1);
    printf("\n");

return 0;
}
