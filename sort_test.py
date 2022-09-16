"""Sorting a large, randomly generated string and writing it to disk"""
import random
import time

def process_infromation_to_file(size=30000):
    information = create_information(size)
    write_information_to_file(information)

def create_information(size):
    random_list = []
    for i in range(size):
        random_list += random.choice('abcdefghijklmnopqrstuvwxyz')
        random_list = sorted(random_list)
    return random_list

def write_information_to_file(list_of_charactes):
    for character in list_of_charactes:
        with open("output.txt", "w") as output_file:
            output_file.write(character)



start = time.time()

process_infromation_to_file()

end = time.time()
total_time = end - start

print(f"Program took {total_time:.2f} seconds to run")
