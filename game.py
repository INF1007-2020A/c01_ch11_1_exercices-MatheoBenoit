"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

import utils


class Weapon:
    """
    Une arme dans le jeu.

    :param name: Le nom de l'arme
    :param power: Le niveau d'attaque
    :param min_level: Le niveau minimal pour l'utiliser
    """
    UNARMED_POWER = 20

    def __init__(self, nom, power, min_level):
        self.__nom = nom
        self.power = power
        self.min_level = min_level

    @classmethod
    def make_unarmed(cls):
        return Weapon("Unarmed", Weapon.UNARMED_POWER, 1)

    def get_nom(self):
        return self.__nom


class Character:
    """
    Un personnage dans le jeu

    :param name: Le nom du personnage
    :param max_hp: HP maximum
    :param attack: Le niveau d'attaque du personnage
    :param defense: Le niveau de défense du personnage
    :param level: Le niveau d'expérience du personnage
    """

    def __init__(self, name, max_hp, attack, defense, level):
        self.__name = name
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.__hp = max_hp
        self.__weapon = None

    @property
    def name(self):
        return self.__name

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val):
        if val is None:
            val = Weapon.make_unarmed()
        if val.min_level > self.level:
            raise ValueError(Weapon)

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, val):
        self.__hp = utils.clamp(val, 0, self.max_hp)

    def compute_damage(self, defender):
        crit = (1 if random.random() > 0.0625 else 2)
        modifier = crit * random.randint(85, 100) / 100
        return (2 + ((2 + 2 * self.level / 5) * self.weapon.power * self.attack / defender.defense) / 50) * modifier, crit


def deal_damage(attacker, defender):
    # TODO: Calculer dégâts
    damage, crit = attacker.compute_damage(defender)
    defender.hp -= damage
    print(f"{attacker.name} used {attacker.weapon.name}")
    if crit:
        print("  Critical hit!")
    print(f"  {defender.name} took {damage} dmg")


def run_battle(c1, c2):
    # TODO: Initialiser attaquant/défendeur, tour, etc.
    print(f"{attacker.name} starts a battle with {defender.name}!")
    while True:
        # TODO: Appliquer l'attaque
        # TODO: Si le défendeur est mort
        print(f"{defender.name} is sleeping with the fishes.")
        break
# Échanger attaquant/défendeur
# TODO: Retourner nombre de tours effectués
