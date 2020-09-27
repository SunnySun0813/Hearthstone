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

        self.master = master
        master.title('Choose Deck')
        master.geometry('900x600+120+120')

        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=60, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        self.title = tk.Label(master, text='Choose your deck', font='Helvetica 18 bold').place(x=350, y=50)
        self.deck11 = tk.Button(master, text=deck1[2] + '\n' + deck1[3] + '\n' + deck1[1], width=20, height=6,
                                command=lambda: self.useDeck1(warningMessage)).place(x=225, y=150)
        self.deck22 = tk.Button(master, text=deck2[2] + '\n' + deck2[3] + '\n' + deck2[1], width=20, height=6, command=lambda: self.useDeck2(warningMessage)).place(
            x=380, y=150)
        self.deck33 = tk.Button(master, text=deck3[2] + '\n' + deck3[3] + '\n' + deck3[1], width=20, height=6, command=lambda: self.useDeck3(warningMessage)).place(
            x=535, y=150)
        self.deck44 = tk.Button(master, text=deck4[2] + '\n' + deck4[3] + '\n' + deck4[1], width=20, height=6, command=lambda: self.useDeck4(warningMessage)).place(
            x=225, y=255)
        self.deck55 = tk.Button(master, text=deck5[2] + '\n' + deck5[3] + '\n' + deck5[1], width=20, height=6, command=lambda: self.useDeck5(warningMessage)).place(
            x=380, y=255)
        self.deck66 = tk.Button(master, text=deck6[2] + '\n' + deck6[3] + '\n' + deck6[1], width=20, height=6, command=lambda: self.useDeck6(warningMessage)).place(
            x=535, y=255)
        self.deck77 = tk.Button(master, text=deck7[2] + '\n' + deck7[3] + '\n' + deck7[1], width=20, height=6, command=lambda: self.useDeck7(warningMessage)).place(
            x=225, y=360)
        self.deck88 = tk.Button(master, text=deck8[2] + '\n' + deck8[3] + '\n' + deck8[1], width=20, height=6, command=lambda: self.useDeck8(warningMessage)).place(
            x=380, y=360)
        self.deck99 = tk.Button(master, text=deck9[2] + '\n' + deck9[3] + '\n' + deck9[1], width=20, height=6, command=lambda: self.useDeck9(warningMessage)).place(
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
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSHunter(self, deck):
        saveDeck = open('Hunter.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSMage(self, deck):
        saveDeck = open('Mage.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSPaladin(self, deck):
        saveDeck = open('Paladin.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSPriest(self, deck):
        saveDeck = open('Priest.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSDemonHunter(self, deck):
        saveDeck = open('DemonHunter.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSRogue(self, deck):
        saveDeck = open('Rogue.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSShaman(self, deck):
        saveDeck = open('Shaman.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSWarlock(self, deck):
        saveDeck = open('Warlock.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()

    def VSWarrior(self, deck):
        saveDeck = open('Warrior.txt', 'r')
        deck1 = saveDeck.readlines()
        removeSpace(deck1)
        saveDeck.close()
        self.master.destroy()
        self.master = tk.Tk()
        self.app = TheGame(self.master, deck[3], deck, deck1[3], deck1)
        self.master.mainloop()


class Edit:

    def __init__(self, master):

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

        self.master = master
        master.title('Edit Deck')
        master.geometry('900x600+120+120')
        self.title = tk.Label(master, text='Deck Editor', font='Helvetica 18 bold').place(x=380, y=50)
        warningMessage = tk.StringVar()
        warning = tk.Label(master, width=60, height=1, anchor="nw", textvariable=warningMessage).place(x=33, y=575)
        self.deck11 = tk.Button(master, text=deck1[2] + '\n' + deck1[3] + '\n' + deck1[1], width=20, height=6,
                                command=lambda: self.openDeck1(warningMessage)).place(x=225, y=150)
        self.deck22 = tk.Button(master, text=deck2[2] + '\n' + deck2[3] + '\n' + deck2[1], width=20, height=6, command=lambda: self.openDeck2(warningMessage)).place(
            x=380, y=150)
        self.deck33 = tk.Button(master, text=deck3[2] + '\n' + deck3[3] + '\n' + deck3[1], width=20, height=6, command=lambda: self.openDeck3(warningMessage)).place(
            x=535, y=150)
        self.deck44 = tk.Button(master, text=deck4[2] + '\n' + deck4[3] + '\n' + deck4[1], width=20, height=6, command=lambda: self.openDeck4(warningMessage)).place(
            x=225, y=255)
        self.deck55 = tk.Button(master, text=deck5[2] + '\n' + deck5[3] + '\n' + deck5[1], width=20, height=6, command=lambda: self.openDeck5(warningMessage)).place(
            x=380, y=255)
        self.deck66 = tk.Button(master, text=deck6[2] + '\n' + deck6[3] + '\n' + deck6[1], width=20, height=6, command=lambda: self.openDeck6(warningMessage)).place(
            x=535, y=255)
        self.deck77 = tk.Button(master, text=deck7[2] + '\n' + deck7[3] + '\n' + deck7[1], width=20, height=6, command=lambda: self.openDeck7(warningMessage)).place(
            x=225, y=360)
        self.deck88 = tk.Button(master, text=deck8[2] + '\n' + deck8[3] + '\n' + deck8[1], width=20, height=6, command=lambda: self.openDeck8(warningMessage)).place(
            x=380, y=360)
        self.deck99 = tk.Button(master, text=deck9[2] + '\n' + deck9[3] + '\n' + deck9[1], width=20, height=6, command=lambda: self.openDeck9(warningMessage)).place(
            x=535, y=360)
        self.newDeck = tk.Button(master, text='New deck', width=12, height=1, command=lambda: self.editToMajor(warningMessage)).place(x=325, y=500)
        self.backForEditDeck = tk.Button(master, text='Back to menu', width=12, height=1,
                                         command=self.editToMain).place(x=485, y=500)

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


class TheGame:

    def shuffle(self, deck):
        trash1 = deck.pop(0)
        trash2 = deck.pop(0)
        trash3 = deck.pop(0)
        trash4 = deck.pop(0)
        random.shuffle(deck)

    def insert(self, card, deck):
        randomIndex = random.randint(0, 9)
        deck.insert(randomIndex, card)

    def editToMain(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Menu(self.master)
        self.master.mainloop()

    def __init__(self, master, myMajor, myDeck, rivalMajor, rivalDeck):

        self.master = master
        master.title('HearthStone')
        master.geometry('900x600+120+120')

        self.rivalMinionButton1 = tk.Button(master, text='Druid', width=10, height=3,).place(x=70, y=100)
        self.rivalMinionButton2 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=180, y=100)
        self.rivalMinionButton3 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=290, y=100)
        self.rivalMinionButton4 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=400, y=100)
        self.rivalMinionButton5 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=510, y=100)
        self.rivalMinionButton6 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=620, y=100)
        self.rivalMinionButton7 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=730, y=100)
        self.friendMinionButton1 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=70, y=180)
        self.friendMinionButton2 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=180, y=180)
        self.friendMinionButton3 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=290, y=180)
        self.friendMinionButton4 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=400, y=180)
        self.friendMinionButton5 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=510, y=180)
        self.friendMinionButton6 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=620, y=180)
        self.friendMinionButton7 = tk.Button(master, text='Druid', width=10, height=3, ).place(x=730, y=180)
        self.placeButton1 = tk.Button(master, text='', width=1, height=1, ).place(x=46, y=195)
        self.placeButton2 = tk.Button(master, text='', width=1, height=1, ).place(x=156, y=195)
        self.placeButton3 = tk.Button(master, text='', width=1, height=1, ).place(x=266, y=195)
        self.placeButton4 = tk.Button(master, text='', width=1, height=1, ).place(x=376, y=195)
        self.placeButton5 = tk.Button(master, text='', width=1, height=1, ).place(x=486, y=195)
        self.placeButton6 = tk.Button(master, text='', width=1, height=1, ).place(x=596, y=195)
        self.placeButton7 = tk.Button(master, text='', width=1, height=1, ).place(x=706, y=195)
        self.placeButton8 = tk.Button(master, text='', width=1, height=1, ).place(x=816, y=195)
        self.rivalHeroButton = tk.Button(master, text='Druid', width=10, height=3, ).place(x=400, y=20)
        self.rivalSkillButton = tk.Button(master, text='', width=3, height=1, ).place(x=486, y=35)
        self.friendHeroButton = tk.Button(master, text='Druid', width=10, height=3, ).place(x=400, y=260)
        self.friendSkillButton = tk.Button(master, text='', width=3, height=1, ).place(x=486, y=275)

        title1 = tk.Label(master, text="Card Detail:").place(x=46, y=309)
        title2 = tk.Label(master, text="Battle History:").place(x=532, y=309)
        title3 = tk.Label(master, text="Your card:").place(x=352, y=350)

        self.backForEditDeck = tk.Button(master, text='Back to menu', width=12, height=1, command=self.editToMain).place(x=739, y=530)
        self.backForEditDeck = tk.Button(master, text='Play', width=12, height=1, command=self.editToMain).place(x=445, y=530)
        self.backForEditDeck = tk.Button(master, text='Show detail', width=12, height=1, command=self.editToMain).place(x=338, y=530)

        detailCardTarget = tk.StringVar()
        cardDetail = tk.Label(master, bg='white', width=42, height=12, textvariable=detailCardTarget).place(x=46, y=330)

        historyMessage = tk.StringVar()
        history = tk.Label(master, bg='white', width=42, height=12, textvariable=historyMessage).place(x=532, y=330)

        self.hand = tk.Listbox(master, width=28, height=9)

        self.hand.place(x=352, y=369)

        self.shuffle(myDeck)
        self.shuffle(rivalDeck)


def main():
    window = tk.Tk()
    app = Menu(window)
    window.mainloop()


if __name__ == '__main__':
    main()