from data.for_tasks import User
from data.db_session import create_session, global_init

global_init('db/mars_explorer.db')
session = create_session()

user1 = User()
user1.surname = 'Scott'
user1.name = 'Ridley'
user1.age = 21
user1.position = 'captain'
user1.speciality = 'research engineer'
user1.address = 'module_1'
user1.email = 'scott_chief@mars.org'
session.add(user1)
session.commit()

user2 = User()
user2.surname = 'Potapova'
user2.name = 'Daria'
user2.age = 15
user2.position = 'captainess'
user2.speciality = 'scientist'
user2.address = 'module_24'
user2.email = 'dariia_potapova@mars.org'
session.add(user2)
session.commit()

user3 = User()
user3.surname = 'Shestakova'
user3.name = 'Ksenya'
user3.age = 15
user3.position = 'captainess'
user3.speciality = 'scientist'
user3.address = 'module_24'
user3.email = 'shestakova_ksenia@mars.org'
session.add(user3)
session.commit()

user4 = User()
user4.surname = 'Melnikov'
user4.name = 'Stepan'
user4.age = 15
user4.position = 'captains assistance'
user4.speciality = 'programmer'
user4.address = 'module_5'
user4.email = 'melnikov_stepan@mars.org'
session.add(user4)
session.commit()

user5 = User()
user5.surname = 'Kolchanova'
user5.name = 'Irina'
user5.age = 15
user5.position = 'trainer'
user5.speciality = 'sportswoman'
user5.address = 'module_24'
user5.email = 'irina14025@mars.org'
session.add(user5)
session.commit()
session.close()