"""Labels in supported languages
"""


_EN = {
    "co-toolbar-title": "Ron Audio",
    "co-no-ps-selected": "No power supply selected",
    "co-ps-label-1": "Power supply",
    "co-exit": "Exit",
    "co-discover-ps": "Discover",
    "co-details": "Details",
    "co-details-l": "details",
    "co-about": "About",
    "co-close-button": "CLOSE",
    "co-app-name": "Ron Audio Book Player",
    "co-app-running-on": "Running on",
    "co-output-current-l": "output current",
    "co-folders": "Folders",
    "co-book": "Book",
}


_RU = {
    "co-toolbar-title": "Ron Аудио",
    "co-no-ps-selected": "Источник не выбран",
    "co-ps-label-1": "Источник",
    "co-exit": "Выход",
    "co-discover-ps": "Обнаружить источники",
    "co-details": "Детали",
    "co-details-l": "детали",
    "co-about": "О приложении",
    "co-close-button": "ЗАКРЫТЬ",
    "co-app-name": "Ron, проигрыватель аудиокниг",
    "co-app-running-on": "Выполняется на",
    "co-output-current-l": "ток в нагрузке",
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
