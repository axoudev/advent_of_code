import requests
import configparser

config = configparser.ConfigParser()
config.read(r'E:\workspace\advent_of_code\2015\5\part_1\config.ini')

URL = 'http://adventofcode.com/2015/day/5/input'
SESSION = config['DEFAULT']['session_id']

def main():
    strings = get_strings();
    print(count_nice_strings(strings));

def count_nice_strings(strings):
    return sum([is_nice_string(s) for s in strings]);

def is_nice_string(s):
    return has_three_vowels(s) and has_double_letter(s) and not has_bad_string(s);

def has_three_vowels(s):
    return sum([c in "aeiou" for c in s]) >= 3;

def has_double_letter(s):
    return any([s[i] == s[i+1] for i in range(len(s) - 1)]);

def has_bad_string(s):
    return any([bad in s for bad in ["ab", "cd", "pq", "xy"]]);

def get_strings():
    response = requests.get(URL, cookies={'session': SESSION});
    return response.text.split('\n');

if __name__ == "__main__":
    main()
