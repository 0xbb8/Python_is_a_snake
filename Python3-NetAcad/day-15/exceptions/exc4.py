# Making Custom Exceptions

class CocktailError(Exception):
    
    def __init__(self,cocktail,message):
        Exception.__init__(self,message)
        self.cocktail = cocktail

class GettingDrunk(CocktailError):
    def __init__(self,cocktail,alcohol,message):
        CocktailError.__init__(self,cocktail,message)
        self.alcohol = alcohol
        print(self,cocktail,message)

def make_cocktail(drink,ethanol):
    if drink not in ['margarita','martini','mimosa']:
        raise CocktailError(drink,'Cocktail Not Available')
    if ethanol > 80:
        GettingDrunk(drink,ethanol,'Way too much booze.')
        print('after')
    print('Drink is served.')

for (drinks,ethanol) in [('martini',90),('margarita',60),('mimosa',30),('boiler-maker',200)]:
    try:
        make_cocktail(drinks,ethanol)
    except GettingDrunk as drunk:
        print(drunk,':',drunk.alcohol)
    except CocktailError as ce:
        print(ce,':',ce.cocktail)
