# two-pizzas


## Setup

1. `git clone https://github.com/twardzikf/two-pizzas/`
2. `cd two-pizzas`
3. `source bin/activate`
4. `pip install -r requirements.txt`
5. `cd two_pizzas_app`
6. `python manage.py migrate`
7. `python manage.py runserver`

## API

- */*: Liste der Produkte
- */orders/* - Liste der Bestellungen, auf der man nach der Erstellung neuer Bestellung landet
- */orders/new* - Formular fuer eine neue Bestellung
