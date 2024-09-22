class LanguagePack:
    def __init__(self) -> None:
        self.dictionary:dict[str, str] = {}

    def __getitem__(self, key:str) -> str:
        if key in self.dictionary:
            return self.dictionary[key]
            

class PL(LanguagePack):
    def __init__(self) -> None:
        super().__init__()

        self.dictionary = {
            'Error' : 'Ups, coś poszło nie tak!',
            'Courses not loaded' : 'Część kursów nie została załadowana',
            'Course loading error' : 'Błąd podczas ładowania kursu',
            'Filter' : 'Filtruj',
            'Filters' : 'Filtry',
            'Clear Filters' : 'Wyczyść Filtry',
            'Details' : 'Szczegóły',
            'ECTS' : 'ECTS',
            'ECTS Winter' : 'ECTS sem. zimowy',
            'ECTS Summer' : 'ECTS sem. letni',
            'ECTS Combined' : 'ECTS łącznie',
            'Suggested Learning Stage' : 'Sugerowany etap kształcenia',
            'Course Name' : 'Nazwa kursu',
            'Teacher' : 'Prowadzący',
            'Room' : 'Sala',
            'Start Hour' : 'Godzina rozpoczęcia',
            'End Hour' : 'Godzina zakończenia',
            'Weekday' : 'Dzień tygodnia',
            'Hours Winter' : 'Godziny tygodniowo sem. zimowy',
            'Hours Summer' : 'Godziny tygodniowo sem. letni',
            'Faculty' : 'Wydział',
            'Additional Pass Info' : 'Dodatkowe informacje o zaliczeniu',
            'Additional Info' : 'Dodatkowe informacje',
            'Place Limit' : 'Ilość miejsc',
            'Course Type' : 'Forma zajęć',
            'Test Type' : 'Forma zaliczenia'            
        }