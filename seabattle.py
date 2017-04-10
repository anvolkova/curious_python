"""
Finds amount of ships on a sea battle game field.
Ships are rectangles. They do not touch each other.

Example.
x--xx---
x--xx---
------x-
--x-----

4 ships.
"""

def count_ships(field):
    count = 0
    for i in xrange(len(field)):
        for j in xrange(len(field[0].strip())):
            if (field[i][j] == 'x' and 
                (i == 0 or field[i - 1][j] == '-') and 
                (j == 0 or field[i][j - 1] == '-')):
                count += 1
    return count


def main():
    with open('seabattle_in.txt') as f:
        print count_ships(f.readlines())


if __name__ == "__main__":
    main()
