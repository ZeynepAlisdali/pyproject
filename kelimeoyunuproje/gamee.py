import time
import random
#buraya Türkçe karakterler için header gelecek onu yapamadım
print("EKRANDA GÖRECEĞİNİZ HARFLERİN TAMAMINI KULLANARAK 20 SANİYEDE ANLAMLI BİR KELİME OLUŞTURMAYA ÇALIŞIN.\n"
      "NE KADAR HIZLI CEVAP VERİLİRSE O KADAR YÜKSEK PUAN ALINIR.\n"
      "DOĞRU CEVAPLAR 20 SANİYE İÇİNDE VERİLMEZSE PUAN ALINMAZ.\n"
      "YANLIŞ CEVAPLAR 20 SANİYE İÇİNDE VERİLMİŞSE 5, VERİLMEMİŞSE 10 PUAN KAYBEDİLİR")
score=0
sayac=20
oyuncu_sayisi=5 #dummy??
en_yuksek=0
birinci=0

kelimeler=["engerek","damacana","potansiyel","battaniye","kitaplık","meşrutiyet","teşekkür","afiyet",
           "teknoloji","malzeme","proje","bildiri","klasör","fazlalık","kırtasiye","ofis","heyet",
           "muhakeme","idrak","derslik","iktidar"]

baslama_secimi=input("OYUNA BAŞLAMAK İÇİN B TUŞUNA BASIN")
if(baslama_secimi=="b" or "B"):

    while(oyuncu_sayisi>4):           #oyuncu sayısı yanlış girilirse tekrar girilme hakkı olması için döngü kullanıldı
        oyuncu_sayisi=int(input("Oyuncu sayisini girin (En fazla 4 oyuncu olabilir)"))
    oyuncular=[]

    for i in range(oyuncu_sayisi):
        for j in range(5):
            kelime= random.choice(kelimeler) #kelimeler kümesinden rastgele eleman seçildi
            kelime_harf = list(''.join(kelime)) #seçilen elemanı oluşturan karakterler ayrı bir listeye atandı
            kelimeler.remove(kelime)  # oyun içinde aynı elemanın birden fazla seçilmemesi için seçilen eleman silinir
            print(random.sample(kelime_harf,len(kelime_harf)))


            start_time=time.time() #sayımın başladığı zaman start_time değişkenine atandı

            tahmin = input("tahmini giriniz")
            finish_time=time.time()

            if(tahmin==kelime or tahmin==kelime.upper()):#caps lock açıkken yazılırsa hata vermemesi için
                if(finish_time-start_time>20):
                    print("Süre aşımı!")
                else:
                    score+=int(20-(finish_time-start_time)) #şu anki zamandan start_time çıkarılıp tahminin kaç
                    # saniyede yapıldığı bulundu, 20'den çıkarılıp alınacak skor belirlendi
            else:
                if(finish_time-start_time>20):
                    print("Yanlış tahmin ve süre aşımı!")
                    score-=10
                else:
                    print("Yanlış tahmin!")
                    score-=5
        oyuncular.append(score)
        if not i==oyuncu_sayisi-1:   #son oyuncudan sonra input beklememesi için
            next=input("Sıradaki oyuncu ile devam etmek için herhangi bir tuşa basın.")

    #skor karşılaştırma
    print("SKORLAR BÜYÜKTEN KÜÇÜĞE")
    for i in range(oyuncu_sayisi):
        en_yuksek=max(oyuncular)
        birinci=oyuncular.index(en_yuksek)
        score_list=[birinci+1,en_yuksek]
        oyuncular.remove(en_yuksek)
        print(score_list)


else:
    print("OYUNA BAŞLAMAK İSTİYORSANIZ B TUŞUNA BASIN")