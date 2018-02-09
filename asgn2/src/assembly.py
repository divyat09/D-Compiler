def datasection():
    print ".data\n"
    for variables in global_vars:
        print variables.name+":\n\t.long"+variables.value

