# solution: http://www.geeksforgeeks.org/pascal-triangle/
# O(n^2) time and O(1) extra space
def print_pascal(n):
    for i in range(1, n+1):
        c = 1
        j = 1
        while j <= i:
            print c
            c = c * (i - j) / j
            j += 1
        print("\n")

print print_pascal(6)
