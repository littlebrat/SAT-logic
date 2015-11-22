from src.structure.sentence import Sentence
import sys
from src.algorithm.solver import *
from os import listdir
from os.path import isfile, join

def main(args):

    # State variables from user input
    t = time()
    mode, params = None, None
    path = None
    is_batch = False
    with_time = False
    output_file = False
    result = None
    model = None
    debug = False

    for i in range(len(args)):
        # Check user inputs
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
        elif args[i] == '-d':
            debug = True

    if is_batch is False:
        sentence = Sentence.from_file(path)
        if mode == 'dpll':
            result, model = Algorithms.setup_dpll(sentence)
        elif mode == 'walk':
            result, model = Algorithms.walksat(sentence, float(params[0]), int(params[1]))
        elif mode == 'gsat':
            result, model = Algorithms.gsat(sentence, int(params[0]), int(params[1]))
        if output_file is True:
            Algorithms.to_file(path, sentence, model, result)
    else:
        if mode == 'dpll':
            result = is_dpll_satisfiable(path, output_file)
        elif mode == 'walk':
            result = is_walk_satisfiable(path, float(params[0]), int(params[1]), output_file)
        elif mode == 'gsat':
            result = is_gsat_satisfiable(path, float(params[0]), int(params[1]), output_file)

    if debug is True:
        print(result)

    if with_time is True:
        print(time() - t)

def get_efficiency(list):
    # Check the amount of satisfied clauses in the algorithm.
    result = 0
    for x in list:
        if x is True:
            result += 1
    if len(list)!=0:
        result = result / len(list)
    else:
        result = 0
    return result

def is_gsat_satisfiable(folder, max_restarts, max_climbs, out):
    # This function checks if all files from a folder are satisfiable or not, using gsat,
    # with probability p, and max_flips, given their known satisfiability.
    files = get_files_from_folder(folder)
    results = []
    for f in files:
        sentence = Sentence.from_file(folder+'/'+f)
        result, model = Algorithms.walksat(sentence, max_restarts, max_climbs)
        if out is True:
            Algorithms.to_file(f, sentence, model, result)
        results.append(result)
    return get_efficiency(results)

def is_walk_satisfiable(folder, p, max_flips, out):
    # This function checks if all files from a folder are satisfiable or not, using walksat,
    # with probability p, and max_flips, given their known satisfiability.
    files = get_files_from_folder(folder)
    results = []
    for f in files:
        sentence = Sentence.from_file(folder+'/'+f)
        result, model = Algorithms.walksat(sentence, p, max_flips)
        if out is True:
            Algorithms.to_file(f, sentence, model, result)
        results.append(result)
    return get_efficiency(results)

def is_dpll_satisfiable(folder, out):
    # This function checks if all files from a folder are satisfiable or not, using DPLL,
    #  given their known satisfiability.
    files = get_files_from_folder(folder)
    results = []
    for f in files:
        sentence = Sentence.from_file(folder+'/'+f)
        result, model = Algorithms.setup_dpll(sentence)
        if out is True:
            Algorithms.to_file(f, sentence, model, result)
        results.append(result)
    return get_efficiency(results)

def get_files_from_folder(path):
    # Returns a list with every file in folder with 'path'.
    only_files = [f for f in listdir(path) if isfile(join(path,f))]
    return only_files

if __name__ == "__main__":
    main(sys.argv)