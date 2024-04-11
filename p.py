import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def print_array(arr):
    print(" ".join(map(str, arr)))

def sorting_game():
    score = 0
    total_time = 0
    num_rounds = 5

    print("Welcome to the Sorting Game!")
    print("You will be presented with an unsorted array of numbers.")
    print("Sort it as quickly as possible using either merge sort or quick sort.")
    print("Earn points based on your speed!\n")

    for round_num in range(1, num_rounds + 1):
        array_size = random.randint(5, 10)
        unsorted_array = generate_random_array(array_size)
        
        print(f"Round {round_num}:")
        print("Unsorted array:")
        print_array(unsorted_array)
        
        start_time = time.time()
        
        # Player sorts the array
        sorted_array = merge_sort(unsorted_array)  # You can replace this with quick_sort if desired
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

        print("\nSorted array:")
        print_array(sorted_array)

        # Calculate score based on elapsed time
        round_score = max(0, 10 - elapsed_time)
        score += round_score

        print(f"\nRound {round_num} completed in {elapsed_time:.2f} seconds.")
        print(f"Round {round_num} score: {round_score}")
        print("----------------------------------------")

    print("\nGame Over!")
    print(f"Total score: {score}")
    print(f"Average time per round: {total_time / num_rounds:.2f} seconds")

if __name__ == "__main__":
    sorting_game()
