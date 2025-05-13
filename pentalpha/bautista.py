import ephem
from ephem import stars
import datetime
import random

def get_constellation(star_name = "", date = datetime.date.today()):
    """ Prints the constellation the given name of a star belongs to """
    if star_name == "":
        star_name = random.choice(stars.STAR_NUMBER_NAME)

    # Observe with the default date
    object = ephem.star(star_name.title())
    object.compute(date)
    constellation = ephem.constellation(object)[1]
    
    print(f"The star {star_name} is part of the " 
            + f"{constellation} constellation")