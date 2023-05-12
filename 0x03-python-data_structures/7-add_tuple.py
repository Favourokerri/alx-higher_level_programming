#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)
    if len_tuple_a >= 2 and len_tuple_b >= 2:
        add1 = int(tuple_a[0]) + int(tuple_b[0])
        add2 = int(tuple_a[1]) + int(tuple_b[1])
        return ((add1, add2))
    elif len_tuple_a == 1:
        tuple_a[1] = 0
    elif len_tuple_b ==1:
        tuple_b[1] = 0
