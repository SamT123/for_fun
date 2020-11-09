def recursive_cucc(depth, string = 'CUCC'):
    if depth == 1:
        return string
    else:
        return recursive_cucc(depth - 1, 'CU ' + string + ' C')

print(recursive_cucc(2))