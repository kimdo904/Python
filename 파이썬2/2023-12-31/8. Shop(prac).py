class Shop:
    total = 0
    menu_list = [ {"떡볶이" : 3000}, {"순대" : 3000}, {"튀김" : 500}, {"김밥" : 2000}]

    @classmethod
    def sales(cls, food, count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total += (menu[food] * count)



# 떡볶이 : 3000, 순대 : 3000, 튀김 : 500, 김밥 : 2000

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)
print(f'매출 : {Shop.total}원')