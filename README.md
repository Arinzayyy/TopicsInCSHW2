Approach 


Task 1
Initialize two variables: candidate and count. candidate represents the potential majority element, and count keeps track of its count.
Traverse through the array of integers.
If count is 0, set the current element as the new candidate.
If the current element is equal to the candidate, increment count by 1. If it's different, decrement count by 1.
Continue this process for each element in the array, effectively canceling out pairs of elements where one of them is the candidate.
After the iteration, the candidate variable will hold the majority element.
The algorithm operates in linear time complexity (O(n)), where n is the size of the array, and has constant space complexity (O(1)).
The algorithm's key insight is that a majority element will eventually dominate the count due to its frequency, and this approach efficiently identifies the majority element without extensive counting or sorting operations.


Task2
The approach to finding the kth largest element in an array using the QuickSelect algorithm can be summarized as follows:
Define a helper function partition that takes three arguments: left, right, and pivot_index. It partitions the array such that elements less than the pivot are on the left, and elements greater than the pivot are on the right.
Initialize left and right pointers to the first and last indices of the array, respectively.
Use a while loop to repeatedly perform the following steps until left is less than or equal to right:
Choose a random pivot index within the current subarray.
Perform the partitioning of the subarray using the partition function, which returns the final position of the pivot.
Compare the pivot_index with k - 1, where k represents the desired kth largest element:
If pivot_index is equal to k - 1, return the element at that index as it is the kth largest.
If pivot_index is less than k - 1, update the left pointer to search in the right partition.
If pivot_index is greater than k - 1, update the right pointer to search in the left partition.
The algorithm continues to narrow down the search range until it finds the kth largest element.
The QuickSelect algorithm leverages the partitioning process to efficiently find the kth largest element in expected linear time complexity (O(n)), making it a powerful tool for such tasks.

Task3
First, check if the length of the input array nums is less than 2. If it is, return 0 because there are not enough elements for a meaningful comparison.
Find the maximum element (max_num) in the array, which is necessary to determine the number of digits for the radix sort.
Initialize max_gap to 0 and divisor to 1. These variables will be used during the radix sort.
Create a list of empty buckets to hold the elements temporarily during the sorting process.
Perform Radix Sort:
Iterate through each digit place (starting from the least significant digit) using the divisor.
For each digit place, distribute the elements from the input array into buckets based on the current digit.
Reconstruct the array from the buckets, preserving the order.
Calculate the maximum gap between two successive elements during this pass and update max_gap.
Continue the Radix Sort process until all digits have been considered (i.e., until max_num // divisor is 0 for all digits).
Return the max_gap, which represents the maximum difference between two successive elements in the sorted form of the input array.
The key idea behind this approach is to use Radix Sort to sort the elements efficiently while simultaneously tracking the maximum gap between successive elements during each pass. The final result is the maximum gap between elements in the sorted array. This approach guarantees linear time complexity and uses linear extra space.
 

TASK4
Approach Explanation:
Initialize an empty stack (stack) to store characters in lexicographical order.
Create a dictionary (char_count) to keep track of character frequencies in the string s.
Create a set (in_stack) to check if a character is already in the stack.
Iterate through the string s to count character frequencies and populate the char_count dictionary.
Iterate through the string s again:
Decrement the count of the current character in char_count.
Skip characters that are already in the stack (in_stack) because they have been processed.
For each character:
While the stack is not empty, and the current character is smaller than the top element of the stack (stack[-1]), and there are more occurrences of the top element in the future (char_count[stack[-1]] > 0), pop characters from the stack and remove them from in_stack.
Append the current character to the stack and add it to in_stack.
Continue this process until all characters have been processed.
Convert the stack to a string and return the result. The stack will contain the unique characters in lexicographical order, ensuring the smallest lexicographical order among all possible results.
The greedy algorithm ensures that the characters in the result are in the correct order while removing duplicates, resulting in the smallest lexicographical order.

Task 5
Create a prefix sum array (prefix_sum) to efficiently compute the sum of any subarray in O(1) time. Initialize it with zeros and fill it by adding the elements of nums cumulatively.
Initialize min_length to positive infinity (as a placeholder for the shortest subarray length) and a deque (dq) to store the indices of elements in nums in ascending order.
Iterate through the prefix sum array:
While the deque is not empty and the current prefix sum minus the prefix sum at the leftmost element of the deque is greater than or equal to k, update min_length with the current subarray length and remove elements from the left of the deque.
Remove elements from the right of the deque if they won't help find a shorter subarray (i.e., they are greater than or equal to the current prefix sum).
Append the current index to the deque.
After iterating through the prefix sum array, min_length will hold the length of the shortest subarray with a sum of at least k. If no such subarray exists, it will remain as positive infinity.
Return min_length if it's not equal to positive infinity; otherwise, return -1 to indicate that no such subarray exists.
The sliding window and deque approach efficiently find the shortest subarray with the desired sum by maintaining a monotonic queue of indices and removing unnecessary elements from both ends of the queue.
