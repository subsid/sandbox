import java.util.HashMap;

public class LongestSubstringKDistinct {
  // Given a string, find the length of the longest substring in it with no more than K distinct characters.
  //

  public static int findLength(String str, int k) {
    var i = 0;
    var counter = new HashMap<Character, Integer>();
    var longest = 0;

    for (int j=0; j < str.length(); j++) {
      counter.put(str.charAt(j), counter.getOrDefault(str.charAt(j), 0) + 1);

      if (counter.size() <= k) {
        longest = Math.max(longest, j - i + 1);
      } else {
        while (counter.size() > k) {
          char key = str.charAt(i);
          int previousCt = counter.getOrDefault(key, 0);

          if (previousCt != 0) {
            var newCt = previousCt - 1;
            if (newCt == 0) {
              counter.remove(key);
            } else {
              counter.put(key, previousCt - 1);
            }
          }
          i += 1;
        }
      }
    }

    return longest;
  }

  public static void main (String[] args) {
    System.out.println("LongestSubstringKDistinct");

    assert findLength("araaci", 2) == 4;
    assert findLength("araaci", 1) == 2;
    assert findLength("cbbebi", 3) == 5;
  }

}
