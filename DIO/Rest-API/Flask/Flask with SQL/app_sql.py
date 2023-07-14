from models import Peoples,Activities
def insert():
    people = Peoples(nome = "Eduardo", idade = "17")
    people.save()
    print(people)

def view():
    people = Peoples.query.all()
    print(people)
    people = Peoples.query.filter_by(nome = "Eduardo")
    
def put():
    people =Peoples.query.filter_by(nome="Eduardo").first()
    people.nome = "Felipe"
    people.save()

def delete():
    people =Peoples.query.filter_by(nome="Eduardo").first()
    people.delete()

if __name__ == '__main__':
    view()