import math

def CountCustomer(bill):
    result = 0
    for i in bill:
        if i >= 0:
            ans = int(math.sqrt(i))
            if ans*ans == i:
                result += 1
    return result

def main():
    bill = [25, 77, 54, 81, 48, 34, 1]
    result = CountCustomer(bill)
    print(result)    
    
if __name__ == "__main__":
    main()
