import abc


class Card(metaclass=abc.ABCMeta):
 name = None
 rarity = None
 type = None
 cost = None
 set = None


class SpellCard(Card):
 name = None
 rarity = None
 type = 'spell'
 cost = None
 set = None
 major = None
 description = None

 directional = None


class MinionCard(Card):
 name = None
 rarity = None
 type = 'minion'
 cost = None
 set = None
 major = None
 description = None

 ATK = None
 health = None
 race = None
 directional = None



class WeaponCard(Card):
 name = None
 rarity = None
 type = 'weapon'
 cost = None
 set = None
 major = None
 description = None

 durability = 2
 ATK = 3


class FleryWarAxe(WeaponCard):
 name = 'Flery War Axe'
 rarity = 'free'
 type = 'weapon'
 cost = 3
 set = 'basic'
 major = 'warrior'
 description = 'none'

 durability = 2
 ATK = 3
 attribute = []


class ArcaneShot(SpellCard):
 name = 'Arcane Shot'
 rarity = 'free'
 type = 'spell'
 cost = 1
 set = 'Basic'
 major = 'hunter'
 description = 'Deal 2 damage.'

 directional = True


class BloodfenRaptor(MinionCard):
 name = 'Bloodfen Raptor'
 rarity = 'free'
 type = 'minion'
 cost = 2
 set = 'Basic'
 major = 'neutral'
 description = 'none'

 attribute = []
 ATK = 3
 health = 2
 race = 'beast'
 directional = False


class AcidicSwampOoze(MinionCard):
 name = 'Acidic Swamp Ooze'
 rarity = 'free'
 type = 'minion'
 cost = 2
 set = 'Basic'
 major = 'neutral'
 description = 'Battlecry: Destroy your opponent\'s\n weapon.'

 attribute = []
 ATK = 3
 health = 2
 race = 'none'
 directional = False


class AldrachiWarblades(WeaponCard):
 name = 'Aldrachi Warblades'
 rarity = 'free'
 type = 'weapon'
 cost = 3
 set = 'Basic'
 major = 'demonHunter'
 description = 'Lifesteal'

 durability = 2
 ATK = 2
 attribute = []


class AncestralHealing(SpellCard):
 name = 'Ancestral Healing'
 rarity = 'free'
 type = 'spell'
 cost = 0
 set = 'Basic'
 major = 'shaman'
 description = 'Restore a minion to full Health and give\n it Taunt.'

 directional = True


class AnimalCompanion(SpellCard):
  name = 'Animal Companion'
  rarity = 'free'
  type = 'spell'
  cost = 3
  set = 'Basic'
  major = 'hunter'
  description = 'Summon a random Beast Companion.'

  directional = False


class ArcaneExplosion(SpellCard):
  name = 'Arcane Explosion'
  rarity = 'free'
  type = 'spell'
  cost = 2
  set = 'Basic'
  major = 'mage'
  description = 'Deal 1 damage to all enemy minions.'

  directional = False


class ArcaneIntellect(SpellCard):
  name = 'Arcane Intellect'
  rarity = 'free'
  type = 'spell'
  cost = 3
  set = 'Basic'
  major = 'mage'
  description = 'Draw 2 cards.'

  directional = False


class ArcaneMissiles(SpellCard):
  name = 'Arcane Missiles'
  rarity = 'free'
  type = 'spell'
  cost = 1
  set = 'Basic'
  major = 'mage'
  description = 'Deal 3 damage randomly split among\n enemy characters.'

  directional = False


class ArcaniteReaper(WeaponCard):
 name = 'Arcanite Reaper'
 rarity = 'free'
 type = 'weapon'
 cost = 5
 set = 'Basic'
 major = 'warrior'
 description = 'none'

 durability = 2
 ATK = 5
 attribute = []


class Archmage(MinionCard):
 name = 'Archmage'
 rarity = 'free'
 type = 'minion'
 cost = 6
 set = 'Basic'
 major = 'neutral'
 description = 'Spell Damage +1'

 attribute = []
 ATK = 4
 health = 7
 race = 'none'
 directional = False


class Assassinate(SpellCard):
  name = 'Assassinate'
  rarity = 'free'
  type = 'spell'
  cost = 5
  set = 'Basic'
  major = 'rogue'
  description = 'Destroy an enemy minion.'

  directional = True


class Assassin_sBlade(WeaponCard):
 name = 'Assassin\'s Blade'
 rarity = 'free'
 type = 'weapon'
 cost = 5
 set = 'Basic'
 major = 'rogue'
 description = 'none'

 durability = 4
 ATK = 3
 attribute = []


class Backstab(SpellCard):
 name = 'Backstab'
 rarity = 'free'
 type = 'spell'
 cost = 0
 set = 'Basic'
 major = 'rogue'
 description = 'Deal 2 damage to an undamaged minion.'

 directional = True


class BlessingofKings(SpellCard):
    name = 'Blessing of Kings'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'paladin'
    description = 'Give a minion +4/+4.(+4 Attack/+4 Health).'

    directional = True

class BlessingofMight(SpellCard):
    name = 'Blessing of Might'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'paladin'
    description = 'Give a minion +3 Attack.'

    directional = True

class Bloodlust(SpellCard):
    name = 'Bloodlust'
    rarity = 'free'
    type = 'spell'
    cost = 5
    set = 'Basic'
    major = 'shaman'
    description = 'Give your minions +3 Attack this turn.'

    directional = False


class BluegillWarrior(MinionCard):
 name = 'Bluegill Warrior'
 rarity = 'free'
 type = 'minion'
 cost = 2
 set = 'Basic'
 major = 'neutral'
 description = 'Charge'

 attribute = []
 ATK = 2
 health = 1
 race = 'murloc'
 directional = False


class BootyBayBodyguard(MinionCard):
     name = 'Booty Bay Bodyguard'
     rarity = 'free'
     type = 'minion'
     cost = 5
     set = 'Basic'
     major = 'neutral'
     description = 'Taunt'

     attribute = ['T']
     ATK = 5
     health = 4
     race = 'none'
     directional = False


class BoulderfistOgre(MinionCard):
     name = 'Boulderfist Ogre'
     rarity = 'free'
     type = 'minion'
     cost = 6
     set = 'Basic'
     major = 'neutral'
     description = 'none'

     attribute = []
     ATK = 6
     health = 7
     race = 'none'
     directional = False


class ChaosNova(SpellCard):
    name = 'Chaos Nova'
    rarity = 'free'
    type = 'spell'
    cost = 5
    set = 'Basic'
    major = 'demonHunter'
    description = 'Deal 4 damage to all minions.'

    directional = False


class ChaosStrike(SpellCard):
    name = 'Chaos Strike'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'demonHunter'
    description = 'Give your hero +2 Attack this turn\n Draw a card.'

    directional = False


class Charge(SpellCard):
    name = 'Charge'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'warrior'
    description = 'Give a friendly minion Charge. It\n can\'t attack heroes this turn.'

    directional = True


class ChillwindYeti(MinionCard):
    name = 'Chillwind Yeti'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'none'

    attribute = []
    ATK = 4
    health = 5
    race = 'none'
    directional = False


class Claw(SpellCard):
    name = 'Claw'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'druid'
    description = 'Give your hero +2 Attack this turn\n and 2 Armor.'

    directional = False


class Cleave(SpellCard):
    name = 'Cleave'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'warrior'
    description = 'Deal 2 damage to two random enemy\n minions.'

    directional = False


class Consecration(SpellCard):
    name = 'Consecration'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'paladin'
    description = 'Deal 2 damage to all enemies.'

    directional = False


class CoordinatedStrike(SpellCard):
    name = 'Coordinated Strike'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'demonHunter'
    description = 'Summon three 1/1 Illidari with Rush.'

    directional = False


class CoreHound(MinionCard):
    name = 'Core Hound'
    rarity = 'free'
    type = 'minion'
    cost = 7
    set = 'Basic'
    major = 'neutral'
    description = 'none'

    attribute = []
    ATK = 9
    health = 5
    race = 'beast'
    directional = False


class Corruption(SpellCard):
    name = 'Corruption'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'warlock'
    description = 'Choose an enemy minion. At the start\n of your turn, destroy it.'

    directional = True


class DalaranMage(MinionCard):
    name = 'Dalaran Mage'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Spell Damage +1'

    attribute = []
    ATK = 1
    health = 4
    race = 'none'
    directional = False


class DarkscaleHealer(MinionCard):
    name = 'Darkscale Healer'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Restore 2 Health to all\n friendly characters.'

    attribute = []
    ATK = 4
    health = 5
    race = 'none'
    directional = True


class DeadlyPoison(SpellCard):
    name = 'Deadly Poison'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'rogue'
    description = 'Give your weapon +2 Attack.'

    directional = False


class DragonlingMechanic(MinionCard):
    name = 'Dragonling Mechanic'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Summon a 2/1 Mechanical\n Dragonling.'

    attribute = []
    ATK = 2
    health = 4
    race = 'none'
    directional = False


class DrainLife(SpellCard):
    name = 'Drain Life'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'warlock'
    description = 'Deal 2 damage. Restore 2 Health to\n your hero.'

    directional = True


class ElvenArcher(MinionCard):
    name = 'Elven Archer'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Deal 1 damage.'

    attribute = []
    ATK = 1
    health = 1
    race = 'none'
    directional = True


class DreadInfernal(MinionCard):
    name = 'Dread Infernal'
    rarity = 'free'
    type = 'minion'
    cost = 6
    set = 'Basic'
    major = 'warlock'
    description = 'Battlecry: Deal 1 damage to ALL other\n characters.'

    attribute = []
    ATK = 6
    health = 6
    race = 'demon'
    directional = False


class Execute(SpellCard):
    name = 'Execute'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'warrior'
    description = 'Destroy a damaged enemy minion.'

    directional = True


class FanofKnives(SpellCard):
    name = 'Fan of Knives'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'rogue'
    description = 'Deal 1 damage to all enemy minions.\n Draw a card.'

    directional = False


class Felstalker(MinionCard):
    name = 'Felstalker'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'warlock'
    description = 'Battlecry: Discard a random card.'

    attribute = []
    ATK = 4
    health = 3
    race = 'demon'
    directional = False


class FireElemental(MinionCard):
    name = 'Fire Elemental'
    rarity = 'free'
    type = 'minion'
    cost = 6
    set = 'Basic'
    major = 'shaman'
    description = 'Battlecry: Deal 3 damage.'

    attribute = []
    ATK = 6
    health = 5
    race = 'elemental'
    directional = True


class Fireball(SpellCard):
    name = 'Fireball'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'mage'
    description = 'Deal 6 damage.'

    directional = True


class Flamestrike(SpellCard):
    name = 'Flamestrike'
    rarity = 'free'
    type = 'spell'
    cost = 7
    set = 'Basic'
    major = 'mage'
    description = 'Deal 4 damage to all enemy minions.'

    directional = False


class FlametongueTotem(MinionCard):
    name = 'Flametongue Totem'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'shaman'
    description = 'Adjacent minions have +2 Attack.'

    attribute = []
    ATK = 0
    health = 3
    race = 'totem'
    directional = False


class FrostNova(SpellCard):
    name = 'Frost Nova'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'mage'
    description = 'Freeze all enemy minions.'

    directional = False

class FrostShock(SpellCard):
    name = 'Frost Shock'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'shaman'
    description = 'Deal 1 damage to an enemy character\n and Freeze it.'

    directional = True


class Frostbolt(SpellCard):
    name = 'Frostbolt'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'mage'
    description = 'Deal 3 damage to a character and\n Freeze it.'

    directional = True


class FrostwolfGrunt(MinionCard):
    name = 'Frostwolf Grunt'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'neutral'
    description = 'Taunt'

    attribute = ['T']
    ATK = 2
    health = 2
    race = 'none'
    directional = False


class FrostwolfWarlord(MinionCard):
    name = 'Frostwolf Warlord'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Gain +1/+1 for each other\n friendly minion on the battlefield.'

    attribute = []
    ATK = 4
    health = 4
    race = 'none'
    directional = False


class GlaiveboundAdept(MinionCard):
    name = 'Glaivebound Adept'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'demonHunter'
    description = 'Battlecry: If your hero attacked this\n turn, deal 4 damage.'

    attribute = []
    ATK = 6
    health = 4
    race = 'none'
    directional = True


class GnomishInventor(MinionCard):
    name = 'Gnomish Inventor'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Draw a card.'

    attribute = []
    ATK = 2
    health = 4
    race = 'none'
    directional = False


class GoldshireFootman(MinionCard):
    name = 'Goldshire Footman'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'neutral'
    description = 'Taunt'

    attribute = ['T']
    ATK = 1
    health = 2
    race = 'none'
    directional = False


class GrimscaleOracle(MinionCard):
    name = 'Grimscale Oracle'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'neutral'
    description = 'Your other Murlocs have +1 Attack.'

    attribute = []
    ATK = 1
    health = 1
    race = 'murloc'
    directional = False


class GuardianofKings(MinionCard):
    name = 'Guardian of Kings'
    rarity = 'free'
    type = 'minion'
    cost = 7
    set = 'Basic'
    major = 'paladin'
    description = 'Battlecry: Restore 6 Health to your\n hero.'

    attribute = []
    ATK = 5
    health = 6
    race = 'none'
    directional = False


class GurubashiBerserker(MinionCard):
    name = 'Gurubashi Berserker'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'neutral'
    description = 'Whenever this minion takes damage,\n gain +3 Attack.'

    attribute = []
    ATK = 2
    health = 7
    race = 'none'
    directional = False


class HammerofWrath(SpellCard):
    name = 'Hammer of Wrath'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'paladin'
    description = 'Deal 3 damage. Draw a card.'

    directional = True


class HandofProtection(SpellCard):
    name = 'Hand of Protection'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'paladin'
    description = 'Give a minion Divine Shield.'

    directional = True


class HealingTouch(SpellCard):
    name = 'Healing Touch'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'druid'
    description = 'Restore 8 Health.'

    directional = True


class Hellfire(SpellCard):
    name = 'Hellfire'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'warlock'
    description = 'Deal 3 damage to ALL characters.'

    directional = False


class HeroicStrike(SpellCard):
    name = 'Heroic Strike'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'warrior'
    description = 'Give your hero +4 Attack this turn.'

    directional = False


class Hex(SpellCard):
    name = 'Hex'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'shaman'
    description = 'Transform a minion into a 0/1 Frog\n with Taunt.'

    directional = True


class HolyLight(SpellCard):
    name = 'Holy Light'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'paladin'
    description = 'Restore 6 Health.'

    directional = True


class HolyNova(SpellCard):
    name = 'Holy Nova'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'priest'
    description = 'Deal 2 damage to all enemy minions\n Restore 2 Health to all friendly characters.'

    directional = False


class HolySmite(SpellCard):
    name = 'Holy Smite'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'priest'
    description = 'Deal 3 damage to a minions.'

    directional = True


class Houndmaster(MinionCard):
    name = 'Houndmaster'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'hunter'
    description = 'Battlecry: Give a friendly Beast\n +2/+2 and Taunt.'

    attribute = []
    ATK = 4
    health = 3
    race = 'none'
    directional = True


class Humility(SpellCard):
    name = 'Humility'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'paladin'
    description = 'Change a minion\'s Attack to 1.'

    directional = True


class Hunter_sMark(SpellCard):
    name = 'Hunter\'s Mark'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'hunter'
    description = 'Change a minion\'s Health to 1.'

    directional = True


class InnerDemon(SpellCard):
    name = 'Inner Demon'
    rarity = 'free'
    type = 'spell'
    cost = 8
    set = 'Basic'
    major = 'demonHunter'
    description = 'Give your hero +8 Attack this turn.'

    directional = False


class Innervate(SpellCard):
    name = 'Innervate'
    rarity = 'free'
    type = 'spell'
    cost = 0
    set = 'Basic'
    major = 'druid'
    description = 'Gain 1 Mana Crystal this turn only.'

    directional = False


class IronbarkProtector(MinionCard):
    name = 'Ironbark Protector'
    rarity = 'free'
    type = 'minion'
    cost = 8
    set = 'Basic'
    major = 'druid'
    description = 'Taunt'

    attribute = ['T']
    ATK = 8
    health = 8
    race = 'none'
    directional = False


class IronforgeRifleman(MinionCard):
    name = 'Ironforge Rifleman'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Deal 1 damage.'

    attribute = []
    ATK = 2
    health = 2
    race = 'none'
    directional = True


class KillCommand(SpellCard):
    name = 'Kill Command'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'hunter'
    description = 'Deal 3 damage. If you have a Beast,\n deal 5 damage instead.'

    directional = True


class IronfurGrizzly(MinionCard):
    name = 'Ironfur Grizzly'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Taunt'

    attribute = ['T']
    ATK = 3
    health = 3
    race = 'beast'
    directional = False


class KoboldGeomancer(MinionCard):
    name = 'Kobold Geomancer'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'neutral'
    description = 'Spell Damage +1'

    attribute = []
    ATK = 2
    health = 2
    race = 'none'
    directional = False


class Kor_kronElite(MinionCard):
    name = 'Kor\'kron Elite'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'warrior'
    description = 'Charge'

    attribute = []
    ATK = 4
    health = 3
    race = 'none'
    directional = False


class Light_sJustice(WeaponCard):
 name = 'Light\'s Justice'
 rarity = 'free'
 type = 'weapon'
 cost = 1
 set = 'Basic'
 major = 'paladin'
 description = 'none'

 durability = 4
 ATK = 1
 attribute = []


class LordoftheArena(MinionCard):
     name = 'Lord of the Arena'
     rarity = 'free'
     type = 'minion'
     cost = 6
     set = 'Basic'
     major = 'neutral'
     description = 'Taunt'

     attribute = ['T']
     ATK = 6
     health = 5
     race = 'none'
     directional = False


class MagmaRager(MinionCard):
     name = 'Magma Rager'
     rarity = 'free'
     type = 'minion'
     cost = 3
     set = 'Basic'
     major = 'neutral'
     description = 'none'

     attribute = []
     ATK = 5
     health = 1
     race = 'elemental'
     directional = False


class MarkoftheWild(SpellCard):
     name = 'Mark of the Wild'
     rarity = 'free'
     type = 'spell'
     cost = 2
     set = 'Basic'
     major = 'druid'
     description = 'Give a minion Taunt and +2/+2.(+2\n Attack/+2 Health).'

     directional = True


class MindControl(SpellCard):
     name = 'Mind Control'
     rarity = 'free'
     type = 'spell'
     cost = 10
     set = 'Basic'
     major = 'priest'
     description = 'Take control of an enemy minion.'

     directional = True


class MindVision(SpellCard):
     name = 'Mind Vision'
     rarity = 'free'
     type = 'spell'
     cost = 1
     set = 'Basic'
     major = 'priest'
     description = 'Put a copy of a random card in your\n opponent\'s hand into your hand.'

     directional = False


class MirrorImage(SpellCard):
     name = 'Mirror Image'
     rarity = 'free'
     type = 'spell'
     cost = 1
     set = 'Basic'
     major = 'mage'
     description = 'Summon two 0/2 minions with Taunt.'

     directional = False


class Moonfire(SpellCard):
     name = 'Moonfire'
     rarity = 'free'
     type = 'spell'
     cost = 0
     set = 'Basic'
     major = 'druid'
     description = 'Deal 1 damage.'

     directional = True


class MortalCoil(SpellCard):
     name = 'Mortal Coil'
     rarity = 'free'
     type = 'spell'
     cost = 1
     set = 'Basic'
     major = 'warlock'
     description = 'Deal 1 damage to a minion. If that\n kills it, draw a card.'

     directional = True


class MultipleShot(SpellCard):
     name = 'Multiple Shot'
     rarity = 'free'
     type = 'spell'
     cost = 4
     set = 'Basic'
     major = 'hunter'
     description = 'Deal 3 damage to two random enemy\n minions.'

     directional = False


class MurlocRaider(MinionCard):
    name = 'Murloc Raider'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'neutral'
    description = 'none'

    attribute = []
    ATK = 2
    health = 1
    race = 'murloc'
    directional = False


class MurlocTidehunter(MinionCard):
    name = 'Murloc Tidehunter'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Summon a 1/1 Murloc Scout.'

    attribute = []
    ATK = 2
    health = 1
    race = 'murloc'
    directional = False


class Nightblade(MinionCard):
    name = 'Nightblade'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Deal 3 damage to the enemy\n hero.'

    attribute = []
    ATK = 4
    health = 4
    race = 'none'
    directional = True


class NoviceEngineer(MinionCard):
    name = 'Novice Engineer'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Draw a card.'

    attribute = []
    ATK = 1
    health = 1
    race = 'none'
    directional = False


class OasisSnapjaw(MinionCard):
    name = 'Oasis Snapjaw'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'none'

    attribute = []
    ATK = 2
    health = 7
    race = 'beast'
    directional = False


class OgreMagi(MinionCard):
    name = 'Ogre Magi'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'Spell Damage +1'

    attribute = []
    ATK = 4
    health = 4
    race = 'none'
    directional = False


class PowerWordShield(SpellCard):
     name = 'Power Word: Shield'
     rarity = 'free'
     type = 'spell'
     cost = 0
     set = 'Basic'
     major = 'priest'
     description = 'Give a minion +2 Health.'

     directional = True


class Plaguebringer(MinionCard):
    name = 'Plaguebringer'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'rogue'
    description = 'Battlecry: Give a friendly minion\n Poisonous.'

    attribute = []
    ATK = 3
    health = 3
    race = 'none'
    directional = True


class Polymorph(SpellCard):
     name = 'Polymorph'
     rarity = 'free'
     type = 'spell'
     cost = 4
     set = 'Basic'
     major = 'mage'
     description = 'Transform a minion into a 1/1 Sheep.'

     directional = True


class PowerInfusion(SpellCard):
     name = 'Power Infusion'
     rarity = 'free'
     type = 'spell'
     cost = 4
     set = 'Basic'
     major = 'priest'
     description = 'Give a minion +2/+6.'

     directional = True


class PsychicConjurer(MinionCard):
    name = 'Psychic Conjurer'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'priest'
    description = 'Battlecry: Copy a card in your\n opponent\'s deck and add it to your hand.'

    attribute = []
    ATK = 1
    health = 1
    race = 'none'
    directional = False


class Radiance(SpellCard):
    name = 'Radiance'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'priest'
    description = 'Restore 5 Health to your hero'

    directional = False


class RaidLeader(MinionCard):
    name = 'Raid Leader'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Your other minions have +1 Attack.'

    attribute = []
    ATK = 2
    health = 2
    race = 'none'
    directional = False


class RazorfenHunter(MinionCard):
    name = 'Razorfen Hunter'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Summon a 1/1 Boar.'

    attribute = []
    ATK = 2
    health = 3
    race = 'none'
    directional = False


class RecklessRocketeer(MinionCard):
    name = 'Reckless Rocketeer'
    rarity = 'free'
    type = 'minion'
    cost = 6
    set = 'Basic'
    major = 'neutral'
    description = 'Charge'

    attribute = []
    ATK = 5
    health = 2
    race = 'none'
    directional = False


class RiverCrocolisk(MinionCard):
    name = 'River Crocolisk'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'neutral'
    description = 'none'

    attribute = []
    ATK = 2
    health = 3
    race = 'beast'
    directional = False


class RockbiterWeapon(SpellCard):
    name = 'Rockbiter Weapon'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'shaman'
    description = 'Give a friendly character +3 Attack\n this turn.'

    directional = True


class SacrificialPact(SpellCard):
    name = 'Sacrificial Pact'
    rarity = 'free'
    type = 'spell'
    cost = 0
    set = 'Basic'
    major = 'warlock'
    description = 'Destroy a friendly Demon. Restore 5\n Health to your hero.'

    directional = True


class Sap(SpellCard):
    name = 'Sap'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'rogue'
    description = 'Return an enemy minion to your\n opponent\'s hand.'

    directional = True


class SatyrOverseer(MinionCard):
    name = 'Satyr Overseer'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'demonHunter'
    description = 'After your hero attacks, summon a\n 2/2 Satyr.'

    ATK = 4
    health = 2
    race = 'demon'
    directional = False


class SavageRoar(SpellCard):
    name = 'Savage Roar'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'druid'
    description = 'Give your characters +2 Attack this\n turn.'

    directional = False


class Sen_jinShieldmasta(MinionCard):
    name = 'Sen\'jinShieldmasta'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'Taunt'

    ATK = 3
    health = 5
    race = 'none'
    directional = False


class ShadowBolt(SpellCard):
    name = 'Shadow Bolt'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'warlock'
    description = 'Deal 4 damage to a minion.'

    directional = True


class ShadowWordDeath(SpellCard):
    name = 'Shadow Word: Death'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'priest'
    description = 'Destroy a minion with 5 or more\n Attack.'

    directional = True

class ShadowWordPain(SpellCard):
    name = 'Shadow Word: Pain'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'priest'
    description = 'Destroy a minion with 3 or less\n Attack.'

    directional = True


class ShaowhoofSlayer(MinionCard):
    name = 'Shaowhoof Slayer'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'demonHunter'
    description = 'Battlecry: Give your hero +1 Attack\n this turn.'

    attribute = []
    ATK = 2
    health = 1
    race = 'demon'
    directional = False


class ShatteredSunCleric(MinionCard):
    name = 'Shattered Sun Cleric'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Give a friendly minion\n +1/+1.'

    attribute = []
    ATK = 3
    health = 2
    race = 'none'
    directional = True


class ShieldBlock(SpellCard):
    name = 'Shield Block'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'warrior'
    description = 'Gain 5 Armor. Draw a card.'

    directional = False


class Shiv(SpellCard):
    name = 'Shiv'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'rogue'
    description = 'Deal 1 damage. Draw a card.'

    directional = True


class SightlessWatcher(MinionCard):
    name = 'Sightless Watcher'
    rarity = 'free'
    type = 'minion'
    cost = 2
    set = 'Basic'
    major = 'demonHunter'
    description = 'Battlecry: Look at 4 cards in your\n deck. Choose one to put on top.'

    attribute = []
    ATK = 3
    health = 2
    race = 'demon'
    directional = False


class SilverbackPatriarch(MinionCard):
    name = 'Silverback Patriarch'
    rarity = 'free'
    type = 'minion'
    cost = 3
    set = 'Basic'
    major = 'neutral'
    description = 'Taunt'

    attribute = ['T']
    ATK = 1
    health = 4
    race = 'beast'
    directional = False


class SinisterStrike(SpellCard):
    name = 'Sinister Strike'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'rogue'
    description = 'Deal 3 damage to the enemy hero.'

    directional = False


class SoulCleave(SpellCard):
    name = 'Soul Cleave'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'demonHunter'
    description = 'Lifesteal Deal 2 damage to two random\n enemy minions.'

    directional = False


class Soulfire(SpellCard):
    name = 'Soulfire'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'warlock'
    description = 'Deal 4 damage. Discard a random card.'

    directional = True


class Sprint(SpellCard):
    name = 'Sprint'
    rarity = 'free'
    type = 'spell'
    cost = 7
    set = 'Basic'
    major = 'rogue'
    description = 'Draw 4 cards.'

    directional = False


class Starfire(SpellCard):
    name = 'Starfire'
    rarity = 'free'
    type = 'spell'
    cost = 6
    set = 'Basic'
    major = 'druid'
    description = 'Deal 5 damage. Draw a card.'

    directional = True


class StarvingBuzzard(MinionCard):
    name = 'Starving Buzzard'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'hunter'
    description = 'Whenever you summon a Beast, draw a\n card.'

    attribute = []
    ATK = 3
    health = 2
    race = 'beast'
    directional = False


class StonetuskBoar(MinionCard):
    name = 'Stonetusk Boar'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'neutral'
    description = 'Charge'

    attribute = []
    ATK = 1
    health = 1
    race = 'beast'
    directional = False


class StormpikeCommando(MinionCard):
    name = 'Stormpike Commando'
    rarity = 'free'
    type = 'minion'
    cost = 5
    set = 'Basic'
    major = 'neutral'
    description = 'Battlecry: Deal 2 damage.'

    attribute = []
    ATK = 4
    health = 2
    race = 'none'
    directional = True


class StormwindChampion(MinionCard):
    name = 'Stormwind Champion'
    rarity = 'free'
    type = 'minion'
    cost = 7
    set = 'Basic'
    major = 'neutral'
    description = 'Your other minions have +1/+1.'

    attribute = []
    ATK = 6
    health = 6
    race = 'none'
    directional = False

class StormwindKnight(MinionCard):
    name = 'Stormwind Knight'
    rarity = 'free'
    type = 'minion'
    cost = 4
    set = 'Basic'
    major = 'neutral'
    description = 'Charge'

    attribute = []
    ATK = 2
    health = 5
    race = 'none'
    directional = False


class Swipe(SpellCard):
    name = 'Swipe'
    rarity = 'free'
    type = 'spell'
    cost = 4
    set = 'Basic'
    major = 'druid'
    description = 'Deal 4 damage to an enemy and 1 damage\n to all other enemies.'

    directional = True


class TimberWolf(MinionCard):
    name = 'Timber Wolf'
    rarity = 'free'
    type = 'minion'
    cost = 1
    set = 'Basic'
    major = 'hunter'
    description = 'Your other Beasts have +1 Attack.'

    attribute = []
    ATK = 1
    health = 1
    race = 'beast'
    directional = False


class TotemicMight(SpellCard):
    name = 'Totemic Might'
    rarity = 'free'
    type = 'spell'
    cost = 0
    set = 'Basic'
    major = 'shaman'
    description = 'Give your Totems +2 Health.'

    directional = False


class Tracking(SpellCard):
    name = 'Tracking'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'hunter'
    description = 'Look at the top three cards of your\n deck. Draw one and discard the others.'

    directional = False


class TruesilverChampion(WeaponCard):
 name = 'Truesilver Champion'
 rarity = 'free'
 type = 'weapon'
 cost = 4
 set = 'Basic'
 major = 'paladin'
 description = 'Whenever your hero attacks, restore 2\n Health to it.'

 durability = 2
 ATK = 4
 attribute = []


class TundraRhino(MinionCard):
     name = 'Tundra Rhino'
     rarity = 'free'
     type = 'minion'
     cost = 5
     set = 'Basic'
     major = 'hunter'
     description = 'Your Beasts have Charge.'

     attribute = []
     ATK = 2
     health = 5
     race = 'beast'
     directional = False


class Voidwalker(MinionCard):
     name = 'Voidwalker'
     rarity = 'free'
     type = 'minion'
     cost = 1
     set = 'Basic'
     major = 'warlock'
     description = 'Taunt'

     attribute = ['T']
     ATK = 1
     health = 3
     race = 'demon'
     directional = False


class VoodooDoctor(MinionCard):
     name = 'Voodoo Doctor'
     rarity = 'free'
     type = 'minion'
     cost = 1
     set = 'Basic'
     major = 'neutral'
     description = 'Battlecry: Restore 2 Health.'

     attribute = []
     ATK = 2
     health = 1
     race = 'none'
     directional = True


class WarGolem(MinionCard):
     name = 'War Golem'
     rarity = 'free'
     type = 'minion'
     cost = 7
     set = 'Basic'
     major = 'neutral'
     description = 'none'

     attribute = []
     ATK = 7
     health = 7
     race = 'none'
     directional = False


class WarsongCommander(MinionCard):
     name = 'Warsong Commander'
     rarity = 'free'
     type = 'minion'
     cost = 3
     set = 'Basic'
     major = 'warrior'
     description = 'Your Charge minions have +1 Attack.'

     attribute = []
     ATK = 2
     health = 3
     race = 'none'
     directional = False


class WaterElemental(MinionCard):
     name = 'Water Elemental'
     rarity = 'free'
     type = 'minion'
     cost = 4
     set = 'Basic'
     major = 'mage'
     description = 'Freeze any character damaged by this\n minion.'

     attribute = []
     ATK = 3
     health = 6
     race = 'elemental'
     directional = False


class Whirlwind(SpellCard):
    name = 'Whirlwind'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'warrior'
    description = 'Deal 1 damage to ALL minions.'

    directional = False


class WildGrowth(SpellCard):
    name = 'Wild Growth'
    rarity = 'free'
    type = 'spell'
    cost = 3
    set = 'Basic'
    major = 'druid'
    description = 'Gain an empty Mana Crystal.'

    directional = False


class Windfury(SpellCard):
    name = 'Windfury'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'shaman'
    description = 'Give a minion Windfury.'

    directional = True


class Windspeaker(MinionCard):
     name = 'Windspeaker'
     rarity = 'free'
     type = 'minion'
     cost = 4
     set = 'Basic'
     major = 'shaman'
     description = 'Battlecry: Give a friendly minion\n Windfury.'

     attribute = []
     ATK = 3
     health = 3
     race = 'none'
     directional = True


class Wolfrider(MinionCard):
     name = 'Wolfrider'
     rarity = 'free'
     type = 'minion'
     cost = 3
     set = 'Basic'
     major = 'neutral'
     description = 'Charge'

     attribute = []
     ATK = 3
     health = 1
     race = 'none'
     directional = False


class TheCoin(SpellCard):
    name = 'The Coin'
    rarity = 'free'
    type = 'spell'
    cost = 0
    set = 'Basic'
    major = 'neutral'
    description = 'Gain 1 Mana Crystal this turn only.'

    directional = False


class DemonClaws(SpellCard):
    name = 'Demon Claws'
    rarity = 'free'
    type = 'spell'
    cost = 1
    set = 'Basic'
    major = 'demonHunter'
    description = 'Hero Power +1 Attack this turn.'

    directional = False


class Shapeshift(SpellCard):
    name = 'Shapeshift'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'druid'
    description = 'Hero Power +1 Attack this turn. +1 Armor.'

    directional = False


class SteadyShot(SpellCard):
    name = 'Steady Shot'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'hunter'
    description = 'Hero Power Deal 2 damage to the enemy hero.'

    directional = False


class Fireblast(SpellCard):
    name = 'Fireblast'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'mage'
    description = 'Hero Power Deal 1 damage.'

    directional = True


class Reinforce(SpellCard):
    name = 'Reinforce'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'paladin'
    description = 'Hero Power Summon a 1/1 Silver Hand Recruit.'

    directional = False


class LesserHeal(SpellCard):
    name = 'Lesser Heal'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'priest'
    description = 'Hero Power Restore 2 Health.'

    directional = True


class DaggerMastery(SpellCard):
    name = 'Dagger Mastery'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'rogue'
    description = 'Hero Power Equip a 1/2 Dagger.'

    directional = False


class TotemicCall(SpellCard):
    name = 'Totemic Call'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'shaman'
    description = 'Hero Power Summon a random Totem.'

    directional = False


class LifeTap(SpellCard):
    name = 'Life Tap'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'warlock'
    description = 'Hero Power Draw a card and take 2 damage.'

    directional = False


class ArmorUp(SpellCard):
    name = 'Armor Up'
    rarity = 'free'
    type = 'spell'
    cost = 2
    set = 'Basic'
    major = 'warrior'
    description = 'Hero Power Gain 2 Armor.'

    directional = False


# x = Backstab()
# print(x.description)





