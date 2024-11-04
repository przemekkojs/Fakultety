# ASYSTENT WYBORU FAKULTETÓW AKADEMII MUZYCZNEJ IM. KAROLA LIPIŃSKIEGO WE WROCŁAWIU
**Autor**: Przemysław Kojs\
**Licencja**: GNU Public License v3\

## Wstęp
Motywacją do napisania programu była nieczytelność ogromnego [pliku Arkuszy Google ze wszystkimi fakultetami](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY). Brak sortowania, dużo kolumn, wiele informacji w jednej kolumnie itp. to tylko niektóre z mankamentów. Dużo łatwiej byłoby się połapać, gdyby istniała możliwość filtrowania po prowadzącym, sali, godzinie rozpoczęcia i zakończenia... byłoby, a nawet jest.

Udało mi się nawiązać współpracę z Akademią, osoby odpowiedzialne za [plik Arkuszy Google](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY) zgodziły się dostosować format pode mnie. Nie planuję wprowadzać żadnych zmian, więć możliwe, że uda się wykonać pewnego rodzaju archiwizację danych - listy z poprzednich lat będą trzymane dalej jako dostępne.

Ale to na razie tylko pomysły, najważniejsze jest, że program działa a prace idą do przodu.

## Funkcje
- Filtrowanie po każdej kolumnie z [pliku arkuszy google](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY).
    - Proponowany etap kształcenia (np. 3L, 2M, 1L itd.)
    - Prowadzący
    - **łączna ilość ECTS**
    - Forma zajęć
    - Forma zaliczenia
    - Sala
    - Dzień tygodnia
    - Godzina rozpoczęcia
    - Godzina zakończenia
    - ...
- Szczegóły każdego kursu
- Dynamiczny interfejs

## Jak korzystać
Starałem się uczynić ten program tak intuicyjnym, jak tylko było to możliwe - żeby nie robić czegoś, co będzie jeszcze mniej pomocne niż [plik arkuszy google](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY). Wszystko powinno być łatwe:
1. Wybierami interesujące nas opcje
2. Klikamy przycisk "Filtruj"
3. Mamy tylko te fakultety, które nas interesują. Aby się dostać do szczegółów, klikamy przycisk "Szczegóły" obok podstawowych informacji o kursie.

Życzę przyjemnego korzystania.

## Dodatkowe informacje dla zainteresowanych
### Desktop
**Język programowania**: Python 3.11\
**Wersje językowe**: PL (od v.1.0)\

**4.11.2024** wsparcie wersji desktop zostało zakończone! Dziękuję wszystkim, którzy pobrali, mam nadzieję że korzystanie z demo było przyjemne.

### Mobile
Na ten moment brak. Wersja webowa jest w zupełności wystarczająca.

### Web
Od dnia **4.11.2024** jest to jedyna oficjalna wersja produktu. Udało się nawiązać współpracę z pracownikami Akademii odpowiedzialnymi za tworzenie i utrzymywanie listy fakultetów. Produkt można zatem uznać za oficjalny.

**Języki programowania**: HTML, CSS, JavaScript\
**Wersje językowe**: PL (w planach)\

**W przypadku chęci rozwoju programu (wersje językowe, pomysły na funkcje, kolaboracja), serdecznie zapraszam do kontaktu**. Wszelkie szczegóły są możliwe do znalezienia w plikach *CHANGELOG.md* oraz *RELEASE NOTES.md*.
