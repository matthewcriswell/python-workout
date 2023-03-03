''' bread nutrition info '''


class Bread():

    calories = 110
    carbs = 10
    sodium = 1
    sugar = 3
    fat = 2

    def __init__(self, slices=1):
        self.slices = slices

    def get_nutrition(self):
        nutrition = {}
        nutrition['calories'] = self.calories * self.slices
        nutrition['carbs'] = self.carbs * self.slices
        nutrition['sodium'] = self.sodium * self.slices
        nutrition['sugar'] = self.sugar * self.slices
        nutrition['fat'] = self.fat * self.slices
        return nutrition

class WholeWheatBread(Bread):

    calories = 150
    carbs = 13
    sodium = 5
    sugar = 2
    fat = 3

class RyeBread(Bread):

    calories = 220
    carbs = 20
    sodium = 30
    sugar = 5
    fat = 5
