import pickle

class CapitaL:
    
    def __init__(self) -> None:
        # stvoření prázdného slovníku
        self.data = {}
    # přidání položek
    def add_data(self,country, capital):
        self.data[country] = capital
        if country in self.data:
            raise ValueError( f"country {country} vskutku exist")
    #mazání položek
    def delete_data(self, country):
        del self.data[country]
    # vyhledání dat
    def find_data(self, country):
        return self.data[country] # country je klíč

    def edit_data(self, country, new_capital):
        if country not in self.data:
            raise ValueError(f"country {country} neexistuje")
        
    def save_data(self, filename):
        with open(filename, 'wb',encoding="utf8") as file: # encoding pro češtinu v souboru 
            pickle.dump(self.data,file)

    def load_data(self, filename):
        with open(filename, 'rb', encoding="utf8") as file:
        self.data

    

c = Capitals()
filename = "capitals.dat" # bo prý může kecat


while True:
    try:
        comando = input (Zadej opraci(adfeslq) ) 
        if comando == a:
            country = input      
            atd:

    except KeyError as e:
        print(f" Neznám takovou zemi")


    



word prý takhle pracuje