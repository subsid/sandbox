

def fruits_into_baskets(fruits):
 # Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
 # You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
 # O(N)


  # TODO: Write your code here
  basket_limit = 2
  basket = set()
  count = 0
  max_count = 0
  i = 0

  for fruit in fruits:
      basket.add(fruit)
      count += 1
      while (len(basket) > basket_limit):
          basket.remove(fruits[i])
          count -= 1
          i += 1
      max_count = max(max_count, count)

  return count

if __name__ == "__main__":
    print("fruits_into_baskets")
    assert(fruits_into_baskets(['A', 'B', 'C', 'A', 'C', 'B', 'C', 'B']) ==  4)
    assert(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) ==  3)
    assert(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']) ==  5)

