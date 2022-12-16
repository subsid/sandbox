#include <stdio.h>

char* display(char* str, int age) {
  printf("My Name is %s and my Age is %d\n", str, age);

  return "Completed";
}

int loop(int from, int to)
{
  int i;
  int s = 0;
 
  for (i = from; i < to; i++)
    if (i % 3 == 0)
      s += i;

  return s;
}
