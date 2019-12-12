#include <unistd.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  /* code */
 char buffer[128];
 int nread;

 nread = read(0, buffer, 128);

 if(nread == -1)
 write(2,"A read error has occurred\n",26);

 if((write(1,buffer,nread))!= nread)
    write(2,"A read error has occurred \n",27):
    
  return 0;
}
