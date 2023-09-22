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
