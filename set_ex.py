food = {
    'candy' : {'sugar', 'butter'},
    'bread' : {'wheat', 'egg', 'sugar', 'milk', 'bitter'},
    'latte' : {'milk', 'caffee'},
    'pizza' : {'wheat', 'tomato', 'onion', 'salt', 'butter'},
    'lemontea' : {'lemon'},
    'cake' : {'sugar', 'seasoning'}
}

for menu, ingredints in food.items() :
    if ingredints & {'sugar', 'butter'} :  # 재료와 {설탕,버터}의 교집합이 공집합이 아니면(원소가 있으면)
        print(menu)
