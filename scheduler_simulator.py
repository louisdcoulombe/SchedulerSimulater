import argparse

from task import Task
from preemptive_scheduler import PreemptiveScheduler

import matplotlib.pyplot as plt


def main(args):
    tasklist = [Task(1, 'watchdog', 9, 2, 1000),
                Task(2, 'FrontEnd', 8, 50, 1000),
                Task(3, 'Main', 7, 10, 1000),
                Task(4, 'Hart', 6, 30, 40),
                Task(5, 'HMI', 5, 40, 143),
                Task(6, 'Slow', 4, 200, 1000)]

    NB_TICKS = 2000

    s = PreemptiveScheduler(tasklist, NB_TICKS)
    actions = s.execute()

    plt.scatter(range(0, NB_TICKS), actions, c=actions, marker='x')

    plt.text(-450, 0, 'Idle')
    for t in tasklist:
        plt.text(-450, t.index, t.name)

    plt.show()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Scheduler task simulator')
    p.add_argument('-f', help='Input JSON file with task list')
    args = vars(p.parse_args())
    main(args)
