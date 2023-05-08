#include "list.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to the head node of the list
 *
 * Return: 1 if a cycle is present, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);

	listint_t *tortoise = list;
	listint_t *hare = list;

	do {
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (hare == NULL || hare->next == NULL)
			return (0);

	} while (tortoise != hare);

	return (1);
}
