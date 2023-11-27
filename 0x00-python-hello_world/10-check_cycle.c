#include "lists.h"

/**
 * check_cycle -This function checks whether a linked list has a cycle
 * @link: this is the linked link to check
 *
 * Return: 1 it cycle is present, and 0 if it is absent
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

