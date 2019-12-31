#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {

  int choice = 0;

  if (!isatty(fileno(stdout))) {

    fprintf(stderr,”You are not a terminal!\n”);
    exit(1);
  }
  do {
    choice = getchoice(“Please select an action”, menu);
    printf(“You have chosen: %c\n”, choice);
    } while(choice != ‘q’);
    exit(0);



  return 0;
}
