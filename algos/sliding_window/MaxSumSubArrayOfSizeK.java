package com.algorithms.sliding_window;

public class MaxSumSubArrayOfSizeK {
  // Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
  // O(N)

    public static int findMaxSumSubArray(int k, int[] arr) {
      int maxSum = 0;
      int windowStart = 0;
      int runningSum = 0;

      for(int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        runningSum += arr[windowEnd];

        if (windowEnd - windowStart + 1 == k) {
          maxSum = Math.max(runningSum, maxSum);
          runningSum -= arr[windowStart];
          windowStart += 1;
        }
      }

      return maxSum;
    }

    public static void main(String[] args) {
        System.out.println("Max sum subarray of size k");

        assert findMaxSumSubArray(3, new int[] { 2, 1, 5, 1, 3, 2 }) == 9 : "FAIL1";
        assert findMaxSumSubArray(2, new int[] { 2, 3, 4, 1, 5 }) == 7 : "FAIL2";
    }
}
