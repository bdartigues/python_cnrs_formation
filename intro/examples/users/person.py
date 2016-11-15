#!/usr/bin/env python

from datetime import date

class Person:
    def __init__(self, first_name, last_name, birth_date, desc = None):
        self.first_name = first_name
        self.last_name  = last_name
        day, month, year = birth_date.split("/")
        self.birth_date = date(int(year), int(month), int(day))
        if desc:
            self.description = desc
        else:
            self.description = "Your average chap."
            
    def age(self):
        return date.today() - self.birth_date
    
    def birthday(self):
        return self.birth_date.replace(year=date.today().year)

    def nextbirthday(self):
        this_year = self.birthday()
        if (this_year < date.today()):
            return this_year.replace(year= date.today().year + 1)
        else :
            return this_year

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self)

    def __str__(self):
        return "{0.first_name} {0.last_name} ".format(self)
    
if (__name__ == '__main__'):
    print "Exercice Person class"
    persons=[]
    with open("users.txt", 'r') as fusers:
        for i, line in enumerate(fusers):
            try:
                last, first, bdate, desc = line.rstrip().split(";")
                p = Person(first.strip(), last.strip(), bdate.strip(), desc.strip())
                persons.append(p)
            except Exception as e:
                print "something bad append while reading line {0}: '{1}'\n\t{2}.".format(i, line, repr(e))
                
    persons.sort(key = lambda u: "{0} {1}".format(u.last_name, u.first_name))

    for i, p in enumerate(persons):
        print "{0}: {1.last_name}, {1.first_name} {1.birth_date}".format(i,p)

    for i, p in enumerate(persons):
        print "{0}: {1}, celebrate on {2}".format(i,p,p.nextbirthday())

        
        
