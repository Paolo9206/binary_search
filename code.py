import random
import time


def check_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        return -1


def linear_search(n, array):
    if n in array:
        print("The number {} is in the sequence at index {}"
               .format(n, array.index(n)))
    else:
        print("The number {} isn't in the sequence".format(n))


def binary_search(n, array):
    low = 0
    high = len(array) - 1
    while low != high:
        current_index = low + (high - low) // 2
        if array[current_index] == n:
            print("The number {} is in the sequence at index {}"
                   .format(n, array.index(n)))
            return
        elif array[current_index] < n:
            low = current_index + 1
            continue
        else:
            high = current_index - 1
            continue
    print("The number {} isn't in the sequence".format(n))


sequence = [0] * 20000

for i in range(0, 20000):
    if i == 0:
        sequence[i] = random.randint(1, 10)
    else:
        sequence[i] = sequence[i - 1] + random.randint(1, 10)

print(sequence)

number = -1
while number < 0:
    number = check_input(input("Please enter a number: "))

print("Executing linear search:")

t0 = time.process_time_ns()
linear_research(number, sequence)
t1 = time.process_time_ns()

print("Executing binary search:")

t2 = time.process_time_ns()
binary_search(number, sequence)
t3 = time.process_time_ns()

final_timer_1 = t1 - t0
final_timer_2 = t3 - t2
print("""The total of nanoseconds spent to perform the function without binary search is: {}
while the total of nanoseconds spent to perform the function with a binary search
is: {} """.format(final_timer_1, final_timer_2))
