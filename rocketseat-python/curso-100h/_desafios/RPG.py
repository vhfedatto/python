"""
JOGO
* objetivo : Usuário controla o heroi que encontra inimigos e batalha com eles.

"""

class Personagem:
    """ Todo personagem tem nome, classe, nivel, vida, ataque, defesa, speed e habilidades 
    
    Todo personagem pode atacar, sofrer dano """

    def __init__(self, nome, classe, lvl, hp, atk, defe, spd, hab)-> None:
        self.nome = nome
        self.classe = classe
        self.lvl = lvl
        self.hp = hp
        self.atk =atk
        self.defe = defe
        self.spd = spd
        self.hab = hab

class Hero(Personagem):
    def __init__(self, nome, classe, lvl, hp, atk, defe, spd, hab, xp) -> None:
        super().__init__(nome, classe, lvl, hp, atk, defe, spd, hab)
        self.xp = xp
    

    
hero_hab_knight = ["Espada Flamejante", "Escudo de Titânio", "Scremham"]
enemy_hab_knight = ["Mordida Flamejante", "Dentes de Titânio", "Scabam"]

herois = {"h-1": {"nome": "Robisbaldo",
                  "classe": "Cavaleiro",
                  "lvl": 1,
                  "hp": 15,
                  "atk": 5,
                  "defe": 5,
                  "spd": 5,
                  "hab": hero_hab_knight[0:2]}}

inimigos = {"e-1": {"nome": "",
                    "classe": "",
                    "lvl": 1,
                    "hp": 15,
                    "atk": 5,
                    "defe": 5,
                    "spd": 5,
                    "hab": enemy_hab_knight[0]}}

us_hero = Hero(nome= herois["h-1"]["nome"],classe=herois["h-1"]["classe"],lvl=herois["h-1"]["lvl"],hp=herois["h-1"]["hp"], atk=herois["h-1"]["atk"], defe=herois["h-1"]["defe"], spd=herois["h-1"]["spd"], hab=herois["h-1"]["hab"], xp=0)
print("="*15+" MENU "+"="*15)
print(us_hero.nome)