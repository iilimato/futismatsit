# Futispelit-sovellus

Kyseessä on sovellus, jossa käyttäjä pystyy etsimään seuraa jalkapallon pelaamiseen. Sovellus siis näyttää kentät ja ajat jolloin ihmisiä on menossa pelaamaan, ja niihin voi ilmoittautua mukaan.

## Toiminnot tällä hetkellä

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan ilmoituksia peleistä.
- Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
- Käyttäjä pystyy etsimään ilmoituksia hakusanalla (hakee otsikosta, kuvauksesta ja sijainnista).
- Käyttäjä pystyy jättämään kommentin tai kysymyksen ilmoitukseen.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät ilmoitukset.
- Käyttäjä pystyy ilmoittautumaan peliin ja katsomaan ilmoittautujien määrän ja käyttäjänimet. Ilmoittautumisen voi myös poistaa.

## Tulossa olevat toiminnot

- Käyttäjäsivulle lisää tilastoja, esim. kuinka moneen peliin on osallistunut.
- Käyttäjä pystyy valitsemaan ilmoitukselle kentän valmiista vaihtoehdoista (luokittelu).
  
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
