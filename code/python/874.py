# https://leetcode.com/problems/walking-robot-simulation/
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_x = {}
        obstacles_y = {}
        for x, y in obstacles:
            obstacles_x.setdefault(x, set()).add(y)
            obstacles_y.setdefault(y, set()).add(x)
        x = y = 0
        res = 0
        route = 0 # 0 = Nord, 1 = East, 2 = South, 3 = West
        shift = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for command in commands:
            is_check = False
            match command:
                case -2:
                    route = (route - 1) % 4
                case -1:
                    route = (route + 1) % 4
                case _:
                    steps = command
                    while steps > 0:
                        if route % 2 == 0:
                            if not is_check:
                                if x not in obstacles_x:
                                    y = y + shift[route][1] * steps
                                    break
                                is_check = True
                            t_y = y + shift[route][1]
                            if t_y in obstacles_x[x]:
                                break
                            y = t_y
                        else:
                            if not is_check:
                                if y not in obstacles_y:
                                    x = x + shift[route][0] * steps
                                    break
                                is_check = True
                            t_x = x + shift[route][0]
                            if t_x in obstacles_y[y]:
                                break
                            x = t_x
                        steps -= 1
            res = max(res, x * x + y * y)
        return res
