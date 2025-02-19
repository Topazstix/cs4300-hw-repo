from tasks.task3 import check_integer, sum_to_100, gen_ten_prime
    
def test_check_integer():
    assert check_integer(1) == "positive"
    assert check_integer(-20) == "negative"
    assert check_integer(0) == "zero"

def test_check_ten_prime():
    correct_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    funct_primes = gen_ten_prime()
    assert len(funct_primes) == 10
    assert correct_primes == funct_primes

def test_sum_100():
    assert sum_to_100() == sum(range(1, 101))