from ephem import constellation, stars
from datetime import date
from random import choice

def get_constellation(star_name = ""):
    """ Prints the constellation the given name of a star belongs to """
    if star_name == "":
        star_name = choice(stars.STAR_NUMBER_NAME)

    # Observe with the default date
    observing_date = date.today()
    object = stars.star(star_name.title())
    object.compute(observing_date)
    constellation_result = constellation(object)[1]
    
    print(f"The star {star_name} is part of the " 
            + f"{constellation_result} constellation")