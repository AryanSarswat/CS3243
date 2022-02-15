from matplotlib.pyplot import summer


def even_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            sum += arr[i]
    return sum