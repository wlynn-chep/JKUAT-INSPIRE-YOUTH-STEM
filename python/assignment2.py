temperature = int (input ("enter temperature :"))
if temperature > 30:
    print("its too hot! Stay hydrated.")
elif 20 <= temperature <= 30:
    print("The weather is pleasant.")
elif 10 <= temperature <= 19:
    print("its a bit chilly. Wear a sweater.")
else:
    print("its very cold! Wear a jacket.")
