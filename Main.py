import tkinter as tk
import sys
import random
from Card import *

neutralCards = ['Voodoo Doctor', 'Stormwind Knight', 'Murloc Raider', 'Ironforge Rifleman', 'Bloodfen Raptor',
                'Grimscale Oracle', 'Gnomish Inventor', 'Frostwolf Grunt', 'Elven Archer', 'Dragonling Mechanic',
                'Darkscale Healer', 'Dalaran Mage', 'Core Hound',
                'War Golem', 'Wolfrider', 'Murloc Tidehunter', 'Ironfur Grizzly', 'Acidic Swamp Ooze',
                'Goldshire Footman', 'Frostwolf Warlord', 'Chillwind Yeti', 'Archmage', 'Bluegill Warrior',
                'Booty Bay Bodyguard', 'Boulderfist Ogre', 'Gurubashi Berserker',
                'Stormwind Champion', 'Stormpike Commando', 'Stonetusk Boar', 'Silverback Patriarch',
                'Shattered Sun Cleric', 'Sen\'jinShieldmasta', 'River Crocolisk', 'Reckless Rocketeer',
                'Razorfen Hunter', 'Raid Leader', 'Ogre Magi', 'Oasis Snapjaw', 'Novice Engineer', 'Nightblade',
                'Magma Rager', 'Lord of the Arena', 'Kobold Geomancer']
mageCards = ['Water Elemental', 'Polymorph', 'Mirror Image', 'Arcane Intellect', 'Frostbolt', 'Frost Nova',
             'Flamestrike', 'Arcane Explosion', 'Arcane Missiles', 'Fireball']
warriorCards = ['Whirlwind', 'Warsong Commander', 'Shield Block', 'Kor\'kron Elite', 'Flery War Axe', 'Arcanite Reaper',
                'Charge', 'Cleave', 'Execute', 'Heroic Strike']
demonHunterCards = ['Soul Cleave', 'Sightless Watcher', 'Shaowhoof Slayer', 'Satyr Overseer', 'Inner Demon',
                    'Aldrachi Warblades', 'Glaivebound Adept', 'Coordinated Strike', 'Chaos Nova', 'Chaos Strike']
druidCards = ['Wild Growth', 'Swipe', 'Starfire', 'Savage Roar', 'Moonfire', 'Mark of the Wild', 'Ironbark Protector',
              'Innervate', 'Claw', 'Healing Touch']
rogueCards = ['Sprint', 'Sinister Strike', 'Shiv', 'Sap', 'Plaguebringer', 'Assassinate', 'Assassin\'s Blade',
              'Fan of Knives', 'Backstab', 'Deadly Poison']
paladinCards = ['Truesilver Champion', 'Light\'s Justice', 'Humility', 'Holy Light', 'Blessing of Kings',
                'Hand of Protection', 'Blessing of Might', 'Consecration', 'Guardian of Kings', 'Hammer of Wrath']
hunterCards = ['Animal Companion', 'Tundra Rhino', 'Tracking', 'Timber Wolf', 'Starving Buzzard', 'Multiple Shot',
               'Kill Command', 'Hunter\'s Mark', 'Arcane Shot', 'Houndmaster']
shamanCards = ['Windfury', 'Ancestral Healing', 'Windspeaker', 'Totemic Might', 'Rockbiter Weapon', 'Bloodlust',
               'Fire Elemental', 'Flametongue Totem', 'Frost Shock', 'Hex']
priestCards = ['Shadow Word: Pain', 'Shadow Word: Death', 'Radiance', 'Psychic Conjurer', 'Power Word: Shield',
               'Power Infusion', 'Mind Vision', 'Mind Control', 'Holy Smite', 'Holy Nova']
warlockCards = ['Voidwalker', 'Soulfire', 'Shadow Bolt', 'Sacrificial Pact', 'Mortal Coil', 'Corruption', 'Drain Life',
                'Dread Infernal', 'Felstalker', 'Hellfire']


def loadDeckFile(deck, deckFile):
    saveDeck = open(str(deckFile), 'r')
    deck = saveDeck.readlines()
    saveDeck.close()


def translate(oldName):
    newName = oldName.replace(" ", "")
    newNewName = newName.replace(":", "")
    newNew1Name = newNewName.replace("'", "_")
    return newNew1Name


def removeSpace(deck):
    for x in range(0, len(deck)):
        deck[x] = deck[x][:-2]


def removeSpace1(deck):
    deck = deck[:-2]
    return deck


def stringToClass(target):
    return getattr(sys.modules[__name__], target)


def alignDeck(deck):
    for x in range(0, len(deck)):
        for y in range(x + 1, len(deck)):
            if (deck[x] > deck[y]):
                temp = deck[x]
                deck[x] = deck[y]
                deck[y] = temp


def countingDeck(deck):
    for x in range(0, len(deck)):
        if (deck[x] == 'none'):
            return x
    return 30


alignDeck(neutralCards)
alignDeck(mageCards)
alignDeck(warriorCards)
alignDeck(demonHunterCards)
alignDeck(druidCards)
alignDeck(rogueCards)
alignDeck(paladinCards)
alignDeck(hunterCards)
alignDeck(shamanCards)
alignDeck(priestCards)
alignDeck(warlockCards)


class Menu:

    def __init__(self, master):
        self.master = master
        master.title('Hearthstone')
        master.geometry('900x600+120+120')
        self.play = tk.Button(master, text='Play Now!', width=20, height=2, command=self.mainToChooseDeck).place(x=380, y=350)
        self.edit = tk.Button(master, text='Edit Deck', width=20, height=2, command=self.mainToEdit).place(x=380, y=400)
        self.quit = tk.Button(master, text='Quit', width=20, height=2, command=self.quitGame).place(x=380, y=450)
        self.title = tk.Label(master, text='Hearthstone', font='Helvetica 29 bold').place(x=340, y=50)
        self.title = tk.Label(master, text='Current version: basic', font='Helvetica 13 bold').place(x=365, y=110)

    def quitGame(self):
        sys.exit()

    def mainToEdit(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Edit(self.master)
        self.master.mainloop()

    def mainToChooseDeck(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = ChooseDeck(self.master)
        self.master.mainloop()


class ChooseDeck:

    def __init__(self, master):
        saveDeck = open('deck0.txt', 'r')
        deck0 = saveDeck.readlines()
        saveDeck.close()

        saveDeck = open('deck1.txt', 'r')
        deck1 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck1[0])
        state1 = 'tk.NORMAL'
        if (temp != 'used'):
           state1 = 'tk.DISABLED'

        saveDeck = open('deck2.txt', 'r')
        deck2 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck2[0])
        state2 = 'tk.NORMAL'
        if (temp != 'used'):
            state2 = 'tk.DISABLED'

        saveDeck = open('deck3.txt', 'r')
        deck3 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck3[0])
        state3 = 'tk.NORMAL'
        if (temp != 'used'):
            state3 = 'tk.DISABLED'

        saveDeck = open('deck4.txt', 'r')
        deck4 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck4[0])
        state4 = 'tk.NORMAL'
        if (temp != 'used'):
            state4 = 'tk.DISABLED'

        saveDeck = open('deck5.txt', 'r')
        deck5 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck5[0])
        state5 = 'tk.NORMAL'
        if (temp != 'used'):
            state5 = 'tk.DISABLED'

        saveDeck = open('deck6.txt', 'r')
        deck6 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck6[0])
        state6 = 'tk.NORMAL'
        if (temp != 'used'):
            state6 = 'tk.DISABLED'

        saveDeck = open('deck7.txt', 'r')
        deck7 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck7[0])
        state7 = 'tk.NORMAL'
        if (temp != 'used'):
            state7 = 'tk.DISABLED'

        saveDeck = open('deck8.txt', 'r')
        deck8 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck8[0])
        state8 = 'tk.NORMAL'
        if (temp != 'used'):
            state8 = 'tk.DISABLED'

        saveDeck = open('deck9.txt', 'r')
        deck9 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck9[0])
        state9 = 'tk.NORMAL'
        if (temp != 'used'):
            state9 = 'tk.DISABLED'

        self.master = master
        master.title('Choose Deck')
        master.geometry('900x600+120+120')

        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=60, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        self.title = tk.Label(master, text='Choose your deck', font='Helvetica 18 bold').place(x=350, y=50)

        self.deck11 = tk.Button(master, text=deck1[2] + '\n' + deck1[3] + '\n' + deck1[1], width=20, height=6, state=eval(state1), command=lambda: self.useDeck1(warningMessage)).place(x=225, y=150)
        self.deck22 = tk.Button(master, text=deck2[2] + '\n' + deck2[3] + '\n' + deck2[1], width=20, height=6, state=eval(state2), command=lambda: self.useDeck2(warningMessage)).place(
            x=380, y=150)
        self.deck33 = tk.Button(master, text=deck3[2] + '\n' + deck3[3] + '\n' + deck3[1], width=20, height=6, state=eval(state3), command=lambda: self.useDeck3(warningMessage)).place(
            x=535, y=150)
        self.deck44 = tk.Button(master, text=deck4[2] + '\n' + deck4[3] + '\n' + deck4[1], width=20, height=6, state=eval(state4), command=lambda: self.useDeck4(warningMessage)).place(
            x=225, y=255)
        self.deck55 = tk.Button(master, text=deck5[2] + '\n' + deck5[3] + '\n' + deck5[1], width=20, height=6, state=eval(state5), command=lambda: self.useDeck5(warningMessage)).place(
            x=380, y=255)
        self.deck66 = tk.Button(master, text=deck6[2] + '\n' + deck6[3] + '\n' + deck6[1], width=20, height=6, state=eval(state6), command=lambda: self.useDeck6(warningMessage)).place(
            x=535, y=255)
        self.deck77 = tk.Button(master, text=deck7[2] + '\n' + deck7[3] + '\n' + deck7[1], width=20, height=6, state=eval(state7), command=lambda: self.useDeck7(warningMessage)).place(
            x=225, y=360)
        self.deck88 = tk.Button(master, text=deck8[2] + '\n' + deck8[3] + '\n' + deck8[1], width=20, height=6, state=eval(state8), command=lambda: self.useDeck8(warningMessage)).place(
            x=380, y=360)
        self.deck99 = tk.Button(master, text=deck9[2] + '\n' + deck9[3] + '\n' + deck9[1], width=20, height=6, state=eval(state9), command=lambda: self.useDeck9(warningMessage)).place(
            x=535, y=360)
        self.backForEditDeck = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain).place(x=405, y=500)

    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()

    def useDeck1(self, warningMessage):
        saveDeck = open('deck1.txt', 'r')
        deck1 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck1)

        if (deck1[0] == 'used'):
            if (deck1[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck1)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)

    def useDeck2(self, warningMessage):
        saveDeck = open('deck2.txt', 'r')
        deck2 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck2)

        if (deck2[0] == 'used'):
            if (deck2[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck2)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck3(self, warningMessage):
        saveDeck = open('deck3.txt', 'r')
        deck3 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck3)

        if (deck3[0] == 'used'):
            if (deck3[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck3)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck4(self, warningMessage):
        saveDeck = open('deck4.txt', 'r')
        deck4 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck4)

        if (deck4[0] == 'used'):
            if (deck4[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck4)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck5(self, warningMessage):
        saveDeck = open('deck5.txt', 'r')
        deck5 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck5)

        if (deck5[0] == 'used'):
            if (deck5[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck5)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck6(self, warningMessage):
        saveDeck = open('deck6.txt', 'r')
        deck6 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck6)

        if (deck6[0] == 'used'):
            if (deck6[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck6)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck7(self, warningMessage):
        saveDeck = open('deck7.txt', 'r')
        deck7 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck7)

        if (deck7[0] == 'used'):
            if (deck7[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck7)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck8(self, warningMessage):
        saveDeck = open('deck8.txt', 'r')
        deck8 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck8)

        if (deck8[0] == 'used'):
            if (deck8[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck8)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


    def useDeck9(self, warningMessage):
        saveDeck = open('deck9.txt', 'r')
        deck9 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck9)

        if (deck9[0] == 'used'):
            if (deck9[1] == 'completed'):
                self.master.destroy()
                self.master = tk.Tk()
                self.app = ChooseRival(self.master, deck9)
                self.master.mainloop()
            else:
                message = "The deck is still incomplete"
                warningMessage.set(message)
        else:
            message = "The item is empty"
            warningMessage.set(message)


class ChooseRival:

    def __init__(self, master, deck):
        self.master = master
        master.title('Choose Rival')
        master.geometry('900x600+120+120')
        self.title = tk.Label(master, text='Choose your rival', font='Helvetica 18 bold').place(x=350, y=50)
        self.druidButton = tk.Button(master, text='Druid', width=20, height=2,
                                     command=lambda: self.VSDruid(deck)).place(x=70, y=325)
        self.demonHunterButton = tk.Button(master, text='Demon Hunter', width=20, height=2,
                                           command=lambda: self.VSDemonHunter(deck)).place(x=225, y=325)
        self.hunterButton = tk.Button(master, text='Hunter', width=20, height=2,
                                      command=lambda: self.VSHunter(deck)).place(x=380, y=325)
        self.mageButton = tk.Button(master, text='Mage', width=20, height=2,
                                    command=lambda: self.VSMage(deck)).place(x=535, y=325)
        self.paladinButton = tk.Button(master, text='Paladin', width=20, height=2,
                                       command=lambda: self.VSPaladin(deck)).place(x=690, y=325)
        self.priestButton = tk.Button(master, text='Priest', width=20, height=2,
                                      command=lambda: self.VSPriest(deck)).place(x=70, y=375)
        self.rogueButton = tk.Button(master, text='Rogue', width=20, height=2,
                                    command=lambda: self.VSRogue(deck)).place(x=225, y=375)
        self.shamanButton = tk.Button(master, text='Shaman', width=20, height=2,
                                      command=lambda: self.VSShaman(deck)).place(x=380, y=375)
        self.warlockButton = tk.Button(master, text='Warlock', width=20, height=2,
                                      command=lambda: self.VSWarlock(deck)).place(x=535, y=375)
        self.warriorButton = tk.Button(master, text='Warrior', width=20, height=2,
                                       command=lambda: self.VSWarrior(deck)).place(x=690, y=375)
        self.backForEditDeck = tk.Button(master, text='Back to menu', width=12, height=1,
                                         command=self.editToMain).place(x=405, y=500)

    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()

    def VSDruid(self, deck):
        saveDeck = open('Druid.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSHunter(self, deck):
        saveDeck = open('Hunter.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSMage(self, deck):
        saveDeck = open('Mage.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSPaladin(self, deck):
        saveDeck = open('Paladin.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSPriest(self, deck):
        saveDeck = open('Priest.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSDemonHunter(self, deck):
        saveDeck = open('DemonHunter.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSRogue(self, deck):
        saveDeck = open('Rogue.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSShaman(self, deck):
        saveDeck = open('Shaman.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSWarlock(self, deck):
        saveDeck = open('Warlock.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSWarrior(self, deck):
        saveDeck = open('Warrior.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Replace(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()


class Edit:

    def __init__(self, master):

        saveDeck = open('deck0.txt', 'r')
        deck0 = saveDeck.readlines()
        saveDeck.close()

        saveDeck = open('deck1.txt', 'r')
        deck1 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck1[0])
        state1 = 'tk.NORMAL'
        if (temp != 'used'):
            state1 = 'tk.DISABLED'

        saveDeck = open('deck2.txt', 'r')
        deck2 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck2[0])
        state2 = 'tk.NORMAL'
        if (temp != 'used'):
            state2 = 'tk.DISABLED'

        saveDeck = open('deck3.txt', 'r')
        deck3 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck3[0])
        state3 = 'tk.NORMAL'
        if (temp != 'used'):
            state3 = 'tk.DISABLED'

        saveDeck = open('deck4.txt', 'r')
        deck4 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck4[0])
        state4 = 'tk.NORMAL'
        if (temp != 'used'):
            state4 = 'tk.DISABLED'

        saveDeck = open('deck5.txt', 'r')
        deck5 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck5[0])
        state5 = 'tk.NORMAL'
        if (temp != 'used'):
            state5 = 'tk.DISABLED'

        saveDeck = open('deck6.txt', 'r')
        deck6 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck6[0])
        state6 = 'tk.NORMAL'
        if (temp != 'used'):
            state6 = 'tk.DISABLED'

        saveDeck = open('deck7.txt', 'r')
        deck7 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck7[0])
        state7 = 'tk.NORMAL'
        if (temp != 'used'):
            state7 = 'tk.DISABLED'

        saveDeck = open('deck8.txt', 'r')
        deck8 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck8[0])
        state8 = 'tk.NORMAL'
        if (temp != 'used'):
            state8 = 'tk.DISABLED'

        saveDeck = open('deck9.txt', 'r')
        deck9 = saveDeck.readlines()
        saveDeck.close()

        temp = removeSpace1(deck9[0])
        state9 = 'tk.NORMAL'
        if (temp != 'used'):
            state9 = 'tk.DISABLED'

        self.master = master
        master.title('Edit Deck')
        master.geometry('900x600+120+120')
        self.title = tk.Label(master, text='Deck Editor', font='Helvetica 18 bold').place(x=380, y=50)
        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=60, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        self.deck11 = tk.Button(master, text=deck1[2] + '\n' + deck1[3] + '\n' + deck1[1], width=20, height=6, state=eval(state1),
                                command=lambda: self.openDeck1(warningMessage)).place(x=225, y=150)
        self.deck22 = tk.Button(master, text=deck2[2] + '\n' + deck2[3] + '\n' + deck2[1], width=20, height=6, state=eval(state2), command=lambda: self.openDeck2(warningMessage)).place(
            x=380, y=150)
        self.deck33 = tk.Button(master, text=deck3[2] + '\n' + deck3[3] + '\n' + deck3[1], width=20, height=6, state=eval(state3), command=lambda: self.openDeck3(warningMessage)).place(
            x=535, y=150)
        self.deck44 = tk.Button(master, text=deck4[2] + '\n' + deck4[3] + '\n' + deck4[1], width=20, height=6, state=eval(state4), command=lambda: self.openDeck4(warningMessage)).place(
            x=225, y=255)
        self.deck55 = tk.Button(master, text=deck5[2] + '\n' + deck5[3] + '\n' + deck5[1], width=20, height=6, state=eval(state5), command=lambda: self.openDeck5(warningMessage)).place(
            x=380, y=255)
        self.deck66 = tk.Button(master, text=deck6[2] + '\n' + deck6[3] + '\n' + deck6[1], width=20, height=6, state=eval(state6), command=lambda: self.openDeck6(warningMessage)).place(
            x=535, y=255)
        self.deck77 = tk.Button(master, text=deck7[2] + '\n' + deck7[3] + '\n' + deck7[1], width=20, height=6, state=eval(state7), command=lambda: self.openDeck7(warningMessage)).place(
            x=225, y=360)
        self.deck88 = tk.Button(master, text=deck8[2] + '\n' + deck8[3] + '\n' + deck8[1], width=20, height=6, state=eval(state8), command=lambda: self.openDeck8(warningMessage)).place(
            x=380, y=360)
        self.deck99 = tk.Button(master, text=deck9[2] + '\n' + deck9[3] + '\n' + deck9[1], width=20, height=6, state=eval(state9), command=lambda: self.openDeck9(warningMessage)).place(
            x=535, y=360)
        self.newDeck = tk.Button(master, text='New deck', width=12, height=1, command=lambda: self.editToMajor(warningMessage)).place(x=325, y=500)
        self.backForEditDeck = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain).place(x=485, y=500)

    def openDeck1(self, warningMessage):
        saveDeck = open('deck1.txt', 'r')
        deck1 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck1)

        if (deck1[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck1[3], deck1, 1)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck2(self, warningMessage):
        saveDeck = open('deck2.txt', 'r')
        deck2 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck2)

        if (deck2[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck2[3], deck2, 2)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck3(self, warningMessage):
        saveDeck = open('deck3.txt', 'r')
        deck3 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck3)

        if (deck3[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck3[3], deck3, 3)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck4(self, warningMessage):
        saveDeck = open('deck4.txt', 'r')
        deck4 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck4)

        if (deck4[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck4[3], deck4, 4)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck5(self, warningMessage):
        saveDeck = open('deck5.txt', 'r')
        deck5 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck5)

        if (deck5[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck5[3], deck5, 5)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck6(self, warningMessage):
        saveDeck = open('deck6.txt', 'r')
        deck6 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck6)

        if (deck6[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck6[3], deck6, 6)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck7(self, warningMessage):
        saveDeck = open('deck7.txt', 'r')
        deck7 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck7)

        if (deck7[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck7[3], deck7, 7)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck8(self, warningMessage):
        saveDeck = open('deck8.txt', 'r')
        deck8 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck8)

        if (deck8[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck8[3], deck8, 8)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def openDeck9(self, warningMessage):
        saveDeck = open('deck9.txt', 'r')
        deck9 = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck9)

        if (deck9[0] == 'used'):
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Editor(self.master, deck9[3], deck9, 9)
            self.master.mainloop()
        else:
            message = "Empty item, if you want to create new deck, click \'New deck\'"
            warningMessage.set(message)

    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()

    def editToMajor(self, warningMessage):
        saveDeck = open('deck0.txt', 'r')
        deck0 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck1.txt', 'r')
        deck1 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck2.txt', 'r')
        deck2 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck3.txt', 'r')
        deck3 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck4.txt', 'r')
        deck4 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck5.txt', 'r')
        deck5 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck6.txt', 'r')
        deck6 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck7.txt', 'r')
        deck7 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck8.txt', 'r')
        deck8 = saveDeck.readlines()
        saveDeck.close()
        saveDeck = open('deck9.txt', 'r')
        deck9 = saveDeck.readlines()
        saveDeck.close()

        if (deck1[0] == deck0[0]):
            self.master.destroy()
            self.master = tk.Tk()
            removeSpace(deck1)
            self.app = Major(self.master, deck1, 1)
            self.master.mainloop()
        else:
            if (deck2[0] == deck0[0]):
                self.master.destroy()
                self.master = tk.Tk()
                removeSpace(deck2)
                self.app = Major(self.master, deck2, 2)
                self.master.mainloop()
            else:
                if (deck3[0] == deck0[0]):
                    self.master.destroy()
                    self.master = tk.Tk()
                    removeSpace(deck3)
                    self.app = Major(self.master, deck3, 3)
                    self.master.mainloop()
                else:
                    if (deck4[0] == deck0[0]):
                        self.master.destroy()
                        self.master = tk.Tk()
                        removeSpace(deck4)
                        self.app = Major(self.master, deck4, 4)
                        self.master.mainloop()
                    else:
                        if (deck5[0] == deck0[0]):
                            self.master.destroy()
                            self.master = tk.Tk()
                            removeSpace(deck5)
                            self.app = Major(self.master, deck5, 5)
                            self.master.mainloop()
                        else:
                            if (deck6[0] == deck0[0]):
                                self.master.destroy()
                                self.master = tk.Tk()
                                removeSpace(deck6)
                                self.app = Major(self.master, deck6, 6)
                                self.master.mainloop()
                            else:
                                if (deck7[0] == deck0[0]):
                                    self.master.destroy()
                                    self.master = tk.Tk()
                                    removeSpace(deck7)
                                    self.app = Major(self.master, deck7, 7)
                                    self.master.mainloop()
                                else:
                                    if (deck8[0] == deck0[0]):
                                        self.master.destroy()
                                        self.master = tk.Tk()
                                        removeSpace(deck8)
                                        self.app = Major(self.master, deck8, 8)
                                        self.master.mainloop()
                                    else:
                                        if (deck9[0] == deck0[0]):
                                            self.master.destroy()
                                            self.master = tk.Tk()
                                            removeSpace(deck9)
                                            self.app = Major(self.master, deck9, 9)
                                            self.master.mainloop()
                                        else:
                                            message = "You cannot create more deck"
                                            warningMessage.set(message)


class Major:

    def __init__(self, master, deck, deckOrder):
        self.master = master
        master.title('Choose Major')
        master.geometry('900x600+120+120')
        self.title = tk.Label(master, text='Choose Major', font='Helvetica 18 bold').place(x=370, y=50)
        self.druidButton = tk.Button(master, text='Druid', width=20, height=2,
                                     command=lambda: self.newDruid(deck, deckOrder)).place(x=70, y=325)
        self.demonHunterButton = tk.Button(master, text='Demon Hunter', width=20, height=2,
                                           command=lambda: self.newDemonHunter(deck, deckOrder)).place(x=225, y=325)
        self.hunterButton = tk.Button(master, text='Hunter', width=20, height=2,
                                      command=lambda: self.newHunter(deck, deckOrder)).place(x=380, y=325)
        self.mageButton = tk.Button(master, text='Mage', width=20, height=2,
                                    command=lambda: self.newMage(deck, deckOrder)).place(x=535, y=325)
        self.paladinButton = tk.Button(master, text='Paladin', width=20, height=2,
                                       command=lambda: self.newPaladin(deck, deckOrder)).place(x=690, y=325)
        self.priestButton = tk.Button(master, text='Priest', width=20, height=2,
                                      command=lambda: self.newPriest(deck, deckOrder)).place(x=70, y=375)
        self.rogueButton = tk.Button(master, text='Rogue', width=20, height=2,
                                     command=lambda: self.newRogue(deck, deckOrder)).place(x=225, y=375)
        self.shamanButton = tk.Button(master, text='Shaman', width=20, height=2,
                                      command=lambda: self.newShaman(deck, deckOrder)).place(x=380, y=375)
        self.warlockButton = tk.Button(master, text='Warlock', width=20, height=2,
                                       command=lambda: self.newWarlock(deck, deckOrder)).place(x=535, y=375)
        self.warriorButton = tk.Button(master, text='Warrior', width=20, height=2,
                                       command=lambda: self.newWarrior(deck, deckOrder)).place(x=690, y=375)
        self.backForChooseMajor = tk.Button(master, text='Back', width=12, height=1, command=self.majorToEdit).place(
            x=405, y=500)

    def majorToEdit(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Edit(self.master)
        self.master.mainloop()

    def newDruid(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'druid', deck, deckOrder)
        self.master.mainloop()

    def newDemonHunter(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'demonHunter', deck, deckOrder)
        self.master.mainloop()

    def newHunter(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'hunter', deck, deckOrder)
        self.master.mainloop()

    def newMage(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'mage', deck, deckOrder)
        self.master.mainloop()

    def newPaladin(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'paladin', deck, deckOrder)
        self.master.mainloop()

    def newPriest(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'priest', deck, deckOrder)
        self.master.mainloop()

    def newShaman(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'shaman', deck, deckOrder)
        self.master.mainloop()

    def newRogue(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'rogue', deck, deckOrder)
        self.master.mainloop()

    def newWarlock(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'warlock', deck, deckOrder)
        self.master.mainloop()

    def newWarrior(self, deck, deckOrder):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Editor(self.master, 'warrior', deck, deckOrder)
        self.master.mainloop()


class Editor:

    def __init__(self, master, major, deck, deckOrder):

        # 卡牌描述
        def printDetail():
            try:
                cardName = self.cardLibrary.get(self.cardLibrary.curselection())
            except:
                message = "Your must choose an item"
                warningMessage.set(message)
            else:
                newCardName = translate(cardName)
                targetClass = stringToClass(newCardName)
                targetDetail = 'Card Name: ' + str(targetClass.name) + '\nCard Rarity: ' + str(
                    targetClass.rarity) + '\nCard Cost: ' + str(targetClass.cost) + '\nCard Major: ' + str(
                    targetClass.major) + '\nCard Set: ' + str(targetClass.set)
                if (targetClass.type == 'weapon'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nDurability: ' + str(
                        targetClass.durability) + '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'spell'):
                    targetDetail += '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'minion'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nHealth: ' + str(
                        targetClass.health) + '\nRace: ' + str(targetClass.race) + '\nDescription: ' + str(
                        targetClass.description)
                detailCardTarget.set(targetDetail)
                message = ""
                warningMessage.set(message)

        # 卡牌搜索的过滤器2
        def filterRec(cardSet):
            for card in cardSet:
                if (filterCost.get() == "All"):
                    if (filterSet.get() == "All"):
                        if (self.keywordFilter.get() == ""):
                            self.cardLibrary.insert('end', card)
                        else:
                            newCardName = translate(card)
                            targetClass = stringToClass(newCardName)
                            if str(targetClass.type) == 'minion':
                                if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                        self.keywordFilter.get().lower() in str(targetClass.description).lower()) or (
                                        self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                        self.keywordFilter.get().lower() == str(targetClass.rarity).lower()) or (
                                        self.keywordFilter.get().lower() == str(targetClass.race).lower()):
                                    self.cardLibrary.insert('end', card)
                            else:
                                if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                        self.keywordFilter.get().lower() in str(targetClass.description).lower()) or (
                                        self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                        self.keywordFilter.get().lower() == str(targetClass.rarity).lower()):
                                    self.cardLibrary.insert('end', card)
                    else:
                        newCardName = translate(card)
                        targetClass = stringToClass(newCardName)
                        if (str(targetClass.set) == filterSet.get()):
                            if (self.keywordFilter.get() == ""):
                                self.cardLibrary.insert('end', card)
                            else:
                                if str(targetClass.type) == 'minion':
                                    if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                            self.keywordFilter.get().lower() in str(
                                        targetClass.description).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.rarity).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.race).lower()):
                                        self.cardLibrary.insert('end', card)
                                else:
                                    if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                            self.keywordFilter.get().lower() in str(
                                        targetClass.description).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.rarity).lower()):
                                        self.cardLibrary.insert('end', card)
                else:
                    newCardName = translate(card)
                    targetClass = stringToClass(newCardName)
                    if (str(targetClass.cost) == filterCost.get()):
                        if (filterSet.get() == "All"):
                            if (self.keywordFilter.get() == ""):
                                self.cardLibrary.insert('end', card)
                            else:
                                if str(targetClass.type) == 'minion':
                                    if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                            self.keywordFilter.get().lower() in str(
                                        targetClass.description).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.rarity).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.race).lower()):
                                        self.cardLibrary.insert('end', card)
                                else:
                                    if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                            self.keywordFilter.get().lower() in str(
                                        targetClass.description).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                            self.keywordFilter.get().lower() == str(targetClass.rarity).lower()):
                                        self.cardLibrary.insert('end', card)
                        else:
                            newCardName = translate(card)
                            targetClass = stringToClass(newCardName)
                            if (str(targetClass.set) == filterSet.get()):
                                if (self.keywordFilter.get() == ""):
                                    self.cardLibrary.insert('end', card)
                                else:
                                    if str(targetClass.type) == 'minion':
                                        if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                                self.keywordFilter.get().lower() in str(
                                            targetClass.description).lower()) or (
                                                self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                                self.keywordFilter.get().lower() == str(
                                            targetClass.rarity).lower()) or (
                                                self.keywordFilter.get().lower() == str(targetClass.race).lower()):
                                            self.cardLibrary.insert('end', card)
                                    else:
                                        if (self.keywordFilter.get().lower() in str(targetClass.name).lower()) or (
                                                self.keywordFilter.get().lower() in str(
                                            targetClass.description).lower()) or (
                                                self.keywordFilter.get().lower() == str(targetClass.type).lower()) or (
                                                self.keywordFilter.get().lower() == str(targetClass.rarity).lower()):
                                            self.cardLibrary.insert('end', card)

        # 卡牌搜索的过滤器1
        def filter():
            self.cardLibrary.delete(0, 'end')
            if (majorCheck.get() == 1):
                if (major == 'mage'):
                    filterRec(mageCards)
                elif (major == 'warrior'):
                    filterRec(warriorCards)
                elif (major == 'demonHunter'):
                    filterRec(demonHunterCards)
                elif (major == 'druid'):
                    filterRec(druidCards)
                elif (major == 'rogue'):
                    filterRec(rogueCards)
                elif (major == 'paladin'):
                    filterRec(paladinCards)
                elif (major == 'hunter'):
                    filterRec(hunterCards)
                elif (major == 'shaman'):
                    filterRec(shamanCards)
                elif (major == 'priest'):
                    filterRec(priestCards)
                elif (major == 'warlock'):
                    filterRec(warlockCards)

            if (neutralCheck.get() == 1):
                filterRec(neutralCards)
            message = ""
            warningMessage.set(message)

        # 添加一个卡牌
        def addCard(deck, deckStatus):
            try:
                cardName = self.cardLibrary.get(self.cardLibrary.curselection())
            except:
                message = "Your must choose an item"
                warningMessage.set(message)
                cardAmount.set(countingDeck(deck))
            else:
                if (deckStatus[0] != 'completed'):
                    for x in range(0, 30):
                        if deck[x] == 'none':
                            newCardName = translate(cardName)
                            targetClass = stringToClass(newCardName)
                            targetRarity = str(targetClass.name)
                            if (targetRarity == 'legendary'):
                                duplicate = 0
                                for y in range(0, 30):
                                    if (deck[y] == cardName):
                                        duplicate += 1
                                if (duplicate == 0):
                                    deck[x] = cardName
                                    message = ""
                                    warningMessage.set(message)
                                else:
                                    message = "Cannot take more of this kind of cards"
                                    warningMessage.set(message)

                            else:
                                duplicate = 0
                                for y in range(0, 30):
                                    if (deck[y] == cardName):
                                        duplicate += 1
                                if (duplicate == 0) or (duplicate == 1):
                                    deck[x] = cardName
                                    message = ""
                                    warningMessage.set(message)
                                else:
                                    message = "Cannot take more of this kind of cards"
                                    warningMessage.set(message)
                            break
                    alignDeck(deck)
                    self.deckBox.delete(0, 'end')
                    for card in deck:
                        self.deckBox.insert('end', card)
                    if (deck[0] != 'none'):
                        deckStatus[0] = 'incomplete'
                        if (deck[29] != 'none'):
                            deckStatus[0] = 'completed'
                else:
                    message = "Your deck is full"
                    warningMessage.set(message)
                cardAmount.set(countingDeck(deck))

        # 删除一个卡牌
        def deleteCard(deck):
            try:
                position = self.deckBox.get(self.deckBox.curselection())
            except:
                message = "Your must choose an item"
                warningMessage.set(message)
                cardAmount.set(countingDeck(deck))
            else:
                for x in range(0, 30):
                    if (position == deck[x]):
                        deck[x] = 'none'
                        break
                alignDeck(deck)
                self.deckBox.delete(0, 'end')
                for card in deck:
                    self.deckBox.insert('end', card)
                if (deck[29] == 'none'):
                    deckStatus[0] = 'incomplete'
                    if (deck[0] == 'none'):
                        deckStatus[0] = 'blank decks'
                message = ""
                warningMessage.set(message)
                cardAmount.set(countingDeck(deck))

        self.master = master
        master.title('Deck Editor')
        master.geometry('900x600+120+120')

        usedOrnot = deck.pop(0)
        usedOrnot = "used"
        deckStatus = []
        deckStatus.append(deck.pop(0))
        deckName = deck.pop(0)
        deckMajor = deck.pop(0)
        deckMajor = major

        majorName = tk.StringVar()
        majorCopy = major
        if (major == "demonHunter"):
            majorCopy = "demon Hunter"
        majorName.set(majorCopy.capitalize())
        self.title = tk.Label(master, width=13, anchor="e", font='Helvetica 13 bold', textvariable=majorName).place(x=660, y=20)
        detailCardTarget = tk.StringVar()
        cardDetail = tk.Label(master, bg='white', width=42, height=12, textvariable=detailCardTarget).place(x=33, y=50)
        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=30, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        cardAmount = tk.IntVar()
        cardAmount.set(countingDeck(deck))
        totalAmount = tk.Label(master, width=13, height=1, anchor="e", textvariable=cardAmount).place(x=370, y=360)

        self.label1 = tk.Label(master, text='Card\'s Library:').place(x=30, y=250)
        self.label2 = tk.Label(master, text='Card\'s Detail:').place(x=30, y=29)
        self.label3 = tk.Label(master, text='Card\'s Filter:').place(x=370, y=400)
        self.label4 = tk.Label(master, text='Cost').place(x=370, y=435)
        self.label5 = tk.Label(master, text='Set').place(x=500, y=435)
        self.label6 = tk.Label(master, text='Keyword').place(x=370, y=485)
        self.label7 = tk.Label(master, text='Deck Name:').place(x=370, y=29)
        self.label8 = tk.Label(master, text='Total amount:').place(x=370, y=360)

        self.Button1 = tk.Button(master, text='Show Detail', width=12, height=1, command=printDetail).place(x=29, y=540)
        self.Button2 = tk.Button(master, text='Add', width=12, height=1,
                                 command=lambda: addCard(deck, deckStatus)).place(x=239, y=540)
        self.Button3 = tk.Button(master, text='Filter', width=12, height=1, command=filter).place(x=690, y=480)
        self.Button4 = tk.Button(master, text='Delete', width=12, height=1, command=lambda: deleteCard(deck)).place(
            x=690, y=370)
        self.Button5 = tk.Button(master, text='Save Deck', width=12, height=1,
                                 command=lambda: self.editorToEdit1(deck, deckStatus[0], self.currName.get(), deckMajor,
                                                                    deckOrder, usedOrnot)).place(x=550, y=540)
        self.Button6 = tk.Button(master, text='Delete Deck', width=12, height=1,
                                 command=lambda: self.editorToEdit2(deckOrder)).place(x=690, y=540)

        self.currName = tk.StringVar(master, value=deckName)
        self.deckName = tk.Entry(master, width=24, show=None, textvariable=self.currName)
        self.deckName.place(x=450, y=29)

        filterCost = tk.StringVar()
        filterCost.set("All")
        self.costFilter = tk.OptionMenu(master, filterCost, "All", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.costFilter.place(x=410, y=430)

        filterSet = tk.StringVar()
        filterSet.set("All")
        self.costFilter = tk.OptionMenu(master, filterSet, "All", "Basic", "Classic")
        self.costFilter.place(x=540, y=430)

        self.keywordFilter = tk.Entry(master, width=36, show=None)
        self.keywordFilter.place(x=430, y=485)

        neutralCheck = tk.IntVar()
        majorCheck = tk.IntVar()
        self.neutralBox = tk.Checkbutton(master, text='neutral', variable=neutralCheck, font=('Arial', 12), onvalue=1,
                                         offvalue=0).place(x=630, y=435)
        self.majorBox = tk.Checkbutton(master, text='major', variable=majorCheck, font=('Arial', 12), onvalue=1,
                                       offvalue=0).place(x=720, y=435)

        self.cardLibrary = tk.Listbox(master, width=50, height=15)

        if (major == 'mage'):
            for card in mageCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'warrior'):
            for card in warriorCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'demonHunter'):
            for card in demonHunterCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'druid'):
            for card in druidCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'rogue'):
            for card in rogueCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'paladin'):
            for card in paladinCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'hunter'):
            for card in hunterCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'shaman'):
            for card in shamanCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'priest'):
            for card in priestCards:
                self.cardLibrary.insert('end', card)
        elif (major == 'warlock'):
            for card in warlockCards:
                self.cardLibrary.insert('end', card)

        for card in neutralCards:
            self.cardLibrary.insert('end', card)

        self.cardLibrary.place(x=30, y=270)

        self.deckBox = tk.Listbox(master, width=70, height=19)

        for card in deck:
            self.deckBox.insert('end', card)

        self.deckBox.place(x=370, y=50)

    def editorToEdit1(self, deck, status, name, major, order, usedOrnot):
        deck.insert(0, major)
        deck.insert(0, name)
        deck.insert(0, status)
        deck.insert(0, usedOrnot)

        fileName = "deck" + str(order) + ".txt"
        file = open(fileName, "w")
        for item in deck:
            file.write(item + " \n")
        file.close()

        self.master.destroy()
        self.master = tk.Tk()
        self.app = Edit(self.master)
        self.master.mainloop()

    def editorToEdit2(self, order):
        saveDeck = open('deck0.txt', 'r')
        deck = saveDeck.readlines()
        saveDeck.close()
        removeSpace(deck)

        fileName = "deck" + str(order) + ".txt"
        file = open(fileName, "w")
        for item in deck:
            file.write(item + " \n")
        file.close()

        self.master.destroy()
        self.master = tk.Tk()
        self.app = Edit(self.master)
        self.master.mainloop()


class Replace:

    def shuffle(self, deck):
        trash1 = deck.pop(0)
        trash2 = deck.pop(0)
        trash3 = deck.pop(0)
        trash4 = deck.pop(0)
        random.shuffle(deck)

    def insert(self, card, deck):
        randomIndex = random.randint(0, len(deck))
        deck.insert(randomIndex, card)


    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()


    def startGame(self, myMajor, myDeck, rivalMajor, rivalDeck, turn, myCard, rivalCard, tempCard):

        for card in tempCard:
            self.insert(card, myDeck)

        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, myMajor, myDeck, rivalMajor, rivalDeck, turn, myCard, rivalCard)
        self.master.mainloop()


    def __init__(self, master, myMajor, myDeck, rivalMajor, rivalDeck):

        noRepeat = []
        approve = [1]

        def replaceCard(tempCard, myCard, cardValue):
            try:
                cardName = self.hand.curselection()
                for i in noRepeat:
                    if (i == cardName[0]):
                        approve[0] = 0
                        break

                if (approve[0] == 1):
                    cardName1 = self.hand.get(self.hand.curselection())
                    tempCard.insert(len(tempCard), cardName1)
                    self.hand.delete(cardName[0])
                    newCard = myDeck.pop(0)
                    self.hand.insert(cardName[0], newCard)
                    myCard[cardName[0]] = newCard
                    noRepeat.insert(len(noRepeat), cardName[0])
                    message = " "
                    warningMessage.set(message)
                else:
                    approve[0] = 1
                    message = "Cannot replace this card"
                    warningMessage.set(message)
            except:
                message = "Your must choose an card"
                warningMessage.set(message)
            else:
                pass


        def printDetail():
            try:
                cardName = self.hand.get(self.hand.curselection())
            except:
                message = "Your must choose an item"
                warningMessage.set(message)
            else:
                newCardName = translate(cardName)
                targetClass = stringToClass(newCardName)
                targetDetail = 'Card Name: ' + str(targetClass.name) + '\nCard Rarity: ' + str(
                    targetClass.rarity) + '\nCard Cost: ' + str(targetClass.cost) + '\nCard Major: ' + str(
                    targetClass.major) + '\nCard Set: ' + str(targetClass.set)
                if (targetClass.type == 'weapon'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nDurability: ' + str(
                        targetClass.durability) + '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'spell'):
                    targetDetail += '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'minion'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nHealth: ' + str(
                        targetClass.health) + '\nRace: ' + str(targetClass.race) + '\nDescription: ' + str(
                        targetClass.description)
                detailCardTarget.set(targetDetail)
                message = ""
                warningMessage.set(message)

        self.master = master
        master.title('HearthStone')
        master.geometry('900x600+120+120')

        turn = random.randint(0, 1)

        title1 = tk.Label(master, text="Card Detail:").place(x=46, y=309)
        title2 = tk.Label(master, text="Choose card to replace:").place(x=352, y=350)
        if (turn == 1):
            self.title = tk.Label(master, text='You get the first hand', font='Helvetica 18 bold').place(x=300, y=50)
        else:
            self.title = tk.Label(master, text='You get the second hand', font='Helvetica 18 bold').place(x=300, y=50)


        detailCardTarget = tk.StringVar()
        cardDetail = tk.Label(master, bg='white', width=42, height=12, textvariable=detailCardTarget).place(x=46, y=330)
        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=30, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)

        self.showDetail = tk.Button(master, text='Show detail', width=12, height=1, command=printDetail).place(x=45, y=530)
        self.backToMenu = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain).place(x=739, y=530)
        self.replace = tk.Button(master, text='Replace', width=12, height=1, command=lambda: replaceCard(tempCard, myCard, cardValue)).place(x=340, y=530)
        self.done = tk.Button(master, text='Done', width=12, height=1, command=lambda: self.startGame(myMajor, myDeck, rivalMajor, rivalDeck, turn, myCard, rivalCard, tempCard)).place(x=445, y=530)

        self.shuffle(myDeck)
        self.shuffle(rivalDeck)

        myCard = []
        rivalCard = []
        tempCard = []

        if (turn == 1):
            myCard.insert(len(myCard), myDeck.pop(0))
            myCard.insert(len(myCard), myDeck.pop(0))
            myCard.insert(len(myCard), myDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))

        else:
            myCard.insert(len(myCard), myDeck.pop(0))
            myCard.insert(len(myCard), myDeck.pop(0))
            myCard.insert(len(myCard), myDeck.pop(0))
            myCard.insert(len(myCard), myDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))
            rivalCard.insert(len(rivalCard), rivalDeck.pop(0))

        cardValue = tk.Variable(value=myCard)
        self.hand = tk.Listbox(master, width=28, height=9, listvariable=cardValue)
        self.hand.place(x=352, y=369)


class GameOver:

    def __init__(self, master, message):
        self.master = master
        master.title('HearthStone')
        master.geometry('900x600+120+120')

        messageCopy = tk.StringVar()
        messageCopy.set(message)
        self.title = tk.Label(master, textvariable=messageCopy, font='Helvetica 30 bold').place(x=370, y=50)
        self.backToMenu = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain).place(x=739, y=530)

    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()


class TheGame:



    def endGame(self, message):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = GameOver(self.master, message)
        self.master.mainloop()


    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()


    def insert(self, card, deck):
        randomIndex = random.randint(0, 9)
        deck.insert(randomIndex, card)


    def __init__(self, master, myMajor, myDeck, rivalMajor, rivalDeck, turn, myCard, rivalCard):

        # 更新随从状态，没有随从的位置按钮将被冻结
        def updateMinionButton():
            if (rivalAssist[0][0] == -1):
                rivalMinionButton0["state"] = "disabled"
            else:
                rivalMinionButton0["state"] = "normal"
            if (rivalAssist[1][0] == -1):
                rivalMinionButton1["state"] = "disabled"
            else:
                rivalMinionButton1["state"] = "normal"
            if (rivalAssist[2][0] == -1):
                rivalMinionButton2["state"] = "disabled"
            else:
                rivalMinionButton2["state"] = "normal"
            if (rivalAssist[3][0] == -1):
                rivalMinionButton3["state"] = "disabled"
            else:
                rivalMinionButton3["state"] = "normal"
            if (rivalAssist[4][0] == -1):
                rivalMinionButton4["state"] = "disabled"
            else:
                rivalMinionButton4["state"] = "normal"
            if (rivalAssist[5][0] == -1):
                rivalMinionButton5["state"] = "disabled"
            else:
                rivalMinionButton5["state"] = "normal"
            if (rivalAssist[6][0] == -1):
                rivalMinionButton6["state"] = "disabled"
            else:
                rivalMinionButton6["state"] = "normal"

            if (myAssist[0][0] == -1):
                friendMinionButton0["state"] = "disabled"
            else:
                friendMinionButton0["state"] = "normal"
            if (myAssist[1][0] == -1):
                friendMinionButton1["state"] = "disabled"
            else:
                friendMinionButton1["state"] = "normal"
            if (myAssist[2][0] == -1):
                friendMinionButton2["state"] = "disabled"
            else:
                friendMinionButton2["state"] = "normal"
            if (myAssist[3][0] == -1):
                friendMinionButton3["state"] = "disabled"
            else:
                friendMinionButton3["state"] = "normal"
            if (myAssist[4][0] == -1):
                friendMinionButton4["state"] = "disabled"
            else:
                friendMinionButton4["state"] = "normal"
            if (myAssist[5][0] == -1):
                friendMinionButton5["state"] = "disabled"
            else:
                friendMinionButton5["state"] = "normal"
            if (myAssist[6][0] == -1):
                friendMinionButton6["state"] = "disabled"
            else:
                friendMinionButton6["state"] = "normal"

        # 进入放置随从模式
        def placeMode():
            modeMessage.set("Place Mode")
            rivalMinionButton1["state"] = "disabled"
            rivalMinionButton2["state"] = "disabled"
            rivalMinionButton3["state"] = "disabled"
            rivalMinionButton4["state"] = "disabled"
            rivalMinionButton5["state"] = "disabled"
            rivalMinionButton6["state"] = "disabled"
            rivalMinionButton0["state"] = "disabled"
            friendMinionButton1["state"] = "disabled"
            friendMinionButton2["state"] = "disabled"
            friendMinionButton3["state"] = "disabled"
            friendMinionButton4["state"] = "disabled"
            friendMinionButton5["state"] = "disabled"
            friendMinionButton6["state"] = "disabled"
            friendMinionButton0["state"] = "disabled"
            rivalHeroButton["state"] = "disabled"
            rivalSkillButton["state"] = "disabled"
            friendHeroButton["state"] = "disabled"
            mySkillButton["state"] = "disabled"
            showDetail["state"] = "disabled"
            backToMenu["state"] = "disabled"
            play["state"] = "disabled"
            done["state"] = "disabled"
            placeButton1["state"] = "normal"
            placeButton2["state"] = "normal"
            placeButton3["state"] = "normal"
            placeButton4["state"] = "normal"
            placeButton5["state"] = "normal"
            placeButton6["state"] = "normal"
            placeButton7["state"] = "normal"
            placeButton8["state"] = "normal"
            cancel["state"] = "normal"


        # 正常模式
        def normalMode():
            modeMessage.set("Normal Mode")
            updateMinionButton()
            rivalHeroButton["state"] = "disabled"
            rivalSkillButton["state"] = "disabled"
            if (myAttack[0] == 0):
                friendHeroButton["state"] = "disabled"
            else:
                friendHeroButton["state"] = "normal"
            mySkillButton["state"] = "normal"
            showDetail["state"] = "normal"
            backToMenu["state"] = "normal"
            play["state"] = "normal"
            done["state"] = "normal"
            placeButton1["state"] = "disabled"
            placeButton2["state"] = "disabled"
            placeButton3["state"] = "disabled"
            placeButton4["state"] = "disabled"
            placeButton5["state"] = "disabled"
            placeButton6["state"] = "disabled"
            placeButton7["state"] = "disabled"
            placeButton8["state"] = "disabled"
            rivalMinionButton1["state"] = "disabled"
            rivalMinionButton2["state"] = "disabled"
            rivalMinionButton3["state"] = "disabled"
            rivalMinionButton4["state"] = "disabled"
            rivalMinionButton5["state"] = "disabled"
            rivalMinionButton6["state"] = "disabled"
            rivalMinionButton0["state"] = "disabled"
            cancel["state"] = "disabled"

        # 如果按了取消
        def quitAnyMode():
            normalMode()

        # 你的回合
        def yourTurn():
            # 是否回合最大上限
            round[0] = round[0] + 1
            if (round[0] == 101):
                self.endGame("Tie")

            # 回合开始
            updateHistory(historyArray, "\nYour turn! (" + str(round[0]) + ")", historyMessage)

            # 所有存在的随从可以攻击
            for x in range(0, len(myAssist)):
                if (myAssist[x][0] == 1):
                    myAssist[x][12] = 1

            # 增加法力值
            if (myMax[0] != 10):
                myMax[0] = myMax[0] + 1
            myLock[0] = myComingLock[0]
            myComingLock[0] = 0
            myAvailable[0] = myMax[0] - myLock[0]

            # 抽牌
            if (len(myDeck) != 0):

                # 牌库警告
                if (len(myDeck) == 2):
                    updateHistory(historyArray, "Running out of cards!", historyMessage)
                elif (len(myDeck) == 1):
                    updateHistory(historyArray, "No cards!", historyMessage)

                newCard = myDeck.pop()
                # 爆牌
                if (self.hand.size() == myMaxCard[0]):
                    updateHistory(historyArray, "There are too many cards!", historyMessage)
                    updateHistory(historyArray, 'Can\'t take ' + newCard, historyMessage)
                # 顺利抽牌
                else:
                    self.hand.insert('end', newCard)
                    newCardName = translate(newCard)
                    targetClass = stringToClass(newCardName)
                    myHandAtt.insert(len(myHandAtt), targetClass)
            # 没有牌，扣疲劳
            else:
                myHealth[0] = myHealth[0] - myVP[0]
                updateHistory(historyArray, "Take " + str(myVP[0]) + " tired damage", historyMessage)
                myVP[0] = myVP[0] + 1
                checkMeDie()

            updateStatus()

        # 对手回合
        def rivalTurn():
            # 是否回合最大上限
            round[0] = round[0] + 1
            if (round[0] == 101):
                self.endGame("Tie")

            # 对手回合开始
            updateHistory(historyArray, "\nOpponent\'s turn! (" + str(round[0]) + ")", historyMessage)

            # 所有存在的随从可以攻击
            for x in range(0, len(rivalAssist)):
                if (rivalAssist[x][0] == 1):
                    rivalAssist[x][12] = 1

            # 增加法力值
            if (rivalMax[0] != 10):
                rivalMax[0] = rivalMax[0] + 1
            rivalLock[0] = rivalComingLock[0]
            rivalComingLock[0] = 0
            rivalAvailable[0] = rivalMax[0] - rivalLock[0]

            # 抽牌阶段
            if (len(rivalDeck) != 0):

                # 牌库警告
                if (len(rivalDeck) == 2):
                    updateHistory(historyArray, "Running out of cards!", historyMessage)
                elif (len(rivalDeck) == 1):
                    updateHistory(historyArray, "No cards!", historyMessage)

                newCard = rivalDeck.pop()
                # 爆牌
                if (len(rivalHandAtt) == rivalMaxCard[0]):
                    updateHistory(historyArray, "There are too many cards!", historyMessage)
                    updateHistory(historyArray, 'Can\'t take ' + newCard, historyMessage)
                # 顺利抽牌
                else:
                    newCardName = translate(newCard)
                    targetClass = stringToClass(newCardName)
                    rivalHandAtt.insert(len(rivalHandAtt), targetClass)
            # 没有牌，扣疲劳
            else:
                rivalHealth[0] = rivalHealth[0] - rivalVP[0]
                updateHistory(historyArray, "Take " + str(rivalVP[0]) + " tired damage", historyMessage)
                rivalVP[0] = rivalVP[0] + 1
                checkRivalDie()

            # AI出牌
            doAgain = 1
            while (doAgain == 1):
                doAgain = 0
                for x in range(0, len(rivalHandAtt)):
                    # 找到一个可以打的牌
                    if (rivalAvailable[0] - rivalHandAtt[x].cost >= 0):
                        # 如果是随从
                        if (rivalHandAtt[x].type == 'minion'):
                            # 确认随从没有满
                            if (totalRm[0] != 7):
                                totalRm[0] = totalRm[0] + 1
                                rivalAvailable[0] = rivalAvailable[0] - rivalHandAtt[x].cost
                                updateHistory(historyArray, "Placed " + rivalHandAtt[x].name, historyMessage)

                                # 取得插入位置
                                place = random.randint(0, len(rivalAssist))
                                # 制作随从信息
                                minion = []
                                minion.insert(len(minion), 1)
                                minion.insert(len(minion), rivalHandAtt[x].name)
                                minion.insert(len(minion), rivalHandAtt[x].rarity)
                                minion.insert(len(minion), rivalHandAtt[x].ATK)
                                minion.insert(len(minion), rivalHandAtt[x].health)
                                minion.insert(len(minion), rivalHandAtt[x].health)
                                minion.insert(len(minion), rivalHandAtt[x].health)
                                minion.insert(len(minion), rivalHandAtt[x].ATK)
                                minion.insert(len(minion), -1)
                                minion.insert(len(minion), rivalHandAtt[x].attribute)
                                minion.insert(len(minion), rivalHandAtt[x].race)
                                minion.insert(len(minion), rivalHandAtt[x].description)
                                minion.insert(len(minion), -1)
                                rivalAssist.insert(place, minion)
                                arrayMinion()
                                updateStatus()
                                normalMode()
                                rivalHandAtt.pop(x)
                                doAgain = 1
                                break
                            else:
                                pass
                        # 如果是法术
                        elif (rivalHandAtt[x].type == 'spell'):
                            rivalAvailable[0] = rivalAvailable[0] - rivalHandAtt[x].cost
                            updateHistory(historyArray, "Used " + rivalHandAtt[x].name, historyMessage)
                            updateStatus()
                            rivalHandAtt.pop(x)
                            doAgain = 1
                            break
                        # 如果是武器
                        elif (rivalHandAtt[x].type == 'weapon'):
                            rivalAvailable[0] = rivalAvailable[0] - rivalHandAtt[x].cost
                            rivalWeapon[0] = 1
                            rivalWeapon[1] = rivalHandAtt[x].name
                            rivalWeapon[2] = rivalHandAtt[x].rarity
                            rivalWeapon[3] = rivalHandAtt[x].ATK
                            rivalWeapon[4] = rivalHandAtt[x].durability
                            rivalWeapon[5] = rivalHandAtt[x].attribute
                            rivalWeapon[6] = rivalHandAtt[x].description
                            updateHistory(historyArray, "Used " + str(rivalHandAtt[x].name), historyMessage)
                            rivalHandAtt.pop(x)
                            doAgain = 1
                            updateStatus()
                            break
                    else:
                        pass

        # 导入新放置的随从
        def getTempMinion():
            minion = []
            minion.insert(len(minion), 1)
            minion.insert(len(minion), tempName[0])
            minion.insert(len(minion), tempRarity[0])
            minion.insert(len(minion), tempATK[0])
            minion.insert(len(minion), tempHP[0])
            minion.insert(len(minion), tempHP[0])
            minion.insert(len(minion), tempHP[0])
            minion.insert(len(minion), tempATK[0])
            minion.insert(len(minion), -1)
            minion.insert(len(minion), tempAttribute[0])
            minion.insert(len(minion), tempRace[0])
            minion.insert(len(minion), tempDescription[0])
            minion.insert(len(minion), -1)
            updateHistory(historyArray, "Placed " + str(tempName[0]), historyMessage)
            return minion


        # 导入新放置的武器
        def getTempWeapon():
            weapon = []
            weapon.insert(len(weapon), 1)
            weapon.insert(len(weapon), tempName[0])
            weapon.insert(len(weapon), tempRarity[0])
            weapon.insert(len(weapon), tempATK[0])
            weapon.insert(len(weapon), tempHP[0])
            weapon.insert(len(weapon), tempAttribute[0])
            weapon.insert(len(weapon), tempDescription[0])
            updateHistory(historyArray, "Used "  + str(tempName[0]), historyMessage)
            return weapon
        

        # 随从信息打印模式转换
        def setUpdate(set0):
            set1 = '[ '
            for x in set0:
                set1 = set1 + x + ' '
            set1 = set1 + ']'
            return set1

        # 删除使用过的卡牌
        def removeCard():
            self.hand.delete(tempOrder[0])
            myHandAtt.pop(tempOrder[0])

        # 排列随从
        def arrayMinion():
            myAssist1 = []
            for item in myAssist:
                if (item[0] == 1):
                    myAssist1.insert(len(myAssist1), item)

            minion = [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1]
            if (len(myAssist1) == 0):
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
            elif (len(myAssist1) == 1):
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
            elif (len(myAssist1) == 2):
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
            elif (len(myAssist1) == 3):
                myAssist1.insert(0, minion)
                myAssist1.insert(0, minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
            elif (len(myAssist1) == 4):
                myAssist1.insert(0, minion)
                myAssist1.insert(len(myAssist1), minion)
                myAssist1.insert(len(myAssist1), minion)
            elif (len(myAssist1) == 5):
                myAssist1.insert(0, minion)
                myAssist1.insert(len(myAssist1), minion)
            elif (len(myAssist1) == 6):
                myAssist1.insert(0, minion)

            myAssist[0] = myAssist1[0]
            myAssist[1] = myAssist1[1]
            myAssist[2] = myAssist1[2]
            myAssist[3] = myAssist1[3]
            myAssist[4] = myAssist1[4]
            myAssist[5] = myAssist1[5]
            myAssist[6] = myAssist1[6]
            if (len(myAssist) == 8):
                myAssist.pop()        
            
            rivalAssist1 = []
            for item in rivalAssist:
                if (item[0] == 1):
                    rivalAssist1.insert(len(rivalAssist1), item)

            minion = [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1]
            if (len(rivalAssist1) == 0):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
            elif (len(rivalAssist1) == 1):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
            elif (len(rivalAssist1) == 2):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
            elif (len(rivalAssist1) == 3):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
            elif (len(rivalAssist1) == 4):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
            elif (len(rivalAssist1) == 5):
                rivalAssist1.insert(0, minion)
                rivalAssist1.insert(len(rivalAssist1), minion)
            elif (len(rivalAssist1) == 6):
                rivalAssist1.insert(0, minion)

            rivalAssist[0] = rivalAssist1[0]
            rivalAssist[1] = rivalAssist1[1]
            rivalAssist[2] = rivalAssist1[2]
            rivalAssist[3] = rivalAssist1[3]
            rivalAssist[4] = rivalAssist1[4]
            rivalAssist[5] = rivalAssist1[5]
            rivalAssist[6] = rivalAssist1[6]
            if (len(rivalAssist) == 8):
                rivalAssist.pop()

            updateStatus()


        # 随从放置按钮
        def place0():
            # 更新法力值
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 0
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place1():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 1
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place2():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 2
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place3():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 3
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place4():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 4
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place5():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 5
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place6():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 6
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        def place7():
            myAvailable[0] = myAvailable[0] - tempCost[0]
            place = 7
            minion = getTempMinion()
            myAssist.insert(place, minion)
            removeCard()
            updateStatus()
            arrayMinion()
            normalMode()

        # 攻击模式
        def attackMode():
            modeMessage.set("Attack Mode")
            updateMinionButton()
            friendMinionButton1["state"] = "disabled"
            friendMinionButton2["state"] = "disabled"
            friendMinionButton3["state"] = "disabled"
            friendMinionButton4["state"] = "disabled"
            friendMinionButton5["state"] = "disabled"
            friendMinionButton6["state"] = "disabled"
            friendMinionButton0["state"] = "disabled"
            rivalHeroButton["state"] = "normal"
            rivalSkillButton["state"] = "disabled"
            friendHeroButton["state"] = "disabled"
            mySkillButton["state"] = "disabled"
            showDetail["state"] = "disabled"
            backToMenu["state"] = "disabled"
            play["state"] = "disabled"
            done["state"] = "disabled"
            placeButton1["state"] = "disabled"
            placeButton2["state"] = "disabled"
            placeButton3["state"] = "disabled"
            placeButton4["state"] = "disabled"
            placeButton5["state"] = "disabled"
            placeButton6["state"] = "disabled"
            placeButton7["state"] = "disabled"
            placeButton8["state"] = "disabled"
            cancel["state"] = "normal"


        # !!
        # 有随从, 名字, 稀有度,   默认攻击, 默认血量, 最大HP, HP, ATK, 临时ATK,    状态, 种族, 描述
        def minionAttack3():
            # 随从无法攻击
            if (myAssist[3][12] != 1):
                message = "The Minion cannot attack in this turn"
                warningMessage.set(message)
            else:
                # 决定是否采用临时ATK
                nowAttack = -1
                if (myAssist[3][8] != -1):
                    nowAttack = myAssist[3][7]
                else:
                    nowAttack = myAssist[3][8]
                # chcek ATK是否为0
                if (nowAttack == 0):
                    message = "The Minion cannot attack"
                    warningMessage.set(message)
                else:
                    # 进入攻击模式
                    attackMode()


        # 出牌但是不含是否成功出牌
        def playCard():
            try:
                cardName = self.hand.curselection()
                # 法力值不够
                if (myAvailable[0] - myHandAtt[cardName[0]].cost < 0):
                    message = "No enough Mana"
                    warningMessage.set(message)
                # 法力值够
                else:
                    # 如果放置随从
                    if (myHandAtt[cardName[0]].type == 'minion'):
                        # 随从满
                        if (totalFm[0] == 7):
                            message = "Cannot place more minions"
                            warningMessage.set(message)
                        else:
                            message = " "
                            warningMessage.set(message)
                            # 存储随从的所有信息
                            totalFm[0] = totalFm[0] + 1
                            placeMode()
                            tempOrder[0] = cardName[0]
                            tempCost[0] = myHandAtt[cardName[0]].cost
                            tempName[0] = myHandAtt[cardName[0]].name
                            tempRarity[0] = myHandAtt[cardName[0]].rarity
                            tempRace[0] = myHandAtt[cardName[0]].race
                            tempHP[0] = myHandAtt[cardName[0]].health
                            tempATK[0] = myHandAtt[cardName[0]].ATK
                            tempDescription[0] = myHandAtt[cardName[0]].description
                            tempDirectional[0] = myHandAtt[cardName[0]].directional
                            tempAttribute[0] = myHandAtt[cardName[0]].attribute
                    # 如果放法术
                    elif (myHandAtt[cardName[0]].type == 'spell'):
                        message = " "
                        warningMessage.set(message)
                        tempOrder[0] = cardName[0]
                        myAvailable[0] = myAvailable[0] - myHandAtt[cardName[0]].cost
                        updateHistory(historyArray, "Used " + myHandAtt[cardName[0]].name, historyMessage)
                        removeCard()
                        updateStatus()
                    # 如果放武器
                    elif (myHandAtt[cardName[0]].type == 'weapon'):
                        message = " "
                        warningMessage.set(message)
                        
                        tempOrder[0] = cardName[0]
                        tempCost[0] = myHandAtt[cardName[0]].cost

                        # 扣法力值        
                        myAvailable[0] = myAvailable[0] - tempCost[0]

                        weapon = getTempWeapon()
                        myWeapon[0] = 1
                        myWeapon[1] = myHandAtt[cardName[0]].name
                        myWeapon[2] = myHandAtt[cardName[0]].rarity
                        myWeapon[3] = myHandAtt[cardName[0]].ATK
                        myWeapon[4] = myHandAtt[cardName[0]].durability
                        myWeapon[5] = myHandAtt[cardName[0]].attribute
                        myWeapon[6] = myHandAtt[cardName[0]].description
                        # 移除卡牌
                        removeCard()
                        updateStatus()
                    else:
                        pass
            except:
                message = "You must choose an card"
                warningMessage.set(message)
            else:
                pass

        # 是否获胜1
        def checkRivalDie():
            if (rivalHealth[0] <= 0):
                self.endGame("You Won")

        def checkMeDie():
            if (myHealth[0] <= 0):
                self.endGame("You Lose")

        # 更新血量，法力值，牌库信息
        def updateStatus():
            cardMessage.set('Rival Max/Library: ' + str(len(rivalHandAtt)) + '/' + str(len(rivalDeck)) + '\n' + 'My Hand/Library: ' + str(self.hand.size()) + '/' + str(len(myDeck)))
            manaMessage.set('Rival Available/Max Mana: ' + str(rivalAvailable[0]) + '/' + str(rivalMax[0]) + '\n' + 'My Available/Max Mana: ' + str(myAvailable[0]) + '/' + str(myMax[0]))
            rivalStatus.set(rivalMajor.title() + '\n' + '+' + str(rivalAttack[0]) + ' ' + str(rivalArmor[0]) + '/' + str(rivalHealth[0]))
            myStatus.set(myMajor.title() + '\n' + '+' + str(myAttack[0]) + ' ' + str(myArmor[0]) + '/' + str(myHealth[0]))

            # 更新武器显示信息
            string00 = myWeapon[1].replace(' ', '\n', 1)
            string11 = rivalWeapon[1].replace(' ', '\n', 1)

            if (myWeapon[0] == -1):
                wp1.set(" ")
            else:
                wp1.set(string00 + '\n' + 'A:' + str(myWeapon[3]) + ' H:' + str(myWeapon[4]) + '\n' + setUpdate(myWeapon[5]))
            if (rivalWeapon[0] == -1):
                wp2.set(" ")
            else:
                wp2.set(string11 + '\n' + 'A:' + str(rivalWeapon[3]) + ' H:' + str(rivalWeapon[4]) + '\n' + setUpdate(rivalWeapon[5]))

            # 更新随从显示信息
            string0 = myAssist[0][1].replace(' ', '\n', 1)
            string1 = myAssist[1][1].replace(' ', '\n', 1)
            string2 = myAssist[2][1].replace(' ', '\n', 1)
            string3 = myAssist[3][1].replace(' ', '\n', 1)
            string4 = myAssist[4][1].replace(' ', '\n', 1)
            string5 = myAssist[5][1].replace(' ', '\n', 1)
            string6 = myAssist[6][1].replace(' ', '\n', 1)

            if (myAssist[0][0] == -1):
                fm0.set(" ")
            else:
                fm0.set(string0 + '\n' + 'A:' + str(myAssist[0][7]) + '  H:' + str(myAssist[0][6]) + '\n' + setUpdate(myAssist[0][9]))
            if (myAssist[1][0] == -1):
                fm1.set(" ")
            else:
                fm1.set(string1 + '\n' + 'A:' + str(myAssist[1][7]) + '  H:' + str(myAssist[1][6]) + '\n' + setUpdate(myAssist[1][9]))
            if (myAssist[2][0] == -1):
                fm2.set(" ")
            else:
                fm2.set(string2 + '\n' + 'A:' + str(myAssist[2][7]) + '  H:' + str(myAssist[2][6]) + '\n' + setUpdate(myAssist[2][9]))
            if (myAssist[3][0] == -1):
                fm3.set(" ")
            else:
                fm3.set(string3 + '\n' + 'A:' + str(myAssist[3][7]) + '  H:' + str(myAssist[3][6]) + '\n' + setUpdate(myAssist[3][9]))
            if (myAssist[4][0] == -1):
                fm4.set(" ")
            else:
                fm4.set(string4 + '\n' + 'A:' + str(myAssist[4][7]) + '  H:' + str(myAssist[4][6]) + '\n' + setUpdate(myAssist[4][9]))
            if (myAssist[5][0] == -1):
                fm5.set(" ")
            else:
                fm5.set(string5 + '\n' + 'A:' + str(myAssist[5][7]) + '  H:' + str(myAssist[5][6]) + '\n' + setUpdate(myAssist[5][9]))
            if (myAssist[6][0] == -1):
                fm6.set(" ")
            else:
                fm6.set(string6 + '\n' + 'A:' + str(myAssist[6][7]) + '  H:' + str(myAssist[6][6]) + '\n' + setUpdate(myAssist[6][9]))

            string0 = rivalAssist[0][1].replace(' ', '\n', 1)
            string1 = rivalAssist[1][1].replace(' ', '\n', 1)
            string2 = rivalAssist[2][1].replace(' ', '\n', 1)
            string3 = rivalAssist[3][1].replace(' ', '\n', 1)
            string4 = rivalAssist[4][1].replace(' ', '\n', 1)
            string5 = rivalAssist[5][1].replace(' ', '\n', 1)
            string6 = rivalAssist[6][1].replace(' ', '\n', 1)
            
            if (rivalAssist[0][0] == -1):
                rm0.set(" ")
            else:
                rm0.set(string0 + '\n' + 'A:' + str(rivalAssist[0][7]) + '  H:' + str(rivalAssist[0][6]) + '\n' + setUpdate(rivalAssist[0][9]))
            if (rivalAssist[1][0] == -1):
                rm1.set(" ")
            else:
                rm1.set(string1 + '\n' + 'A:' + str(rivalAssist[1][7]) + '  H:' + str(rivalAssist[1][6]) + '\n' + setUpdate(rivalAssist[1][9]))
            if (rivalAssist[2][0] == -1):
                rm2.set(" ")
            else:
                rm2.set(string2 + '\n' + 'A:' + str(rivalAssist[2][7]) + '  H:' + str(rivalAssist[2][6]) + '\n' + setUpdate(rivalAssist[2][9]))
            if (rivalAssist[3][0] == -1):
                rm3.set(" ")
            else:
                rm3.set(string3 + '\n' + 'A:' + str(rivalAssist[3][7]) + '  H:' + str(rivalAssist[3][6]) + '\n' + setUpdate(rivalAssist[3][9]))
            if (rivalAssist[4][0] == -1):
                rm4.set(" ")
            else:
                rm4.set(string4 + '\n' + 'A:' + str(rivalAssist[4][7]) + '  H:' + str(rivalAssist[4][6]) + '\n' + setUpdate(rivalAssist[4][9]))
            if (rivalAssist[5][0] == -1):
                rm5.set(" ")
            else:
                rm5.set(string5 + '\n' + 'A:' + str(rivalAssist[5][7]) + '  H:' + str(rivalAssist[5][6]) + '\n' + setUpdate(rivalAssist[5][9]))
            if (rivalAssist[6][0] == -1):
                rm6.set(" ")
            else:
                rm6.set(string6 + '\n' + 'A:' + str(rivalAssist[6][7]) + '  H:' + str(rivalAssist[6][6]) + '\n' + setUpdate(rivalAssist[6][9]))

        # 更新历史记录
        def updateHistory(historyArray, newMessage, historyMessage):
            trash = historyArray.pop(0)
            historyArray.insert(len(historyArray), newMessage)
            historyMessage.set(historyArray[0] + '\n' + historyArray[1] + '\n' + historyArray[2] + '\n' + historyArray[3] + '\n' + historyArray[4] + '\n' + historyArray[5] + '\n' + historyArray[6] + '\n' + historyArray[7] + '\n' + historyArray[8])

        # 查看手牌的信息
        def printDetail():
            try:
                cardName = self.hand.get(self.hand.curselection())
            except:
                message = "Your must choose an card"
                warningMessage.set(message)
            else:
                newCardName = translate(cardName)
                targetClass = stringToClass(newCardName)
                targetDetail = 'Card Name: ' + str(targetClass.name) + '\nCard Rarity: ' + str(
                    targetClass.rarity) + '\nCard Cost: ' + str(targetClass.cost) + '\nCard Major: ' + str(
                    targetClass.major) + '\nCard Set: ' + str(targetClass.set)
                if (targetClass.type == 'weapon'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nDurability: ' + str(
                        targetClass.durability) + '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'spell'):
                    targetDetail += '\nDescription: ' + str(targetClass.description)
                elif (targetClass.type == 'minion'):
                    targetDetail += '\nATK: ' + str(targetClass.ATK) + '\nHealth: ' + str(
                        targetClass.health) + '\nRace: ' + str(targetClass.race) + '\nDescription: ' + str(
                        targetClass.description)
                detailCardTarget.set(targetDetail)
                message = ""
                warningMessage.set(message)

        # 选择结束回合后，直到你下一次开始出牌前，系统要做的所有事
        def operation():
            message = ""
            warningMessage.set(message)
            rivalTurn()
            yourTurn()

        # 创建界面
        self.master = master
        master.title('HearthStone')
        master.geometry('900x600+120+120')

        # 使用卡牌时需要的变量
        tempOrder = [0]
        tempCost = [-1]

        tempName = ['']
        tempRarity = ['']
        tempRace = ['']
        tempHP = [-1]
        tempATK = [-1]
        tempDescription = ['']
        tempDirectional = [False]
        tempAttribute = [[]]

        #各种游戏变量
        round = [0]  # 回合数

        myHealth = [30]
        rivalHealth = [30]
        myArmor = [0]
        rivalArmor = [0]
        myAttack = [0] # 英雄攻击
        rivalAttack = [0]

        rivalMax = [0]  # 当前最大法力
        myMax = [0]
        rivalAvailable = [0]  # 当前可用法力
        myAvailable = [0]
        rivalLock = [0]  # 当前过载
        myLock = [0]
        rivalComingLock = [0]   # 下一回合过载
        myComingLock = [0]

        rivalMaxCard = [10]  # 最大手牌数
        myMaxCard = [10]

        rivalVP = [1]  # 疲劳值
        myVP = [1]

        totalFm = [0]  # 目前随从数
        totalRm = [0]

        historyArray = ['', '', '', '', '', '', '', '', '']

        # 手牌属性
        rivalHandAtt = []
        myHandAtt = []

        # 随从列表
        myAssist = [[-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1]]

        # 有随从, 名字, 稀有度,   默认攻击, 默认血量, 最大HP, HP, ATK, 临时ATK,    状态, 种族, 描述
        rivalAssist = [[-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1],
                    [-1, "none", "none", -1, -1, -1, -1, -1, -1, [], "none", "none", -1]]

        # 武器槽
        # 有随从, 名字, 稀有度,  攻击, 耐久度  状态, 描述
        myWeapon = [-1, "none", "none", -1, -1, [], "none"]
        rivalWeapon = [-1, "none", "none", -1, -1, [], "none"]

        # 战场按钮
        rm0 = tk.StringVar()
        rm1 = tk.StringVar()
        rm2 = tk.StringVar()
        rm3 = tk.StringVar()
        rm4 = tk.StringVar()
        rm5 = tk.StringVar()
        rm6 = tk.StringVar()

        fm0 = tk.StringVar()
        fm1 = tk.StringVar()
        fm2 = tk.StringVar()
        fm3 = tk.StringVar()
        fm4 = tk.StringVar()
        fm5 = tk.StringVar()
        fm6 = tk.StringVar()

        wp1 = tk.StringVar()
        wp2 = tk.StringVar()

        friendWeaponLabel = tk.Label(master, bg='white', textvariable=wp1, width=10, height=4)
        friendWeaponLabel.place(x=324, y=248)
        rivalWeaponLabel = tk.Label(master, bg='white', textvariable=wp2, width=10, height=4)
        rivalWeaponLabel.place(x=324, y=18)

        rivalMinionButton0 = tk.Button(master, textvariable=rm0, width=12, height=4, )
        rivalMinionButton0.place(x=40, y=90)
        rivalMinionButton1 = tk.Button(master, textvariable=rm1, width=12, height=4, )
        rivalMinionButton1.place(x=160, y=90)
        rivalMinionButton2 = tk.Button(master, textvariable=rm2, text='', width=12, height=4, )
        rivalMinionButton2.place(x=280, y=90)
        rivalMinionButton3 = tk.Button(master, textvariable=rm3, text='', width=12, height=4, )
        rivalMinionButton3.place(x=400, y=90)
        rivalMinionButton4 = tk.Button(master, textvariable=rm4, text='', width=12, height=4, )
        rivalMinionButton4.place(x=520, y=90)
        rivalMinionButton5 = tk.Button(master, textvariable=rm5, text='', width=12, height=4, )
        rivalMinionButton5.place(x=640, y=90)
        rivalMinionButton6 = tk.Button(master, textvariable=rm6, text='', width=12, height=4, )
        rivalMinionButton6.place(x=760, y=90)
        friendMinionButton0 = tk.Button(master, textvariable=fm0, width=12, height=4, )
        friendMinionButton0.place(x=40, y=170)
        friendMinionButton1 = tk.Button(master, textvariable=fm1, width=12, height=4, )
        friendMinionButton1.place(x=160, y=170)
        friendMinionButton2 = tk.Button(master, textvariable=fm2, width=12, height=4, )
        friendMinionButton2.place(x=280, y=170)
        friendMinionButton3 = tk.Button(master, textvariable=fm3, width=12, height=4, command=minionAttack3)
        friendMinionButton3.place(x=400, y=170)
        friendMinionButton4 = tk.Button(master, textvariable=fm4, width=12, height=4, )
        friendMinionButton4.place(x=520, y=170)
        friendMinionButton5 = tk.Button(master, textvariable=fm5, width=12, height=4, )
        friendMinionButton5.place(x=640, y=170)
        friendMinionButton6 = tk.Button(master, textvariable=fm6, width=12,  height=4, )
        friendMinionButton6.place(x=760, y=170)
        placeButton1 = tk.Button(master, text='P', width=1, height=1, command=place0, state='disabled')
        placeButton1.place(x=19, y=195)
        placeButton2 = tk.Button(master, text='P', width=1, height=1, command=place1, state='disabled')
        placeButton2.place(x=139, y=195)
        placeButton3 = tk.Button(master, text='P', width=1, height=1, command=place2, state='disabled')
        placeButton3.place(x=259, y=195)
        placeButton4 = tk.Button(master, text='P', width=1, height=1, command=place3, state='disabled')
        placeButton4.place(x=379, y=195)
        placeButton5 = tk.Button(master, text='P', width=1, height=1, command=place4, state='disabled')
        placeButton5.place(x=499, y=195)
        placeButton6 = tk.Button(master, text='P', width=1, height=1, command=place5, state='disabled')
        placeButton6.place(x=619, y=195)
        placeButton7 = tk.Button(master, text='P', width=1, height=1, command=place6, state='disabled')
        placeButton7.place(x=739, y=195)
        placeButton8 = tk.Button(master, text='P', width=1, height=1, command=place7, state='disabled')
        placeButton8.place(x=859, y=195)
        rivalStatus = tk.StringVar()
        rivalHeroButton = tk.Button(master, textvariable=rivalStatus, width=10, height=4)
        rivalHeroButton.place(x=407, y=15)
        rivalSkill = tk.StringVar()
        rivalSkillButton = tk.Button(master, textvariable=rivalSkill, width=4, height=1)
        rivalSkillButton.place(x=493, y=35)
        myStatus = tk.StringVar()
        friendHeroButton = tk.Button(master, textvariable=myStatus, width=10, height=4)
        friendHeroButton.place(x=407, y=245)
        mySkill = tk.StringVar()
        mySkillButton = tk.Button(master, textvariable=mySkill, width=4, height=1)
        mySkillButton.place(x=493, y=265)

        # 框架描述
        title1 = tk.Label(master, text="Card Detail:").place(x=46, y=309)
        title2 = tk.Label(master, text="Battle History:").place(x=532, y=309)
        title3 = tk.Label(master, text="Your card:").place(x=352, y=350)

        # 各种按钮
        showDetail = tk.Button(master, text='Show detail', width=12, height=1, command=printDetail)
        showDetail.place(x=45, y=530)
        backToMenu = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain)
        backToMenu.place(x=739, y=530)
        play = tk.Button(master, text='Play', width=12, height=1, command=playCard)
        play.place(x=340, y=530)
        done = tk.Button(master, text='Done', width=12, height=1, command=operation)
        done.place(x=445, y=530)
        cancel = tk.Button(master, text='Cancel', width=6, height=1, state="disabled", command=quitAnyMode)
        cancel.place(x=215, y=270)

        # 各种信息栏
        detailCardTarget = tk.StringVar()
        cardDetail = tk.Label(master, bg='white', width=42, height=12, textvariable=detailCardTarget).place(x=46, y=330)
        historyMessage = tk.StringVar()
        history = tk.Label(master, bg='white', width=42, height=12, textvariable=historyMessage).place(x=532, y=330)
        modeMessage = tk.StringVar()
        modeMessage.set("Normal Mode")
        modeButton = tk.Label(master, width=10, height=1, anchor="nw", textvariable=modeMessage, font='Helvetica 18 bold').place(x=45, y=267)
        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=30, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        cardMessage = tk.StringVar()
        card = tk.Label(master, width=30, height=2, anchor="nw", textvariable=cardMessage).place(x=545, y=262)
        manaMessage = tk.StringVar()
        mana = tk.Label(master, width=30, height=2, anchor="nw", textvariable=manaMessage).place(x=685, y=262)

        #加入幸运币
        if (turn == 0):
            myCard.insert(len(myCard), "The Coin")
        else:
            rivalCard.insert(len(rivalCard), "The Coin")

        # 放置技能
        if (myMajor == 'druid'):
            mySkill.set('S -2')
        elif (myMajor == 'demonHunter'):
            mySkill.set('DC -1')
        elif (myMajor == 'hunter'):
            mySkill.set('SS -2')
        elif (myMajor == 'mage'):
            mySkill.set('F -2')
        elif (myMajor == 'paladin'):
            mySkill.set('R -2')
        elif (myMajor == 'priest'):
            mySkill.set('LH -2')
        elif (myMajor == 'rogue'):
            mySkill.set('DM -2')
        elif (myMajor == 'shaman'):
            mySkill.set('TC -2')
        elif (myMajor == 'warlock'):
            mySkill.set('LT -2')
        elif (myMajor == 'warrior'):
            mySkill.set('AU -2')

        if (rivalMajor == 'druid'):
            rivalSkill.set('S -2')
        elif (rivalMajor == 'demonHunter'):
            rivalSkill.set('DC -1')
        elif (rivalMajor == 'hunter'):
            rivalSkill.set('SS -2')
        elif (rivalMajor == 'mage'):
            rivalSkill.set('F -2')
        elif (rivalMajor == 'paladin'):
            rivalSkill.set('R -2')
        elif (rivalMajor == 'priest'):
            rivalSkill.set('LH -2')
        elif (rivalMajor == 'rogue'):
            rivalSkill.set('DM -2')
        elif (rivalMajor == 'shaman'):
            rivalSkill.set('TC -2')
        elif (rivalMajor == 'warlock'):
            rivalSkill.set('LT -2')
        elif (rivalMajor == 'warrior'):
            rivalSkill.set('AU -2')

        # 初始化手牌界面
        self.hand = tk.Listbox(master, width=28, height=9)
        for card in myCard:
            self.hand.insert('end', card)
            newCardName = translate(card)
            targetClass = stringToClass(newCardName)
            myHandAtt.insert(len(myHandAtt), targetClass)
        self.hand.place(x=352, y=369)

        normalMode()

        for card in rivalCard:
            newCardName = translate(card)
            targetClass = stringToClass(newCardName)
            rivalHandAtt.insert(len(rivalHandAtt), targetClass)

        # 更新状态
        updateStatus()
        updateMinionButton()

        # 如果你先手
        if (turn == 1):
            yourTurn()
        else:
            rivalTurn()
            yourTurn()


def main():
    window = tk.Tk()
    app = Menu(window)
    window.mainloop()


if __name__ == '__main__':
    main()