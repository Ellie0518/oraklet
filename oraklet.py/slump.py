import random

ditt_nummer = random.randint(1, 8)
datorns_nummer = random.randint(1, 8) 

namn = input("Vad heter du?")
gissa = input("Vad är din gissning?")

if ditt_nummer: int(ditt_nummer > datorns_nummer)
print("Rätt gissat!")

else datorns_nummer: int(datorns_nummer > ditt_nummer)
print("tyvärr datorn vann.")