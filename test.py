import timeit

phil_func = '''
Reference_data = ['test', '1ST2020082200']
Additional_match_references = ['01', '02', '03', '04', '05', '06']
stored_matchIDs = ['13A2020072600', '1ST2020082200', '1ST2006052700', 'SUN2020083000', '1ST2020091200', '1ST2020082201', '1ST2020082202']
def Reference_switch(stored_matchIDs, Reference_data, Additional_match_references):
    for i in range(len(stored_matchIDs)):
        if Reference_data[1] in stored_matchIDs[i]:
            temp = list(Reference_data[1])
            temp[-2:] = Additional_match_references.pop(0)
            Reference_data[1] = "".join(temp)
            print(Reference_data)
    return Reference_data
    #Reference_switch(stored_matchIDs, Reference_data)
'''

jamie_func = '''
Reference_data = ['test', '1ST2020082200']
Additional_match_references = ['01', '02', '03', '04', '05', '06']
stored_matchIDs = ['13A2020072600', '1ST2020082200', '1ST2006052700', 'SUN2020083000', '1ST2020091200', '1ST2020082201', '1ST2020082202']
def reference_switch1(stored_matchIDs, Reference_data, Additional_match_references):
    stored_matchIDs_tail = [i[-2:] for i in stored_matchIDs if i[:-2] == Reference_data[1][:-2]]
    stored_matchIDs_tail_set = set(stored_matchIDs_tail)
    potential_match_id_tails = set(Additional_match_references) - stored_matchIDs_tail_set
    potential_match_ids = [Reference_data[1] + i for i in potential_match_id_tails]
    return potential_match_ids
'''

print(timeit.timeit(phil_func, number=10000000))
print(timeit.timeit(jamie_func, number=10000000))