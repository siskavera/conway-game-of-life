def get_title(i_step, attractor_found, newline="<br>"):
    title = "Conway's Game of Life{}".format(newline)
    title += "Step {}".format(i_step)
    if attractor_found:
        title += ", System reached attractor"

    return title