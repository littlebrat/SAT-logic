def main(args):
    # Dictionary for choosing the desired algorithm
    algorithm = {'walk': None, 'hill_climbing': None,
                 '-dpll': None
                 }

    # If no algorithm is chosen, always go with uniform cost search
    desired_alg = SearchAgent.uniformCostSearch

    # Debug mode is always off, if nothing more is said
    debug = False

    # Check arguments inserted on the command line
    if len(args) >= 4:
        modes = args[3:len(args)]
        for m in modes:
            if m == '-d':
                debug = True
            elif m in algorithm.keys():
                desired_alg = algorithm[m]

    # Create the map object for this file
    try:
        earth = World()
        earth.from_file(args[1])
    except FileNotFoundError:
        print(".map file does not exist.")

    # Create the client requests object for this file
    try:
        clients = Pawns(earth)
        clients.from_file(args[2])
    except FileNotFoundError:
        print(".cli file does not exist.")

    #Search Procedure
    if debug is True:
        print('>>>  RUN SEARCH')
        i = 1
    towrite = []
    for c in clients:

        # Search algorithm
        plan = desired_alg(c)
        towrite.append(plan)

        # For debugging on terminal only
        if debug is True:
            print('>> client: '+str(i))
            i += 1
            print(c.writeActions(plan))

    # Write result to file
    clients.to_file(towrite)

if __name__ == "__main__":
    main(sys.argv)