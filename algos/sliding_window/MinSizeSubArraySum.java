public class MinSizeSubArraySum {
  // Given an array of positive numbers and a positive number ‘S,’
  // find the length of the smallest contiguous subarray whose sum
  // is greater than or equal to ‘S’. Return 0 if no such subarray exists.
  // O(N)


  public static int findMinSubArray(int S, int[] arr) {
    int i = 0, currentSum = 0;
    int smallestLength = Integer.MAX_VALUE;

    for (int j = 0; j < arr.length; j++) {
      currentSum += arr[j];

      while (currentSum >= S) {
        smallestLength = Math.min(smallestLength, j - i + 1);
        currentSum -= arr[i];
        i += 1;
      }
    }

    return smallestLength == Integer.MAX_VALUE ? 0 : smallestLength;
  }

  public static void main(String[] args) {
    System.out.println("MinSizeSubArray Sum");

    assert findMinSubArray(7, new int[]{ 2, 1, 5, 2, 3, 2 }) == 2;
    assert findMinSubArray(7, new int[]{ 2, 1, 5, 2, 8 }) == 1;
    assert findMinSubArray(8, new int[]{ 3, 4, 1, 1, 6 }) == 3;
    assert findMinSubArray(100, new int[]{ 3, 4, 1, 1, 6 }) == 0;
  }
}
