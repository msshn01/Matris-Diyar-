
class İşlemler:
    def __init__(self,matris1,matris2,a,b,c,d) -> None:
        self.matris1=matris1
        self.matris2=matris2
        self.a=a
        self.b=b
        self.c=c
        self.d=d

        
    
    
    def toplama(self):
        matristop = [[0 for i in range(self.a)] for i in range(self.b) ]
        
        for i in range(len(self.matris1)):
            for a in range(len(self.matris1[0])):
                matristop[i][a] = self.matris1[i][a] + self.matris2[i][a] 
        return matristop
    
    def çikarma(self):
        matrisçikar = [[0 for i in range(self.a)] for i in range(self.b) ]
        
        for i in range(len(self.matris1)):
            for a in range(len(self.matris1[0])):
                matrisçikar[i][a] = self.matris1[i][a] - self.matris2[i][a] 
        return matrisçikar

    def çarpma(self):
        matrisçarp = [[0 for i in range(self.a)] for i in range(self.b) ]
        
        for i in range(len(self.matris1)):
            for a in range(len(self.matris1[0])):
                matrisçarp[i][a] = self.matris1[i][a] * self.matris2[i][a] 
        return matrisçarp
    
    def bolme(self):
        matrisbolme = [[0 for i in range(self.a)] for i in range(self.b) ]
        
        for i in range(len(self.matris1)):
            for a in range(len(self.matris1[0])):
                matrisbolme[i][a] = self.matris1[i][a] / self.matris2[i][a] 
        return matrisbolme



while True:
    print("matris diyarına hoşgeldiniz \nYapmak istediğiniz işlemi giriniz")
    seçim = input("1-Toplama \n2-Çıkarma \n3-Çarpma \n4-Bölme \n5-Matris oluşturma \n6-ÇIKIŞ \nSeçiminiz: ")
    try:
        if seçim == "6":
        
            print("kayıtlı matris var ise silinecektir Çıkış Yapmak isteiğinize eminmisiniz!!!")
            emin = input("(e/h): ")
            if emin=="e":
                print("Matriste İşlemlerden çıkış yapılmıştır")
                break
            elif emin == "h":
                continue
            else :
                print("geçersiz cevap grilmiştir guvenlik sebebi ile matris silinmedi çıkış iptal edildi")

        else:
            if seçim == "1":
                işlemler = İşlemler(matris1=matris1,matris2=matris2,a=a,b=b,c=c,d=d)
                print(f"{matris1}+{matris2} ==> {işlemler.toplama()}")
            elif seçim == "2":
                işlemler = İşlemler(matris1=matris1,matris2=matris2,a=a,b=b,c=c,d=d)
                print(f"{matris1}-{matris2} ==> {işlemler.çikarma()}")
            elif seçim == "3":
                işlemler = İşlemler(matris1=matris1,matris2=matris2,a=a,b=b,c=c,d=d) 
                print(f"{matris1}*{matris2} ==> {işlemler.çarpma()}")
            elif seçim == "4":
                işlemler = İşlemler(matris1=matris1,matris2=matris2,a=a,b=b,c=c,d=d)
                print(f"{matris1}/{matris2} ==> {işlemler.bolme()}")
            elif seçim == "5":
                a = int(input("matris bir satır sayısı:"))
                b = int(input("matris bir sutun sayısı:"))
                c = int(input("matris iki satır sayısı:"))
                d = int(input("matris iki sutun sayısı:"))


                matris1=[[0 for i in range(b)] for k in range(a)]
                matris2=[[0 for i in range(d)] for k in range(c)]



                print("self.matris1 i giriniz")
                for z in range(a):
                    for w in range(b):
                        matris1[z][w] = int(input(f"matris 1 in {z} indxli {w} iç indexli sayısı: "))
                print("self.matris2 i giriniz")
                for z in range(c):
                    for w in range(d):
                        matris2[z][w] = int(input(f"matris 2 in {z} indxli {w} iç indexli sayısı: "))

            else:
                print("Yanlış işlem seçim değeri seçtiniz")
    except Exception:
        print("Önce birer matris tanımlayınız!!!!!!!!!!!")
        
        

    

    
    

