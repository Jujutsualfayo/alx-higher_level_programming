#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: double pointer to head node of the linked list
 * @number:  number to  insert
 * Return: the address of the new node
 *         else NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *n_node, *old = NULL;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);

	n_node->n = number;
	n_node->next = NULL;

	tmp = *head;
	while (tmp && n_node->n > tmp->n)
	{
		old = tmp;
		tmp = tmp->next;
	}
	/* for double node */
	if (tmp && n_node->n == tmp->n)
	{
		n_node->next = tmp;
		old->next = n_node;
	}
	/* if n_node  is low than first node */
	else if (!old)
	{
		n_node->next = *head;
		*head = n_node;
	}
	else
	{
		n_node->next = old->next;
		old->next = n_node;
	}

	return (n_node);
}
