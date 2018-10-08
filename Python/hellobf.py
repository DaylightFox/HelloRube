#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

string = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+\
++++++++++++++.>.+++.------.--------.>+.>."
loops = []

out_arr = [0]
ptr = 0
index = 0


def inc_data():
    global ptr
    global out_arr
    out_arr[ptr] += 1


def dec_data():
    global ptr
    global out_arr
    out_arr[ptr] -= 1


def inc_ptr():
    global ptr
    global out_arr
    ptr += 1

    if len(out_arr) == ptr:
        out_arr.append(0)


def dec_ptr():
    global ptr
    global out_arr
    ptr -= 1
    if ptr < 0:
        ptr = len(out_arr) - 1


def out_data():
    global ptr
    global out_arr
    sys.stdout.write(chr(out_arr[ptr]))


def loop_start():
    global ptr
    global out_arr
    global index
    global loops
    if out_arr[ptr] > 0:
        if len(loops) == 0 or not loops[-1] == index:
            loops.append(index)
    else:
        if loops[-1] == index:
            loops.remove(index)
        while string[index] != "]":
            index += 1
        #  index += 1


def loop_end():
    global ptr
    global out_arr
    global index
    index = loops[-1] - 1


op_codes = {
    "+": inc_data,
    "-": dec_data,
    ">": inc_ptr,
    "<": dec_ptr,
    ".": out_data,
    "[": loop_start,
    "]": loop_end,
}

while index < len(string):
    op_codes[string[index]]()
    index += 1
    #  print("INDEX:" + str(index))
    #  print("OPCODE:" + string[index])
    #  print("PTR:" + str(ptr))
    #  print("LOOPS" + str(loops))
    #  print("ARR" + str(out_arr))
    #  input()
