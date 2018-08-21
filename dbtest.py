import sqlite3
from employee import Employee


#Create connection to sqlitedb
conn = sqlite3.connect(':memory:')

#Create cursor for DB traversal
c = conn.cursor()


#Create employees table
c.execute("CREATE TABLE employees (first text, last text,pay integer)")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("UPDATE employees SET pay = :pay WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})






#Instanciate 2 employee objects
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Charlie', 'Doe', 100000)


insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)


update_pay(emp_2, 95000)
remove_emp(emp_1)


emps = get_emps_by_name('Doe')
print(emps)



#Various string replacement methods

#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
#c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})


#Method vulnerable to sql injeciton (Dont Use)
#c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_3.first, emp_3.last, emp_3.pay))


#conn.commit()


#Find all rows where last name is Schafer
#c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
#print(c.fetchall())

#Find all rows where last name is Doe
#c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
#print(c.fetchall())


#conn.commit()

conn.close()

