# Function to calculate the sum of the first n numbers
def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

# Main function
if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    print(f"The sum of the first {n} numbers is {sum(n)}")
