class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curent_node = self.head
        while curent_node:
            print(curent_node.data)
            curent_node = curent_node.next

    def append(self, data):
        """ Adds a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """ Adds element to begining of the list"""
        new_node = Node(data)

        # Make it point to the first item in the list
        new_node.next = self.head
        # adds it as new head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node, not in the list!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """ Assuming no duplicate objects within the list"""
        curent_node = self.head

        if curent_node and curent_node.data == key:
            self.head = curent_node.next
            curent_node = None
            return
        prev_node = None
        while curent_node and curent_node.data != key:
            prev_node = curent_node
            curent_node = curent_node.next
        if curent_node is None:
            return

        prev_node.next = curent_node.next
        curent_node = None

    def delete_node_at_pos(self, pos):
        curent_node = self.head

        if pos == 0:
            self.head = curent_node.next
            return
        prev_node = None
        count = 0
        while curent_node and count != pos:
            prev_node = curent_node
            curent_node = curent_node.next
            count += 1
        if curent_node is None:
            print("The position was higher than the elements in the list.")
            return
        prev_node.next = curent_node.next
        curent_node = None

    def len_iterative(self):

        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2

        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1

        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):
        # Reversing pointers
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_reccursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        P = self.head
        Q = llist.head
        S = None

        if not P:
            return Q
        if not Q:
            return P

        if P and Q:
            if P.data <= Q.data:
                S = P
                P = S.next
            else:
                S = Q
                Q = S.next
            new_head = S

        while P and Q:
            if P.data <= Q.data:
                S.next = P
                S = P
                P = S.next
            else:
                S.next = Q
                S = Q
                Q = S.next
        if not P:
            S.next = Q
        if not Q:
            S.next = P

        return new_head


llist = LinkedList()
llist1 = LinkedList()

list_of_objects = ["A", "B", "C", "D", "E", "F", "H", "I"]
list_of_numbers = [1, 5, 7, 9, 10, 2, 3, 4, 6, 8]


for i in range(0, 4):
    llist.append(list_of_numbers[i])

for i in range(5, len(list_of_numbers)):
    llist1.append(list_of_numbers[i])

llist.merge_sorted(llist1)
llist.print_list()
