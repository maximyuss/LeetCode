# https://leetcode.com/problems/design-task-manager
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap_tasks = []
        for userId, taskId, priority in tasks:
            entry = (-priority, -taskId, userId)
            self.tasks[-taskId] = entry
            self.heap_tasks.append(entry)
        heapify(self.heap_tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        entry = (-priority, -taskId, userId)
        self.tasks[-taskId] = entry
        heappush(self.heap_tasks, entry)

    def edit(self, taskId: int, newPriority: int) -> None:
        priority, _, userId = self.tasks[-taskId]
        if priority == -newPriority:
            return
        entry = (-newPriority, -taskId, userId)
        self.tasks[-taskId] = entry
        heappush(self.heap_tasks, entry)

    def rmv(self, taskId: int) -> None:
        del self.tasks[-taskId]

    def execTop(self) -> int:
        while self.heap_tasks:
            priority, taskId, userId = heappop(self.heap_tasks)
            if (taskId not in self.tasks
                or priority != self.tasks[taskId][0]
                or userId != self.tasks[taskId][2]):
                continue
            del self.tasks[taskId]
            return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
