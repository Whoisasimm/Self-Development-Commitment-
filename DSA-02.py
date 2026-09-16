numbers = [2, 3, 5, 7, 9, 11]
i = 0
j = len(numbers) -1
target = 12

while i<j:
    current_sum = numbers[i] + numbers[j]
    if current_sum == target:
        print("found", current_sum)
        break
    elif current_sum< target:
        i=i+1
    else:
        j=j-1
