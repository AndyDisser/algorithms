from operator import itemgetter, attrgetter

class Task:
    def __init__(self, release, deadline, weight):
        self.release = release
        self.deadline = deadline
        self.weight = weight

    def get_release(self):
        return self.release

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight



def dynamic_IntSched(tasks):
    """
    The function takes a list of items of class Task and returns the optimal tasks and their weight
    """
    # Problem: How do I store the times so that I know if they are release times or deadlines?
    # How do I connect them to the tasks?
    # sorted() https://docs.python.org/3/howto/sorting.html
    # how do I make the connection to the task?
    times = []
    for task in tasks:
        task.append((task.get_release(), "r", task.get_weight()))
        task.append((task.get_deadline(), "d", task.get_weight()))

    # sort all tuples with regard to their times
    sorted(times, key=itemgetter(0))

    # algorithm
    weight = 0
    tasks
    for t in times:
        if t[1] == "r":
            pass
