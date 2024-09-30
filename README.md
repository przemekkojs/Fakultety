# ASYSTENT WYBORU FAKULTETÓW
**Autor**: Przemysław Kojs\
**Licencja**: GNU Public License v3

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻\
👉🏻👉🏻👉🏻 [POBIERZ](https://raw.githubusercontent.com/przemekkojs/Fakultety/main/src/dist/Fakultety.exe) 👈🏻👈🏻👈🏻\
☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻☝🏻

## Wstęp
Motywacją do napisania programu była nieczytelność ogromnego [pliku Arkuszy Google ze wszystkimi fakultetami](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY). Brak sortowania, dużo kolumn, wiele informacji w jednej kolumnie itp. to tylko niektóre z mankamentów. Dużo łatwiej byłoby się połapać, gdyby istniała możliwość filtrowania po prowadzącym, sali, godzinie rozpoczęcia i zakończenia... byłoby, a nawet jest.

Program jest darmowy, open-source'owy, wystarczy pobrać i śmiało korzystać. Lista fakultetów będzie przeze mnie co rok aktualizowana, przynajmniej **dopóki tu studiuję**. No ale może uda się przekonać zarząd do uczynienia z tego narzędzia nieco bardziej oficjalnej wersji, z ilością miejsc i zapisywaniem się aktualizowanymi na żywo? To już pole do działania dla nas, studentów.

Proszę jednak pamiętać, że to tylko proste narzędzie - za błędy nie odpowiadam. Proponuję użyć raczej w celu poglądowego sprawdzenia, co jest kiedy i pomocy w filtrowaniu, a potem zweryfikować to w tym wielkim excelu.

Przy próbie uruchomienia prawdopodobnie pojawi się komunikat, że *ten program może być niebezpieczny*. Proszę go zignorować - po prostu nie posiadam certyfikatu (otrzymanie go to trochę za dużo zachodu na taką prostą zabawkę... chyba że zostanie nawiązana współpraca z Akademią).

## Funkcje
- Filtrowanie po każdej kolumnie z [pliku arkuszy google](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY).
    - Proponowany etap kształcenia (np. 3L, 2M, 1L itd.)
    - Prowadzący (bez tytułu, przykro mi...)
    - **łączna ilość ECTS**
    - Forma zajęć
    - Forma zaliczenia
    - Sala
    - Dzień tygodnia
    - Godzina rozpoczęcia
    - Godzina zakończenia
    - ...
- Szczegóły każdego kursu
- Dynamiczny (tzn. reagujący na zmiany) interfejs

## Jak korzystać
Starałem się uczynić ten program tak intuicyjnym, jak tylko było to możliwe - żeby nie robić czegoś, co będzie jeszcze mniej pomocne niż [plik arkuszy google](https://docs.google.com/spreadsheets/d/1WNC7SpdYdrO9oj3SaTiqJYlVr9a5uHMvBgeVfWYMPaY). Wszystko powinno być intuicyjne:
1. Wybierami interesujące nas opcje
2. Klikamy przycisk "Filtruj"
3. Mamy tylko te fakultety, które nas interesują. Aby się dostać do szczegółów, klikamy przycisk "Szczegóły" obok podstawowych informacji o kursie.

Możliwe, że część rzeczy nie wyświetla się jak powinno - nazwiska i nazwy kursów mogą być przekręcone. Miałem mały problem z polskimi znakami, nie wszystko mogło udać się poprawić tak, jak trzeba.

Życzę przyjemnego korzystania.

## Dodatkowe informacje dla zainteresowanych
**Język programowania**: Python 3.11
**Wersje językowe**: PL (od v.1.0)

Kod zawiera dokumentację **tylko w języku angielskim**.

**W przypadku chęci rozwoju programu (wersje językowe, pomysły na funkcje, kolaboracja), serdecznie zapraszam do kontaktu.**
