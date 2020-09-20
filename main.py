lista_zakupów = {
     "warzywniak": ["Chleb", "Pączek", "Bułki"],
    "Piekarnia": ["Marchew", "Seler", "Rukola"]
}
count = 0
for sklep, produkt in lista_zakupów.items():
    print(f"Idę do {sklep.upper()} i kupuję tam następujące rzeczy {str(produkt).upper()}")
    for item in produkt:
        count = count + 1
print(f"W sumie kupuję {count} produktów")
print ("Second commit")