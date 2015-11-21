from src.structure.sentence import Sentence
import sys
from src.algorithm.solver import *
from os import listdir
from os.path import isfile, join

def main(args):

    t = time.time()

    mode, params = None, None
    path = None
    is_batch = False
    with_time = False
    output_file = False
    result = None

    for i in range(len(args)):
        if args[i] == '-a':
            if args[i+1] == 'dpll':
                mode = 'dpll'
            elif args[i+1] == 'walk':
                mode = 'walk'
                params = [args[i+2], args[i+3]]
            elif args[i+1] == 'gsat':
                mode = 'gsat'
                params = [args[i+2], args[i+3]]
            else:
                return Exception('Unknown algorithm or wrong parameter size.')
        elif args[i] == '-f':
            if isinstance(args[i+1], str):
                path = args[i+1]
            else:
                return Exception('Unknown path.')
        elif args[i] == '-b':
            is_batch = True
        elif args[i] == '-t':
            with_time = True
        elif args[i] == '-o':
            output_file = True

    if is_batch is False:
        sentence = Sentence.from_file(path)
        if mode == 'dpll':
            result = Algorithms.setup_dpll(sentence)
        elif mode == 'walk':
            result = Algorithms.walksat(sentence, params[0], params[1])
        elif mode == 'gsat':
            result = Algorithms.gsat(sentence, params[0], params[1])
    # else:



    if output_file is True:
            with open(path + '_sol.cnf', "w") as text_file:
                text_file.write(str(result))

    if with_time is True:
        print(time() - t)

def is_walk_satisfiable(folder, p, max_flips, satisfiability):
    # This function checks if all files from a folder are satisfiable or not, using walksat,
    # with probability p, and max_flips, given their known satisfiability.

def is_dpll_satisfiable(folder, satisfiability):
    # This function checks if all files from a folder are satisfiable or not, using DPLL,
    #  given their known satisfiability.
    files = get_files_from_folder(folder)
    results = []
    for f in files:
        sentence = Sentence.from_file(folder+'/'+f)
        my_val = Algorithms.setup_dpll(sentence)
        results.append(my_val)
    for bl in results:
        if bl != satisfiability:
            print('Error')

def get_files_from_folder(path):
    # Returns a list with every file in folder with 'path'.
    only_files = [f for f in listdir(path) if isfile(join(path,f))]
    return only_files

if __name__ == "__main__":
    is_all_satisfiable('test_files/75vars_325clauses/not_satis',False)
    # main(sys.argv)