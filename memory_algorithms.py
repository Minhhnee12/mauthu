def best_fit(block_size, process_size):
    block_count = len(block_size)
    allocation = [-1] * block_count
    for i in range(block_count):
        best_index = -1
        for j in range(len(process_size)):
            if block_size[i] >= process_size[j]:
                if best_index == -1 or block_size[best_index] > block_size[j]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[best_index]
    return allocation

def first_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
    return allocation

def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        worst_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if worst_index == -1 or block_size[worst_index] < block_size[j]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_size[worst_index] -= process_size[i]
    return allocation