def check_integer(n: int) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
    
def gen_ten_prime() -> list:
    
    def __prime_checker(n:int) -> bool:
        """private method used for validating prime numbers
        """
        if n < 2:
            return False
        
        for i in range(2, (int(n**.5) + 1)):
            if n % i == 0:
                return False
        
        return True
    
    prime_list = []
    prime_num = 2
    while len(prime_list) < 10:
        if __prime_checker(prime_num):
            prime_list.append(prime_num)
        prime_num += 1
    return prime_list

def sum_to_100() -> int:
    
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
        
    return total