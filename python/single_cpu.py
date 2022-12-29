class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        """
        time = 1
        while tasks:
            pass

    def pick_task(self, tasks, time):
        waiting_list = []
        for task in tasks:
            if time >= task[0]: waiting_list.append(task)
        if not waiting_list: return None
        for item in waiting_list:
            return None
