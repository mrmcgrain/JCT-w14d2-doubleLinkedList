class Node:
    def __init__(self, val=None, prev=None, next=None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



def flatten(head: 'Node') -> 'Node':
    if not head:
        return None
    
    def flat_recursively(node: 'Node') -> 'Node':
        current = node
        tail = node


        while current:
            next_node = current.next
            if current.child:
                print(f'Flattening child list starting from node {current.child.val}')
                child_head = current.child
                child_tail = flat_recursively(child_head)

                current.next = child_head
                child_head.prev = current
                current.child = None


                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

                tail = child_tail

            else:
                tail = current

            current = next_node

        return tail
    
    flat_recursively(head)
    return head
    

# Helper function for testing; will print new node list

def print_new_node_list(head: 'Node'):
    current = head
    while current:    
        print(f'Node({current.val})', end=" <-> " if current.next else " ")
        current = current.next
    print()


