import json
def clean_data_for_network_analysis(data):

    with open("data/edgelist.txt", "w+") as f:
        for key, value in data.items():
            #print(f"{key}: {value}\n")
            f.write(f"{key[0]}\t{key[1]}\t{value}\n")