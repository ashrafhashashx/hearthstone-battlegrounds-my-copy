from typing import List, Dict, Any

from lxml import etree
from lxml.etree import Element
from CardDefsXML.helpers import pprint
from CardDefsXML.values import irrelevant_carddefs_tags


def get_only_bg_cards_xml_elements(carddefxml_path: str) -> List[Element]:
    # load xml
    tree = etree.parse(carddefxml_path)
    root = tree.getroot()

    # Find all Entity elements directly under CardDefs
    all_cards: [Element] = root.xpath('./Entity')
    bg_cards: [Element] = []
    for c in all_cards:
        card_id: str = c.get('CardID')
        if (not card_id.startswith(('bg', 'Bg', 'bG', 'BG'))) or (card_id.endswith(('e', 'G'))):
            continue
        else:
            bg_cards.append(c)

    return bg_cards


# def carddefs_to_dicts(carddefxml_path: str, output_path: str) -> List[Dict[str, str]]:
#     bg_cards = get_only_bg_cards_xml_elements(carddefxml_path)
#     result = []
#     for element in bg_cards:
#         card = {}
#
#         x = element.xpath('Tag[@name="CARDNAME"]/enUS')[0].text
#         if x is None: raise Exception(f'Card has no name: {str(element)}')
#         card['name'] = x
#
#         x = element.xpath('Tag[@name="CARDTEXT"]/enUS')[0].text
#         if x is None: raise Exception(f'Card has no text: {str(element)}')
#         card['text'] = x
#
#
#     return result


# def extract_names(carddefxml_path: str):
#     bg_cards: [Element] = get_only_bg_cards_xml_elements(carddefxml_path)
#     result: [str] = []
#     for c in bg_cards:
#         result.append(c.xpath('Tag[@name="CARDNAME"]/enUS')[0].text)
#     return list(set(result))


def carddefs_to_dicts(carddefxml_path: str, output_path: str) -> List[Dict['str', Any]]:
    bg_cards = get_only_bg_cards_xml_elements(carddefxml_path)

    result = []
    for c in bg_cards:
        one_card_info = {}
        # get card id
        card_id: str = c.get('CardID')
        if card_id is not None:
            x = {'card_id': card_id}
        # collect all elements (tags):
        tags: [Element] = (c.xpath('Tag') + c.xpath('ReferencedTag'))
        # extract their names:
        tags_names: [str] = list(map(lambda t: t.get('name'), tags))
        # skip the whole card entity (tag) if it is a skin:
        if set(tags_names) & {'BACON_SKIN_PARENT_ID', 'BACON_SKIN', 'HERO_POWER'}:
            continue
        for tag in tags:
            tag_name: str = tag.get('name')
            value: str = tag.get('value') or None
            # skip the tag if we know it is irrelevant
            if tag_name in irrelevant_carddefs_tags:
                continue
            match tag_name:
                case 'CARDNAME':
                    x = tag.find('enUS').text
                    if x is None:
                        raise Exception(f'Card has no name:\n {pprint(c)}')
                    one_card_info['name'] = x
                case 'CARDTEXT':
                    x = tag.find('enUS').text
                    if x is None:
                        raise Exception(f'Card has no text:\n {pprint(c)}')
                    one_card_info['text'] = x
                case 'HEALTH':
                    one_card_info['health'] = int(value)
                case 'ATK':
                    one_card_info['attack'] = int(value)
                case 'CARDRACE':
                    one_card_info['tribe'] = int(value)
                case 'TECH_LEVEL':
                    one_card_info['level'] = int(value)
                case 'CARDTYPE':
                    one_card_info['cardtype'] = int(value)
                case 'IS_BACON_DUOS_EXCLUSIVE':
                    one_card_info['is_duos_exclusive'] = True
                case 'HERO_POWER':
                    one_card_info['heropower'] = value
                case _:
                    raise Exception(f'Unknown tag name. Card is:\n {pprint(c)}\n And the tag name is: {tag_name}')
        result.append(one_card_info)
    result_str = list(map(lambda d: str(d) + '\n', result))
    with open(output_path, "w", encoding="utf-8") as file:
        file.writelines(result_str)
    return result
