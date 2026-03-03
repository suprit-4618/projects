# Two Sum in Sorted Array

## Problem Statement

Given a **sorted** array of integers and a target sum, determine if there exist two numbers in the array that add up to the target value.

### Examples

**Example 1:**
```
Input: arr = [1, 2, 3, 4, 6, 8, 10], target = 10
Output: True
Explanation: 4 + 6 = 10 (indices 3 and 4)
```

**Example 2:**
```
Input: arr = [1, 3, 5, 7], target = 10
Output: False
Explanation: No two numbers sum to 10
```

**Example 3:**
```
Input: arr = [0, 1, 3, 4, 5, 6, 8, 9], target = 9
Output: True
Explanation: Multiple pairs exist: (0,9), (1,8), (3,6), (4,5)
```

---

## Approach: Two-Pointer Technique

### Why Two Pointers?

Since the array is **sorted**, we can use two pointers to efficiently find the pair in **O(n)** time complexity, which is much better than the brute force approach of checking all pairs O(n²).

### Algorithm

1. Initialize two pointers:
   - `left` at the start (index 0)
   - `right` at the end (last index)

2. While `left < right`:
   - Calculate `current_sum = arr[left] + arr[right]`
   - If `current_sum == target`: Found the pair! ✅
   - If `current_sum > target`: Move `right` pointer left (decrease sum)
   - If `current_sum < target`: Move `left` pointer right (increase sum)

3. If no pair found, return False

### Visual Example

```
Array: [1, 2, 3, 4, 6, 8, 10], Target: 10

Step 1: left=0, right=6 → 1+10=11 (too big, move right left)
        [1, 2, 3, 4, 6, 8, 10]
         ↑                 ↑

Step 2: left=0, right=5 → 1+8=9 (too small, move left right)
        [1, 2, 3, 4, 6, 8, 10]
         ↑              ↑

Step 3: left=1, right=5 → 2+8=10 ✅ FOUND!
        [1, 2, 3, 4, 6, 8, 10]
            ↑           ↑
```

---

## Solutions

### Solution 1: Find Single Pair (Basic)

Returns `True` if any pair exists, `False` otherwise.

```python
def two_sum(arr, target):
    """
    Find if there exists a pair of numbers that sum to target.
    
    Args:
        arr: Sorted list of integers
        target: Target sum to find
    
    Returns:
        bool: True if pair exists, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return True
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    return False


# Test cases
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 6, 8, 10]
    target1 = 10
    print(f"Array: {arr1}, Target: {target1}")
    print(f"Result: {two_sum(arr1, target1)}")  # Output: True
    
    arr2 = [1, 3, 5, 7]
    target2 = 10
    print(f"\nArray: {arr2}, Target: {target2}")
    print(f"Result: {two_sum(arr2, target2)}")  # Output: False
```

---

### Solution 2: Return Indices

Returns the indices of the pair if found, otherwise returns `None`.

```python
def two_sum_indices(arr, target):
    """
    Find indices of two numbers that sum to target.
    
    Args:
        arr: Sorted list of integers
        target: Target sum to find
    
    Returns:
        tuple: (left_index, right_index) if found, None otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    return None


# Test
arr = [1, 2, 3, 4, 6, 8, 10]
target = 10
result = two_sum_indices(arr, target)
if result:
    print(f"Found at indices: {result}")
    print(f"Values: {arr[result[0]]} + {arr[result[1]]} = {target}")
else:
    print("No pair found")
```

---

### Solution 3: Find All Pairs

Returns all unique pairs that sum to the target.

```python
def two_sum_all_pairs(arr, target):
    """
    Find all pairs of numbers that sum to target.
    
    Args:
        arr: Sorted list of integers
        target: Target sum to find
    
    Returns:
        list: List of tuples containing all pairs
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is number of pairs
    """
    left = 0
    right = len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1   # Move both pointers to find other pairs
            right -= 1
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    return pairs


# Test
arr = [0, 1, 3, 4, 5, 6, 8, 9]
target = 9
result = two_sum_all_pairs(arr, target)
print(f"All pairs that sum to {target}: {result}")
# Output: [(0, 9), (1, 8), (3, 6), (4, 5)]
```

---

## Complete Implementation with Input

```python
def main():
    """Complete implementation with user input"""
    # Input array
    arr = list(map(int, input("Enter sorted array (space-separated): ").split()))
    target = int(input("Enter target sum: "))
    
    left = 0
    right = len(arr) - 1
    found = False
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            print(f"Found pair at indices ({left}, {right})")
            print(f"Values: {arr[left]} + {arr[right]} = {target}")
            found = True
            break
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    if not found:
        print("No pair found that sums to target")


if __name__ == "__main__":
    main()
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
|--------|-----------|-------------|
| **Time** | O(n) | Single pass through array with two pointers |
| **Space** | O(1) | Only using two pointer variables |

### Comparison with Brute Force

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force (nested loops) | O(n²) | O(1) |
| Two Pointers (this solution) | O(n) | O(1) |

---

## Key Insights

1. **Why it works**: The sorted nature of the array allows us to make smart decisions:
   - If sum is too large → decrease it by moving right pointer left
   - If sum is too small → increase it by moving left pointer right

2. **Important constraints**:
   - Array **must be sorted** for this approach to work
   - For unsorted arrays, either sort first O(n log n) or use hash map approach

3. **Edge cases to consider**:
   - Empty array
   - Array with single element
   - No valid pair exists
   - Multiple pairs exist (decide if you need one or all)
   - Duplicate numbers in array

---

## Practice Variations

1. **Three Sum**: Find three numbers that sum to target
2. **Two Sum - Unsorted Array**: Use hash map instead
3. **Two Sum - Count Pairs**: Return count of all pairs
4. **Two Sum - Closest Sum**: Find pair with sum closest to target

---

