# Hip Hop Hudební Databáze

Webová aplikace v Django pro správu a prohlížení hip hop hudby, interpretů, alb a písní.

## Funkce
- Prohlížení hip hop interpretů a jejich profilů
- Zobrazení alb a seznamů skladeb
- Prozkoumání jednotlivých písní s detaily
- Administrační rozhraní pro správu obsahu

## Instalace
1. Vytvoření virtuálního prostředí:
```bash
python -m venv venv
```

2. Aktivace virtuálního prostředí:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Instalace závislostí:
```bash
pip install -r requirements.txt
```

4. Spuštění migrací:
```bash
python manage.py migrate
```

5. Vytvoření superuživatele:
```bash
python manage.py createsuperuser
```

6. Spuštění vývojového serveru:
```bash
python manage.py runserver
```

## Struktura projektu
- `hiphop/` - Hlavní adresář projektu
- `music/` - Hlavní adresář aplikace
  - `models.py` - Databázové modely
  - `views.py` - Logika zobrazení
  - `urls.py` - Směrování URL
  - `admin.py` - Konfigurace administračního rozhraní 