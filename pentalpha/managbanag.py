from faker import Faker

def make_fake_person():
    fake = Faker()
    user_input = int(input("How many fake profiles do you like to generate? "))

    for count in range(user_input):
        print("")
        print(f"Profile #{count + 1}:")
        
        person_info = {
            "Name": fake.name(),
            "Birthday": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "Contact Number": fake.phone_number(),
            "Email": fake.email(),
            "Address": fake.address(),
            "Job": fake.job(),
            "Company": fake.company()
        }
        
        for title, info in person_info.items():
            print(f"{title}: {info}")