import random

def findKthLargest(nums, k):
    # Define a helper function to partition the array
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # Move the pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # Move the pivot back to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    left, right = 0, len(nums) - 1
    while left <= right:
        # Choose a random pivot_index
        pivot_index = random.randint(left, right)
        # Perform the partition and get the final position of the pivot
        pivot_index = partition(left, right, pivot_index)

        # Check if the pivot is in its final sorted position
        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index < k - 1:
            # If kth largest is in the right partition, update the left pointer
            left = pivot_index + 1
        else:
            # If kth largest is in the left partition, update the right pointer
            right = pivot_index - 1

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
result = findKthLargest(nums, k)
print(result)  # Output: 5