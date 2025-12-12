import re
from itertools import combinations

def parse_line(line):
    indicator_match = re.search(r'\[([.#]+)\]', line)
    indicator = indicator_match.group(1)
    n_lights = len(indicator)
    target = [1 if c == '#' else 0 for c in indicator]
    
    buttons = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        indices = [int(x) for x in match.group(1).split(',')]
        buttons.append(indices)
    
    return n_lights, target, buttons

def solve_machine(n_lights, target, buttons):
    n_buttons = len(buttons)
    
    for num_presses in range(n_buttons + 1):
        for combo in combinations(range(n_buttons), num_presses):
            # Simulate pressing these buttons
            state = [0] * n_lights
            for btn_idx in combo:
                for light_idx in buttons[btn_idx]:
                    state[light_idx] ^= 1
            
            if state == target:
                return num_presses
    
    return -1 

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total = 0
    for line in lines:
        if not line.strip():
            continue
        n_lights, target, buttons = parse_line(line)
        presses = solve_machine(n_lights, target, buttons)
        total += presses
    
    print(total)

if __name__ == '__main__':
    main()