# https://leetcode.com/problems/walking-robot-simulation-ii/
class Robot:
    route_str = ["North", "East", "South", "West"]
    shift = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.width = width - 1
        self.height = height - 1
        self.perimeter = 2 * (self.width + self.height)
        self.route = 1  # 0 = Nord, 1 = East, 2 = South, 3 = West

    def step(self, num: int) -> None:
        steps = num
        while steps > 0:
            if steps > self.perimeter:
                steps = steps % self.perimeter
                if steps == 0 and self.x == 0 and self.y == 0:
                    self.route = 2
            cur_step = min(steps, self.max_steps())
            self.x = self.x + self.shift[self.route][0] * cur_step
            self.y = self.y + self.shift[self.route][1] * cur_step
            steps -= cur_step
            if steps > 0:
                self.route = (self.route - 1) % 4

    def max_steps(self):
        match self.route:
            case 0:
                return self.height - self.y
            case 1:
                return self.width - self.x
            case 2:
                return self.y
            case 3:
                return self.x

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.route_str[self.route]
