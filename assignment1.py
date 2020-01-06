"""
Name:Navjot Kaur
Date started: 15-12-2019
GitHub URL:https://github.com/JCUB-CP1404-SP23/a1-movies-to-watch-navsandhu30
"""
from operator import itemgetter
"""used intemgetter topic given in reffrence of assignment """
"""this will open and read csv movies file """
def movies_file():
    in_file = open("movies.csv" , "r")
    created_list = in_file.readlines()
    sorted_movies = []
    """now it will furthur split output into different lines """
    for line in created_list :
        split_line = line.split(",")
        split_line[1] = int(split_line[1])
        sorted_movies.append(split_line)
        in_file.close()
        return sorted_movies
        def get_sorted_movies_list(new_list):
            new_list.sort(key=itemgetter(1,0))
            return new_list
        def display_menu():
            print("L - list movies \n A- Add new movies \n W- Watch a movie \n Q- quit")
            list = ["L", "A", "W","Q"]
            choice = input("choose L,A,W,Q ;\n").upper()
while choice not in  list:
    print("Invalid choice make a selection again ")
    choice = input("choose L,A,W,,Q :\n").upper()
    return choice
"""show * in front the movies those fall under the category of unwatched """
def watch_movies(sorted_movies_list):
    for i in range(5):
        if 'u' in sorted_movies_list[i]:
            print("{}.{:>3s} {} \t - {} ({})".format(i, "*", sorted_movies_list[i][0], sorted_movies_list[i][1], sorted_movies_list[i][2], sorted_movies_list[3]))
        else:
            print("{}.{:>3s} {} \t - {} ({})".format(i, " ", sorted_movies_list[i][0], sorted_movies_list[i][1], sorted_movies_list[i][2], sorted_movies_list[3]))

            def adding_movies():
            movie_title = input("please enter the title of your movie")
            movie_year = input("please enter the year of movie")
            movie_category = input("please enter category of your movie" )
            while not movie_category.isalpha():
                print ("invalid choice . type again . ")
                movie_category = input("please enter category of your movie ")
            while int(movie_year) <=0:
                print("invalid input. please enter again ")
                movie_year = input("please enter the year of movie:")
                print("{} ({} from {}) added to movies list".format(movie_title, movie_category, movie_year))
                new_movie = ("{} , {} , {}, u".format(movie_title, movie_category, movie_year))
                return new_movie



def main():
    """asking user for input wher eL demonstrate to list movies, A represents addind new movie and Q means quit and it will ends the code """
    print("Movies To Watch 1.0 - by <navjot kaur>")
new_list = get_sorted_movie_list(movies_file())
choice = display_menu()
while choice != "Q":
    if choice == "L":
        watch_movies(new_list)
        choice = display_menu()
    elif choice == "A":
        adding_movies()
        choice = display_menu()
    elif choice == "W":
        print("choose your movie you would like to watch now from list")
        watch_movies(new_list)
        choice = display_manu()
        print("thank you , have a great day ")
    main()