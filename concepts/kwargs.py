def greet(name, nationality):
    print(name)
    print(nationality)

greet(nationality="usa", name=  "Sam")

def employee (**kwargs):
    print (kwargs)

employee(name="Sam", age=30, department="HR")
employee(name="Alice", age=25, department="Finance", country="Canada")