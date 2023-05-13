#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_a = tuple_a + (0, 0)
    new_b = tuple_b + (0, 0)
    add1 = int(new_a[0]) + int(new_b[0])
    add2 = int(new_a[1]) + int(new_b[1])
    return add1, add2
