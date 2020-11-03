#! python3
# RecipeCrawler.py - Extracts all recipes from dk-kogebogen.dk

import os, requests, bs4, pprint, re, ast
def crawler():
    #Create file
    os.chdir('C:\\Users\\kenny\\Documents\\Exercises projects')
    filename_recipes = 'Recipes.txt'
    filename_ingredients = 'Ingredients.txt'
    filename_description = 'Descriptions.txt'
    recipe_dictionary = open(filename_recipes, 'w', encoding='utf-8')
    ingredient_dictionary = open(filename_ingredients, 'w', encoding='utf-8')
    description_dictionary = open(filename_description, 'w', encoding='utf-8')
    print('Created file called ' + filename_recipes + ' in folder ' + os.getcwd())

    #Definition of variables
    ingredients_list = {}
    #Crawler
    for recipe_id in range(0, 40000):
        recipes = requests.get('https://www.dk-kogebogen.dk/opskrifter/%s/' % recipe_id)
        try:
            recipes.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % exc)
        recipe_bs4 = bs4.BeautifulSoup(recipes.text, features="html.parser")
        # Information-finder
        titles = recipe_bs4.select('span')
        dish = (titles[0].getText()).strip()
        print(dish,end='')
        #Required items
        descriptions = {}
        ingredients_html = recipe_bs4.select('span[class=hidden]')
        description = recipe_bs4.select('.recipe')
        description = (description[0].getText()).replace('\r','').replace('\n','')
        descriptions[recipe_id] = description

        ingredients_list = {}
        ingredients = {}
        #ingredient finder
        for count in range(0, len(ingredients_html)):

            ingredient = (ingredients_html[count].getText()).strip()
            if ingredient == '':
                continue
            ingredient_regex = re.compile(r'''(
            ^(^\d* #heltal
            ([,.]) #adskiller
            ?\d*) #kommatal
            (-)?
            (\d* #heltal
            ([,.])? #adskiller
            \d*)?
            (\s)? #mellemrum
            ((gram|dl|tsk|spsk|g|stk|kg)?(\.)?)? #
            (.*))
            ''', re.VERBOSE)

            ingredients_found = ingredient_regex.findall(ingredient)
            amount = (ingredients_found[0][1]).strip()
            amount += (ingredients_found[0][3]).strip()
            amount += (ingredients_found[0][4]).strip()
            unit = (ingredients_found[0][8]).strip()
            ingredient = (ingredients_found[0][10]).strip()
            key = ingredient
            value = (amount + ' ' + unit).strip()
            ingredients[key] = [value]
            ingredients_list[recipe_id] = ingredients

            #print(ingredients_found)
            #print('unit: ' + unit)
            #print('amount: ' + amount)
            #print('ingredient: ' + ingredient)

        #Add to file
        print ('recipe found: ' + str(recipe_id))
        ingredient_dictionary.write(str(ingredients_list) + '\n')
        description_dictionary.write((str(descriptions) + '\n'))





    #End collection of recipes, if nothing is found
        if dish is '':
            print('No more recipes found.')
            continue
    #Add to file
        #print('Dish found: ' + dish + ' ID: ' + str(i))
        recipe_dictionary.write('id ' + str(recipe_id) + ' : ' + dish + '\n')

    recipe_dictionary.close()
    ingredient_dictionary.close()
    description_dictionary.close()

def recipelookup(recipename):
    os.chdir('C:\\Users\\kenny\\Documents\\Exercises projects')
    filename_recipes = 'Recipes.txt'
    filename_ingredients = 'Ingredients.txt'
    filename_description = 'Descriptions.txt'
    recipe_dictionary = open(filename_recipes, 'r', encoding='utf-8')
    ingredient_dictionary = open(filename_ingredients, 'r', encoding='utf-8')
    description_dictionary = open(filename_description, 'r', encoding='utf-8')


    recipename = int(recipename)
    ingredients = ingredient_dictionary.readlines()

    ingredients_dict = ast.literal_eval(ingredients[recipename])
    ingredients_dict = (ingredients_dict.get(recipename))

    ingredients_list = list(ingredients_dict.keys())
    ingredient_units = list(ingredients_dict.values())

    length = 0
    for i in range(len(ingredients_list)):
        unitlength = len(ingredient_units[i][0])
        if length < unitlength:
            length = unitlength

    for x in range(len(ingredients_list)):
        insert = str('{0: <' + str(length + 1) + '}')
        print(insert.format(ingredient_units[x][0]),end='')
        print(ingredients_list[x])


    recipe_dictionary.close()
    ingredient_dictionary.close()
    description_dictionary.close()

def whatcaniget():


    os.chdir('C:\\Users\\kenny\\Documents\\Exercises projects')
    filename_recipes = 'Recipes.txt'
    filename_ingredients = 'Ingredients.txt'
    filename_description = 'Descriptions.txt'
    recipe_dictionary = open(filename_recipes, 'r', encoding='utf-8')
    ingredient_dictionary = open(filename_ingredients, 'r', encoding='utf-8')
    description_dictionary = open(filename_description, 'r', encoding='utf-8')

    ingredients = ingredient_dictionary.readlines()

    # create list of ingredients
    fridge = []
    fridge_list = []
    print('Input what you want to use. End with \'\'')
    while True:
        fridgeinput = input()
        fridge.append(fridgeinput)
        if fridgeinput == '':
            break
        else:
            fridge_list += fridge
    lines = recipe_dictionary.readlines()
    for count in range(0,len(lines)):
        recipe_id = count
        ingredients_dict = ast.literal_eval(ingredients[recipe_id])
        ingredients_dict = (ingredients_dict.get(recipe_id))
        if ingredients_dict == None:
            continue

        ingredients_list = list(ingredients_dict.keys())
        ingredient_units = list(ingredients_dict.values())


        #check for possible recipes
        found = 0
        for i in range(0,len(fridge_list)):
            for b in range(0,len(ingredients_list)):
                if fridge_list[i] == ingredients_list[b]:
                    found += 1
                    continue
                else:
                    continue
        if found == len(fridge_list):
            line = lines[recipe_id]
            print((str(round(len(fridge_list)/len(ingredients_list)*100)).ljust(2) + ' % '),end='')
            print(([s for s in lines if ('id' + ' ' + str(recipe_id) + ' ') in s][0]),end='')

    print('Search finished.')





#print('What recipe would you like to find?')
inputs = input()
recipelookup(inputs)
whatcaniget()
