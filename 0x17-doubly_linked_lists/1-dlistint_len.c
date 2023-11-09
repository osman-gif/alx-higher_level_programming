#include "lists.h"

/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list.
 * @h: First pointer to the dlistint_t linked list
 * Return: returns the number of element in the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count;

	if (!h)
		return (0);

	count = 0;
	while (h)
	{
		count++;
		h = h->next;
	}
	return (count);
}
