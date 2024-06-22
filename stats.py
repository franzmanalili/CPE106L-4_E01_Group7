# stats.py

def mean(numbers):

    if not numbers:
        raise ValueError("The list is empty")
    return sum(numbers) / len(numbers)


def median(numbers):

    if not numbers:
        raise ValueError("The list is empty")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def mode(numbers):
    
    if not numbers:
        raise ValueError("The list is empty")
    
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]
    
    if len(modes) == 1:
        return modes[0]
    else:
        print("The list has multiple modes:", modes)
        return modes
