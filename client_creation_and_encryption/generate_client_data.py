from faker import Faker
import csv
import random
import lock
import argparse
from const import get_platform_genre_map
from const import get_genres
from const import get_headers

# Initialize faker 
fake = Faker()

# Get constants from const.py library
platform_genre_map = get_platform_genre_map()
genres = get_genres()


def create_client_data() -> dict:
    """
    Use faker library to generate a fake name and fake phone number.
    """
    client_dict = {}
    # Get constants from const.py library
    client_dict[get_headers()[0]] = lock.lock(fake.name())
    client_dict[get_headers()[1]] = lock.lock(fake.phone_number())
    return client_dict


def select_platforms() -> dict:
    """
    Randomly select which platforms an individual subscribes to.
    The threshold that they need to surpass to select a platform increases
    each time they subscribe to a platform.  This is done to try to emulate
    real behavior: people are less likely to subscribe to another platform
    with each platform they subscribe to.
    Initial threshold = 1 / number of platforms available.
    Threshold = threshold ^ .5 for each time a platform is selected.
    """
    platforms = list(platform_genre_map.keys())
    platform_dict = {}
    threshold = 1 / len(platforms)
    exponent_factor = .5
    platforms_selected = 0 
    while platforms:
        random_value = random.random()
        platform_value = 1 if random_value > threshold else 0
        platform_dict[platforms.pop(random.randint(0, len(platforms) - 1))] = platform_value
        if platform_value:
            threshold = threshold ** exponent_factor
    return platform_dict


def select_genres(platform_dict) -> dict:
    """
    The platform dictionary is loaded and the genres associated with each
    platform are counted and placed into the genre_score dictionary.  The
    scores from this are used to calculate the threshold that is required
    to surpass in order to select this genre as a 1 for the client.
    Formula: 1 - x^(1/(1+n)) where n is the score from the genre_score dictionary.
    If the value is 0 then the formula will equal .5.
    A random value between 0-1 is used to check if it is larger than the threshold,
    if it is then the platform is marked as 1, else 0.
    :param platform_dict: A dictionary of the platforms an individual is subscribed to.
    """
    genre_dict = {}

    # set baseline threshold
    x = .5

    # Initialize a dictionary with all genres set to 0
    genre_score = {}
    for genre in genres:
        genre_score[genre] = 0

    # Get the number of times this genre is associated to a platform they subscribe to
    for key in platform_dict.keys():
        if platform_dict[key] == 1:
            for i in platform_genre_map[key]:
                genre_score[i] = genre_score[i] + 1

    # Take the number of times a genre appears in their personal map
    # and use that to calculate the liklihood that they like that genre
    # add these values to the individual dict, and return
    for genre in genres:
        threshold = 1 - (x ** (1/(1+genre_score[genre])))
        random_value = random.random()
        genre_dict[genre] = 1 if random_value > threshold else 0
    return genre_dict 


def randomize_genres(genre_dict) -> dict:
    """
    Allows for additional randomization of user data beyond the 
    selection based on probability.
    Each genre has a 5% chance to flip
    :param genre_dict: Dictionary of genres specific to one person
    """
    for genre in genre_dict.keys(): 
        if random.randint(1,100) > 95:
            genre_dict[genre] = 1 if genre_dict[genre] == 0 else 0
    return genre_dict


def join_dictionaries(client_dict, platform_dict, genre_dict) -> dict:
    """
    Return a single dictionary combining the three input dictionaries.
    """
    return {**client_dict, **platform_dict, **genre_dict}

def generate_data() -> None:
    """
    Primary function which:
    1. Generates fake client data
    2. Encrypts client data
    3. Generate platform data
    4. Generate genre data based on platforms
    5. Randomize genre data
    6. Write all client data to outfile
    """
    with open('data.csv', 'w', newline='') as csv_file:
        headers = get_headers()         # Get constants from const.py library
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for i in range(0,1000):
            client_dict = create_client_data()
            platform_dict = select_platforms()
            genre_dict = select_genres(platform_dict)
            randomized_genre_dict = randomize_genres(genre_dict)
            combined_dict = join_dictionaries(client_dict, platform_dict, randomized_genre_dict)
            writer.writerow({
                headers[0]:combined_dict.get(headers[0]),   # name
                headers[1]:combined_dict.get(headers[1]),   # phone number
                headers[2]:combined_dict.get(headers[2]),   # Amazon
                headers[3]:combined_dict.get(headers[3]),   # Disney+
                headers[4]:combined_dict.get(headers[4]),   # HBO Max
                headers[5]:combined_dict.get(headers[5]),   # Hulu
                headers[6]:combined_dict.get(headers[6]),   # Netflix
                headers[7]:combined_dict.get(headers[7]),   # Paramount+
                headers[8]:combined_dict.get(headers[8]),   # Action
                headers[9]:combined_dict.get(headers[9]),   # Comedy
                headers[10]:combined_dict.get(headers[10]), # Drama
                headers[11]:combined_dict.get(headers[11]), # Family
                headers[12]:combined_dict.get(headers[12]), # Horror
                headers[13]:combined_dict.get(headers[13])  # Thriller
            })

def get_csv_data() -> None:
    """
    Decrypts client name and phone numbers, prints to screen.
    """
    try:
        with open('data.csv', 'r') as csv_read:
            reader = csv.DictReader(csv_read)
            for row in reader:
                print(
                    type(lock.unlock(row.get('name'))),
                    lock.unlock(row.get('name')),
                    lock.unlock(row.get('phone_number')),
                    row.get('Amazon'),
                    row.get('Disney+'),
                    row.get('HBO Max'),
                    row.get('Hulu'),
                    row.get('Netflix'),
                    row.get('Paramount+'),
                    row.get('Action'),
                    row.get('Comedy'),
                    row.get('Drama'),
                    row.get('Family'),
                    row.get('Horror'),
                    row.get('Thriller')
                    )
    except Exception as e:
        print(f"Unable to open file.  Error {e}.  Quitting.")
        quit()


def main() -> None:
    """
    Main function.  By default it will create new fake user data
    and print it to screen.  
    To use the args you can enter the following on the command line:
        $ python generate_client_data.py --gen True
        $ python generate_client_data.py --view_data True
    :Args: --gen True will generate new fake client data
    :Args: --view_data True will read the data.csv file and decrypt all data
    :Args: blank = run both
    """
    parser = argparse.ArgumentParser(description='Take user options')
    parser.add_argument('--gen', type=bool, required=False)
    parser.add_argument('--view_data', type=bool, required=False)
    args = parser.parse_args()
    if args.gen:
        generate_data()
    if args.view_data:
        get_csv_data()
    if not args.gen and not args.view_data:
        generate_data()
        get_csv_data()


if __name__ == "__main__":
    main()