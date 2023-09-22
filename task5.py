from collections import deque

def shortestSubarrayWithSumAtLeastK(nums, k):
    n = len(nums)
    
    # Initialize a prefix sum array to compute the sum of any subarray in O(1) time
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Initialize a deque to store the indices of elements in ascending order
    min_length = float('inf')
    dq = deque()
    
    for i in range(n + 1):
        # While the deque is not empty and the current prefix sum is greater than or equal to k,
        # update the minimum length and pop elements from the left of the deque
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            min_length = min(min_length, i - dq.popleft())
        
        # Remove elements from the right of the deque if they won't help find a shorter subarray
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    return min_length if min_length != float('inf') else -1

# Example usage:
nums = [2, -1, 2]
k = 3
result = shortestSubarrayWithSumAtLeastK(nums, k)
print(result)  # Output: 3