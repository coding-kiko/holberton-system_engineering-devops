#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - jjjajajaja
 */

int infinite_while(void)
{
  while (1)
    {
      sleep(1);
    }
  return (0);
}

/**
 * main - jjjajajaja
 */

int main(void)
{
  pid_t child_pid;
  int i;

  while (i <= 4)
    {
      child_pid = fork ();
      (int)child_pid;
      if (child_pid > 0)
	{
	  sleep (1);
	  printf("Zombie process created, PID: %i\n", child_pid);
	}
      else
	{
	  exit (0);
	}
      i++;
    }
  infinite_while();
}
