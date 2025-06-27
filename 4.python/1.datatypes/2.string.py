str = "Hello, World!"
str2= "Welcome to sesac class"
print(str)

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str2.title())
print(str2.strip()) #앞 뒤 불필요한 공백 제거cd
print(str2.lstrip()) #앞 뒤 불필요한 공백 제거cd
print(str2.rstrip()) #앞 뒤 불필요한 공백 제거cd
print(str2.split()) #앞 뒤 불필요한 공백 제거cd


words = str2.split()
print(words[0])
print(",".join(words))