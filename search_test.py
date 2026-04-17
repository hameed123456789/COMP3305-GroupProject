import csv
import time

# Load the data
data = []
with open('c:\\Users\\hamee\\Downloads\\FEN_Best_moves_100k.csv.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        data.append(row[0])  # FENs

# Compute keys for interpolation search
keys = [sum(ord(c) for c in fen) for fen in data]

# Sort by keys
sorted_pairs = sorted(zip(keys, data))
sorted_keys = [k for k, f in sorted_pairs]
sorted_fens = [f for k, f in sorted_pairs]

# Pick target (middle one)
target_index = len(sorted_keys) // 2
target_key = sorted_keys[target_index]
target_fen = sorted_fens[target_index]

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Exponential Search
def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    low = i // 2
    high = min(i, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        if pos < low or pos > high:
            return -1
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Test Binary Search
start = time.perf_counter()
result_bin = binary_search(sorted_keys, target_key)
end = time.perf_counter()
time_bin = end - start

# Test Exponential Search
start = time.perf_counter()
result_exp = exponential_search(sorted_keys, target_key)
end = time.perf_counter()
time_exp = end - start

# Test Interpolation Search
start = time.perf_counter()
result_int = interpolation_search(sorted_keys, target_key)
end = time.perf_counter()
time_int = end - start

# Display results
print(f"Target FEN: {target_fen}")
print(f"Target Key: {target_key}")
print(f"Binary Search: Found at index {result_bin}, Time: {time_bin:.10f} seconds")
print(f"Exponential Search: Found at index {result_exp}, Time: {time_exp:.10f} seconds")
print(f"Interpolation Search: Found at index {result_int}, Time: {time_int:.10f} seconds")