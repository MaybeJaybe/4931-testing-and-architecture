# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


name_input = input('Please enter your username: ')
save_into_db(name_input)
year_input = int(input('Please enter your birth year: '))
age = 2023 - year_input
print("You are",age, "years old this year.")
