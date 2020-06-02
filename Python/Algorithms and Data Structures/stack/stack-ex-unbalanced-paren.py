"""
Use stack to check whether or not a string has balaned usage of parenthesis.

Example:
    (), ()(), (({[]})) <- Balanced
    ((), {{{)}], [][]]] <- Unbalanced

"""

from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("()()"))
