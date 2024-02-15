class Player():
    def __init__(self, healt, speed, strong, armor, iq, money, name):
        self.healt = healt
        self.strong = strong
        self.armor = armor
        self.iq = iq
        self.money = money
        self.name = name
    
    def print_info(self):
        print('Здоровье - ', self.healt)
        print('Скорость - ', self.strong)
        print('Броня - ', self.armor)
        print('Интеллект - ', self.iq)
        print('Баланс - ', self.money)
    
    def kick(self, enemy):
        enemy.armor -= self.strong
        if enemy.armor <= 0:
            enemy.healt += enemy.armor
            enemy.armor = 0
            if enemy.healt <= 0:
                print('Игрок', enemy.name, 'был повержен игроком', self.name)
        
        print('Игрок', self.name, 'ударил игрока ', enemy.name)
        print('Здоровье врага:', enemy.healt)
        print('Броня врага:', enemy.armor)

    def shop(self, item):
        chest = {'sword': 100, 'iron helmet': 200, 'healt poison': 150}
        if self.money >= chest[item]:
            self.money -= chest[item]
            self.info_item(item)
        else:
            print('Недостаточно средств! Стоимость предмета:', chest[item], 'Ваш баланс:', self.money)

    def info_item(self, item):
        if item == 'sword':
            self.strong += 100
            self.armor += 10

