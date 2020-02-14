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

    """
    YOUR CODE HERE
    """

    # we need to loop through the tickets array to get those keys and values
    for ticket in tickets:
        while ticket.source is not None:
            # use the insert() function to hash the ticket.source as the key and
            # the value will be ticket.destination
            hash_table_insert(hashtable, ticket.source, ticket.destination)
            prev_ticket = None
            if ticket.source is None:
                hash_table_insert(hashtable, ticket.source, ticket.destination) # adds the first ticket
                hash_table_resize() # resizes the hashtable
                prev_ticket = ticket # this ticket will now be prev ticket
                print(ticket.source, ticket.destination)
            elif ticket.source == prev_ticket.destination: # run a while loop, to try to organize the source to connect to destination
                hash_table_insert(hashtable, ticket.source, ticket.destination) # insert said tickets in order
                hash_table_resize()
                prev_ticket = ticket
                print(ticket.source, ticket.destination).



    return route

