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


# def fib2(n):
#     if n == 0 or n == 1:
#         return 1
#     a = 0
#     b = 0
#     for i in range(n + 1):
#         if i == 0:
#             a = 1
#         elif i == 1:
#             b = 1
#         else:
#             temp = b
#             b = a + b
#             a = temp
#
#     return b
#
#
# for i in range(20):
#     print i, fib2(i)
