# SP_Programowanie_komputerow_lab_PP_4
Studia podyplomowe Podstawy programowania - Python, Wydział Informatyki, ZUT w Szczecinie - Laboratorium 4

Zadanie	1:
Napisz	program,	który	usunie	z	pewnej	listy	wszystkie	powtórzenia	jej	elementów.	Np.	
jeśli	w	programie	dana	jest	następująca	lista:
[2,	6,	7,	1,	34,	64,	2,	7,	35,	1]
to	po	wykonaniu	Twojego	programu	powinna	prezentować	się	następująco:
[2,	6,	7,	1,	34,	64,	35]

Zadanie	2:	
Napisz	 program,	 który	 odwraca	 kolejność	 elementów	 listy,	 jednak	 bez	 użycia	 funkcji	
reversed().	Np.	jeśli	w	programie	dana	jest	następująca	lista:
[2,	6,	7,	1,	34,	64,	2,	7,	35,	1]
to	po	wykonaniu	Twojego	programu powinna	prezentować	się	następująco:
[1,	35,	7,	2,	64,	34,	1,	7,	6,	2]

Zadanie	3:	
Napisz	 program,	 który	 analizuje	 zawartość	 dwóch	 list	 i	 buduje	 trzecią	 listę	 z	 takich	
elementów	pierwszej	listy,	które	nie	występują	w	drugiej	i	z	 takich	elementów	drugiej	
listy,	które	nie	występują	w	pierwszej. Wartości	do	obu	list	można	wpisać	w	programie	
na	stałe	albo	pobrać	od	użytkownika.

Zadanie	4:	
Napisz program, który sprawdza, czy pewne dwie listy zawierają takie same elementy (ich
kolejność w listach jest bez znaczenia). Wartości	do	obu	list	można	wpisać	na	stałe	albo	
pobrać	od	użytkownika.	Wypisz	te	elementy,	które	są	takie	same	w	obu	listach.
Można	 przygotować	 dwa	 rozwiązania	 tego	 zadania	 (ogólne	 podejście	 możliwe	 do	
zastosowania w	dowolnym	języku	lub	podejście	Python’owe).	Podpowiedź	dla	podejścia	
Python’owego:	 zamień	 listy	 na	 zbiory	 i	 analizuj	 zbiory	 operatorem	 logicznym	 &.	
Konwersja	listy	do	zbioru:	set(),	konwersja	zbioru	do	listy:	list().	

Zadanie 5:
Napisz	 program,	 który	 sprawdza,	 czy	 ciąg	 znaków	 podany	 przez	 użytkownika	 jest	
palindromem,	tzn.	czy	kolejność	jego elementów	jest	identyczna	przy	czytaniu	od	lewej	i	
od	prawej.	Np.	palindromem	jest	napis:
ala
a	nie	jest	palindromem:
ala	ma	kota
Zdefiniuj	 funkcję	czyPalindrom,	której	argumentem	będzie	napis.	Funkcja	ma	zwracać	
wartość	False jeśli	ciąg	znaków	nie	jest	palindromem	i	True w	przeciwnym	przypadku.

Zadanie	6:
Napisz	 program,	 który	 sprawdza,	 czy 2	 ciągi	 znaków	 podane	 przez	 użytkownika	 są
anagramami,	tzn.	czy	składają	się	z	tych	samych	znaków.	Zdefiniuj	funkcję	czyAnagram,	
której	argumentami	będą	dwa	napisy.	Funkcja	ma	zwracać	wartość	True jeśli	dwa	napisy	
są	 anagramami	i	False w	 przeciwnym	 przypadku. Np. słowa KIMA i MIKA są swoimi
anagramami, a MIKA i MIKI nie.
Podpowiedź. Mogą	być	różne	sposoby	rozwiązania	tego	zadania.	Np.	można policzyć,	ile	
razy	występują	poszczególne	znaki	w	obu	napisach,	a	następnie	porównać,	czy	te	liczności	
się	pokrywają.	Można	wykorzystać	słownik,	kluczem	będzie	dany	znak,	a	stowarzyszoną	
wartością	liczba	jego	wystąpień	w	napisie.	Pamiętaj,	że	porównanie	dwóch	słowników	
jest	już	zaimplementowane	w	Pythonie! Czekam	też	na	inne	rozwiązania J

Zadanie	7:
Napisz	program,	który	sprawdza,	czy	pewien	napis	może	być	adresem	e-mail.

Zadanie	8:
Przedostatnia	 cyfra	 numeru	 PESEL	 określa	 płeć: jeśli	 jest	 nieparzysta,	 to	 PESEL	 jest	
przypisany	mężczyźnie,	jeśli	parzysta	– kobiecie.	Napisz	program,	który	odgaduje	płeć	na	
podstawie	 wprowadzonego	 numeru	 PESEL. Sprawdź,	 czy	 Twojemu	 programowi	 na	
pewno	podano	11	cyfr.

Zadanie	9:
Ostatnia	 cyfra	 numeru	 PESEL	 jest	 tzw.	 cyfrą	 kontrolną.	 Weryfikacja	 numeru	 PESEL	
następuje	w	wyniku	obliczenia	wartości	wyrażenia:	
c1 +	3c2 +	7c3 +	9c4 +	c5 +	3c6 +	7c7 +	9c8 +	c9 +	3c10 +	c11
gdzie	ci to	i-ta	cyfra	numeru	PESEL. Następnie	sprawdza	się	ostatnią	cyfrę	otrzymanego	
wyniku: jeśli	 jest	 to	 0,	 to	 PESEL	 jest	 poprawny;	 jeśli	 nie,	 PESEL	 jest	 błędny.	 Napisz	
program,	który	wczytuje	numer	PESEL	i sprawdza czy	jest	on	poprawny.

Zadanie	10:
Wylosuj	 5	 wartości rzeczywistych z	 zakresu	 podanego	 przez	 użytkownika	 (musisz	
przewidzieć,	że	 użytkownik	może	 podać	wartości	 całkowite).	Wyniki	podaj	jako	liczby	
rzeczywiste	zaokrąglone	do	3	miejsc	po	przecinku.
Podpowiedź.	Skorzystaj z	modułu	random i	funkcji	random.uniform().

Zadanie	11:
Korzystając	 z	 algorytmu	 Euklidesa	 w	 wersji	 z	 dzieleniem	 modulo	
(https://pl.wikipedia.org/wiki/Algorytm_Euklidesa,	
https://www.matemaks.pl/algorytm-euklidesa.html)
oblicz	i	wypisz	NWD	(Największy	Wspólny	Dzielnik)	oraz	NWW	(Najmniejszą	Wspólną	
Wielokrotność)	dwóch	liczb	naturalnych	pobranych	od	użytkownika.

Zadanie	12:
Ciąg	Fibonacciego	to	ciąg,	w	którym	pierwsze	dwa	pierwsze wyrazy	są	równe	1,	a	kolejne	
liczy	się	zawsze	jako	sumę	dwóch	poprzednich.	Oznacza	to,	że	początkowe	wyrazy	tego	
ciągu	to:	1,	1,	2,	3,	5,	8,	13,	21,	34,	...	(było	na	wykładzie	:-))
Napisz	program,	który	zapyta	użytkownika	o	numer	wyrazu	i	obliczy	jego	wartość.	Należy	
wypisać	tylko	wyraz	o	podanym	numerze,	np.	liczba	nr	4	to:	3).
