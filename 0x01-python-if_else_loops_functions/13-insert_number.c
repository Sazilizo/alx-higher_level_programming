#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (current == NULL || current->n >= number)
	{
		newNode->next = current;
		*head = newNode;
		return (newNode);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}

