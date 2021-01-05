import matplotlib.pyplot as plt
plt.title("Macronutrients Consumed")
plt.ylabel("Nutrients (G)")
plt.xlabel("Macronutrient")
macros = ['Protein', 'Carbohydrates', 'Fats']
grams = [30,15,10]
plt.bar(macros,grams)
plt.show()