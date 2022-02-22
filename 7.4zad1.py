import numbers
from random import random, randit, shuffle
import time

now = time.strftime("%d/%m/%Y")

#biblioteka filmów
class MovieLibrary:
    def __init__(self, title, publishment_year, type_of, number_of_plays):
        self.title = title
        self.publishment_year = publishment_year
        self.type_of = type_of
        self.number_of_plays = number_of_plays
    
    # metoda play
    def play(self):
        self.number_of_plays = self.number_of_plays+ 1
        print(f"Liczba odtworzeń: {self.number_of_plays:02}")

    #wyświetlanie filmów
    def __str__(self):
        return (f"{self.title} {self.publishment_year}")
    
############################################################################################################
#biblioteka seriali
class SerialLibrary(MovieLibrary):
    def __init__(self, title, publishment_year, type_of, number_of_plays, episode_number, season_number):
        super().__init__(title, publishment_year, type_of, number_of_plays)
        self.episode_number = episode_number
        self.season_number = season_number
    
    #wyświetlanie serialu
    def __str__(self):
        if self.episode_number <10:
            self.episode_number = "0" + str(self.episode_number)
        if self.season_number <10:
            self.season_number = "0" + str(self.season_number)
        return(f"{self.title} S{self.season_number} E{self.episode_number}")



################################################################################################################
#zwracanie filmu
def get_movies():
    movie_total = []
    for movie in General_list:
        if len(movie) < 5:
            movie_total.append(movie)
            movie_total = sorted(movie_total)
    print(movie_total)

#zwracanie serialu
def get_series():
    serial_total = []
    for serial in General_list:
        if len(serial) > 4:
            serial_total.append(serial)
            serial_total = sorted(serial_total)
    print(serial_total)

###############################################################################################################

#wyszukiwanie po tytule

def search():
    search_name = input("Napisz tutuł filmu lub serialu:")
    for search_object in General_list:               
      if search_object[0]() == search_name():                
        print(search_object)

##############################################################################################################

#losowa ilość odtworzeń

def generate_views(MovieLibrary):
    random.shuffle(MovieLibrary)
    for i in range(random.randit(1,100)):
        MovieLibrary[0].generate_views()

# uruchomienie generate_views
def generate_views_10(MovieLibrary):
    for i in range(10):
        generate_views(MovieLibrary)


################################################################################################################

#lista filmów i seriali


movie_1= MovieLibrary(title= "Qu'est-ce qu'on a fait au Bon Dieu?", publishment_year= 2014, type_of= "comedy", number_of_plays= 70)
movie_2= MovieLibrary(title= "Intouchables", publishment_year= 2011, type_of= "drama/comedy" , number_of_plays= 45)
movie_3= MovieLibrary(title= "The Green Mile", publishment_year= 1999, type_of= "drama" , number_of_plays= 50)
movie_4= MovieLibrary(title= "The Godfather ", publishment_year= 1972, type_of= "drama", number_of_plays= 54)
movie_5= MovieLibrary(title= "Forrest Gump", publishment_year= 1994, type_of= "drama/comedy", number_of_plays= 38)
movie_6= MovieLibrary(title= "The Pianist", publishment_year= 2002, type_of= "drama/war", number_of_plays= 49)
movie_7= MovieLibrary(title= "A Beautiful Mind ", publishment_year= 2001, type_of= "drama", number_of_plays=34 )
movie_8= MovieLibrary(title= "Django Unchained ", publishment_year= 2012, type_of= "western", number_of_plays= 55)
movie_9= MovieLibrary(title= "The Silence of the Lambs", publishment_year= 1991 , type_of= "thriller", number_of_plays= 47)
movie_10= MovieLibrary(title= "American History X", publishment_year= 1998, type_of= "drama", number_of_plays= 33)
movie_11= MovieLibrary(title= "Saving Private Ryan ", publishment_year= 1998, type_of= "drama/war", number_of_plays= 22)
movie_12= MovieLibrary(title= "The Boy in the Striped Pyjamas", publishment_year= 2008, type_of= "drama/war", number_of_plays= 66)
movie_13= MovieLibrary(title= "Braveheart", publishment_year= 1995, type_of= "drama", number_of_plays= 39)
movie_14= MovieLibrary(title= "The Help", publishment_year= 2011, type_of= "drama", number_of_plays= 53)
movie_15= MovieLibrary(title= "The Pursuit of Happyness ", publishment_year= 2006, type_of= "drama", number_of_plays= 50)
movie_16= MovieLibrary(title= "Seven Pounds", publishment_year= 2008, type_of= "drama", number_of_plays= 30)
movie_17= MovieLibrary(title= "Monty Python and the Holy Grail ", publishment_year= 1975, type_of= "comedy", number_of_plays= 57)
movie_18= MovieLibrary(title= "The Devil's Advocate", publishment_year= 1997, type_of= "thriller", number_of_plays= 26)
movie_19= MovieLibrary(title= "The Meaning of Life", publishment_year= 1983, type_of= "comedy", number_of_plays= 70)
movie_20= MovieLibrary(title= "The Illusionist ", publishment_year= 2006, type_of= "fantasy", number_of_plays= 20)


serial_1 = SerialLibrary(title= "The Marvelous Mrs. Maisel", publishment_year= 2017, type_of= "drama/comedy", number_of_plays= 59, episode_number= 8, season_number= 4)
serial_2 = SerialLibrary(title= "Chicago fire", publishment_year= 2012, type_of= "action", number_of_plays= 60, episode_number= 16, season_number= 10)
serial_3 = SerialLibrary(title= "Euphoria", publishment_year= 2019, type_of= "drama", number_of_plays= 33, episode_number= 8, season_number= 3)
serial_4 = SerialLibrary(title= "L'amica geniale", publishment_year= 2018, type_of= "drama", number_of_plays= 17, episode_number= 8, season_number= 3)
serial_5 = SerialLibrary(title= "After life", publishment_year= 2019, type_of= "drama", number_of_plays= 18, episode_number= 6, season_number= 3)
serial_6 = SerialLibrary(title= "Billions", publishment_year= 2016, type_of= "drama", number_of_plays= 35, episode_number= 6, season_number= 6)
serial_7 = SerialLibrary(title= "New Amsterdam", publishment_year= 2018, type_of= "drama", number_of_plays= 37, episode_number= 16, season_number= 4)
serial_8 = SerialLibrary(title= "State of the Union", publishment_year= 2019, type_of= "comedy", number_of_plays= 20, episode_number= 10, season_number= 2)
serial_9 = SerialLibrary(title= "Sweet Magnolias", publishment_year= 2020, type_of= "drama", number_of_plays= 27, episode_number= 10, season_number= 2)
serial_10 = SerialLibrary(title= "Inventing Anna", publishment_year= 2022, type_of= "drama", number_of_plays= 12, episode_number= 9, season_number= 1)
serial_11 = SerialLibrary(title= "Space Forc", publishment_year= 2020, type_of= "comedy", number_of_plays= 32, episode_number= 7, season_number= 2)
serial_12 = SerialLibrary(title= "Undercover", publishment_year= 2019, type_of= "drama", number_of_plays= 26, episode_number= 8, season_number= 3)
serial_13 = SerialLibrary(title= "Resident alien", publishment_year= 2021, type_of= "drama", number_of_plays= 31, episode_number= 6, season_number= 2)
serial_14 = SerialLibrary(title= "Peacemaker", publishment_year= 2022, type_of= "comedy", number_of_plays= 23, episode_number= 8, season_number= 2)
serial_15 = SerialLibrary(title= "Ozark", publishment_year= 2017, type_of= "drama", number_of_plays= 34, episode_number= 7, season_number= 4)

movie_total = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6, movie_7, movie_8, movie_9, movie_10, movie_11, movie_12, movie_13, movie_14, movie_15, movie_16, movie_17, movie_18, movie_19, movie_20]
serial_total = [serial_1, serial_2, serial_3, serial_4, serial_5, serial_6, serial_7, serial_8, serial_9, serial_10, serial_11, serial_12, serial_13, serial_14, serial_15]

General_list= []



#################################################################################################################

#wybór najpopularniejszych filmów lub seriali

def top_titles(General_list):
    content_type = input("Dla filmów wybierz :1, dla seriali wybierz: 2\n")
    if content_type == '1':
        lsorted=sorted(movie_total, key=lambda movie_total: movie_total.number_of_plays,reverse=True)
        for m in range (int(numbers)):
            print(f'nr wyświetleń:{lsorted[m].number_of_plays:003},tytuł:{lsorted[m].title}')

    elif content_type == '2':
        lsorted=sorted(serial_total, key=lambda series: series.number_of_plays,reverse=True)
        for s in range(int(numbers)):
            print(f'nr wyświetleń:{lsorted[s].number_of_plays:003},tytuł:{lsorted[s].title}')

#wyświetlenie top 3

def top_three(MovieLibrary):
    top_3=sorted(MovieLibrary, key=lambda index: index.number_of_plays,reverse=True)
    for nr in range (3):
        print(f'Top nr{nr+1}:{top_3[nr].number_of_plays:003},tytuł:{top_3[nr].title}')

# wyświetlanie

print("\t\t**** Biblioteka filmów ****\n" "\t\t"+ "-" * 26)
get_movies()
get_series()
print(f"\t\t**** Najpopularniejsze filmy i seriale dnia {now} ****\n" + "\t\t" + "-" * 59)

generate_views(MovieLibrary)
generate_views_10(MovieLibrary)
top_titles(MovieLibrary)
print(f"\n Najpopularniejsze produkcje dnia {date.today()}")
top_three(MovieLibrary)