import numpy as np
from matplotlib import pyplot as plt
from time import time as t


def sieve(n): 
    prime = np.array([True for i in range(n+1)])
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
        
    numbers = {i for i in range(n+1) if prime[i]}
    numbers.remove(0)
    
    return numbers


def build_spiral(size, primes):
    grid = np.zeros([size, size])
    
    center = (size // 2, size // 2)
    y, x = center
    number = 1
    direction = 'right'
    
    not_in_the_box = False
    while not not_in_the_box:
        try:
            if number in primes:
                grid[y, x] = 1
                primes.remove(number)
            else:
                grid[y, x] = -1

            number += 1
        
            if direction == 'down':
                y += 1
                if grid[y, x+1] == 0:
                    direction = 'reset'  
                
            if direction == 'left':
                x -= 1
                if grid[y+1, x] == 0:
                    direction = 'down'
                
            if direction == 'up':
                y -= 1
                if grid[y, x-1] == 0:
                    direction = 'left'
                
            if direction == 'right':
                x += 1
                if grid[y-1, x] == 0:
                    direction = 'up'
            
            if direction == 'reset':
                direction = 'right'

        except(IndexError):
            not_in_the_box = True
            
    return grid


t0 = t()
grid_size = 1728
primes = sieve(grid_size*grid_size)
ulam = build_spiral(grid_size, primes)
runtime = t() - t0
print('runtime : ' + str(runtime))

plt.imsave('ulam.pdf', ulam)