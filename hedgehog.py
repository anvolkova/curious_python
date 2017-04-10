"""
Solve the classic dynamic programming task about a hedgehog.

There is a rectangular garden of size n x m. Each cell contains a certain
amount of apples. A hedgehog wants to find as more apples as possible when
he runs from cell (1, 1) to cell (n, m). On each step, the hedgehog moves
one cell left or one cell down.

Input.
n m
n x m numbers

Output.
Max amount of apples that can be found.
"""

def scan_matrix(filename):
    with open(filename) as f:
        split_line = f.readline().split()
        n = int(split_line[0])
        a = [[]] * n
        for i in xrange(n):
            a[i] = [int(c) for c in f.readline().split()]
    return a
                

def print_matrix(a):
    for i in xrange(len(a)):
        for j in xrange(len(a[i])):
            print a[i][j],
        print
        

def find_best_route(a):
    b = [[0] * len(a[0]) for i in xrange(len(a))]    
    b[0][0] = a[0][0]
    for j in xrange(1, len(a[0])):
        b[0][j] = b[0][j - 1] + a[0][j]
    for i in xrange(1, len(a)):
        b[i][0] = b[i - 1][0] + a[i][0]

    for j in xrange(1, len(a[0])):
        for i in xrange(1, len(a)):
            b[i][j] = max(b[i - 1][j], b[i][j - 1]) + a[i][j]

    return b[-1][-1]
    

def main():
    print find_best_route(scan_matrix("hedgehog_in.txt"))


if __name__ == "__main__":
    main()
