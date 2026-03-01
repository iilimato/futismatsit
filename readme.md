# Futispelit-sovellus

Kyseessä on sovellus, jossa käyttäjä pystyy etsimään seuraa jalkapallon pelaamiseen. Sovellus siis näyttää kentät ja ajat jolloin ihmisiä on menossa pelaamaan, ja niihin voi ilmoittautua mukaan.

## Toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan ilmoituksia peleistä.
- Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
- Käyttäjä pystyy etsimään ilmoituksia hakusanalla (hakee otsikosta, kuvauksesta ja sijainnista).
- Käyttäjä pystyy jättämään kommentin tai kysymyksen ilmoitukseen.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät ilmoitukset ja tilastoja.
- Käyttäjä pystyy ilmoittautumaan peliin ja katsomaan ilmoittautujien määrän ja käyttäjänimet. Ilmoittautumisen voi myös poistaa.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

## Suuren tietomäärän käsittely

Sovellusta on testattu suurella tietomäärällä tiedoston `seed.py` avulla. Testitiedot sisältävät 1000 käyttäjää, 100000 peliä ja 1000000 kommenttia.

Raportti löytyy tiedostosta `performance-report.md`.
