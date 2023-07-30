import random
from guess import Guess

guess = Guess()

guess.jawaban = random.randint(1, 10)

guess.tebakan = int(input('tebak dari angka 1 - 10 : '))

if guess.cek () :
        print ("benar")

else :
        print ("salah")
