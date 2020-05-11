""" Stack Data Structure """


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def reverse_string(stack, input_str):
    # Loop and push contents char by char
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()
input_str = "Some random string."
print(reverse_string(stack, input_str))

# s = Stack()
# s.push("A")
# s.push("B")
# s.push("C")
# s.push("D")
# print(s.peek())
