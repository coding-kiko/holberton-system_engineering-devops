#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - jjjajajaja
 * Return: 0
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
 * Return: 1
 */

int main(void)
{
	pid_t child_pid;
	int i = 0;

	while (i <= 4)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %i\n", (int)child_pid);
		}
		else
		{
			exit(0);
		}
		i++;
	}
	infinite_while();
}
