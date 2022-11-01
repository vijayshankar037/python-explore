#User defined class
class User:
  age = 0
  gender = ''
  mobileNo = ''
  
  # constructor in python
  def __init__(self, age=0, gender='M', mobileNo='0'):
    self.age = age
    self.gender = gender
    self.mobileNo = mobileNo
  
  #Instance method in python
  def show(self):
    print("My age is {} and gender is {} and mobile no is {}".format(self.age, self.gender, self.mobileNo))
  
  
#Creating class object
user = User(30, 'M', '+1-1234567890')

#Accessing attributes of user object
print(user.age)
print(user.gender)
print(user.mobileNo)

#Invoking instance method with user object
user.show()
