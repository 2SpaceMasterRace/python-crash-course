# Write your solution here

temp = int(input("What is the weather forecast for tomorrow?"))
rain = input("Will it rain (yes/no):")

if temp > 20:
        print("Wear jeans and a T-shirt")
    
if temp <= 20:
        print("Wear jeans and a T-shirt")
        if rain == "no":
             print("I reccomend a jumper as well")
        if temp <= 10:
            if rain == "no":
                print("Take a jacket with you")
if temp <= 5:
            print("Wear jeans and a T-shirt")
            print("I reccomend a jumper as well")
            if rain == "yes":
                print("Take a jacket with you")
                print("Make it a warm coat, actually") 
                print("I think gloves are in order") 
                print("Don't forget your umbrella!") 
