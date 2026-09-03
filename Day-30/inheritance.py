'''class whatsappV1:
    def messaging(self):
        print('You can send messages')

class whatsappV2:
    def calls(self):
        print('You can do audio and video calls')

class whatsappV3(whatsappV2,whatsappV1):
    def status(self):
        print('24 hrs status update')

a=whatsappV1()
a.messaging()
#a.calls()
dheeraj=whatsappV2()
dheeraj.messaging()
dheeraj.calls()
c=whatsappV3()
c.messaging()
c.calls()
c.status()'''
#--------------- super method super().object ---------------------------------------------------
'''class whatsappV1:
    def status(self):
        print('You can share images and videos ')

class whatsappV2(whatsappV1):
    def status(self):
        super().status()
        print('You can share music and stickers')

class whatsappV3(whatsappV2):
    def status(self):
        super().status()
        print('you can like and react')

a=whatsappV3()
a.status()
'''
class whatsappV1:
    def status(self):
        print('You can share images and videos ')

class whatsappV2:
    def status(self):
        super().status()
        print('You can share music and stickers')

class whatsappV3(whatsappV1,whatsappV2):
    def status(self):
        whatsappV1.status(self)
        whatsappV2.status(self)
        print('you can like and react')

a=whatsappV3()
a.status()
