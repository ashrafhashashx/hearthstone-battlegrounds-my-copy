import re
from enum import Enum, IntEnum
from typing import Dict


def iprint(line_number: int, x: str):
    pass
    # print(f'{str(line_number+1).zfill(7)} ' + x)


# keys_values_pattern = r'(\w+)=\[?([^\s\]]+)'
# keys_values_pattern = r'(\w+)=((?:[^\s=]+\s?)+?)(?=\s+\w+=|$)'
# keys_values_pattern = r'(\w+)=((?:(?!\w+=).)+)'
keys_values_pattern = r'(\w+)=((?:(?!\s\w+=).)+)'

def extract_keys_and_values(line: str, i: int) -> Dict:
    if 'Entity=[' in line:
        line = line.replace('Entity=[','').replace(']','').replace('[','')
    else:
        line = line.replace('[','').replace(']','')
    pairs = re.findall(keys_values_pattern, line)
    result = dict(pairs)

    for k in result.keys():
        pass
        # if not (k in relevant_keys):
        #     raise Exception(f'Line {i+1}: a new key name found : {k}')

    return result

class Depth(IntEnum):
    Undefined = 0
    A = 1
    B = 5
    C = 9
    D = 13
    E = 17
    F = 21
    G = 23
    H = 27
    I = 31
    J = 35

def number_of_consecutive_spaces_after_first_dash(line: str) -> Depth:
    match = re.search(r'-( +)', line)
    if match:
        result = len(match.group(1))
    else:
        result = 0
    return Depth(result)

# class Event(Enum):
#     TG = 'TAG_CHANGE'
#     BS = 'BLOCK_START'
#     BE = 'BLOCK_END'
#     FE = 'FULL_ENTITY'
#     SE = 'SHOW_ENTITY'
#     HE = 'HIDE_ENTITY'
#     MD = 'META_DATA'
#     SSS = 'SUB_SPELL_START'
#     SSE = 'SUB_SPELL_END'
#     CE = 'CHANGE_ENTITY'
#     CG = 'CREATE_GAME'
#
#
# class Function(Enum):
#     GSDPP = 'GameState.DebugPrintPower()'
#     PTLDPP = 'PowerTaskList.DebugPrintPower()'
#     GSDPO = 'GameState.DebugPrintOptions()'                         # ignore
#     PTLDD = 'PowerTaskList.DebugDump()'                             # ignore
#     PPPHFCTL = 'PowerProcessor.PrepareHistoryForCurrentTaskList()'  # ignore
#     PPECTL = 'PowerProcessor.EndCurrentTaskList()'                  # ignore
#     PPDTLFC = 'PowerProcessor.DoTaskListForCard()'
#     GSDPPL = 'GameState.DebugPrintPowerList()'                      # ignore
#     GSSO = 'GameState.SendOption()'                                 # ignore
#     GSDPECs = 'GameState.DebugPrintEntityChoices()'                 # ignore
#     PSC = 'PowerSpellController'
#     GSDPECn = 'GameState.DebugPrintEntitiesChosen()'                # ignore
#     GSSC = 'GameState.SendChoices()',                               # ignore
#     CCMWTSC = 'ChoiceCardMgr.WaitThenShowChoices()',                # ignore
#     CCMWTHCFP = 'ChoiceCardMgr.WaitThenHideChoicesFromPacket()'     # ignore
#     GSDPG = 'GameState.DebugPrintGame()'                            # ignore

functions = [
    'GameState.DebugPrintPower()',
    'PowerTaskList.DebugPrintPower()',
    'GameState.DebugPrintOptions()',                                # ignore
    'PowerTaskList.DebugDump()',                                    # ignore
    'PowerProcessor.PrepareHistoryForCurrentTaskList()',            # ignore
    'PowerProcessor.EndCurrentTaskList()',                          # ignore
    'PowerProcessor.DoTaskListForCard()',
    'GameState.DebugPrintPowerList()',                              # ignore
    'GameState.SendOption()',                                       # ignore
    'GameState.DebugPrintEntityChoices()',                          # ignore
    '.InitPowerSpell()', # which is also 'PowerSpellController'      # ignore
    'GameState.DebugPrintEntitiesChosen()',                         # ignore
    'GameState.SendChoices()',                                      # ignore
    'ChoiceCardMgr.WaitThenShowChoices()',                          # ignore
    'ChoiceCardMgr.WaitThenHideChoicesFromPacket()',                # ignore
    'GameState.DebugPrintGame()'                                    # ignore
]

functions_to_ignore = list(map(lambda i: functions[i], [2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

events = [
    'TAG_CHANGE',
    'BLOCK_START',
    'BLOCK_END',
    'FULL_ENTITY',
    'SHOW_ENTITY',
    'HIDE_ENTITY',
    'META_DATA',
    'SUB_SPELL_START',
    'SUB_SPELL_END',
    'CHANGE_ENTITY',
    'CREATE_GAME',
]

events_to_ignore = [
    'BLOCK_END',
    'META_DATA',
    'SUB_SPELL_START',
    'SUB_SPELL_END'
]
