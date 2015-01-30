# -*- coding: utf-8 -*-

# Roman Numerals
romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def toRoman(n):
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NorIntegerError("decimals can not be converted")
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1..4999)")
        
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

# Metoden forklart: Hvis man for eksempel skriver inn input 894, så går
# for-løkken gjennom "listen"(?) og henter ut både numeral(romertegn) og integer(desimaltall).
# Inne i for-løkken kjøres så en while-løkke som først sammenlikner n (input) med integer (tall i listen),
# og ser om n er større eller lik integer.
# Med 894 som eksempel tar den da og ser at tallet er mindre enn første i listen, nemlig 1000 for M.
# Dermed kjøres løkken med en gang om igjen, og den sammenligner så med neste, som er 900. Igjen er n mindre,
# så derfor går den på nytt videre og ser om neste er lik eller mindre.
# Da finner den 500 eller D, som jo ER mindre enn n (894).
# Dermed kjøres while-løkken og numeral(romertall) legges inn i (og plusses) variabelen result,
# slik at result så langt har D for 500.
# Deretter trekkes 500 fra n, (n -= integer) og n har nå tallet 394. Videre ser vi at det er lavere enn 400 for CD.
# Deretter ser man at den vil gå 3 ganger gjennom while-løkken siden 394 har 3 "hundrere".
# Så plusses de på i result, som da blir DCCC.
# Nå har n bare 94, og ved neste runde blir det 4 da 94 er større enn 90 for XC.
# Da har result romertallet DCCCXC.
# Til slutt hopper den over en haug med tall til den kommer til 4 for IV, og dermed har den "tømt" n for tall
# som nå kun står igjen med 0, og 0 har ingen verdi i romertall.
# Dermed inneholder result nå DCCCXCIV. result = "" over gjør at den returnerer en string.
