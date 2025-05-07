from CardDefsXML.values import Tribe, CardType, HeroPower, Hero


class CardInfo:
    def __init__(self,
        card_id: str = None,
        name: str = None,
        text: str = None,
        cardtype: CardType = None,
        heropower: HeroPower = None,
        hero: Hero = None,
        health: int = None,
        attack: int = None,
        tribe: Tribe = None,
        level: int = None,
        is_secret: bool = None,
        is_choose_one: bool = None,
        is_magnetic: bool = None,
        is_aura: bool = None,
        is_darkmoon_prize: int = None,
        darkmoon_level: int = None,
        cannot_attack: bool = None,
        is_duos_exclusive: bool = None,
        extras: {} = None
                 ):

        self.card_id = card_id or None
        self.name = name or None
        self.text = text or None
        self.cardtype = cardtype or None
        self.hero = hero or None
        self.heropower = heropower or None
        self.health = health or None
        self.attack = attack or None
        self.tribe = tribe or None
        self.level = level or None
        self.is_secret = is_secret or None
        self.is_choose_one = is_choose_one or None
        self.is_magnetic = is_magnetic or None
        self.is_aura = is_aura or None
        self.is_darkmoon_prize = is_darkmoon_prize or None
        self.darkmoon_level = darkmoon_level or None
        self.cannot_attack = cannot_attack or None
        self.is_duos_exclusive = is_duos_exclusive or None
        self.extras = extras or {}

    def validate(self):
        if self.cardtype == CardType.Minion:
            if self.tribe is None:
                self.tribe= Tribe.NoTribe

    def __str__(self):
        result = ''

        def safe_add(x, key: str):
            nonlocal result
            if x:
                result += f'{key} = {str(x)} \n'


        safe_add(self.card_id, 'cardid')
        safe_add(self.name, 'name')
        safe_add(self.text, 'text')
        safe_add(self.health, 'health')
        safe_add(self.attack, 'attack')
        if self.tribe: safe_add(Tribe(self.tribe), 'tribe')
        safe_add(self.level, 'level')
        if self.cardtype: safe_add(CardType(self.cardtype), 'cardtype')
        safe_add(self.is_magnetic, 'is_magnetic')
        safe_add(self.is_aura, 'is_aura')
        safe_add(self.extras, 'extras')

        return result

    def print_only_if_still_unexplained_extras(self):
        if self.extras:
            print(self)

