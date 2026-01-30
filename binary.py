import multiprocessing
from concurrent.futures import ProcessPoolExecutor # io bound vs cpu bound think about it <3
from typing import List, Tuple
from time import perf_counter
from math import isqrt
from collections.abc import Generator
from functools import wraps
import math
import sys
import time
# so binary how does it work its base 2 well it looks like this.
binary_values : List[Tuple[int]] = [(a,b) for a in range(2) for b in range(2)]
# what is a list well its a box we put things into and we can write a list like this
listy : List = []
# for adding or removing and editing the list we can acces the index we can use the .pop() operator and the append() also .jion() to add it to a string for prints
rangey : Generator = range(10)
#range is a generator and gives values from the start 0 if not specified to the given number in this case 10 with a step size we select.
rangy_2 : Generator = range(0,10)
print(rangey == rangy_2)
print(*rangey)
print(range(0,10,2)) # this is range(0,10,2)  thing of it like this --> range(start= 0, stop=10, step=2) but they dont take key word arugments 
print(*range(0,10,2)) # the * is the unpacking operator for turning the generator into actual values
print(*range(0,10,6))
print(*range(0,10,3))
data_all : Generator = [*range(0,10,1)]
print(data_all)
data_sliced = data_all[0:10:2] # this is called array indexing and is the exact same thing as 
print(data_sliced)


# Coool things to think about yield vs return 



# generators well range is giving us generators we can also make our own generator functions using yeild
# Note this one needs testing and might not work as intended fully we ca
def primes_example(start_value, max_value : int) -> List :
    data: List = []
    for  num in range(start_value,max_value,1): 
        squared_num_max: int = int(pow(max_value,0.5) // 1 ) + 1
        if all(num%test != 0 for test in range(2,squared_num_max) if test!=num ):
            data.append(num)
            
    data_cleaned = [values for values in data if values not in (1,)]
    return data_cleaned
# we can make this a generator just by adding the check for 1 or by converitng it at the end 
def primes_a(start_value, max_value : int) -> Generator :
    data: List = []
    for  num in range(start_value,max_value,1): 
        squared_num_max: int = int(pow(max_value,0.5) // 1 ) + 1
        if all(num%test != 0 for test in range(2,squared_num_max) if test!=num ):
            data.append(num)
            
    data_cleaned = [values for values in data if values not in (1,)]
    yield from data_cleaned # this is slow and is like putting a loop at the end 


def primes_b(start_value, max_value : int) -> Generator :
    for  num in range(start_value,max_value,1): 
        squared_num_max: int = int(pow(max_value,0.5) // 1 ) + 1
        if all(num%test != 0 for test in range(2,squared_num_max) if test!=num ):
            if num != 1:
                yield num

test_a = primes_a(0,1000)
test_b = primes_b(0,1000)
print(f"If primes A is equal to Primes B print true (in terms of values):  {list(test_a) == list(test_b)}") # HERE IS WHERE I AM TALKING ABOUT LINE 63
print(f" Does genreator object primes A {type(test_a)} and Generator primes B {type(test_b)} equal one another? {test_a==test_b}")
for i in test_a:
    print(i)
    if i==247:
        break
# wait this didnt print anything that is because we emptied the generator on line 63 of the code or here 
test_a = primes_a(0,1000)
for i in test_a:
    print(i)
    if i==251:
        break
# now it prints


# this is a cool ideaa for this simply prove that its not 
values_idea : List[bool] = [False for i in range(0, 100)]
# we can make the same thing be going
values_idea_2 : List[bool] = [False] *100

print(f" Testing if these 2 lists are the same {values_idea == values_idea_2} printing the first 5 values of idea_2 {values_idea_2[5::]}")



# F strings would be like this 
string_text: str = "Hello world" # LAME!!!!!!!!!!!!!!

secret_data : str = "The world will [*;::;*] end and it will be me who does it AHAHAHA everyone will go somewhere" # o no we need to fix this

#we can use the .split() on the text with the most comon text sequeances

secret_sec_1 , secret_sec_2, *args  = secret_data.split("[*;::;*]")
secret_sec_3 , secret_sec_4 = secret_sec_2.split("AHAHA")

# The f string automaticly formats to allow us to combine strings togeather

new_string = f"{secret_sec_1}go on to be a bueatiful thing{secret_sec_4[2::]} lovely it will be wholesome and awsome." # looks like we had to slice of the exta Ha we left in

print(new_string)

# if we had some white space at the start of some text and we wanted to remove it then we can run the following to clean up our text 
testing_input = "                                                                        Hello                                                                  "
print(f"{len(testing_input.strip())} vs the orginal length {len(testing_input)}")




# We can use the ** to give squre power and the pow(<value>, <to the power of>)
# we use the //1 operator to cast our value down the int() would also work and the math.floor() would do the same form import math
# note the pow operator will return a float so this value is a float because of how types work particularly after division

def cout_time(func):
    @wraps(func)
    def run_func(*args,**kwargs):
        start_time = perf_counter()
        output = func(*args,**kwargs)
        end_time = perf_counter()
        print(f"{func.__name__} took : {end_time-start_time}")
        return output
    return run_func


# BOUNOUS QUESTIONS!!!! 
# this was my implementation but its not corret and is missing one value can you figure out what and why it is doing this
@cout_time
def primes(start_value, max_value : int) -> List :
    data: List = []
    for  num in range(start_value,max_value,1): 
        squared_num_max: int = int(pow(max_value,0.5) // 1 ) + 1
        if all(num%test != 0 for test in range(2,squared_num_max) if test!=num ):
            data.append(num)

    data_cleaned = [values for values in data if values not in (1,)]
    return data_cleaned
        
# ai gen dont trust it Qwen ai made this function
@cout_time
def primes_corect(start_value: int, max_value: int) -> Generator[int, None, None]:
    """Correct prime generator - no post-filtering needed"""
    for num in range(max(2, start_value), max_value):  # Skip numbers < 2
        if num == 2:
            yield num
            continue
        if num % 2 == 0:  # Skip even numbers > 2
            continue
        
        # Only check odd divisors up to √num
        limit = int(num ** 0.5) + 1
        for divisor in range(3, limit, 2):
            if num % divisor == 0:
                break
        else:
            yield num  # Prime found!

@cout_time
def sieve(limit: int) -> list:
    """Blazing fast prime generator for single process"""
    if limit < 2:
        return []
    is_prime = bytearray(b'\x01') * limit
    is_prime[0:2] = b'\x00\x00'
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i*i:limit:i] = b'\x00' * ((limit - 1 - i*i) // i + 1)
    return [i for i, prime in enumerate(is_prime) if prime]





your_primes = primes(0, 1_000_0)
print(your_primes)
correct_primes = list(primes_corect(0, 1_000_0))


print(f"Your count: {len(your_primes)}")
print(f"Correct count: {len(correct_primes)}")
print(f"First 10 of your primes: {your_primes[:10]}")
print(f"First 10 correct primes: {correct_primes[:10]}")

# Find the exact difference
if your_primes != correct_primes:
    # Check if you're just missing '2' at the start
    if primes_corect[0] == 2 and your_primes[0] == 3:
        print("\n🚨 YOUR BUG: You're missing the prime number 2!")
        print("Your list starts at 3, but correct list starts at 2.")
    else:
        # Find first mismatched index
        for i in range(min(len(your_primes), len(correct_primes))):
            if your_primes[i] != correct_primes[i]:
                print(f"\nFirst mismatch at index {i}:")
                print(f"  Yours: {your_primes[i]}")
                print(f"  Correct: {correct_primes[i]}")
                break



def format_as_grid(primes, col_width=22, cols_per_row=4):
    """Aligns numbers into a stable hacker-style grid."""
    lines = []
    for i in range(0, len(primes), cols_per_row):
        row = primes[i:i + cols_per_row]
        formatted_row = "".join(str(p).ljust(col_width) for p in row)
        lines.append(formatted_row)
    return "".join(lines)

def sieve_segment(start, end, seeds):
    """The math engine processing a tiny slice of infinity."""
    size = end - start
    segment = bytearray(b'\x01') * size
    offset = start % 2
    segment[offset::2] = b'\x00' * ((size - offset + 1) // 2)

    for p in seeds:
        if p == 2: continue
        first = (start + p - 1) // p * p
        if first < p * p: first = p * p
        if first < end:
            segment[first - start : end - start : p] = b'\x00' * ((end - 1 - first) // p + 1)
            
    return [start + i for i, is_p in enumerate(segment) if is_p and start + i > 1]

def Prime_generations():
    SEXTILLION = 1_000_000_000_000_000_000_000
    chunk_size = 100_000 
    seeds = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    
    # Start the green text!
    sys.stdout.write("\033[92m") 
    
    start_time = time.time()
    current = 0
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        while current < SEXTILLION:
            # Dispatch the work
            future = executor.submit(sieve_segment, current, current + chunk_size, seeds)
            primes = future.result()
            
            if primes:
                # 1. Print the primes to stdout (the scrolling window)
                grid_output = format_as_grid(primes)
                sys.stdout.write(grid_output)
                sys.stdout.flush()
            
            current += chunk_size
            
            # 2. Update the Speedometer on stderr (doesn't interfere with the grid)
            elapsed = time.time() - start_time
            percent = (current / SEXTILLION) * 100
            # Using carriage return \r to keep the status on one line
            status = f"\r\033[93m[PROGRESS: {current:,} / {SEXTILLION:,}] | {percent:.20f}% TO SEXTILLION\033[92m"
            sys.stderr.write(status)
            sys.stderr.flush()


A_sextillion =  1_000_000_000_000_000_000_000 # 1,000,000,000,000,000,000,000
# A_sextillion = sieve( 1_000_000_000_000_000_000_000) # crashes

# 
# A sextillion 1,000,000,000,000,000,000,000
# well printing prime numbers who new that Unfrotinitly well be here for the next many thousand years before we get to our sextillion  




# Prime_generations() # DONT DO IT