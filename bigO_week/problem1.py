def restoreString(s, indices):
    start = time.process_time()    
    map = zip(s, indices)

    sorted_map = sorted(map, key=lambda mapping: mapping[1])
    
    return ''.join([mapping[0] for mapping in sorted_map])
