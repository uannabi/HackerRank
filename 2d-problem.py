#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize to negative infinity

    # Loop through all possible hourglass starting points
    for i in range(4):  # Rows from 0 to 3
        for j in range(4):  # Columns from 0 to 3
            # Calculate the hourglass sum
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
                arr[i+1][j+1] +                        # Middle
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )

            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)

    return max_sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

