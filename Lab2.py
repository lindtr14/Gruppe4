# -*- coding: utf-8 -*-

# laster inn regular expressions-modul
import re

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

"""Metoden forklart: Ved input går for-løkken gjennom ordboka og
henter ut numeral (romertegn) og integer (desimaltall).

I for-løkken kjøres så en while-løkke som først sammenlikner n (input) med integer (tall i ordboka),
# og ser om n er større eller lik integer.
# Med 894 som eksempel tar den da og ser at tallet ikke er større eller lik første i listen, nemlig 1000 for M.
# Dermed kjøres løkken med en gang om igjen, og den sammenligner så med neste, som er 900. Igjen er n mindre,
# så derfor går den på nytt videre og ser om neste er lik eller mindre.
# Da finner den 500 eller D, som jo ER mindre enn n (894).
# Dermed kjøres while-løkken og numeral(romertall) legges til variabelen result,
# slik at result så langt har D for 500.
# Deretter trekkes 500 fra n, (n -= integer) og n har nå tallet 394. Videre ser vi at det er lavere enn 400 for CD.
# Deretter ser man at den vil gå 3 ganger gjennom while-løkken siden 394 har 3 "hundrere".
# Så plusses de på i result, som da blir DCCC.
# Nå har n bare 94, og ved neste runde blir det 4 da 94 er større enn 90 for XC.
# Da har result romertallet DCCCXC.
# Til slutt hopper den over en haug med tall til den kommer til 4 for IV, og dermed har den "tømt" n for tall
# som nå kun står igjen med 0, og 0 har ingen verdi i romertall.
# Dermed inneholder result nå DCCCXCIV. result = "" over gjør at den returnerer en string"""

# Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string                                
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)
    
# re.VERBOSE er et såkalt 'Flag' i metoden som gjør at man kan skrive
# inn ting i metodekallet mer oversiktlig, slikt som kommentarer, samt
# at den ignorerer whitespaces.

def fromRoman(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s

""" For-løkken går gjennom hvert nøkkel-verdipar med romertall og desimalverdier.
Index = 0, og While-løkken bruker derfor slice fra venstre til høyre og deler
stringen 's' opp i biter som passer til nøklene (romertallene) og legger de
tilsvarende verdiene (desimaltall) til result. Avhengig av lengden til numeral, vokser index
med 1 eller 2 for hver gang while-løkken kjører, og programmet tar dermed for seg romertallet
bit for bit til hele tallet er lest. Når s[index:index+len(numeral)] ikke lengre tilsvarer en numeral (nøkkel)
er while-løkken ferdig og result viser verdien i desimaltall."""


result = 0
index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
