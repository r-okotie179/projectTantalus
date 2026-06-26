# problem A.1
def load_cows(filename):
    with open(filename, "r") as file: 
        content = file.read()
        content_list = content.split("\n")
        dict = {}
        for pair in content_list:
            pair = pair.split(",")
            dict[pair[0]] = pair[1]
        file.close()
    return dict
    
dict = load_cows("ps1_cow_data.txt")

# problem A.2
def greedy_cow_transport(dict): # input of the dictionary of values of cow weights
    '''
    to review greedy algorithm
    '''
    return trip_list # returns the necessary lists for this 
