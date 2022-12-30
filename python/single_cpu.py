# Dummy Solution:
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


# Official Solution:
# Use the heap data structure to solve the question.
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort based on min task processing time or min task index.
        next_task: List[Tuple[int, int]] = []
        tasks_processing_order: List[int] = []
        
        # Store task enqueue time, processing time, index.
        sorted_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()
        
        curr_time = 0
        task_index = 0
        
        # Stop when no tasks are left in array and heap.
        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                # When the heap is empty, try updating curr_time to next task's enqueue time. 
                curr_time = sorted_tasks[task_index][0]
            
            # Push all the tasks whose enqueueTime <= currtTime into the heap.
            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                _, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_index))
                task_index += 1
            
            process_time, index = heapq.heappop(next_task)
            
            # Complete this task and increment curr_time.
            curr_time += process_time
            tasks_processing_order.append(index)
        
        return tasks_processing_order
