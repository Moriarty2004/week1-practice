def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
            
    return total, average, highest, lowest, even_count, odd_count


def numbers_above_average(numbers, average):
    above_avg = []
    for num in numbers:
        if num > average:
            above_avg.append(num)
    return above_avg


user_input = input("Enter numbers separated by space: ")
number_strings = user_input.split()

numbers = []
for item in number_strings:
    numbers.append(int(item))

total, avg, high, low, evens, odds = analyze_numbers(numbers)
greater_than_avg = numbers_above_average(numbers, avg)

print("RESULTS")
print("Sum of Numbers:", total)
print("Average:", avg)
print("Highest Number:", high)
print("Lowest Number:", low)
print("Even Number Count:", evens)
print("Odd Number Count:", odds)
print("Numbers Greater Than Average:", greater_than_avg)