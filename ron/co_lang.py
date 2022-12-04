"""
Labels in supported languages
"""


_EN = {
    "co-toolbar-title": "Ron Audio",
    "co-about": "About",
    "co-close-button": "CLOSE",
    "co-app-name": "Ron Audio Book Player",
    "co-app-running-on": "Running on",
    "co-folders": "Folders",
    "co-book": "Book",
}


_RU = {
    "co-toolbar-title": "Ron Аудио",
    "co-about": "О приложении",
    "co-close-button": "ЗАКРЫТЬ",
    "co-app-name": "Ron, проигрыватель аудиокниг",
    "co-app-running-on": "Выполняется на",
    "co-folders": "Папки",
    "co-book": "Книга",
}


_T = _EN


_LANG = {
    "EN": _EN,
    "RU": _RU,
}


def T(key):
    return _T[key]


def languages():
    return _LANG


def set_language(lng):
    global _T
    _T = _LANG[lng]
