
#String data type and it's functions

text='welcome to python coding'
print(text,text)

#Some built in functions in String
#print(text.capitalize())
#print(text.upper())
#print(text.lower())
#print(text.title())
#print(len(text))
#print(text.count('n'))

#slicing
print(text[-3]) #we can give index in negative numbers to show the value from right (i) in this text
print(text[11:]) #limitation of words in the string to show /print
print(text[11:18]) #limit to get the exact word/letter in String

#Extracting the text like this index form
text1=text[18]+' '+text[:8]+text[25:29]+' '+text[8:11]+' '+text[13:14]+text[12:13]+text[1:2]+text[8:9]
print(text1.title())
print(text1[::-1].title())#reverse the string letters 
