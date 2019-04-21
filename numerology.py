# Numerology:

def sum_digits(n):
    num = 0
    while n:
        n, digit = divmod(n, 10)
        num += digit
    return num
	
print (" Input your complete date of birth (without spaces): ")	
n = int(input())

while n > 9:
    n = sum_digits(n)
	
print(" Your Life path number is",n)

if n ==  1:
   print(" You are a determined leader in the truest sense")
elif n == 2:
   print(" You are very sensitive and diplomatic")
elif n == 3:
   print(" You have a highly-developed creative talent and are a natural-born artist")
elif n == 4:
   print(" You're every employer's dream: a hard working, detail-oriented individual with high principles")
elif n == 5:
   print(" You are highly adaptable and communicative")
elif n == 6:
   print(" You're a generous family person, a a kind soul with a strong skill in keeping the peace")
elif n == 7:
   print(" Your mind is your greatest asset")
elif n == 8:
   print(" You are efficient, realistic and confident in your skills")
elif n == 9:
   print(" You are charming and well-liked by others")
