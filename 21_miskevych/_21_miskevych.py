#21
import random 
print("Tere tulemast mängule 21, kui näitad vähem või rohkem kui 21")
koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)
arv = 0
while arv!=21:
    while True:
      choice = input("Kas võtad kaardi? jah/ei" )
      if choice == "jah":
            number = koloda.pop()
            print("Sul on kaardi number %d" %number)
      arv += number
      if arv > 21:
        print("Vabandust, aga sa kaotasid")
        break
      elif arv == 21:
        print("palju õnne, tabasite numbrit 21!")
        break
      else:
        print("Teil on %d punkti." %arv)
        if choice == "ei":
            print("Teil on %d punkti ja olete mängu lõpetanud." %arv)
            break
    
    
    
print("Aitäh mängimast!")
