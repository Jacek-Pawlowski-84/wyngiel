import json
import time
from time import localtime, strftime
from urllib.request import Request, urlopen

koniec = time.time() + 65*60

plikLogiNazwa = "log\pgg_"+strftime("%Y%m%d_%H%M%S", localtime())+".txt"
txt = "\n"+"Zaczynamy: "+strftime("%d-%m-%Y %H:%M:%S", localtime())

plikLogi = open(plikLogiNazwa, "a")
plikLogi.write(txt+"\n")

print(txt)

while True:
 
    if time.time() >= koniec:
        print("\n\r"+"konczymy na dzis!"+"\n\r")
        plikLogi.write("\n\r"+"konczymy na dzis!"+"\n\r")
        plikLogi.close()
        break
    else:
        jestemFirefox = Request("https://sprawdzwegiel.pl/coal-stock.json", headers={'User-Agent': 'Mozilla/5.0'})
        plikOnline = urlopen(jestemFirefox).read()
        plikJSON = json.loads(plikOnline)

        dostGroszek = []
        dostGroszek = plikJSON["data"]

        sprawdzenie = 0
        print(strftime("\n"+"%d-%m-%Y %H:%M:%S", localtime()))
        plikLogi.write("\n"+strftime("%d-%m-%Y %H:%M:%S", localtime())+"\n")
        for i in dostGroszek:
            if i["stockStatus"] != False:
                sprawdzenie += 1
                nazwaGroszek = i["productName"]
                if "Paleta" in nazwaGroszek:
                    ciach = nazwaGroszek.find("\n")
                    txtStan = str(sprawdzenie)+". "+nazwaGroszek[:ciach]+", "+nazwaGroszek[ciach+1:]+" *****"
                    print(txtStan)
                    plikLogi.write(txtStan+"\n")
                else:
                    ciach = nazwaGroszek.find("\n")
                    txtStan = str(sprawdzenie)+". "+nazwaGroszek[:ciach]+", "+nazwaGroszek[ciach+1:]
                    print(txtStan)
                    plikLogi.write(txtStan+"\n")

        if sprawdzenie == 0:
            print ("Brak towaru!")
            plikLogi.write("Brak towaru!"+"\n")
        
        time.sleep(10)
