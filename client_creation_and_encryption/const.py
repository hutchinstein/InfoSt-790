# This file contains variables which are treated as constants.  This has been moved to its own
# file to help increase readability of the entire project.

def get_platform_genre_map() -> dict:
    '''
    Returns a dictonary with the genres that are associated with each platform
    for client data generation.  
    '''
    platform_genre_map = {
                        'Amazon': ['Action', 'Comedy', 'Drama'],
                        'Disney+': ['Family'],
                        'HBO Max': ['Thriller', 'Horror'],
                        'Hulu': ['Drama', 'Family'],
                        'Netflix':['Comedy', 'Drama'],
                        'Paramount+': ['Drama', 'Thriller']
                      }
    return platform_genre_map


def get_genres() -> list:
    '''
    Returns a list with all genres available.
    '''
    genres = ['Action', 'Comedy', 'Drama', 'Family', 'Horror', 'Thriller']
    return genres


def get_headers() -> list:
    '''
    Returns a list of all of the headers for the csv output file.
    '''
    headers = ['name', 'phone_number']
    for platform in list(get_platform_genre_map()):
        headers.append(platform)
    for genre in get_genres():
        headers.append(genre)
    return headers
