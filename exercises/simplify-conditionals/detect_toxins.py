# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')



def check_ingredients(toxin_list):
    return 'sodium nitrate' in toxin_list or 'sodium benzoate' in toxin_list\
        or 'sodium oxide' in toxin_list

ingredients = ['sodium benzoate']

if check_ingredients(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
