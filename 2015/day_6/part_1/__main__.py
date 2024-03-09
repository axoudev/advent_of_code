import requests
import configparser

config = configparser.ConfigParser()
config.read(r'E:\workspace\advent_of_code\2015\day_6\part_1\config.ini')

URL = 'http://adventofcode.com/2015/day/6/input'
SESSION = config['DEFAULT']['session_id']

LIGHTS = [[0 for i in range(1000)] for j in range(1000)]

def main():
    instructions = format_instructions(get_instructions());
    execute_instructions(instructions);
    
    print(sum([sum(row) for row in LIGHTS]));

def execute_instructions(instructions):
    for instr in instructions:
        start_coords, end_coords, command = instr
        for i in range(start_coords[0], end_coords[0] + 1):
            for j in range(start_coords[1], end_coords[1] + 1):
                if(command == 'on'):
                    LIGHTS[i][j] = 1
                elif(command == 'off'):
                    LIGHTS[i][j] = 0
                else:
                    LIGHTS[i][j] = 1 if LIGHTS[i][j] == 0 else 0
    

def get_instructions():
    response = requests.get(URL, cookies={'session': SESSION});
    return response.text.split('\n');

def format_instructions(instructions):
    formatted_instructions = []
    for instr in instructions:
        if(instr == ''): continue
        parts = instr.split(' ')
        command = parts[1] if parts[0] == 'turn' else parts[0]
        start_coords = tuple(map(int, parts[-3].split(',')))
        end_coords = tuple(map(int, parts[-1].split(',')))
        formatted_instructions.append([start_coords, end_coords, command])
    return formatted_instructions

if __name__ == "__main__":
    main()