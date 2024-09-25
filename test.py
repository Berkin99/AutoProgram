from itertools import combinations

# Verilen ders bilgileri
classes = {
    'BENG215': [('mon', '13:30', '16:20')],
    'INF211': [('mon', '14:30', '17:30'), ('tue', '13:30', '15:30')],
    'ENG346': [('mon', '13:30', '16:30')],
    'MATH113': [('mon', '09:30', '12:20'), ('wed', '13:30', '15:20')],
    'INAS501': [('wed', '13:30', '16:30')],
    'STEC564': [('mon', '09:30', '12:20')],
    'CSE557': [('tue', '13:30', '16:20')],
    'CSE562': [('tue', '09:30', '12:20')],
    'CSE564': [('thu', '13:30', '16:20')],
    'CSE654': [('mon', '13:30', '16:20')],
    'CSE655': [('tue', '14:30', '17:20')],
    'IE515': [('fri', '09:30', '12:30')],
    'ELEC769': [('tue', '09:30', '12:30')],
    'ME524': [('fri', '09:30', '12:30')],
}

# Zaman çakışmalarını kontrol eden fonksiyon
def check_overlap(class1, class2):
    for day1, start1, end1 in class1:
        for day2, start2, end2 in class2:
            if day1 == day2:
                if not (end1 <= start2 or end2 <= start1):  # Çakışma var mı?
                    return True
    return False

# Derslerin çakışıp çakışmadığını kontrol et
def is_valid_schedule(selected_classes):
    for i in range(len(selected_classes)):
        for j in range(i + 1, len(selected_classes)):
            if check_overlap(classes[selected_classes[i]], classes[selected_classes[j]]):
                return False
    return True

# Seçilen derslerin en fazla 2 gün olmasını kontrol eden fonksiyon
def check_max_days(selected_classes, max_days=2):
    days = set()
    for cls in selected_classes:
        for day, _, _ in classes[cls]:
            days.add(day)
    return len(days) <= max_days

# 4 ders seçilip, çakışma olmadan ve maksimum 2 gün sınırına uyulup uyulmadığını kontrol eden fonksiyon
def find_valid_schedules():
    valid_schedules = []
    for combination in combinations(classes.keys(), 4):
        if is_valid_schedule(combination) and check_max_days(combination):
            valid_schedules.append(combination)
    return valid_schedules

# Uygun programları bul
valid_schedules = find_valid_schedules()

# Sonuçları yazdır
if valid_schedules:
    print("Geçerli programlar:")
    for schedule in valid_schedules:
        print(schedule)
else:
    print("Uygun bir program bulunamadı.")
