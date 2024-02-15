from item import *

Nikita = Player(healt=100, speed=150, strong=200, armor=250, iq=131, money=1, name='Nikita')
Vlad = Player(healt=150, speed=150, strong=200, armor=190, iq=131, money=1, name="Vlad")


Nikita.kick(Vlad)
Nikita.shop('sword')