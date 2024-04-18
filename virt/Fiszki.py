import random
import tkinter as tk
from tkinter import ttk
import random
from random import choice
import time

window= tk.Tk()
window.title("Angielski")
window.geometry("700x600")

slownik2 = {
    "przegląd personelu": "reassess manpower",
    "praktykant inżynierii": "engineering intern",
    "otrzymywać różnorodne dodatkowe korzyści": "receive various perks",
    "odwołanie kierownika": "dismissal of the executive",
    "przydział, świadczenie": "allowance",
    "ograniczenie nadmiaru pracowników": "workforce redundancy",
    "wykonalny": "viable",
    "raty": "installments",
    "zabezpieczenie np. do kredytu": "collateral",
    "próg rentowności": "break even point",
    "ostateczny rezultat finansowy": "bottom line",
    "zdolność kredytowa": "creditworthiness",
    "oszukany": "ripped off",
    "dotacja rządowa": "government subsidy",
    "stopa procentowa": "interest rate",
    "kapitał podwyższonego ryzyka": "venture capital",
    "przekonać kogoś do projektu": "get sb on board",
    "zyskać popularność": "catch on",
    "być w sytuacji kryzysowej": "be at the end of rope",
    "zalegać z płatnościami": "fall behind on loan payments",
    "sięgnąć po pieniądze": "draw on money",
    "rozłożyć płatności w czasie": "space out payments",
    "przydać się": "come in handy",
    "udział w biznesie": "stake in business",
    "część udziałów": "part of equity",
    "liczba osób które kliknęły w dany link": "CTR- click through rate",
    "być połączonym": "combined into",
    "działać po cichutku": "act on the sly",
    "zakupy powyżej możliwości": "buy beyond your means",
    "fikcyjne imię": "made up name",
    "przedstawić": "put across",
    "treści generowane przez użytkowników": "UGC - user generated content",
    "społeczna odpowiedzialność biznesu": "CSR- corporate social responsibility",
    "opłata za kliknięcie": "PPC - pay per click",
    "rozprzestrzeniać się jak pożar": "spread like wildfire",
    "dopasować": "tailor",
"zdolność poruszania się po nowych mediach": "new media literacy",
    "zdolność racjonalnego analitycznego myślenia": "sense-making",
    "zarządzanie obciążeniem poznawczym": "cognitive load management",
    "myślenie nowatorskie": "novel thinking",
    "upoważniony": "commissioned",
    "strategiczne": "strategised",
    "ulożone": "arranged",
    "wdrożony": "implemented",
    "zdobyć, otrzymać, zaprojektować": "procure",
    "klasyfikowany": "classify",
    "wyznaczać": "appoint",
    "przeznaczyć": "allocate",
    "wykonany, przeprowadzony": "conducted",
    "rozdzielać, rozdawać": "distribute",
    "zjednoczony, wzmocniony": "consolidated",
    "osiągnięty": "attained",
    "ukierunkowane": "targeted",
    "uproszczony": "streamlined",
    "opracowany": "formulated",
    "przebudowany": "remodeled",
    "rozszyfrowany": "deciphered",
    "z poboru, pozyskany, poprosić": "enlisted",
    "modny zwrot": "buzzword",
    "przekazywać": "convey",
    "zagrażać, narażać": "jeopardize",
    "nowicjusz": "novice",
    "odznaczać się": "stand out",
    "osiągnięcia": "track record",
    "zmienny": "volatile",
    "niepewny": "uncertain",
    "złożony": "complex",
    "dwuznaczny": "ambiguous",
    "zwiększanie zakresu umiejętności": "scale up skills",
    "utrwalone": "set in stone",
    "wspomagać": "contribute to",
    "rynek pomysłów": "knowledge economy",
    "zdolności do": "aptitude for",
    "mieć wpływ na": "bearing on",
    "sedno": "at the heart",
    "jasno określone normy": "clear-cut norms",
    "niwelować": "to level down",
    "bagatelizować": "play down",
    "przyswajać informacje": "process information",
    "rozważyć wszystkie za i przeciw": "weigh up all the pros and cons",
    "wpływać na obie strony": "flow both ways",
    "odnajdywać się w sytuacji": "read the situation",
    "wewnętrzne procesy": "inner workings",
    "jawny": "explicit",
    "ukryty": "implicit",
    "nawigacja w nieznanym": "manage unknown",
    "struktura, szkielet": "framework",
    "jasne, przejrzyste": "straightforward",
    "niejasny": "vague",
    "owijać w bawełnę": "beating around the bush",
    "samoświadomy": "self-aware",
    "pokorny": "humble",
    "przekonanie": "conviction",
    "współpracujący": "collaborative",
    "życzliwy": "benevolent",
    "prowadzić spotkanie": "run a meeting",
    "zwolnić ludzi": "lay people off",
    "brytyjski termin na zwolnić ludzi": "make people redundant",
    "zawrzeć umowę": "to conclude a contract",
    "nawiązać kontakt": "establish rapport",
    "mierzenie wydajności": "measure performance",
    "rozwijać personel": "develop people",
    "podległy": "subordinate",
    "wypłata": "remuneration",
    "restrukturyzacja": "turnaround",
    "sprzedaż hurtowa": "wholesale",
    "sprzedaż detaliczna": "retail"
}
slownik = slownik2

slownik_slowotworstwo2 = {
    "The meeting has been rescheduled for next week (SCHEDULE)" : "rescheduled",
    "If you need to leave early, speak to your immediate  ... SUPERVISE.": "supervisor",
    "She was elected to the board of ... in 2014  DIRECT.": "directors",
    "Can I speak to the ...  , please? She told me to contact\n her today MANAGE.": "manager",
    "Promotion should be based on merit, not  ... SENIOR.": "seniority",
    "He demands total ... from his staff  COMMIT." : "commitment",
    "Continual correcting someone's mistakes can be a big ... MOTIVATE.": "demotivator",
    "The bank's chief ... has reduced his forecast \nfor growth to 0.5%  ECONOMY.": "economist",
    "The merger was a sound ... move  STRATEGY." : "strategic",
    "The store has a ... card-scheme  LOYAL.": "loyalty",

    "The company focuses on... marketing and creates content that \naligns with the needs of your target audiences BIND": "inbound",
    "Critics of the advertisement accused the company of using... tactics to\n manipulate consumer behavior HAND": "underhand",
    "The brand offers... personalized experience CUSTOM": "customisation",
    "After the successful launch of the new ad campaign, the company \nsaw a significant increase in... among consumers RECOGNIZE": "recognition",
    "The company uses... analysis to understand the personality traits \nand preferences of their target audience PSYCHOLOGICAL": "psychometric",
    "The company's... strategy focuses on building long-term relationships \nwith their customers rather than just one-time sales RETAIN": "retention",
    "By implementing new digital marketing techniques, the company was \nable to improve their... rate by 20% CONVERT": "conversion",
    "The ... of his intentions led to the breakdown of their \npartnership  INTERPRET": "interpretation",
    "Despite their ideological differences, the two CEOs decided to engage \nin a constructive ... during the debate CONFRONT": "confrontation",

    "His ... in the workplace is evident through his punctuality, \neffective communication skills, and attention to detail PROFESSION": "professionalism",
    "... is the belief that everything in life happens because of\n a predetermined plan DETERMINATE": "determinism",
    "The board of directors implemented a ... system to maintain order\n in the workplace DISCIPLINE": "disciplinary",
    "The successful negotiation between the two companies was a product \nof their cross-cultural ... and respect UNDERSTAND": "understanding",
    "The ... of the event was evident from the guests' elegant attire and\n the fine dining options available FORM": "formality",
    "Multiculturalism is the cornerstone of our society, fostering an \nenvironment where diverse beliefs, traditions, and perspectives coexist ... HARMONY":"in harmony",
    "With her ... knowledge and competence, she quickly rose to the top \nposition in the company EXTEND": "extended"

    }
slownik_slowotworstwo = slownik_slowotworstwo2
slownik_niepoprawnych = {}
def wyswietl_tabele_niepoprawnych():
    global slownik_niepoprawnych

    window2 = tk.Tk()
    window2.title("Tabela niepoprawnych")
    window2.geometry("800x600")
    table = ttk.Treeview(window2, columns=("zdanie", "odpowiedz"), show="headings")
    table.heading("zdanie", text="zdanie")
    table.heading("odpowiedz", text="odpowiedz")
    table.pack(fill="both", expand=True)
    for klucz, wartosc in slownik_niepoprawnych.items():
        table.insert("", "end", values=(klucz, wartosc))

    window2.mainloop()


global powtorzenia
powtorzenia = 0
combo1 = None
global punkty
punkty = 0
def wybor_fiszki():
    global odpowiedz
    global wartosc
    odpowiedz = choice(list(fiszki_slownik.keys()))
    wartosc = fiszki_slownik[odpowiedz]
    return fiszki_slownik[odpowiedz], wartosc


def koniec_fiszki():
    global tekscik
    global punkty
    global powtorzenia2
    global powtorzenia
    global powtorz
    global przejdz_dalej
    global combo1
    global entry
    global startbtn
    global startbtn2
    global tabelabtn




    entry = None

    canvas.delete("all")
    if startbtn:
        startbtn.pack_forget()
    if startbtn2:
        startbtn2.pack_forget()
    if combo1:
        combo1.pack_forget()

    canvas.create_text(350, 200,
                       text=f"\t Koniec! Twoje punkty: {punkty}/10 \nJeśli chcesz wyświetlić tabelę z zadaniami,\n które sprawiły Ci problem, kliknij poniżej",
                       font=("Times New Roman", 16), anchor="center")

    powtorz = tk.Button(window, text="Zacznij od nowa", command=fiszki_wprowadzenie)
    powtorz.config(width=20, height=3)
    powtorz.pack(side="left", padx=10)

    przejdz_dalej = tk.Button(window, text="Przejdź do słowotwórstwa", command=slowotworstwo_wprowadzenie)
    przejdz_dalej.config(width=20, height=3)
    przejdz_dalej.pack(side="right", padx=10)

    powtorzenia2 = 0
    powtorzenia = 0
    punkty = 0

    tabelabtn = tk.Button(window, text="Pokaż tabelkę z błędami", command=wyswietl_tabele_niepoprawnych, width=20,
                          height=2)
    tabelabtn.pack(side="bottom", pady=10)


def sprawdz_i_idz_dalej():
    global powtorzenia
    global punkty
    global slownik_niepoprawnych
    global slownik

    if combo1.get() == wartosc:
        canvas.delete("all")
        combo1.destroy()
        poprawna = canvas.create_text(350, 200, text="Poprawna odpowiedź!", font=("Arial", 30))
        print("Poprawna odpowiedź!")
        window.after(2000, start)
        powtorzenia += 1
        punkty += 1
        #tu
        slownik.pop(odpowiedz)



    else:
        canvas.delete("all")
        combo1.destroy()
        niepoprawna = canvas.create_text(350, 200, text=f"Oj nie nie. Poprawna to {fiszki_slownik[odpowiedz]}", font=("Arial", 20))

        print("Oj nie nie!")
        window.after(2000, start)
        powtorzenia += 1
        slownik_niepoprawnych[odpowiedz] = fiszki_slownik[odpowiedz]





combo1 = None
def start():
    global punkty
    global combo1
    global powtorzenia
    global wartosc
    global startbtn
    global startbtn2
    global entry
    global slownik
    global fiszki_slownik
    global tabelabtn


    wylosowane_klucze = random.sample(list(slownik.keys()), 7)
    fiszki_slownik = {}
    for klucz in wylosowane_klucze:
        fiszki_slownik[klucz] = slownik[klucz]
    print(fiszki_slownik)

    startbtn2.place(x= 250, y=400, width=200, height=50)


    if startbtn:
        startbtn.config(text="Zatwierdź", command=sprawdz_i_idz_dalej)
    if startbtn is not None:
        startbtn.config(text="Zatwierdź", command=sprawdz_i_idz_dalej)
        startbtn.pack()
    if startbtn2:
        startbtn2.grid_forget()
    canvas.delete("all")
    wybor_fiszki()
    if powtorzenia == 10:
        koniec_fiszki()
    else:

        tekst = canvas.create_text(350, 100, text= odpowiedz, font=("Times New Roman", 18))
        values = sorted(fiszki_slownik.values())
        combo1 = ttk.Combobox(window, values=values, width=52, font=("Times New Roman", 16))
        combo1.focus_set()
        combo1.place(relx=0.5, rely=0.5, anchor="center")
        combo1.bind("<Return>", lambda event: sprawdz_i_idz_dalej())




global powtorzenia2
powtorzenia2 = 0
#zatwierdz = tk.Button(text="Zatwierdź", command=sprawdz_i_idz_dalej, width=20, height=3)

def fiszki_wprowadzenie():
    global powtorz
    global przejdz_dalej
    global destroy
    global startbtn
    global startbtn2
    global entry
    global zatwierdz
    global tabelabtn

    if tabelabtn:
        tabelabtn.destroy()


    if entry:
        entry.pack_forget()
    if startbtn:
        startbtn.pack_forget()
    if startbtn2:
        startbtn2.pack_forget()
    if combo1:
        combo1.pack_forget()
    powtorz.pack_forget()
    przejdz_dalej.pack_forget()
    canvas.delete('all')
    wprowadzenie = canvas.create_text(350, 100, text="Zaraz rozpoczniesz fiszki! Ale nudy D;", font=("Times New Roman", 15), anchor="center")
    window.after(2000, start)


def slowotworstwo_wprowadzenie():
    global powtorz
    global przejdz_dalej
    global combo1
    global startbtn
    global startbtn2
    global tabelabtn
    if tabelabtn:
        tabelabtn.destroy()

    if entry:
        entry.destroy()
    if startbtn:
        startbtn.pack_forget()
    if startbtn2:
        startbtn2.pack_forget()
    if combo1:
        combo1.pack_forget()
    powtorz.pack_forget()
    przejdz_dalej.pack_forget()
    canvas.delete("all")
    wprowadzenie = canvas.create_text(350, 50, text="Zaraz rozpoczniesz słowotwórstwo. Trzymaj się D:", font=("Times New Roman", 15), anchor= "center")
    window.after(2000, slowotworstwo)


def koniec_slowotworstwo():
    global tekscik
    global punkty
    global powtorzenia2
    global powtorz
    global przejdz_dalej
    global combo1
    global entry
    global slownik_slowotworstwo
    global slownik_niepoprawnych
    global tabelabtn






    canvas.delete("all")
    if entry:
        entry.destroy()
    if startbtn:
        startbtn.pack_forget()
    if startbtn2:
        startbtn2.pack_forget()
    if combo1:
        combo1.pack_forget()

    canvas.create_text(350, 200, text=f"    Koniec! Twoje punkty: {punkty}/15 \nJeśli chcesz wyświetlić tabelę z zadaniami,\n które sprawiły Ci problem, kliknij poniżej", font=("Times New Roman", 16), anchor="center")

    powtorz = tk.Button(window, text="Zacznij od nowa", command=slowotworstwo_wprowadzenie)
    powtorz.config(width=20, height=3)
    powtorz.pack(side="left", padx=10)

    przejdz_dalej = tk.Button(window, text="Przejdź do fiszek", command=fiszki_wprowadzenie)
    przejdz_dalej.config(width=20, height=3)
    przejdz_dalej.pack(side="right", padx=10)


    powtorzenia2 = 0
    punkty = 0

    #Wyswietl tabelke
    tabelabtn = tk.Button(window, text="Pokaż tabelkę z błędami", command=wyswietl_tabele_niepoprawnych, width=20,
                          height=2)
    tabelabtn.pack(side="bottom", pady=10)






def sprawdz_slowotworstwo():
    global punkty
    global powtorzenia2
    global zdanie_slowotworstwo
    global slownik_niepoprawnych
    global slownik_slowotworstwo
    global wartosc_slowotworstwo
    canvas.delete("all")
    wprowadzona_odpowiedz = entry.get()
    poprawna_odpowiedz = slownik_slowotworstwo[zdanie_slowotworstwo]
    if wprowadzona_odpowiedz == poprawna_odpowiedz:
        entry.destroy()
        poprawna = canvas.create_text(350, 200, text="Poprawna odpowiedź!", font=("Arial", 30))
        print("DOBRZE")
        window.after(2000, slowotworstwo)
        punkty += 1
        powtorzenia2 +=1

        #tu

        slownik_slowotworstwo.pop(zdanie_slowotworstwo)


    else:
        entry.destroy()
        niepoprawna = canvas.create_text(350, 200, text=f"Oj nie nie. Poprawna to {slownik_slowotworstwo[zdanie_slowotworstwo]}!",
                                         font=("Arial", 20))
        window.after(2000, slowotworstwo)
        powtorzenia2 += 1
        slownik_niepoprawnych[zdanie_slowotworstwo] = slownik_slowotworstwo[zdanie_slowotworstwo]





def wybor_zdania_slowotworstwo():
    global zdanie_slowotworstwo
    global wartosc_slowotworstwo
    zdanie_slowotworstwo = choice(list(slownik_slowotworstwo.keys()))
    wartosc_slowotworstwo = slownik_slowotworstwo[zdanie_slowotworstwo]


def slowotworstwo():
    global powtorzenia2
    global startbtn2
    global zdanie_slowotworstwo
    global entry
    global tekscik
    global powtorz
    global przejdz_dalej
    global tabelabtn



    if powtorzenia2 == 15:
        canvas.delete("all")
        koniec_slowotworstwo()
        startbtn2.grid_forget()
        startbtn.grid_forget()
    else:
        wybor_zdania_slowotworstwo()
        canvas.delete("all")

        tekscik = canvas.create_text(350, 100, text= zdanie_slowotworstwo, font=("Times New Roman", 18), anchor="center")
        entry = tk.Entry(window, font=("Arial", 24))
        entry.focus_set()
        entry.place(x=250, y=300, width=200, height=50)
        startbtn2.config(text="Zatwierdź", command= sprawdz_slowotworstwo)
        startbtn.place(x= 250, y=400, width=200, height=50)
        startbtn2.pack()
        entry.bind("<Return>", lambda event: sprawdz_slowotworstwo())








zmiana_mot = 1
def zmiana_na_jasny():
    global zmiana_mot
    zmiana_mot += 1

    if zmiana_mot == 1:
        canvas.config(bg="#33A1C9")
    elif zmiana_mot == 2:
        canvas.config(bg="grey")
    elif zmiana_mot == 3:
        canvas.config(bg='skyblue')
    elif zmiana_mot == 4:
        canvas.config(bg='#66CDAA')
        zmiana_mot-=4





zmianamotywu = tk.Button(window, text="Zmień motyw", command=zmiana_na_jasny)
zmianamotywu.pack()

canvas = tk.Canvas(window, bg="#33A1C9")
canvas.create_window(50,100)

canvas.create_text(350, 100, text="     ANGIELSKI\n NAUKA NA TEST", font=("Helvetica", 24))

def show_message(event):
    label.config(text= choice(["Syl malarski Paint!",
                               "Co cię tak interesuje ten trójkąt?", "Zostaw to, tu nie ma interakcji!"]))
def leave_message(event):
    label.config(text=(""))
def draw_triangle(canvas):
    x1, y1 = 250, 150
    x2, y2 = 350, 250
    x3, y3 = 450, 150
    triangle_id = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="#B8B8B8", outline="black", width=6)
    canvas.tag_bind(triangle_id, "<Enter>", show_message)
    canvas.tag_bind(triangle_id, "<Leave>", leave_message)
draw_triangle(canvas)
canvas.pack(fill = "both", expand = True)


button_frame = tk.Frame(window)
button_frame.pack(side="top", pady=20)

startbtn = tk.Button(button_frame, text="Fiszki", command=start)
startbtn.config(width=20, height=3)
startbtn.pack(side="left", padx=10)

startbtn2 = tk.Button(button_frame, text="Słowotwórstwo", command= slowotworstwo)
startbtn2.config(width=20, height=3)
startbtn2.pack(side="left", padx=10)



def show_text(event):
    label.config(text= choice(["No kurwa kliknij, a się zastanawiasz!",
                               "No śmiało!", "Dasz radę!", "Weź już w to kliknij", "Ale super Ci idzie misiu",
                               "Idzie Ci jak starej babie zakupy- powoli, ale konksekwentie!"]))

def hide_text(event):
    label.config(text="")

label = tk.Label(window, text="", fg="black")
label.pack()

# Związanie zdarzeń "Enter" i "Leave" z funkcjami show_text i hide_text
startbtn.bind("<Enter>", show_text)
startbtn.bind("<Leave>", hide_text)
startbtn2.bind("<Enter>", show_text)
startbtn2.bind("<Leave>", hide_text)



window.mainloop()
