import unittest


class TaskState:
    READY = 0
    RUNNING = 1
    SLEEPING = 2


class Task:

    def __init__(self, index, name, priority, exec_time, sleep_time):
        self.index = index
        self.name = name
        self.priority = priority
        self.exec_time = exec_time
        self.sleep_time = sleep_time

        self.state = TaskState.READY
        self.run_count = 0
        self.sleep_count = 0

        self.state_list = []

    def incrementSleep(self):
        self.sleep_count = (self.sleep_count + 1) % (self.sleep_time)
        # self.state_list.append(self.index)
        if self.sleep_count == 0:
            self.state = TaskState.READY

    def incrementRunning(self):
        self.run_count = (self.run_count + 1) % (self.exec_time)
        # self.state_list.append(self.index + 1)
        if self.run_count == 0:
            self.state = TaskState.SLEEPING

    def step(self):
        if self.state == TaskState.SLEEPING or \
           self.state == TaskState.READY:
            self.incrementSleep()
        if self.state == TaskState.RUNNING:
            self.incrementRunning()

    def __str__(self):
        return '{} - {} : priority {} ({},{})'.format(self.index,
                                                      self.name,
                                                      self.priority,
                                                      self.run_count,
                                                      self.sleep_count)


class Unittest(unittest.TestCase):

    def test_initialState(self):
        t = Task(1, 'test', 1, 2, 2)
        self.assertEqual(t.state, TaskState.READY)

    def test_runStep(self):
        t = Task(1, 'test', 1, 2, 2)
        t.state = TaskState.RUNNING
        self.assertEqual(t.run_count, 0)
        t.step()
        self.assertEqual(t.run_count, 1)
        t.step()
        self.assertEqual(t.run_count, 0)
        self.assertEqual(t.state, TaskState.SLEEPING)

        # self.assertEqual(t.state_list, [2, 2])

    def test_sleepStep(self):
        t = Task(1, 'test', 1, 2, 2)
        t.state = TaskState.SLEEPING
        self.assertEqual(t.sleep_count, 0)
        t.step()
        self.assertEqual(t.sleep_count, 1)
        t.step()
        self.assertEqual(t.sleep_count, 0)
        self.assertEqual(t.state, TaskState.READY)

        # self.assertEqual(t.state_list, [1, 1])

    def test_transitions(self):
        t = Task(1, 'test', 1, 2, 2)
        t.state = TaskState.RUNNING
        t.step()
        t.step()
        self.assertEqual(t.state, TaskState.SLEEPING)
        t.step()
        t.step()
        self.assertEqual(t.state, TaskState.READY)

        # self.assertEqual(t.state_list, [2, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()
