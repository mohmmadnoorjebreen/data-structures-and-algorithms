# Hashtables
In computing, a hash table (hash map) is a data structure that implements
an associative array abstract data type, a structure that can map keys to values.

## Challenge

Implement a Hashtable Class with the following methods:

1. add
2. get
3. contains
4. hash

## Approach & Efficiency
Simple, quick and direct Approach have been taken
big O space = O(1)
big O time = O(n)

## API

1. add
Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

2. get
Arguments: key
Returns: Value associated with that key in the table

3. contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

4. hash
Arguments: key
Returns: Index in the collection for that key
