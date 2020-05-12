
def earliest_ancestor(ancestors, starting_node, called=False):
    for tup in ancestors:
        if tup[1] == starting_node:
            called = True
            return earliest_ancestor(ancestors, tup[0], called)
    if called == True:
        return starting_node
    else:
        return -1


def iter_earliest_ancestor(ancestors, starting_node):
    stack = [starting_node]
    called = False
    while len(stack) > 0:
        current = stack.pop()
        for tup in ancestors:
            if tup[1] == current:
                called = True
                stack.append(tup[0])
    if called == True:
        return current
    else:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# a2 = [(2, 3), (1, 3), (3, 6), (5, 6), (5, 7),
#       (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (10, 2), (10, 4), (10, 11), (15, 3)]


print(iter_earliest_ancestor(test_ancestors, 6))
print(iter_earliest_ancestor(test_ancestors, 2))

print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 2))

"""
if 2nd value in tuple is starting node
    call earliest with ancestors and first value (parent)



"""
