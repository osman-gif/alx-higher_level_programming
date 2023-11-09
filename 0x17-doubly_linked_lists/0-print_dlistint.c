/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: First pointer of the dlistint_t linked list
 * Return: Returns the number of elements in the dlistint_t linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count;

	count = 0;
	while (h)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (count);
}
