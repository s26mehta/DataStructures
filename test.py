def find_elements(arr, total_sum):
    start = 0
    end = len(arr) - 1
    combinations = []

    for i in range(len(arr)):
        start = i
        if total_sum - arr[start] == arr[end]:
            combinations.append(str(arr[start]) + ',' + str(arr[end]))
        if total_sum - arr[start] > arr[end]:
            continue
        while total_sum - arr[start] < arr[end]:
            if arr[start] + arr[end] = total_sum:
                combinations.append(str(arr[start]) + ',' + str(arr[end]))
            end -= 1

        end = len(arr) - 1

    return combinations


def find_elements1(arr, total_sum):
    i = 0
    j = len(arr) - 1
    combinations = []

    while i != j:
        if total_sum - arr[i] == arr[j]:
            combinations.append(str(arr[i]) + ',' + str(arr[j]))
            i =
        if total_sum - arr[i] > arr[j]:
            i += 1
        if total_sum - arr[i] < arr[j]:
            j -= 1


10 - 1 = 9 > 8
10 - 2 = 8 < 8

a = [1, 2, 8, 9]
total_sum = 13