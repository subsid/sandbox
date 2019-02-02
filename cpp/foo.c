#include <stdio.h>
#include <stdlib.h>

int main() {
  int* a = (int*) malloc(sizeof(int)*3);
  /* a[11] = 2; */

  printf("%d", a[10000000]);

  return 0;
}
