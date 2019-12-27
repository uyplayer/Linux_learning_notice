#include "stdio.h"
#include "stdlib.h"

int main(int argc, char const *argv[]) {

  int c ;
  FILE *in , *out;

  in = fopen("file.n","r")
  out = fopen("file.out","w")

  while ((c = fgetc(in)) != EOF ) {
    /* code */
    fputc(c,out)
      
  }


  return 0;
}
