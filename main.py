import markdown_test

class Task:
    def __init__(self,
                 start_time=None,
                 end_time=None,
                 start_date=None,
                 end_date=None,
                 priority=0):
        
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date

        self.priority = priority
        # self.start_proximity = start_proximity
        # self.duration = duration
        # self.time_to_complete = 
        # self.deadline_proximity = 

        # self.tags = tags
        # self.project_name = 
        # self.completion_amount = 

    
# class Event:
    # pass

class Bullet:
    def __init__(self,content):
        self.content = content

class User:
    def __init__(self,day_start_time, day_end_time):
        self.day_start_time = day_start_time
        self.day_end_time = day_end_time

class DayCalendar:
    def __init__(self):
        self.day_blocks = list(range(0,(24*60)+1))




if __name__ == "__main__":
    # import a .txt or .md file
    
    # parse text and append each 
    # split each bullet into a class
    # Parse Tasks and Events Recipe 
    for bullet in bullets:
        print(bullet)
        # newtask = Task(start_time,end_time)



    # organize Tasks and Events 

    # Rules: 
    # 4 Priorities: Most Urgent first
    # 