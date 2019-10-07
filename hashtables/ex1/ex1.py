#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # store weights in hashtable as keys
    # return instance of an Answer tuple (zero, one) or None
    for weight in range(0, len(weights)):
        hash_table_insert(ht, weights[weight], weight)

    # test each weight with ( limit - weight )
    # if ( limit - weight ) is in our hashtable, we have found a pair that adds up to the limit
    for i in range(0, len(weights)):
        weight_match = hash_table_retrieve(ht, (limit-weights[i]))
        if weight_match != None:
            return ( weight_match, i )

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
