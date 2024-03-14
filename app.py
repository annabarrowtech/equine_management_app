
from horse import Horse

h1 = Horse("Missy", 6, "female", "American Quarter Horse", "gray", "stubborn", "not boarded")
h2 = Horse("Bullet", 2, "male", "Friesian", "black", "nervous", "boarded")
h3 = Horse("Flynn", 12, "male", "Percheron", "chestnut", "easygoing", "boarded")
h4 = Horse("Bella", 17, "female", "American Saddlebred", "bay", "friendly", "boarded")


def livery_age_classification(horse_list):
    for horse in horse_list:
        if horse.age > 15:
            print(horse.name + " is " + str(horse.age) + " years old and is an aged " + horse.sex + ".")
        elif horse.age < 4:
            if horse.sex == "male":
                print(horse.name + " is " + str(horse.age) + ", and is a colt.")
            else:
                print(horse.name + " is " + str(horse.age) + ", and is a filly.")
        else:
            if horse.sex == "male":
                print(horse.name + " is " + str(horse.age) + ", and is a stallion.")
            else:
                print(horse.name + " is " + str(horse.age) + ", and is a mare.")


def boarding_tracker(horse_list):
    for horse in horse_list:
        if horse.is_boarded == "boarded":
            print(horse.name + " is boarded.")
        else:
            print(horse.name + " is not currently boarded.")


def horse_profile(horse_list):
    choice = input("Enter 'search' to find a specific horse, or 'list' to view all horses: ").strip().lower()

    if choice == 'search':
        search = input("What is the name of the horse you are looking for?: ").strip()
        found_horse = None  # This will store the matched horse object
        for horse in horse_list:
            if horse.name.lower() == search.lower():  # Case insensitive comparison
                found_horse = horse
                break  # Stop searching once the horse is found

        if found_horse:
            print(f"Name: {found_horse.name}, Age: {found_horse.age}, Sex: {found_horse.sex}, "
                  f"Breed: {found_horse.breed}, Color: {found_horse.color}, Temperament: {found_horse.temperament}, "
                  f"Boarded: {found_horse.is_boarded}")
        else:
            print("Horse is not associated with this stable.")
    elif choice == 'list':
        print("List of all horses:")
        for horse in horse_list:
            print(f"Name: {horse.name}, Age: {horse.age}, Sex: {horse.sex}, "
                  f"Breed: {horse.breed}, Color: {horse.color}, Temperament: {horse.temperament}, "
                  f"Boarded: {horse.is_boarded}")
    else:
        print("Invalid input. Please enter 'search' or 'list'.")


horse_list = [h1, h2, h3, h4]

horse_profile(horse_list)
