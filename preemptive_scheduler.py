import unittest

from task import TaskState, Task


class PreemptiveScheduler:

    def __init__(self, tasklist, ticks):

        self.tasklist = tasklist
        self.ticks = ticks

    def taskReady(self, t):
        return t.state == TaskState.READY or t.state == TaskState.RUNNING

    def findHighestReady(self):
        ready_list = filter(self.taskReady, self.tasklist)
        if len(ready_list) == 0:
            return None
        ready_list[0].state = TaskState.RUNNING
        return ready_list[0]

    def execute(self):
        action_list = []
        for i in range(0, self.ticks):
            currentTask = self.findHighestReady()
            if currentTask is None:
                # print 'Doing nothing'
                action_list.append(0)
            else:
                # print 'Executing: {}'.format(currentTask)
                action_list.append(currentTask.index)

            # Step every task
            map(lambda x: x.step(), self.tasklist)

        return action_list


class Unittest(unittest.TestCase):

    def test_findHighestReady(self):
        tasklist = []
        tasklist.append(Task(1, 'a', 2, 1, 3))
        tasklist.append(Task(2, 'b', 1, 1, 3))
        tasklist.append(Task(3, 'c', 0, 1, 3))

        def fprint(x):
            print x

        s = PreemptiveScheduler(tasklist, 10)

        map(lambda x: fprint(x), tasklist)
        self.assertEqual(s.findHighestReady().index, 1)

        map(lambda x: x.step(), tasklist)
        map(lambda x: fprint(x), tasklist)
        self.assertEqual(s.findHighestReady().index, 2)

        map(lambda x: x.step(), tasklist)
        map(lambda x: fprint(x), tasklist)
        self.assertEqual(s.findHighestReady().index, 3)

    def test(self):
        tasklist = []
        tasklist.append(Task(1, 'a', 2, 2, 3))
        tasklist.append(Task(2, 'b', 1, 1, 2))
        tasklist.append(Task(3, 'c', 0, 2, 2))

        s = PreemptiveScheduler(tasklist, 20)
        s.execute()

    def test_realTest(self):
        tasklist = []
        tasklist.append(Task(1, 'watchdog', 9, 2, 1000))
        tasklist.append(Task(2, 'frontend', 8, 40, 1000))
        tasklist.append(Task(3, 'hart', 7, 30, 38))
        tasklist.append(Task(4, 'main', 6, 40, 1000))
        tasklist.append(Task(5, 'hmi', 5, 50, 143))
        tasklist.append(Task(6, 'slow', 4, 200, 500))

        s = PreemptiveScheduler(tasklist, 20000)
        actions = s.execute()
        print actions

        # plt.plot(range(0, 20000), actions)
        # plt.show()

if __name__ == '__main__':
    unittest.main()
