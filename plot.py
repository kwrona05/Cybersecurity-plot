import matplotlib.pyplot as plt

categories = [
    "Phishing",
    "Wyłudzenia finansowe",
    "Ransomware",
    "Oszustwa internetowe",
    "Ataki na bankowość elektroniczną",
    "Inne cyberprzestępstwa"
]

percentages = [35, 25, 20, 10, 5, 5]

fig, ax = plt.subplots()
ax.pie(percentages, labels=categories, autopct= '%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)

ax.axis('equal')
plt.title("Procentowy udział cyberprzestępstw w Polsce w 2023 roku")

plt.show()