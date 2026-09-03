class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phno,address):
        self.name=name
        self.phno=phno
        self.address=address
        print(f'Hello {name} ,welcome to flipkart')

    @staticmethod
    def displaydiscount():
        print(f'{Flipkart.discount}% is going on,grab the products...')

dheeraj=Flipkart()
dheeraj.userinfo('dheeraj',86888665522,'NZB')
dheeraj.displaydiscount()
dheeraj.display()

sathvik=Flipkart()
sathvik.userinfo('sathvik',9491866106,'Nirmal')
sathvik.displaydiscount()
sathvik.display()