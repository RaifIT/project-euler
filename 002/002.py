# Get Fibonacci sequence up to $maxNum
def fib(max_num=1):
    fib_list = [1, 2]
    return aux_fib(max_num, fib_list)


# Helper function to get Fibonacci sequence up to $maxNum
def aux_fib(max_num, fib_list):
    # Base case: max_num has been reached, so return the list
    if fib_list[-1] >= max_num:
        return fib_list
    else:
        # Recursion step: append the sum of the last two numbers in the fibonacci sequence
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib <= max_num:
            fib_list.append(next_fib)
            return aux_fib(max_num, fib_list)
        else:  # Break case: if the $next_fib is greater than $max_num
            return fib_list


# Get the list of even numbers in the Fibonacci sequence up to $max_num
def even_fib(max_num=1):
    fib_to_num = fib(max_num)
    # print(fib_to_num)
    even_fibs = filter(lambda n: n % 2 == 0, fib_to_num)
    return list(even_fibs)


if __name__ == '__main__':
    # print(evenFib(1000))
    print(sum(even_fib(4_000_000)))
