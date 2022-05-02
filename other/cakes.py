def cakes(recipe, available):
    result = list()
    available.get('flour', 0)

    for ing in recipe.keys():
        if ing in available.keys():
            result.append(available[ing] // recipe[ing])
        else:
            return 0

    return min(result)


print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000}))
print(cakes({'eggs': 45, 'sugar': 87, 'nuts': 47},
            {'eggs': 8019, 'sugar': 9784, 'nuts': 6248, 'pears': 3429, 'crumbles': 1232, 'cream': 8847, 'oil': 1987,
             'flour': 3451, 'milk': 6, 'chocolate': 6721}))
