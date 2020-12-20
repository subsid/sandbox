package com.algorithms.sliding_window;

import java.util.Optional;
import java.util.Arrays;

public class AverageOfSubarrayOfSizeK {
  // Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
  // Complexity O(N)

  public static double[] findAverages(int K, int[] arr) {
    double[] result = new double[arr.length - K + 1];
    var sum = 0.0;
    var windowStart = 0;
    var windowEnd = 0;

    // pre-condition
    if (arr.length < K) {
      new IllegalArgumentException("Window size greater than array length!");
    }

    // Create first window
    while (windowEnd - windowStart < K) {
      sum += arr[windowEnd];
      windowEnd += 1;
    }

    result[windowStart] = sum / K;
    windowStart += 1;

    while (windowStart < (arr.length - K + 1)) {
      sum -= arr[windowStart - 1];
      sum += arr[windowEnd];

      result[windowStart] = sum / K;
      windowStart += 1;
      windowEnd += 1;
    }

    return result;
  }

  public static void main(String[] args) {

    System.out.println("Average of subarray of size K");

    // Tests
    int[] arr1 = { 1, 3, 2, 6, -1, 4, 1, 8, 2 };
    double[] expected1 = { 2.2, 2.8, 2.4, 3.6, 2.8 };
    double[] actual = findAverages(5, arr1);
    assert Arrays.equals(findAverages(5, arr1), expected1) : String.format("FAIL %s != %s",
        Arrays.toString(actual),
        Arrays.toString(expected1));
  }
}
