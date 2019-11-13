import sys
import os

#Open the separate file containing our list of music



def imported_albums():
    library = []
    with open("text_albums_data.txt", "r") as file:
        for item in file:
            library.append(item.strip("\n").split(","))
    library2 = [item[0] for item in library]
    print(library2)

# def albums_by_genre():
#     genre_list = []
#     with open("text_albums_data.txt", "r") as file:




def main():

    print("Welcome to your personal music collector application")
    print("1.View all imported albums\n2.Find all abums by genre\n3.Find all albums by given time range\n4.Find shortest/longest album\n5.Find all albums created by given artist\n6.Find album by given name\n7.Show all albums and its details ")
    user_choice = input("\nChoose an option: ")
    if user_choice == '1':
        print(list(imported_albums()))
    elif user_choice == '2':
        print

main()
