""" Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """
a = "merhaba dünya"
print(len(a))

"""Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""
a = input("bir metin giriniz: ")
print(a[:2] + a[-2:])

"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen
 metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

metin = input("bir metin giriniz: ")
eskiharf = input("metinde değişecek seçiniz: ")
yeniharf =input("metine eklenecek harfi seçiniz: ")
print(metin.replace(eskiharf,yeniharf))



"""Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

def isPalindrome(s):
	
	rev = ''.join(reversed(s))

	# Checking if both string are
	# equal or not
	if (s == rev):
		return True
	return False

# main function
a = input("bir string giriniz: ")
print(isPalindrome(a))

"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz. """
x = input("bir input giriniz: ")
x = x[-2:] *4
print(x)

""" 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız. """
a = [1,2,3,4,5]

a[1] = a[1]*100
print(a)

"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + (liste2)
print(liste3)

liste1.append(liste2)
liste3 = liste1
print(liste3)

liste1.extend(liste2)
liste3 = liste1
print(liste3)

"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """

liste = [1,2,3,4,5,6]
liste.insert(0, "Elma")
print(liste)

"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
removeThreeItem = liste[3:]
print(removeThreeItem)

""" liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız. Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı """

liste1 = ["1",1,2,"3"]
liste2 = liste1.copy()
liste2.append(250)
print("Liste1: " , liste1)
print("Liste2: " , liste2)

"""

Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
 dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60} Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """

dict1={1:10, 2:20} 
dict2={3:30, 4:40} 
dict3={5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız Beklenen Çıktı :(6,60) """
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x = sozluk.popitem()
print(x)

"""dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """

dict1={1:10, 2:20}
dict1[3] = 30
print(dict1)

"""liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun b.sözlüğün her 
elamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. 
Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50} """

liste=[1,2,3,4,5]
dictionary = {k:k*10 for  k in liste}

 
print(dictionary)


"""sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

"""

sozluk={1:10,2:20,3:30,4:40,5:50}

x = sozluk.setdefault(6,60)
print(sozluk)

"""Seven segment sorusu"""

representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),
}

def seven_segment(number):
    # treat the number as a string, since that makes it easier to deal with
    # on a digit-by-digit basis
    digits = [representations[digit] for digit in str(number)]
    # now digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc.
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))
seven_segment(0)




""" Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted = {x: sorted(y) for x,y in num.items()}
print(sorted)

"""sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """
sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
#yapılmadı

""" liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? """

liste1=[1,2,3]
liste2=[4,5,6,7,8]
liste1.extend(liste2)
liste3 = liste1
print(liste3)

"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?"""
liste=[1,2,3,4,5,6]
del liste[0]
print(liste)

""" liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz? """
liste=["elma" , "armut", "çilek"]
liste.append(3)
print(liste)

"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""


"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

liste = [1,2,3,4,5,6,7,8,9,10]
max1 = (max(liste))
liste.remove(max1)
max2 = max(liste)
liste.remove(max2)
max3 = max(liste)
print(max1 , max2, max3)

"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

string = "FuRkAn"
lower = []
upper = []

for i in string:
    if(i == i.lower()):
        lower.append(i)
    elif(i == i.upper()):
        upper.append(i)
print(lower)
print(upper)

"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

list1 = [10, 21, 4, 45, 66, 93, 11,88,102,5]

even_count, odd_count = 0, 0
num = 0


while(num < len(list1)):
	

	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	
	
	num += 1
	
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


