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

### Testidata

Testidata generoitiin seed.py-tiedostolla:

- Käyttäjät: 1000
- Pelit: 100000
- Kommentit: 1000000

### Tulokset ilman indeksejä

| Sivu | Aika |
|------|------|
| Etusivu: / | 0,50 s |
| Pelisivu: /game/ | 0,07–0,28 s |
| Käyttäjäsivu: /user/ | 0,02–0,08 s |
| Haku: /find_game?query=Oulu | 0,34 s |

### Tulokset indekseillä

| Sivu | Aika |
|------|------|
| Etusivu: / | 0,55 s |
| Pelisivu: /game/ | 0,00–0,02 s |
| Käyttäjäsivu: /user/ | 0,00–0,02 s |
| Haku: /find_game?query=Oulu | 0,11 s |

### Tulokset

Indeksit paransivat pelisivun latausaikoja huomattavasti. Etusivu on edelleen hidas. Tämä johtuu todennäköisesti siitä, että se lataa kaikki 100000 peliä. Tämä voidaan todennäköisesti ratkaista sivutuksella. Teen sen seuraavaksi.

### Tulokset indekseillä ja sivutuksella

| Sivu | Aika |
|------|------|
| Etusivu: / | 0,00–0,02 s |
| Etusivu (sivu 2): /2 | 0,00-0,02 s |
| Pelisivu: /game/ | 0,00-0,02 s |
| Käyttäjäsivu: /user/ | 0,00–0,01 s |
| Käyttäjäsivu (sivu 2): /user/2/2 | 0,00–0,01 s |
| Haku: /find_game?query=Oulu | 0,08 s |

### Johtopäätökset

Sivutuksen lisääminen korjasi etusivun hitauden. Kaikki sivut latautuvat nyt nopeasti.