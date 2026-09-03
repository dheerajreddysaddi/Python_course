'''full name validation
import re
fullname=input('enter the name')
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("valid full name"if res else "Invalid full name")'''

''' email validation
import re
mail=input('enter the mail')
pattern=r"^[A-Za-z0-9._]+@[A-Za-z0-9._]+\.[a-zA-Z]{2,}$"
res=re.fullmatch(pattern,mail)
print("valid mail"if res else "Invalid mail")'''

'''phone number validation
import re
phno=input('enter the mobile number')
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
res=re.fullmatch(pattern,phno)
print("valid mobile number" if res else "Invalid mobile number")'''

'''password validation
import re
pwd=input('enter the password')
pattern=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res=re.fullmatch(pattern,pwd)
print("valid password"if res else "Invalid password")'''

import re
username=input('enter the username')
aadhaar=(input('enter the aadhaar number'))
pan=input('enter the pan card')
pattern1=r'^[A-Za-z0-9._]{6,}$'
pattern2=r'^[0-9]{12}$'
pattern3=r'^[A-Z]{5}+[0-9]{4}+[A-Z]{1}$'
res=re.fullmatch(pattern1,username)
res2=re.fullmatch(pattern2,aadhaar)
res3=re.fullmatch(pattern3,pan)
print("valid username"if res else "Invalid username")
print("valid aadhaar"if res2 else "Invalid aadhaar")
print("valid pan"if res3 else "Invalid pan")

