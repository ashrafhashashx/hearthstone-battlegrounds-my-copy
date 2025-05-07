from enum import Enum

class CardType(Enum):
    Hero = 3
    Minion = 4
    Spell = 5
    ToolTip = 6
    HeroPower = 10
    BG22_BuddyMeter = 24
    QuestReward = 40
    TavernSpell = 42
    Anomaly = 43
    MinionEffect = 44

class Tribe(Enum):
    NoTribe = 00000000
    Quilboar = 43
    Beast = 20
    Murloc = 14
    Undead = 11
    Demon = 15
    Elemental = 18
    Mech = 17
    Pirate = 23
    Dragon = 24
    Naga = 92
    All = 26

class Hero(Enum):
    Rokara = 80229
    Xyrella = 70957
    OverlordSaurfang = 71455
    DeathSpeakerBlackthorn = 71459
    Voljin = 71464
    MasterNguyen = 71909
    GuffRunetotem = 68130
    KurtusAshfallen = 104875
    TamsinRoame = 77911
    Galewing = 75703
    MutanusTheDevourer = 71914
    Diablo = 72471
    CarielRoame = 73941
    ScabbsCutterbutter = 76563
    CookieTheCook = 77434
    Sneed = 76520
    TavishStormpike = 77990
    Brukan = 79720
    Drekthar = 80244
    VanndarStormpike = 80248
    VardenDawngrasp =  80539
    QueenAzshara = 79619
    IniStormcoil = 81572
    AmbassadorFaelin = 81570
    Onyxia = 82114
    Ozumat = 86014
    MurlocHolmes = 90403
    LadyVashj = 85126
    HeistbaronTogwaggle = 86292
    SylvanasWindrunner = 89294
    SireDenathrius = 92961
    EnhanceoMechano = 96872
    ProfessorPutricide = 97814
    TeronGorefiend = 98728
    ETCBandManager = 101346
    CapnHoggarr = 101132
    IngeTheIronHymn = 103501
    RockMasterVoone = 99034
    ThorimStormlord = 104628
    SnakeEyes = 105315
    TaethelanBloodwatcher = 105432
    DoctorHollidae = 110472
    MarinTheManager = 113311
    FarseerNobundo = 116924
    ZerekMasterCloner = 117410
    ExarchOthaar = 117426
    JimRaynor = 118681
    Artanis = 119196
    KerriganQueenOfBlades = 120362
    TheNamelessOne = 104569
    FlobbidinousFloop = 104672
    MadamGoya = 107184
    Cho = 104983
    Gall = 104985

class HeroPower(Enum):
    pass

relevant_carddefs_tags = [
    'CARDNAME',
    'CARDTEXT',
    'HEALTH',
    'ATK',
    'CARDRACE',
    'TECH_LEVEL',
    'CARDTYPE',
    'MAGNETIC',
    'AURA',
    'BATTLEGROUNDS_DARKMOON_PRIZE_TURN',
    'CANT_ATTACK',
    'IS_BACON_DUOS_EXCLUSIVE',
    'SECRET',
    'CHOOSE_ONE',
    'HERO_POWER'
]

irrelevant_carddefs_tags = [
    'AURA',
    'CANT_ATTACK',
    'BATTLEGROUNDS_DARKMOON_PRIZE_TURN',
    'SECRET',
    'CHOOSE_ONE',
    'ARTISTNAME',
    'MAGNETIC',
    'HEALING_DOES_DAMAGE',
    'TAG_SCRIPT_DATA_NUM_4',
    'FLAVORTEXT',
    'BACON_TRIPLE_UPGRADE_MINION_ID',
    'CARD_SET',
    'CLASS',
    'FACTION',
    'RARITY',
    'BACON_REFRESH_TOOLTIP',
    'BACON_FREEZE_TOOLTIP',
    'TRIGGER_VISUAL',
    'IS_BACON_POOL_MINION',
    'BACON_SPELLCRAFT_ID',
    'SPELL_SCHOOL',
    'BATTLECRY',
    'WINDFURY',
    'DIVINE_SHIELD',
    'USE_DISCOVER_VISUALS',
    'DISCOVER',
    'TAUNT',
    'END_OF_TURN_TRIGGER',
    'ELITE',
    'DEATHRATTLE',
    'REBORN',
    'VENOMOUS',
    'SCORE_VALUE_1',
    'AVENGE',
    'OVERKILL',
    'ADAPT',
    'BACON_REBORN_TOOLTIP',
    'TAG_SCRIPT_DATA_NUM_1',
    'TAG_SCRIPT_DATA_NUM_2',
    'TAG_SCRIPT_DATA_NUM_3',
    'BACON_HEROPOWER_BASE_HERO_ID',
    'HAS_ACTIVATE_POWER',
    'ENCHANTMENT_BIRTH_VISUAL',
    'ENCHANTMENT_IDLE_VISUAL',
    'BACON_SELL_VALUE',
    'TARGETING_ARROW_TEXT',
    'BACON_BUDDY',
    'IMP',
    'HIDE_COST',
    'COST',
    'START_OF_COMBAT',
    'WHELP',
    'BACON_TRINKET',
    'BACON_TRIGGER_XY',
    'BACON_PASS_TOOLTIP',
    'BACON_EVOLUTION_CARD_ID',
    'BACON_DONT_DISPLAY_HP_IN_LEADERBOARD_OR_STATS',
    'PREMIUM',
    'BACON_BLOOD_GEM_TOOLTIP',
    'InvisibleDeathrattle',
    'BONUS_KEYWORDS',
    'POISONOUS',
    'MULTIPLE_CLASSES',
    'STEALTH',
    'ENCHANTMENT_INVISIBLE',
    'ZERG',
    'IMMUNE_WHILE_ATTACKING',
    'IS_BACON_POOL_SPELL',
    'MAGNETIC_TO_RACE',
    'BACON_TRIPLED_BASE_MINION_ID',
    'FRENZY',
    'IMMUNE',
    'BACON_TRIGGER_UPBEAT',
    'PROTOSS',
    'HOW_TO_EARN',
    'HOW_TO_EARN_GOLDEN',
    'COLLECTIBLE',
    'TERRAN',
    'FREEZE',
    'BACON_TURNS_TILL_ACTIVE',
    'HEROPOWER_UNLIMITED_USES',
    'BACON_TRIGGER_XY_STAY',
    'SIGIL',
    'BACON_ANOMALY_ALL_HEROES_ARE_THIS_DBID',
    'BACON_TRINKETS_ACTIVE',
    'TAG_SCRIPT_DATA_NUM_6',
    'BACON_IS_MAGIC_ITEM_DISCOVER',
    'BACON_IS_POTENTIAL_TRINKET',
    'BACON_TURNS_LEFT_TO_DISCOVER_TRINKET',
    'OBJECTIVE',
    'BACON_EVOLUTION_CARD_ID_2',
    'QUEST_PROGRESS_TOTAL',
    'OBJECTIVE_AURA',
    'BACON_DONT_SHOW_PAIR_TRIPLE_DISCOVER_VFX',
    'FALLBACK_ENCHANTMENT_PORTRAIT_DBID',
    'BACON_BUY_BUDDY',
    'TWINSPELL',
    'BACON_SHOW_REFRESH_LEFT_BANNER',
    'BACON_HERO_POWER_ACTIVATED',
    'QUEST',
    'QUEST_HIDE_PROGRESS',
    'BACON_COSTS_HEALTH_TO_BUY',
    'BACON_MINION_TYPE_REWARD',
    'BACON_CARD_DBID_REWARD',
    'LITERALLY_UNPLAYABLE',
    'BACON_QUESTS_ACTIVE',
    'DARKMOON_FAIRE_PRIZES_ACTIVE',
    'SCORE_VALUE_2',
    'HIDE_STATS',
    'BACON_DIED_LAST_COMBAT_HINT',
    'BACON_DOUBLE_QUEST_HERO_POWER',
    'SIDE_QUEST',
    'BACON_IS_BOB_QUEST',
    'BACON_STEALTH_TOOLTIP',
    'BACON_BUDDY_ENABLED',
    'CHOICE_NAME_DISPLAY_TYPE',
    'CHOICE_ACTOR_TYPE',
    'BACON_NO_TIER_UP_BUTTON',
    'BACON_CONSUME_TOOLTIP',
    'COLLECTION_RELATED_CARD_DATABASE_ID',
    'BACON_PUTRICIDES_CREATION_TOOLTIP',
    'SPELLCRAFT_HINT',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '10',
    '11',
    '14',
    '15',
    '16',
    '17',
    '18',
    '20',
    '23',
    '24',
    '25',
    '33',
    '43',
    '50',
    '51',
    '60',
    '70',
    '75',
    '80',
    '83',
    '85',
    '88',
    '90',
    '92',
    '95',
    '100',
    '105',
    '110',
    '115',
    '120',
    '125',
    '130',
    '135',
    '140',
    '145',
    '150',
    '160',
    '170',
    '175',
    '180',
    '190',
    '200',
    '205',
    '210',
    '235',
    '250',
    '300',
    '315',
    '400',
    '600',
    '999',
    '17376',
    '17377',
    '17378',
    '17379',
    '17409',
    '17412',
    '17423',
    '17429',
    '17445',
    '17446',
    '17447',
    '17448',
    '17449',
    '17454',
    '17458',
    '17459',
    '17460',
    '17461',
    '17462',
    '17463',
    '17464',
    '17466',
    '17504',
    '17511',
    '17547',
    '17548',
    '17549',
    '17551',
    '17552',
    '17553',
    '17554',
    '17555',
    '17556',
    '17557',
    '17558',
    '17559',
    '17560',
    '17563',
    '17569',
    '17570',
    '17571',
    '17581',
    '17582',
    '17584',
    '17643',
    '17644',
    '17647',
    '17648',
    '17649',
    '17747',
    '17781',
    '17782',
    '17784',
    '17785',
    '17891',
    '17892',
    '17893',
    '17894',
    '17895',
    '17896',
    '17897',
    '17898',
    '17899',
    '18041',
    '18061',
    '18062',
    '18039',
    '18059',
    '18208',
    '18209',
    '18212',
    '18213',
    '18215',
    '18217',
    '18300',
    '18717',
    '18718',
    '18719',
    '18722',
    '18765',
    '18812',
    '18813',
    '18814',
    '18817',
    '18818',
    '18820',
    '19011',
    '19012',
    '19013',
    '19209',
    '19210',
    '19238',
    '19239',
    '19241',
    '19242',
    '19243',
    '19244',
    '19245',
    '19247',
    '19248',
    '19258',
    '19259',
    '19260',
    '19261',
    '19285',
    '19291',
    '86227',
    '89725',
    '92971',
    '96813',
    '96923',
    '96924',
    '96925',
    '96926',
    '96927',
    '98579',
    '98582',
    '98586',
    '101308',
    '105944',
    '107909',
    '107913',
    '112365',
    '115722',
    '115990',
    '116246',
    '116247',
    '116915',
    '116917',
    '119138',
    '119204',
    '120023',
    '120042',
    '120044'
]
