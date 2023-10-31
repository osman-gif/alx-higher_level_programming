#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts an new_node to the listint_t list
 * @head: Pointer to the first node in the list
 * @number: The data section of the new_node
 * Return: Returns NULL if functions fail otherwise returns address of newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp, *next;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	tmp = *head;

	for (; tmp != NULL; tmp = tmp->next)
	{
		next = tmp->next;
		if (next == NULL)
		{
			return (NULL);
		}
		new_node->n = number;
		if (next->n > number)
		{
			new_node->next = next;
			tmp->next = new_node;
			return (new_node);
		}
	}

	return (new_node);
}
