def primes_until(n):
    criba=list(range(2,n+1))
    for i in range(2,int(n/2)+1):
        for e in criba:
            if e!=i and e%i==0:
                criba.remove(e)
    return criba

print(primes_until(int(input())))