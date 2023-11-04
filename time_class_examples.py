import time

print("first")
time.sleep(5)
print("second")

def is_prime(number):
    """
    Tells whether given number is prime or not
    :param number: int
    :return: returns true if prime else false
    """
    time.sleep(2)
    print(1)
    if number==1:
        return True, "prime"
    print(2)
    for i in range(2,number):
        print("*")
        if number%i==0:
            print(4)
            return False, "not prime"
        else:
            print(5)
            return True, "prime"
        print(6)

t1 = time.perf_counter()
is_prime(23)
t2 = time.perf_counter()
print(f"Is prime function took execution time of {t2-t1}  secs")













