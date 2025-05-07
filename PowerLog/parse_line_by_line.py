import re
from typing import List, Dict
from PowerLog.helpers import extract_keys_and_values, functions_to_ignore, events, events_to_ignore

# function_pattern = re.compile(r"\s(\w+\.\w+\(\))\s*-")
function_pattern = re.compile(r'([A-Za-z0-9_.]+\(\))(?=\s*-\s*)')
first_word_after_first_dash_pattern = re.compile(r'-\s*([^\s=]+)')


def parse_line_by_line(lines: List[str]) -> List[Dict]:
    game_state_updates = []
    update_batch = {}
    for i in range (len(lines)):
        line = lines[i]
        # for now, ignoring BLOCK_START and BLOCK_END:
        match = function_pattern.search(line)
        if not match:
            raise Exception(f'Line {i+1}: cannot find a function.')
        function = match.group(1)
        if function in functions_to_ignore:
            continue # TODO but maybe we append the update batch
        match = first_word_after_first_dash_pattern.search(line)
        if not match:
            print(line)
            raise Exception(f'Line {i+1}: The line starts with a function but still I cannot find any event nor "tag=" after the first dash symbol.')
        first_word_after_first_dash = match.group(1)
        if first_word_after_first_dash in events:
            # if we encounter an event, then we are done with the previous one, and we can safely append update batch:
            if update_batch: game_state_updates.append(update_batch)
            if first_word_after_first_dash in events_to_ignore:
                continue
            # start a new update batch if the event is to be considered (not ignored):
            update_batch = {'event': first_word_after_first_dash}
            update_batch.update(extract_keys_and_values(line, i))
        elif 'tag=' in line:
            x = extract_keys_and_values(line, i)
            tag = list(x.keys())[0]
            value = list(x.values())[0]
            update_batch[tag] = value
        elif 'GameEntity EntityID=' in line:
            update_batch['GameEntity'] = extract_keys_and_values(line, i)['EntityID']
        elif 'Player EntityID=' in line:
            game_state_updates.append(update_batch)
            update_batch = {'Player': extract_keys_and_values(line, i)['EntityID']}
        elif any(x in line for x in ['Info[', 'Source = [', ' Source = ', 'Targets[']):
            pass
        else:
            print(i+1, line)
            print(function)
            raise Exception(f'Line {i+1}: Unknown keyword (the first word after the first dash symbol); Not a known event, nor a "tag=".')



    return game_state_updates