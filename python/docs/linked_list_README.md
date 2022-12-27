# Singly Linked List
LinkedList class which uses Node class. These classes are used to create items within a linked list. Linked List items have two values connected to them, their data and the next link in the list. The head of the list needs to be tracked so you can go through the chain and find the next.

## Challenge
Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Linked List
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
---
Must pass the following tests: </br>
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
Inserting into this LinkedList will be O(1) as it always replaces the head. Space will be O(n) has every new item in the list will need to be stored in memory.

## API
insert - replaces head with node created, and moves head down 1 link in the list
includes - searches the list and returns true or false if the item is in the list
to string - str(LinkedList) returns all values in the list formatted to include NULL at the end of the list and have arrows pointing between nodes

## Files located at
- [code](../data_structures/linked_list.py)
- [tests](../tests/data_structures/test_linked_list.py)
