# Futispelit-sovellus

Kyseessä on sovellus, jossa käyttäjä pystyy etsimään seuraa jalkapallon pelaamiseen. Sovellus siis näyttää kentät ja ajat jolloin ihmisiä on menossa pelaamaan, ja niihin voi ilmoittautua mukaan.

## Toiminnot tällä hetkellä

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan ilmoituksia peleistä.
- Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
- Käyttäjä pystyy etsimään ilmoituksia hakusanalla (hakee otsikosta, kuvauksesta ja sijainnista).
- Käyttäjä pystyy jättämään kommentin tai kysymyksen ilmoitukseen.

## Tulossa olevat toiminnot

- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät ilmoitukset.
- Käyttäjä pystyy valitsemaan ilmoitukselle kentän valmiista vaihtoehdoista (luokittelu).
- Käyttäjä pystyy ilmoittautumaan peliin ja katsomaan ilmoittautujien määrän ja käyttäjänimet. Ilmoittautumisen voi myös poistaa.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut:

```
$ sqlite3 database.db < schema.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```