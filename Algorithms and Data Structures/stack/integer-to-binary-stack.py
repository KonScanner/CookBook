""" Use a stack data struct to convert int to binary

Example : 242
242/2 = 121 -> 0
121/2 = 60 ->  1
... reminder gives us binary representation
"""
from stack import Stack


def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


print(int(str(div_by_2(242)), 2))
print(div_by_2(242))
