weather = ["sunny", "rainy", "cold"] # Available weather suggestions

weather = input("What's the weather like today? (sunny/rainy/cold): ").lower() #prompts the user for their input on the current weather condition

#match user input with the variables and give recommendations
if weather == "sunny":
 print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
 print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
 print("Make sure to wear a warm coat and a scarf.")

else: 
 print("Sorry, I don't have recommendation for this weather")