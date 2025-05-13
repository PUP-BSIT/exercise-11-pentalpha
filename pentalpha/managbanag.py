from faker import Faker

def make_fake_person():
    """Generate a fake person profile using the Faker library."""
    fake = Faker()

    person_info = {
        "Name": fake.name(),
        "Birthday": fake.date_of_birth(minimum_age=18, maximum_age=90), 
        "Contact Number": fake.phone_number(),
        "Email": fake.email(),
        "Address": fake.address(), 
        "Job": fake.job(),
        "Company": fake.company()
    }
    return person_info
