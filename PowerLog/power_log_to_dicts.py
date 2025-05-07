from typing import List, Dict

from PowerLog.parse_line_by_line import parse_line_by_line


def power_log_to_dicts(power_log_path: str, output_path: str):

    with open(power_log_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result: List[Dict] = parse_line_by_line(lines)
    result_str = list(map(lambda x: str(x) + '\n', result))

    with open(output_path, "w", encoding="utf-8") as file:
        file.writelines(result_str)
