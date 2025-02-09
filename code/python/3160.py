# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors, color_cnt = {}, {}
        res = []
        cnt_diff_colors = 0
        for x, y in queries:
            if x in ball_colors:
                y0 = ball_colors[x]
                color_cnt[y0] -= 1
                if color_cnt[y0] == 0:
                    cnt_diff_colors -= 1
                    del color_cnt[y0]
            if y in color_cnt:
                color_cnt[y] += 1
            else:
                cnt_diff_colors += 1
                color_cnt[y] = 1
            ball_colors[x] = y
            res.append(cnt_diff_colors)
        return res
