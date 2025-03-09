# https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_1 = fruit_2 = last_fruit = -1
        cnt = last_fruit_cnt = max_cnt = 0 
        
        for f in fruits:
            if f == fruit_1 or f == fruit_2:
                cnt += 1
                if last_fruit == f:
                    last_fruit_cnt += 1
                else:
                    last_fruit = f
                    last_fruit_cnt = 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = last_fruit_cnt + 1
                fruit_1 = last_fruit
                fruit_2 = f
                last_fruit_cnt = 1                    
                last_fruit = f 
        return max(max_cnt, cnt)
