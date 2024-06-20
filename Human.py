class Human:
    def __init__(self,ful_name, date_of_birth,contact_number, city, country,home_address):
        self.full_name = ful_name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def get_name(self):
        return(self.ful_name)
    
    def set_color(self, new_color):
        self.color = new_color

    def get_date_of_birth(self):
        return(self.date_of_birth)
    
    def set_contact(self, new_contact_number):
        self.contact_number = new_number

    def get_city(self):
        return(self.city)
    
    def set_country(self, new_country):
        self.country = new_country

    def get_address(self):
        return(self.home_address)


human = Human("Adolf Hitler", "8.4.1918", "+48 605 456 789", "Berlin", "Bundesrepublik Deutschland", "Orlí Hnízdo" )

print(human.get_city())


human.set_country("Argentina")
print(human.country)
