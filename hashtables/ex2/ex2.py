#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # find the ticket that `source` none, add to storage
    # then find the ticket that has initial ticket's `destination` as its `source`

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # starting point
    route[0] = hash_table_retrieve(hashtable, "NONE")
    
    for i in range(1, length):
        # set route[1] source to route[0] destination 
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
