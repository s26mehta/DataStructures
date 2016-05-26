def fibonnaci(n):
    try:
        if n == 0 or n == 1:
            return 1
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    input_var = input("Enter a number you would like to determine the fibonnaci sequence for: ")
    fib = fibonnaci(int(input_var))
    print("The fibonnaci sequence of %s is %s" % (input_var, fib))







