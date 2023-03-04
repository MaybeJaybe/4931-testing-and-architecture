# by Kami Bigdely
# Extract class

first_names = ['Elizabeth', 'Jim']
last_names = ['Debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor:
    def __init__(self, first_names, last_names, birth_year, movies, emails):
        self.first_names = first_names
        self.last_names = last_names
        self.birth_year = birth_year
        self.movies = movies
        self.emails = emails

def send_hiring_email(email):
    print("email sent to: ", email)

for i, value in enumerate(emails):
    if birth_year[i] > 1985:
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
        send_hiring_email(value)

