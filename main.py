lista_zakupów = {
     "warzywniak": ["Chleb", "Pączek", "Bułki"],
    "Piekarnia": ["Marchew", "Seler", "Rukola"]
}

for sklep, produkt in lista_zakupów.items():
    print(f"Idę do {sklep} i kupuję tam następujące rzeczy {str(produkt)}")
