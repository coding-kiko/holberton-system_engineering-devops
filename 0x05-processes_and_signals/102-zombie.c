#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite while
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
 * main - main func
 * Return: 1
 */

int main(void)
{
	pid_t c1, c2, c3, c4, c5;

	c1 = fork();
	if (c1 > 0)
		printf("Zombie process created, PID: %d\n", c1);
	else
		exit(0);
	c2 = fork();
	if (c2 > 0)
		printf("Zombie process created, PID: %d\n", c2);
	else
		exit(0);
	c3 = fork();
	if (c3 > 0)
		printf("Zombie process created, PID: %d\n", c3);
	else
	{
		exit(0);
	}
	c4 = fork();
	if (c4 > 0)
	{
		printf("Zombie process created, PID: %d\n", c4);
	}
	else
	{
		exit(0);
	}
	c5 = fork();
	if (c5 > 0)
	{
		printf("Zombie process created, PID: %d\n", c5);
	}
	else
	{
		exit(0);
	}
	infinite_while();
}
