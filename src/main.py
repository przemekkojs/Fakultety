from ui import app
from dictionary import LanguagePack, PL

if __name__ == '__main__':
    language_pack:LanguagePack = PL()
    program:app = app(language_pack, 'src/resources/fakultety2.csv')
