import re 
filepath = "D:\\Users\\barte\\OneDrive\\Pulpit\\WDI\\zestaw9zad9tekst.txt" # podwojne ukosniki aby \ nie byl symbolem uciecki
f = open(filepath, "r")
tekst = f.read()

#ponizsza linijka wyszukuje wzorca, gdzie beda kolejno: kropka, spacja, wielka litera alfabetu lacinskiego
endOfSentence = re.compile(r'\. (?=A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|W|X|Y|Z)')
#powyzsza linijka nie policzy ostatniego zdania, bo nie stoi za nim zadna duza litera
#z tego powodu dodaje 1 do liczby znalezionych wzorcow
#print(endOfSentence.findall(tekst))
print(len(endOfSentence.findall(tekst))+1)

'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. 
Cras vel lorem. 
Etiam pellentesque aliquet tellus. 
Phasellus pharetra nulla ac diam. 
Quisque semper justo at risus. 
Donec venenatis, turpis vel hendrerit interdum, dui ligula ultricies purus, sed posuere libero dui id orci. 
Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu, vel tempus metus leo non est. 
Etiam sit amet lectus quis est congue mollis. 
Phasellus congue lacus eget neque. 
Phasellus ornare, ante vitae consectetuer consequat, purus sapien ultricies dolor, et mollis pede metus eget nisi. 
Praesent sodales velit quis augue. 
Cras suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa nibh nec erat.

'''