class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_backup = [item for item in tasks]
        time = 1
        order_list = []
        while tasks:
            picked_item, tasks = self.pick_task(tasks, time)
            if picked_item is not None: 
                time += picked_item[1]
                for index, item in enumerate(tasks_backup):
                    if item == picked_item:
                        order_list.append(index)
                        break
            else: 
                time += 1
        return order_list

    def pick_task(self, tasks, time):
        waiting_list = []
        for index, task in enumerate(tasks):
            if time >= task[0]: waiting_list.append((index, task))
        if not waiting_list: return None, tasks
        
        picked_item = waiting_list[0]
        for item in waiting_list:
            if item[1][1] < picked_item[1][1]: picked_item = item
        tasks.pop(picked_item[0])    
        return picked_item[1], tasks
