import sys
sys.path.append(sys.path[0]+"/aima-python") 

from time import time
from csp import Sudoku, AC3, backtracking_search, min_conflicts
from search import depth_first_graph_search

def time_str(ms):
    if ms > 1: return "{:.2f}s".format(ms)
    else: return "{:.2f}ms".format(ms * 1000)

def print_result(puzzle, search_name="", exec_time="", show_board=True):
    if show_board: print()
    if puzzle.goal_test(puzzle.infer_assignment()):
        print("{} solution (took {}):".format(search_name, time_str(exec_time)))
        if show_board: puzzle.display(puzzle.infer_assignment())
    else:
        print("{} failed after {} - domains: {}".format(search_name, time_str(exec_time), puzzle.curr_domains))
        if show_board: puzzle.display(puzzle.infer_assignment())


def sudoku_search_benchmarks(initial_state, runs=3):
    puzzle = Sudoku(initial_state) 
    print("Start:")
    puzzle.display(puzzle.infer_assignment())

    options = [backtracking_search, AC3, min_conflicts, depth_first_graph_search]
    exec_times = {"backtracking_search": [], 'AC3':[], 'min_conflicts':[], 'depth_first_graph_search':[]}

    for run in range(runs):
        for i in range(3):
            i = 0
            start = time()
            options[i](puzzle)
            exec_time = time() - start
            search_name = options[i].__name__
            exec_times[search_name].append(exec_time)
            # print_result(puzzle, options[i].__name__, exec_time, False)
    for key in exec_times:
        num_runs = len(exec_times[key])
        if num_runs:
            print(time_str(sum(exec_times[key]) / num_runs), "average for", key,"(",end='')
            for ms_time in exec_times[key]:
                print(time_str(ms_time),end=', ')
            print(")")
    


initial_state = {
    'solved': '483921657967345821251876493548132976729564138136798245372689514814253769695417382', # (Figure 6.4.b)
    'easy': '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..',  # (Figure 6.4.a)
    'harder': '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......', # (csp.py)
    'hardest': '1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..' # (AI Escargot)
}

sudoku_search_benchmarks(initial_state['easy'])