"""Sorting a large, randomly generated string and writing it to disk"""
import random


def process_infromation_to_file(size=10**5):
    information = create_information(size)
    write_string_to_file(information)

def create_information(size):
    random_string = ''
    for i in range(size):
        random_string += random.choice('abcdefghijklmnopqrstuvwxyz')
        random_string = sorted(random_string)
    # sorted_string = sorted(random_string)
    return random_string

def write_string_to_file(text):
    with open("output.txt", "w") as sorted_text:
        for character in text:
            sorted_text.write(character)



process_infromation_to_file()