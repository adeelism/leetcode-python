"""904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Return the length of the longest contiguous subarray containing at most two
distinct values.

Approach: Slide a window keeping a frequency map of fruit types; when more than
two types appear, shrink from the left until only two remain.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        answer = 0
        basket = {}
        for right in range(len(fruits)):
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit, 0) + 1
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            window = right - left + 1
            answer = max(answer, window)
        return answer
