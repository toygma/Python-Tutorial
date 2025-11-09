# # ============================================================================
# # FILE: 02_string_operations.py
# """
# STRING OPERATIONS
# =================

# Strings are sequences of characters. Python provides many methods and operations
# to manipulate strings.

# Key Concepts:
# - String indexing and slicing
# - String methods
# - String concatenation
# - String formatting
# """

# # String creation
# text = "Python Programming"
# single_quote = 'Hello'
# double_quote = "World"

# # String indexing (starts at 0)
# print("String Indexing:")
# print(f"First character: {text[0]}")  # P
# print(f"Last character: {text[-1]}")  # g
# print(f"Third character: {text[2]}")  # t

# # String slicing [start:end:step]
# print("\nString Slicing:")
# print(f"First 6 characters: {text[0:6]}")  # Python
# print(f"From index 7 to end: {text[7:]}")  # Programming
# print(f"Last 4 characters: {text[-4:]}")  # ming
# print(f"Every 2nd character: {text[::2]}")  # Pto rgamn

# # String methods
# print("\nString Methods:")
# print(f"Uppercase: {text.upper()}")
# print(f"Lowercase: {text.lower()}")
# print(f"Title case: {text.title()}")
# print(f"Replace: {text.replace('Python', 'Java')}")

# sample = "  hello world  "
# print(f"Strip whitespace: '{sample.strip()}'")
# print(f"Split: {text.split()}")

# # String checking methods
# print("\nString Checking:")
# print(f"Starts with 'Python': {text.startswith('Python')}")
# print(f"Ends with 'ing': {text.endswith('ing')}")
# print(f"Contains 'gram': {'gram' in text}")
# print(f"Is alphanumeric: {text.isalnum()}")
# print(f"Is alphabetic: {text.isalpha()}")

# # String concatenation
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print(f"\nConcatenation: {full_name}")

# # String formatting
# age = 25
# # f-strings (modern way)
# message1 = f"My name is {full_name} and I am {age} years old"
# # format() method
# message2 = "My name is {} and I am {} years old".format(full_name, age)
# # % formatting (old way)
# message3 = "My name is %s and I am %d years old" % (full_name, age)

# print("\nString Formatting:")
# print(message1)
# print(message2)
# print(message3)

# # String length
# print(f"\nLength of text: {len(text)}")

# # Character counting
# print(f"Count of 'a': {text.count('a')}")
# print(f"Index of 'Programming': {text.find('Programming')}")

# Practice Exercises:
print("\n--- EXERCISES ---")
print("1. Create a string with your full name")
print("2. Print the first letter, last letter, and middle letters")
print("3. Convert your name to uppercase and lowercase")
print("4. Count how many vowels are in your name")


#--------------- EXERCISES ------------------------

# 🧩 Soru 1: Karma İndeksleme ve Tersleme

# Bir değişkende tam adın "Ad Soyad" şeklinde tutuluyor.
# Aşağıdaki koşulları tek satırda sağlayan bir string ifadesi yaz:

# İlk harfi büyük harfle başlasın.

# Tüm harfler küçük olsun, sadece soyad tersten yazılsın.

# Arada sadece bir boşluk bulunsun.
# Örnek: "Ali Vural" → "Ali laruv"

# s = "Ali Vural"
# print(s.split()[0].capitalize() + " " + s.split()[1].lower()[::-1])

# 🧩 Soru 2: Orta Harflerin Palindrom Kontrolü

# Bir isim al (örneğin "Zeynep") ve sadece ilk ve son harf hariç kısmın ("eyne") palindrom (tersi kendine eşit) olup olmadığını kontrol et.
# Bu kontrolü case-insensitive (büyük/küçük fark etmeden) yap.
# Palindromsa "Orta harfler palindrom", değilse "Değil" yaz.

# s = "Zeynep"
# middle = s[1:-1].lower() 
# if middle == middle[::-1]:
#     print("Orta harfler palindrom")
# else:
#     print("Değil")



# 🧩 Soru 3: Vowel Index Pattern

# Bir isimdeki tüm sesli harflerin (a, e, i, o, u, ı, ö, ü) dizin (index) numaralarını bulan bir Python kodu yaz.
# Ancak:

# Dizinler ters sırayla listelensin.

# İsimde tekrarlanan sesliler varsa, sadece ilk geçtiği index alınsın.

# Çıktı bir tuple (demet) olsun.

# s = "Mustafa"
# vowels = "aeiouıöüAEIOUİÖÜ"
# indexes = []

# for i, ch in enumerate(s):
#     if ch in vowels and i not in indexes:
#         indexes.append(i)

# result = tuple(indexes[::-1])
# print(result)



# 🧩 Soru 4: ASCII Fark Testi

# Adının karakterlerinin ASCII değerlerini kullanarak şunu yap:

# Her komşu karakterin ASCII farkını al (örneğin "Ali" → |A-l|, |l-i|).

# Bu farkların ortalamasını hesapla.
# Sonuç 10’dan küçükse, "Karakterler birbirine benzer", değilse "Farklı karakter yapısı" yazdır.


# s = "Ali"
# diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
# avg_diff = sum(diffs) / len(diffs)

# if avg_diff < 10:
#     print("Karakterler birbirine benzer")
# else:
#     print("Farklı karakter yapısı")




# 🧩 Soru 5: Şifreleme Challenge

# Adını şu kurallarla “şifreleyen” bir Python ifadesi yaz:

# Her harfi 2 karakter ileri taşı (a→c, b→d, y→a, z→b döngüsel şekilde).

# Sesli harfler büyük harfe, sessizler küçük harfe dönüşsün.

# Boşluk karakteri "_" ile değiştirilsin.

# Çıktı tek bir string olsun.

# Örnek: "Ali Can" → "Cnk_Ecp"

# s = "Ali Can"
# vowels = "aeiouıöüAEIOUİÖÜ"
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# encrypted = ""
# s = "Ali Can"
# vowels = "aeiouıöüAEIOUİÖÜ"
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# encrypted = ""

# for ch in s:
#     if ch == " ":
#         encrypted += "_"
#     elif ch.isalpha():  
#         idx = alphabet.index(ch.lower())
#         print(idx)
#         new_char = alphabet[(idx + 2) % 26]
#         if new_char in vowels.lower():
#             encrypted += new_char.upper()
#         else:
#             encrypted += new_char.lower()
#     else:
#         encrypted += ch

# print(encrypted)



# s = "Bora Can"
# vowels = "aeiouıöüAEIOUİÖÜ"
# encrypted = ""
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in s:
#     if char == " ":
#         encrypted += "_"
#     elif char.isalpha():
#         idx = alphabet.index(char.lower())
#         new_char = alphabet[(idx + 3) % 26 ]
#         if new_char in vowels.lower():
#             encrypted += new_char.upper()
#         else:
#             encrypted += new_char.lower()
#     else:
#         encrypted += char



# 🧩 Zor Soru: Palindrome Alt Diziler

# Görev:

# Bir string al (s = "ababa" gibi).

# Stringi küçük harfe çevir ve boşlukları kaldır.

# Stringin içindeki tüm ardışık palindrom alt dizileri bulun.

# Bir karakter de palindrom sayılır.

# Örnek: "aba" → palindrom

# Tüm farklı palindromları bir listeye ekle (tekrarlayanları ekleme).

# Listeyi ekrana yazdır.

# s = "ababa".lower() 

# palindromes = set()  
# for i in range(len(s)):
#     for j in range(i+1, len(s)+1):
#         substring = s[i:j]
#         if substring == substring[::-1]:
#             palindromes.add(substring)

# print(sorted(palindromes))
