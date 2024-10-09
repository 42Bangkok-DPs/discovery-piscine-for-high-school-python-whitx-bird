#!/usr/bin/env python3
def multiplication_tables(): 
    num_1 = 0
    while num_1 <= 10:
        table = []
        num_2 = 0
        while num_2 <= 10:
            table.append(num_1*num_2)
            num_2 += 1
        print(f"Table de {num_1}: {' '.join(map(str, table))}")
        num_1 += 1

multiplication_tables()