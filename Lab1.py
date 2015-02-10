# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Andreas Kjærner-Semb', 
            'student2': 'Linda Tran', \
            'student3': 'Frank William Hansen', \
            'student4': 'Ole Aarsnes', \
            'student5': 'Mikael Kile', \
            'student6': 'Lasse Johnsen', \
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_fugl():
    print"#       \/"
    print"#       \/_"
    print"#  \,   /( ,/"
    print"#   \\\\\\' ///"
    print"#    \_ /_/"
    print"#    (./"
    print"#     '`"

ascii_fugl()

# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre


# Hva gjør den? Den ser på binærtallene (110 osv) og
# sammenlikner om de har en binær-plassering hvor begge har 1.
# Derfor får vi 4 av (6, 5) fordi 2-tallsystemversjonen av 6 og 5 har
# begge 1 på tredje plass, eller 1 * 2 ^ 2 = 4
def bitAnd(x, y):
	i = (x & y)
    	print i
    
bitAnd(5, 3)


#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#

# Hva gjør den? Sammenlikner for å se om binærtallene
# der kun en av de har 1 på en plassering mens den andre har 0.
# Derfor blir (4, 5) = 1 fordi 4 = 100 og 5 = 101, dermed ser vi at
# det kun er 101 (5) som har et ettall på den første plassen (høyre).
def bitXor(x, y):
	i = x ^ y
	print i

bitXor(4, 5)


#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1


# Hva gjør den? Den ser om en ELLER begge binærtallene har
# 1 på en av plasseringene, og vi får et 1-tall på tilsvarende 
# plassering HVIS en av de har 1. Hvis begge tallene har 0 på en 
# plassering får vi 0. Derfor blir (0, 1) = 1 fordi mens 0 har 0 på 
# første plassen, har 1 tilsvarende 1 på første plassen.
def bitOr(x, y):
	i = x | y
	print i

bitOr(0, 1)


#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110

# obs viktig å huske den lille b'en etter 8, for binært.
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#

#    Svar: Resultatet med 'å' er at den sender tilbakemelding om å ha 
#          funnet en string med 2 bokstaver i lengde, og ikke 1.
#          Hvorfor gjør den det? Det er fordi ascii 8 bin vil si at den 
#          bruker 8 binærtall, med andre ord er 128 det høyeste tallet 
#          man får i en bit. Dermed blir Å som er nummer 143 satt sammen
#          av 2 bits, og derfor tolker den det som 'string of 2'
def ascii8Bin(letter):
	i = ord(letter)
    	print '{0:08b}'.format(i)	#.format formaterer tallet
	
ascii8Bin('A')


# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
#
# Tar en string som argument. Lager en liste av string, collection med
# variabelen l. Deretter kjører den en for loop som gjør noe med
# hvert objekt c i liste l. For hver c (bokstav) i list l (ordet).
# Ordet er selve listen, første bokstav på [0] osv.
# Deretter kjører den metoden ascii8Bin på det objektet c som er hentet
# fra listen nå.
def transferBin(string):
	print "Den binære representasjonen for %r" % string
	l = list(string)
	for c in l:
		ascii8Bin(c)	# variabelen c viser til en bokstav.
		

#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  

def ascii2Hex(letter):
	i = ord(letter)
	# gjør om integeren i variabelen i til hexadesimal med 2 tegn. A blir for
	# eksempel 0x41. %x konverterer det til hexadesimal. Man kan også bruke
	# hex(tall). 02 betyr at den legger på nullere om det trengs, og at den skriver
	# det ut med minst 2 tegn. Konverteringen fungerer slik at man tar et
	# hexadesimalt tegn, xFF for eksempel, og ganger. F tilsvarer 15 i titallssystemet.
	# (15*16^1) + (15*16^0) = 15*16 + 15*1 = 240 + 15 = 255.
	print '0x%02X' % i


def transferHex(string):
	print "Den heksadesimale representasjonen for %s" % string
	l = list(string)
	for c in l:
		ascii2Hex(c)

transferHex('hei')

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
# 
# kjører bytearray-metoden på parameter, for å hente hvilke bits som representerer tegnet,
# for eksempel /xe5/xa4. Deretter sjekkes det om tegnet faktisk er representert med flere
# enn en bit. Hvis så er tilfelle henter den ut hver representasjon av tegnet i array
# og konverterer det til binærtall med "{0:08b} ".format(char). Tallene kommer på samme linje
# og den setter et mellomrom til neste bit.
#
#
def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(unicode_char)
    
    return outstr

unicodeBin('å')
	

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
# Psutil sjekker ikke hardware på den måten at den viser slikt som RAM eller modell
# eller operativsystem. Den viser prosesser som kjører og systemforbruk/bruk på
# datamaskinen der og da.
#
def printSysInfo():
	# printer ut cpu-bruken i prosent
	psutil.cpu_percent(interval=3)
	# printer ut antall cpu'er, inklusive virtuelle.
	psutil.cpu_count()
	psutil.disk_usage('/')

# man kan bruke "sudo lshw -short" i GNU/Linux, eller "free -m" for å se RAM-bruk
# eller inxi for å få opp en oversiktlig oversikt.


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
#print test()
		
