from CardDefsXML.xml_to_card import carddefs_to_dicts
from GUI.gui import HearthstoneApp
from PowerLog.power_log_to_dicts import power_log_to_dicts

POWER_LOG_INPUT_PATH = 'INPUT/Power.log'
POWER_LOG_OUTPUT_PATH = 'OUTPUT/OUTPUTPower.log'
CARDDEFSXML_INPUT_PATH = 'INPUT/CardDefs.xml'
CARDDEFSXML_OUTPUT_PATH = 'OUTPUT/OUTPUTCardDefs.xml'
CARD_PATHS = list(map(lambda x: 'CardArt/' + x,['drakari.png', 'drakari.png', 'drakari.png', 'drakari.png', 'drakari.png', 'drakari.png']))

if __name__ == "__main__":
    # carddefs_to_dicts(CARDDEFSXML_INPUT_PATH, CARDDEFSXML_OUTPUT_PATH)
    # power_log_to_dicts(POWER_LOG_INPUT_PATH, POWER_LOG_OUTPUT_PATH)
    HearthstoneApp().run()
