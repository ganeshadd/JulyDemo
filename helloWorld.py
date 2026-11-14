# Introduction to Python
# print("Hi Guys")
# print("Welcome to GenAI and Agentic Ai Training")

# Variables 
text = 25
text2 = 65

text3 = "You guys are amazing"
# print("The addtion of text and text2 is  :", (text + text2))


# Functions 
def substraction(text,text2):
    result = text2-text
    #print(result)
    return result

# Functions 2
def Addition(text,text2):
    result = text2 + text
    #print(result)
    return result

#sub = substraction(text,text2)

#add =Addition(text2,text)
#print(sub)
#print(add)

#List & dictionaries 

mylist1 =[10,20,30,40,50]
mylist2 =["ganesh","Hemant","Ravi","Sunil","Sunil","Sunil"]
mylist =[1,"hello",3.5,True]

#print(mylist) #entire list
#print(mylist[1]) #Posional value

#print(mylist1)
mylist1.append(60)
mylist1.remove(30)

# print(mylist1)

dict1=[
    {
    "name":"Ganesh",
    "Age":30,
    "City":"Bangalore"
},
{
    "name":"Ramesh",
    "Age":28,
    "City":"Hyderabad"
}
]

#print(dict1["name"])

#dict1["Age"] = 36        #Update
#dict1["Country"]="India" #add
#del dict1["City"]        #delete

#print(dict1)

#Condition 
Age1 =14
if Age1>18:
    print("You can get a DL")
else:
    print("You are yet to grow up to get a DL")    


#loops

for person in dict1:
    print("Name:" ,person["name"])


# Variable
# Functions
# lists and Dictionaries
# Condition
# loops 
# File handling 