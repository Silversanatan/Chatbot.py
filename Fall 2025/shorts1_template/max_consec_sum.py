def max_consec_sum(numbers, n):
    if not numbers or n > len(numbers):
        return 0
    maxsum = sum(numbers[0:n]) 
    for i in range(len(numbers) - n + 1):
        currentsum = sum(numbers[i:i+n])
        if currentsum > maxsum:
            maxsum = currentsum
    return maxsum