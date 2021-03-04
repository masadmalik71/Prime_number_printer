lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
depend = input("Tell you want to print prime straight or reverse: ")
def get_prime_number(lower, upper):
    prime = []
    for num in range(lower,upper + 1):  
        if num > 1:  
            
            for i in range(2,num):  
                if (num % i) == 0:  
                    break
            else:  
                prime.append(num)
    return prime

prime = get_prime_number(lower, upper)
if depend == "reverse" or depend == "r":
    prime_length = len(prime) -1
    for i in range(prime_length, -1, -1):
        print(prime[i])
elif depend == "straight" or depend == "s":
    prime_length = len(prime)
    for i in range(0, prime_length):
        print(prime[i])
else:
    print("You did't right option")

