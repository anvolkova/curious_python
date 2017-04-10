"""
Give a list of prime factors of a number.
"""
 
def prime_factors(a):
    if a <= 1:
        return None
    factors = []
    i = 2
    while i * i <= a:
        while a % i == 0:
            factors.append(i)
            a /= i
        i += 1
    if a > 1:
        factors.append(a)
    return factors
      

def main():
    with open("prime_factors_in.txt") as f:
        print prime_factors(int(f.readline().split()[0]))
        

if __name__ == "__main__":
    main()
      
