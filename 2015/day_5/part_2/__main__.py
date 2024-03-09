import requests
import configparser

config = configparser.ConfigParser()
config.read(r'E:\workspace\advent_of_code\2015\day_5\part_1\config.ini')

URL = 'http://adventofcode.com/2015/day/5/input'
SESSION = config['DEFAULT']['session_id']

def main():
    strings = get_strings();
    print(count_nice_strings(strings));

def count_nice_strings(strings):
    return sum([is_nice_string(s) for s in strings]);

def is_nice_string(s):
    return has_double_pair(s) and has_sandwich(s);

def has_double_pair(s):
    for i in range(len(s) - 1):
        if s[i:i+2] in s[i+2:]:
            return True
    return False

def has_sandwich(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False

def get_strings():
    response = requests.get(URL, cookies={'session': SESSION});
    return response.text.split('\n');

if __name__ == "__main__":
    main()
