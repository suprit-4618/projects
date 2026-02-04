def sum_tar(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return pairs


arr = list(map(int, input("Enter the sorted array elements: ").split(",")))
target = int(input("Enter the target sum: "))
print(sum_tar(arr, target))
