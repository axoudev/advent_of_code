import requests
import configparser

config = configparser.ConfigParser()
config.read(r'E:\workspace\advent_of_code\config.ini')

URL = 'http://adventofcode.com/2015/day/7/input'
SESSION = config['DEFAULT']['session_id']

DOORS = {}

def main():
    instructions = get_instructions();
    execute_instructions(instructions);
    instructions[instructions.index('44430 -> b')] = str(DOORS['a'])+' -> b'
    execute_instructions(instructions);
    print(DOORS['a'])


def execute_instructions(instructions):
    for instr in instructions:
        parts = instr.split(' ')
        if(len(parts) == 3):
            if(parts[0].isdigit()):
                DOORS[parts[2]] = int(parts[0])
            else:
                if(parts[0] in DOORS):
                    DOORS[parts[2]] = DOORS[parts[0]]
                else:
                    instructions.append(instr)
        elif(len(parts) == 4):
            if(parts[1] in DOORS):
                DOORS[parts[3]] = ~ DOORS[parts[1]]
            else:
                instructions.append(instr)
        elif(len(parts) == 5):
            first = 0
            second = 0
            if(parts[0].isdigit()):
                first = int(parts[0])
            else:
                if(parts[0] in DOORS):
                    first = DOORS[parts[0]]
                else:
                    instructions.append(instr)
                    continue
            if(parts[2].isdigit()):
                second = int(parts[2])
            else:
                if(parts[2] in DOORS):
                    second = DOORS[parts[2]]
                else:
                    instructions.append(instr)
                    continue

            if(parts[1] == 'AND'):
                DOORS[parts[4]] = first & second
            elif(parts[1] == 'OR'):
                DOORS[parts[4]] = first | second
            elif(parts[1] == 'LSHIFT'):
                DOORS[parts[4]] = first << second
            elif(parts[1] == 'RSHIFT'):
                DOORS[parts[4]] = first >> second
    
    
def get_instructions():
    response = requests.get(URL, cookies={'session': SESSION});
    return response.text.split('\n');
    

if __name__ == "__main__":
    main()