int main(int argc, char const *argv[]) {


 char *topdie = ".";
 if (argc >=2)
  topdir=argv[1];

  printf(“Directory scan of %s\n”,topdir);
  printdir(topdir,0);
  printf(“done.\n”);  


  return 0;
}
