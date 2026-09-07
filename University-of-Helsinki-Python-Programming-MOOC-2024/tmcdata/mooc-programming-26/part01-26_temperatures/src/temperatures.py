# Write your solution here

temperature_fahrenheit = int(input("Please type in a temperature (F):"))
temperature_celsius = 	(temperature_fahrenheit - 32) / (9/5)

print(f"{temperature_fahrenheit} degrees Fahrenheit equals {temperature_celsius} degrees Celsius")

if temperature_celsius < 0:
    print("Brr! It's cold in here!")