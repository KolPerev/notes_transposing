def notes_transposing(ton, new_ton, notes2):
    notes = notes2.copy()
    tons = {"до мажор": ["до", "ре", "ми", "фа", "соль", "ля", "си"],
            "ре мажор": ["ре", "ми", "фа#", "соль", "ля", "си", "до#"],
            "ми мажор": ["ми", "фа#", "соль#", "ля", "си", "до#", "ре#"],
            "ля мажор": ["ля", "си", "до#", "ре", "ми", "фа#", "соль#"],
            "соль мажор": ["соль", "ля", "си", "до", "ре", "ми", "фа#"],
            "си мажор": ["си", "до#", "ре#", "ми", "фа#", "соль#", "ля#"],
            "фа мажор": ["фа", "соль", "ля", "си♭", "до", "ре", "ми"]}
    notes_transport = []
    if ton.lower() in tons.keys() and new_ton.lower() in tons.keys():
        for t in tons.keys():
            if t == ton.lower():
                for new_t in tons.keys():
                    if new_t == new_ton.lower():
                        for note in notes:
                            if note.lower() in tons[t]:
                                for ind in range(len(tons[t])):
                                    if tons[t][ind].lower() == note.lower():
                                        notes_transport.append(tons[new_t][ind].capitalize())
                            else:
                                print(f"Ноты {note} нет в тональности {t}")
                                return -1
    else:
        print(f"Нет тональности {ton} или {new_ton}")
        return -1
    return notes_transport


print("Введите исходную тональность: ")
ton = input().capitalize()
print("Введите новую тональность: ")
new_ton = input().capitalize()
print("Введите ноты: ")
notes = input().title().split()
print(f"Ноты в тональности {ton}:", *notes)
print(f"Ноты в тональности {new_ton}:", *notes_transposing(ton, new_ton, notes))