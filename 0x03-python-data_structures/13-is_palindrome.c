#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list listint_t list
 * @head: A pointer to the first node in the list
 * Return: Returns the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *new, *ptr;

	current = NULL;

	for (ptr = *head; ptr != NULL; ptr = ptr->next)
	{
		new = malloc(sizeof(new));
		new->n = ptr->n;
		new->next = current;
		current = new;
	}

	return (current);
}

/**
 * is_palindrome - Checks if a slingly linked list is a palindrome
 * @head: Pointer to the first node in the list
 * Return: Returns 1 if palindrome or 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr1, *reversed;

	if (*head == NULL)
		return (1);

	ptr = *head;
	reversed = reverse_list(head);
	ptr1 = reversed;

	for (; ptr != NULL && ptr1 != NULL; ptr = ptr->next, ptr1 = ptr1->next)
	{

		if (ptr->n != ptr1->n)
		{
			return (0);
		}
	}

	return (1);
}
