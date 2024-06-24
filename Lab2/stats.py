def mean(numbers):
    """
    Compute the mean (average) of a list of numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def mode(numbers):
    """
    Compute the mode (most frequently occurring number) of a list of numbers.
    """
    if not numbers:
        return 0
    theDictionary = {}
    for number in numbers:
        count = theDictionary.get(number, 0)
        theDictionary[number] = count + 1
    mode_number = max(theDictionary, key=theDictionary.get)
    return mode_number

def median(numbers):
    """
    Compute the median of a list of numbers.
    """
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def main():
    """
    Test the statistical functions with a given list.
    """
    test_list = [1, 2, 3, 4, 5, 5, 6, 8, 7]
    print("List of Numbers:", test_list)
    print("Mean:", mean(test_list))
    modes = mode(test_list)
    if isinstance(modes, list):
        print("Modes:", ", ".join(str(mode_num) for mode_num in modes))
    else:
        print("Mode:", modes)
    print("Median:", median(test_list))

if __name__ == "__main__":
    main()


