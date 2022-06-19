# List of Integers which is sorted in ascending order
# We are given an int, target which we need to search for in the list
# If target exists return its index
# Else return -1
# Unique numbers only
# O(log(n)), Binary search algorithm would be used to achieve this

# We can build some test cases and examples

input_1 = ([1, 2, 3, 4, 5], 5)
output_1 = 4

input_2 = ([], 4)
output_2 = -1

input_3 = ([1, 2, 3, 4, 5], 1)
output_3 = 0

input_4 = ([1, 2, 3, 4, 5], 6)
output_4 = -1

input_5 = ([1], 1)
output_5 = 0


def search(nums, target):
    # Initialise the start of array and End of array
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        # Get the middle index of array
        mid = (lo + hi) // 2

        # Get the number at the middle index
        mid_number = nums[mid]

        # Return the index if the number matches the target
        if mid_number == target:
            return mid

        # Set hi to index one less than the middle if middle number
        # greater than target
        elif mid_number > target:
            hi = mid - 1

        # Set the lo to one greater than middle index
        # if middle number less than target
        elif mid_number < target:
            lo = mid + 1

    return -1


if __name__ == "__main__":

    print(search([1], 1) == 0)
