def fibonnaci(n):
    try:
        if n == 0 or n == 1:
            return 1
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)

    except Exception as e:
        print(e)

def iter_fib(n):
    minus_one = 0
    minus_two = 0
    cur_sum = 1
    for i in range(n):
        minus_two = minus_one
        minus_one = cur_sum
        cur_sum = minus_one + minus_two
    return cur_sum


def fib_memo(n, memo):
    if n < 2:
        return 1
    if n in memo:
        return memo[n]
    res = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = res
    return res

if __name__ == "__main__":
    import time
    input_var = input("Enter a number you would like to determine the fibonnaci sequence for: ")
    start_iter = time.time()
    fib = iter_fib(int(input_var))
    end_iter = time.time()
    print("The fibonnaci iter sequence of %s is %s" % (input_var, fib))
    print("Time take is %s" %(end_iter-start_iter))


    start_memo = time.time()
    fib = fib_memo(int(input_var), {})
    end_memo = time.time()
    print("The fibonnaci memo sequence of %s is %s" % (input_var, fib))
    print("Time take is %s" %(end_memo-start_memo))

    start_recur = time.time()
    fib = fibonnaci(int(input_var))
    end_recur = time.time()
    print("The fibonnaci recurse sequence of %s is %s" % (input_var, fib))
    print("Time take is %s" %(end_recur-start_recur))

