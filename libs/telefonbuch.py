import json

def telefonbuch_lesen():
    data = {}
    try:
        with open('telefonbuch.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

def eintrag_speichern(name, telefon_nummer):
    telefonbuch = telefonbuch_lesen()
    telefonbuch[name] = {"name": name, "telefon": telefon_nummer}   
    print(telefonbuch)
    with open('telefonbuch.txt', "w", encoding="utf-8") as open_file:
        json.dump(telefonbuch, open_file)

    


    

