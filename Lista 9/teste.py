def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

first_1000_primes = [n for n in range(2, 5001) if is_prime(n)][:1000]
print(first_1000_primes)