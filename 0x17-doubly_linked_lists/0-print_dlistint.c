#include "lists.h"
size_t print_dlistint(const dlistint_t *h)
{
	int count;

	if (!h)
		return (0);
	count = 0;
	while(h)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (count);
}
