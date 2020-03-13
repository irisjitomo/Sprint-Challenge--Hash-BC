#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop thru weights list length: for i in range(length) 
    # set a variable y that retrieves from ht
    # limit - weights[i] is the key that we will retrieve
    for weight1 in range(length):
        weight2 = hash_table_retrieve(ht, limit - weights[weight1])
        print(weight2)
        print('------------', weights)
        if weight2 is not None:
            print(weight1, weight2)
            return (weight1, weight2)
        else:
            hash_table_insert(ht, weights[weight1], weight1)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
