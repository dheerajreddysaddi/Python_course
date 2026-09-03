class Instagram:
    def __init__(self,username,pwd):
        self.username=username
        self.__pwd=pwd
        self._post=[]

    def getpwd(self):
        return self.__pwd

    def setpwd(self,newpwd):
        self.__pwd=newpwd

    @property
    def accesspost(self):
        return self._post
    
    @accesspost
    def accesspost(self,newpost):
       self._post=newpost

    def display(self):
        print(self.username,self.__pwd,self._post)

dheeraj=Instagram('dheeraj','d@1234')
dheeraj.display()
print(dheeraj.username)
print(dheeraj.getpwd())
print(dheeraj.accesspost)

dheeraj.username='reddy'
dheeraj.setpwd('@234')
dheeraj.accesspost='sunrise.png'
dheeraj.accesspost='beach.png'


print(dheeraj.username)
print(dheeraj.getpwd())
print(dheeraj.accesspost)








'''
class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"Hello {self.name}, Welcome to the flipkart")

dheeraj=Flipkart('dheeraj',8688665522)
sathvik=Flipkart('sathvik',9491866106)
'''