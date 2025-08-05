from datetime import datetime,date

class person:
    id_number= 1

    def __init__(self, name, last_name,birth_date):
        self.name=name.format_name(name)
        self.last_name=last_name.format.name(last_name)
        self.birth_date=birth_date.parse_birthday(birth_date)
        person.id_number+=1

    @staticmethod
    def parse_birthday(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y').date()
    
    @staticmethod
    def format_name(name):
        if not name[0].isupper():
            return name.capatalize()
        else:
            return name
            
    



print(datetime.today())
p1=person('john','snow','8-6-2000')
print(p1.birth_date)

