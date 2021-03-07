# coding=utf-8

from __future__ import print_function

import random
from simpleai.search.viewers import WebViewer,ConsoleViewer,BaseViewer
from simpleai.search import SearchProblem, astar, breadth_first, depth_first, uniform_cost,greedy, limited_depth_first, iterative_limited_depth_first


def string_to_list(a_string):
    a_list = a_string.split()
    map_object = map(int, a_list)

    return list(map_object)


def list_to_string(a_list):
    string_ints = [str(int) for int in a_list]

    return " ".join(string_ints)



n = int(input("Enter the number of pancake: "))
choose = input("Do you want to enter ordering?: ")
a = n + 1
b = n - 1

if choose == "yes":
    print("Enter top to bottom ordering between [ 0 -",n-1,"]")
    order = input("seperated by space: ")
    s_initial = order.split()
    initial = list_to_string(s_initial)
    print("initial state: ", initial)


if choose == "no":
    l_initial = list(range(n))
    random.shuffle(l_initial)
    initial= list_to_string(l_initial)
    print("initial state: ", initial)



GOAL = list_to_string(list(range(n)))



class pancakeProblem(SearchProblem):


    def __init__(self, initial_state = initial):
        self.initial_state = initial_state


    def actions(self, state):

        if state != GOAL:
            return list(range(2,n+1))
        else:
            return []

    def result(self, state, action):
        s_state = string_to_list(state)

        newList = s_state[:].copy()
        temp = newList[:action]
        temp.reverse()
        newList[:action] = temp

        s_newList = list_to_string(newList)
        return s_newList

    def is_goal(self, state):
        return state == GOAL

    def cost(self, state, action, state2):

        return action

    def heuristic(self, state):
        i = b
        d_state = string_to_list(state)
        goal = list(range(n))
        while 0 < i:
            if goal[i] != d_state[i]:
                temp = goal[i]
                break
            else:
                temp = 0
            i -= 1
        return temp


problem = pancakeProblem()
my_viewer=WebViewer()

result = limited_depth_first(problem,depth_limit=1, viewer= my_viewer)

print(result.state)
print(result.path())

