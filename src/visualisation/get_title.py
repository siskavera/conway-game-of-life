def get_title(i_step, automaton, newline="<br>"):
    title = "Conway's Game of Life{}".format(newline)
    title += "Step {}".format(i_step)
    if automaton.attractor is not None:
        title += ", System reached attractor with period {}".format(automaton.attractor_period)

    return title