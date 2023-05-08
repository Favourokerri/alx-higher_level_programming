#include "list.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *runner;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list->next;
	runner = list->next->next;

	while (current && runner && runner->next)
	{
		if (current == runner)
			return (1);

		current = current->next;
		runner = runner->next->next;
	}

	return (0);
}
