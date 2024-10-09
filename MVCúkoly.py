# Model ukazuje data úkolů a logiku pro add a view úkolů.
class UkolnicekModel:
    def __init__(self) -> None:
        self.tasks = []

    def add_ukol(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks
    
    # Rozšíření o možnost mazání a změnu úkolů.
    def del_task(self, index):
        if 0 <= index <= len(self.tasks):
            self.tasks.pop(index)

    def apdejt_task(self, index, new_task):
        if 0 <= index <= len(self.tasks):
            self.tasks[index] = new_task

# View zobrazuje data, umožňuje přidávat úkoly
class UkolnicekView:
    def show_tasks(self, tasks):
        if tasks:
            print('Seznam úkolů:')
            print(20*'*')
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")
        else:
            print("Všistko zrobene.")

    def prompt_task(self):
        return input("Zadej nový úkol.\n")
    
    # Musím zjistit, který úkol smazat nebo přepsat
    def cislo_tasku(self):
        return int(input('Zadej číslo ukolu, který chceš změnit nebo smazat:\n'))-1
    
    def zmenit_task(self):
        return input('Zadej upravený text úkolu.')

    
# Controller řídí apku, propojuje M a V
class UkolnicekContra:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
    
    def add_ukol(self):
        new_task = self.view.prompt_task()
        self.model.add_ukol(new_task)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

    #Tu tež musím přidat fce pro del či apdejt úkolu.
    def dele_task(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)
        index = self.view.cislo_tasku()
        self.model.del_task(index)

    def update_task(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)
        index = self.view.cislo_tasku()
        new_task = self.view.zmenit_task()
        self.model.apdejt_task(index, new_task)

    
    

# A teď prý to hlavní, was ist das nevím
if __name__ == "__main__":
    model = UkolnicekModel()
    view = UkolnicekView()
    kontroler = UkolnicekContra(model, view)
    
    while True:
        print(20*'*')
        print("\n1. Zobrazit úkoly")
        print("2. Přidat úkol")
        # tu si přidám odebrat a upravit
        print("3. Upravit úkol")
        print("4. Odebrat úkol")
        print("5. Ende, šlus")

        volba = input('Vyber akci:\n')

        if volba == '1':
            kontroler.show_tasks()
        elif volba =='2':
            kontroler.add_ukol()
        elif volba =='3':
            kontroler.update_task()
        elif volba =='4':
            kontroler.dele_task()
        elif volba =='5':
            print(('Mýdlo končí.'))
            break
        else:
            print('Neumíš do pěti, vole?')

    

