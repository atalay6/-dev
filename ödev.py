sozluk = {
    
    "nebula" : "bulutsu",
    "güneş" : "yildiz",
    
    
    
    
    }
        
kelime = input().lower()
if kelime in sozluk.keys():
    print(sozluk[kelime])
else:
    print("yok gardaş")
