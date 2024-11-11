# Vecuma aprēķins dažādās laika zonās, izmantojot pytz un datetime

from datetime import datetime
import pytz  # Nepieciešams instalēt: pip install pytz

# Funkcija vecuma aprēķināšanai,
# ievadot dzimšanas datumu un laika zonu
def aprekini_vecumu_ar_laika_zonu(dzimsanas_datums, laika_zona):
    # pārvēršam dzimšanas datumu par datetime objektu
    dz_datums = datetime.strptime(dzimsanas_datums, "%d/%m/%Y")
    
    # Iegūstam šodienas datumu konkrētajā laika zonā
    timezone = pytz.timezone(laika_zona)
    sodienas_datums = datetime.now(timezone)

    # Aprēķinām vecumu gados
    vecums_gados = sodienas_datums.year - dz_datums.year
    
    # Pārbaudām, vai dzimšanas diena šogad jau bija
    if sodienas_datums.month < dz_datums.month or \
       (sodienas_datums.month == dz_datums.month and sodienas_datums.day < dz_datums.day):
        vecums_gados -= 1
    
    # Aprēķinām vecumu dienās un mēnešos
    vecums_dienas = (sodienas_datums - dz_datums).days
    vecums_menesos = vecums_gados * 12 + (sodienas_datums.month - dz_datums.month)
    
    # Atgriežam vecumu dažādos formātos
    return vecums_gados, vecums_menesos, vecums_dienas
# Lietotāja ievadītie dati
dzimsanas_datums = input("Ievadi savu dzimšanas datumu (DD/MM/GGGG): ")

# Piemēram, dažādas laika zonas
laika_zonas = ["Europe/Riga", "America/New_York", "Asia/Tokyo"]


# Vecuma aprēķins katrā laika zonā

for zona in laika_zonas:
    vecums_gadi, vecums_menesos, vecums_dienas = aprekini_vecumu_ar_laika_zonu(dzimsanas_datums, zona)
    print(f"Laika zonā {zona}:")
    print(f"Vecums gados: {vecums_gadi}, mēnešos: {vecums_menesos}, dienās: {vecums_dienas}")
    print('-' * 40)
