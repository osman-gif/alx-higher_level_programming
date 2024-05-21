#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	return (new);
}


listint_t *reverse_list(listint_t **head)
{       
	if (*(head) == NULL)
	{
		return (NULL);
	}

	prev = NULL;

	for (ptr = *head; ptr != NULL; ptr = ptr->next)
	{
		tmp = ptr;
		tmp->next = prev;
		prev = tmp;
	}

	return prev
}

int main()
{
	listint_t *head;
	listint_t *rev;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);

	for (; head != NULL; head = head->next)
	{
		printf("%d\n", head->n);
	}
	rev = reverse_list(&head);

	for (; rev != NULL; rev = rev->next)
	{
		printf("%d\n", rev->n);
	}

}
