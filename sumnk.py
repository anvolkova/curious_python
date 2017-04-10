"""
Finds a way to represent n as a sum of k numbers that belong to
the given set.
"""

def find_sum(k, s, data):
    # composable[i][j] is a list of "j" numbers that have sum "i"
    # Initially, an empty list (j=0) is the way to get sum i=0.
    composable = {0: {0: []}}
    for d in sorted(data):
        # composable will keep all combinations that we can get using "data" elements up to "d", including d.
        old_s_list = sorted(composable.iterkeys(), key=lambda x: -x)
        for old_s in old_s_list:
            old_combs = composable[old_s]
            new_s = old_s + d
            if new_s > s:
                # Too big sum. Ignore.
                continue
            new_s_lists = composable.setdefault(new_s, {})
            for old_n_els, old_list in old_combs.iteritems():
                if old_n_els + 1 == k and new_s == s:
                    # Solution found.
                    return old_list + [d]
                # Check that the length of the list is not too long - otherwise we ignore it.
                if old_n_els < k:
                    # Meaning: if we add "d" to the old_list, then we get a list with lengths (old_n_els+1) 
                    new_s_lists.setdefault(old_n_els + 1, old_list + [d]) 

    # No solution found.
    return None


def main():
    print find_sum(3, 51, [7, 3, 6, 10, 43, 54, 2])


if __name__ == "__main__":
    main()
