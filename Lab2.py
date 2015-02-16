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
    
    # ENKLE MATTEFUNKSJONER
    
    # Addisjon: Gjør om begge paramterene (romertall) til decimal. Utfører deretter addisjon og gjør om
    # svaret til romertall igjen

def additionRoman(x, y):
    a = fromRoman(x)
    b = fromRoman(y)
    
    c = a + b 
    d = toRoman(c)
    return d

    # Subtraksjon: Gjør om begge paramterene (romertall) til decimal. Utfører deretter subtraksjon og gjør om
    # svaret til romertall igjen
    
def subtractionRoman(x, y):
    a = fromRoman(x)
    b = fromRoman(y)
    
    c = a - b 
    d = toRoman(c)
    return d

    # Multiplikasjon: Gjør om begge paramterene (romertall) til decimal. Utfører deretter multiplikasjon og gjør om
    # svaret til romertall igjen

def multiplicationRoman(x, y):
    a = fromRoman(x)
    b = fromRoman(y)
    
    c = a * b 
    d = toRoman(c)
    return d
    
    # VANSKELIGE MATTEFUNKSJONER

def romanAddition(x, y):
    
    # Gjør om parameterene (x og y) til lange romertall    
    suby1 = y.replace("CM", "DCCCC")
    suby2 = suby1.replace("CD", "CCCC")
    suby3 = suby2.replace("XC", "LXXXX")
    suby4 = suby3.replace("XL", "XXXX")
    suby5 = suby4.replace("IX", "VIIII")
    suby6 = suby5.replace("IV", "IIII")
    
    subx1 = x.replace("CM", "DCCCC")
    subx2 = subx1.replace("CD", "CCCC")
    subx3 = subx2.replace("XC", "LXXXX")
    subx4 = subx3.replace("XL", "XXXX")
    subx5 = subx4.replace("IX", "VIIII")
    subx6 = subx5.replace("IV", "IIII")

    # resultat = string
    # legger sammen parameterene til en
    result = ""
    add = subx6 + suby6
    result += add

    # Sorterer med verdien høyest fra venstre til høyre
    valueOrder = "MDCLXVI"
    sortingList = sorted(result, key=valueOrder.index)
    

    
    str1 = ''.join(sortingList)
    
    # gjør om lange romertall til ordinære romertall
    tmp1 = str1.replace("IIIII", "V")
    tmp2 = tmp1.replace("VV", "X")
    tmp3 = tmp2.replace("XXXXX", "L")
    tmp4 = tmp3.replace("LL", "C")
    tmp5 = tmp4.replace("CCCCC", "D")
    tmp6 = tmp5.replace("DD", "M")
    
    tmp7 = tmp6.replace("VIIII", "IX")
    tmp8 = tmp7.replace("IIII", "IV")
    tmp9 = tmp8.replace("XXXX", "XL")
    tmp10 = tmp9.replace("LXXXX", "XC")
    tmp11 = tmp10.replace("CCCC", "CD")
    tmp12 = tmp11.replace("DCCCC", "CM")
    
    return tmp12
    
def romanSubtraction(x, y):
                   
    # Gjør om parameterene (x og y) til et lengre romertall
    suby1 = y.replace("CM", "DCCCC")
    suby2 = suby1.replace("CD", "CCCC")
    suby3 = suby2.replace("XC", "LXXXX")
    suby4 = suby3.replace("XL", "XXXX")
    suby5 = suby4.replace("IX", "VIIII")
    suby6 = suby5.replace("IV", "IIII")
    suby7 = suby6.replace("M", "DD")
    suby8 = suby7.replace("D", "CCCCC")
    suby9 = suby8.replace("C", "LL")
    suby10 = suby9.replace("L", "XXXXX")
    suby11 = suby10.replace("X", "VV")
    suby12 = suby11.replace("V", "IIIII")
    
    subx1 = x.replace("CM", "DCCCC")
    subx2 = subx1.replace("CD", "CCCC")
    subx3 = subx2.replace("XC", "LXXXX")
    subx4 = subx3.replace("XL", "XXXX")
    subx5 = subx4.replace("IX", "VIIII")
    subx6 = subx5.replace("IV", "IIII")
    subx7 = subx6.replace("M", "DD")
    subx8 = subx7.replace("D", "CCCCC")
    subx9 = subx8.replace("C", "LL")
    subx10 = subx9.replace("L", "XXXXX")
    subx11 = subx10.replace("X", "VV")
    subx12 = subx11.replace("V", "IIIII")
    
    # Legger hver bokstav i x og y i en liste
    charX = []
    for string in subx12:
        for char in string:
            charX.append(char)
                
    charY = []
    for string in suby12:
        for char in string:
            charY.append(char)
            
     # For hver bokstav i listene, fjern bokstav               
    for char in charX[:]:
        if char in charY:
            charX.remove(char)
            charY.remove(char)

    # Gjør om resultatet til string
    result = ""
    
    sub1 = ''.join(charX)
    sub2 = ''.join(charY)
    
    sub = sub1 + sub2
    result += sub
    
    # Sorterer listen i en rekkefølge hvor høyest verdi er fra venstre mot høyre
    valueOrder = "MDCLXVI"
    sortingList = sorted(result, key=valueOrder.index)
    

    
    str1 = ''.join(sortingList)
    
    # Gjør om lange romertall til "vanlig"/ordinær romertall
    tmp1 = str1.replace("IIIII", "V")
    tmp2 = tmp1.replace("VV", "X")
    tmp3 = tmp2.replace("XXXXX", "L")
    tmp4 = tmp3.replace("LL", "C")
    tmp5 = tmp4.replace("CCCCC", "D")
    tmp6 = tmp5.replace("DD", "M")
    
    tmp7 = tmp6.replace("VIIII", "IX")
    tmp8 = tmp7.replace("IIII", "IV")
    tmp9 = tmp8.replace("LXXXX", "XC")
    tmp10 = tmp9.replace("XXXX", "XL")
    tmp11 = tmp10.replace("DCCCC", "CM")
    tmp12 = tmp11.replace("CCCC", "CD")
    
    return tmp12
