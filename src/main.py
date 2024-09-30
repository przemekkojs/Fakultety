from ui import app
from dictionary import LanguagePack, PL
from utils import *

if __name__ == '__main__':
    language_pack:LanguagePack = PL()
    program:app = app(language_pack, get_resource_path('resources\\fakultety2024_2025.csv'))
