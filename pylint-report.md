# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:7:0: E0401: Unable to import 'flask' (import-error)
app.py:8:0: E0401: Unable to import 'markupsafe' (import-error)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:71:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:139:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:146:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:148:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:159:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:161:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:168:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:159:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:181:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:201:4: W0621: Redefining name 'time' from outer scope (line 5) (redefined-outer-name)
app.py:219:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:223:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:237:4: W0621: Redefining name 'time' from outer scope (line 5) (redefined-outer-name)
app.py:263:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:268:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:296:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:305:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:296:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:316:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:325:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:335:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:348:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:353:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:369:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:374:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module games
games.py:1:0: C0114: Missing module docstring (missing-module-docstring)
games.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:18:0: R0913: Too many arguments (8/5) (too-many-arguments)
games.py:18:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
games.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:63:0: R0913: Too many arguments (8/5) (too-many-arguments)
games.py:63:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
games.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:85:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:107:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:121:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:130:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:135:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:140:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:148:0: C0116: Missing function or method docstring (missing-function-docstring)
games.py:154:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:20:4: R1705: Unnecessary "else" after "return" (no-else-return)
users.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.71/10
```

Käydään seuraavaksi läpi tarkemmin raportin sisältö ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suuri osa raportin ilmoituksista on seuraavanlaisia:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja. Funktioiden nimet on pyritty valita kuvaaviksi (esim. `get_game`, `check_logged_in`, `create_comment`), joten niiden toiminta on ymmärrettävissä ilman erillistä dokumentaatiota.

## Import-ilmoitukset

Raportissa on seuraavat ilmoitukset liittyen `import`-komentoihin:

```
app.py:6:0: E0401: Unable to import 'flask' (import-error)
app.py:7:0: E0401: Unable to import 'flask' (import-error)
app.py:8:0: E0401: Unable to import 'markupsafe' (import-error)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
```

Pylint antaa nämä ilmoitukset, koska se ei löydä Flask-kirjastoa ja sen riippuvuuksia ajoympäristöstä. Käytännössä `import`-komennot toimivat sovelluksessa ongelmitta, koska Flask on asennettu kehitysympäristön virtuaaliympäristöön. Nämä ilmoitukset voi siis jättää huomiotta.

## Nimen uudelleenmäärittely ulommasta näkyvyysalueesta

Raportissa on seuraavat ilmoitukset liittyen muuttujien nimiin:

```
app.py:71:4: W0621: Redefining name 'game' from outer scope (line 70) (redefined-outer-name)
app.py:201:4: W0621: Redefining name 'time' from outer scope (line 5) (redefined-outer-name)
```

Ensimmäinen ilmoitustyyppi koskee tilanteita, joissa reittifunktion `game()` sisällä käytetään paikallista muuttujaa `game`. Sama muuttujanimi esiintyy myös monissa muissa funktioissa, joissa haetaan peli tietokannasta muuttujaan `game`. Esimerkiksi:

```python
@app.route("/game/<int:game_id>")
def game(game_id):
    game = games.get_game(game_id)
```

Pylint varoittaa, koska paikallinen muuttuja `game` peittää ulommassa näkyvyysalueessa olevan funktion `game`. Käytännössä tämä ei aiheuta ongelmia, koska näissä funktioissa ei ole tarvetta kutsua `game`-reittifunktiota, ja muuttujanimi `game` on luonnollinen nimitys peliobjektille. Mielestäni on selkeämpää pitää muuttujanimi `game` kuin valita sille uusi, vähemmän kuvaava nimi.

Toinen ilmoitustyyppi koskee muuttujaa `time`, joka peittää moduulitason `import time` -komennon:

```python
time = request.form["time"]
```

Tässäkään ei ole käytännön ongelmaa, koska `time`-moduulia ei tarvita näissä funktioissa. Muuttujanimi `time` on luonnollinen nimitys pelin kellonajalle. Mielestäni on selkeämpää pitää muuttujanimi `time` kuin valita sille uusi, vähemmän kuvaava nimi.

## Tarpeeton else

Raportissa on seuraavat ilmoitukset liittyen `else`-haaroihin:

```
app.py:168:8: R1705: Unnecessary "else" after "return" (no-else-return)
app.py:305:8: R1705: Unnecessary "else" after "return" (no-else-return)
users.py:20:4: R1705: Unnecessary "else" after "return" (no-else-return)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa koodia:

```python
if "confirm" in request.form:
    games.delete_game(game_id)
    return redirect("/")
else:
    return redirect(f"/game/{game_id}")
```

Tämä koodi olisi mahdollista kirjoittaa ilman `else`-haaraa:

```python
if "confirm" in request.form:
    games.delete_game(game_id)
    return redirect("/")
return redirect(f"/game/{game_id}")
```

Kuitenkin sovelluksen kehittäjän näkemyksen mukaan `else`-haara tekee koodista selkeämpää, koska se tuo esille kaksi vaihtoehtoista toimintatapaa tasavertaisina haaroina.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:159:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:296:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
@app.route("/delete_game/<int:game_id>", methods=["GET", "POST"])
def delete_game(game_id):
    ...
    if request.method == "POST":
        ...
        return redirect("/")
    if request.method == "GET":
        return render_template("delete_game.html", game=game)
```

Tässä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla `GET` tai `POST`.

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset liittyen vaaralliseen oletusarvoon:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Tässä parametrin oletusarvo `[]` on tyhjä lista. Ongelmaksi voisi tulla, että sama oletusarvona oleva tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken ja jos jossain kutsussa listan sisältöä muutettaisiin, tämä muutos näkyisi myös muihin kutsuihin. Käytännössä tässä tapauksessa tämä ei kuitenkaan haittaa, koska koodi ei muuta listaoliota.

## Liian monta argumenttia

Raportissa on seuraavat ilmoitukset liittyen funktioiden argumenttien määrään:

```
games.py:18:0: R0913: Too many arguments (8/5) (too-many-arguments)
games.py:18:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
games.py:63:0: R0913: Too many arguments (8/5) (too-many-arguments)
games.py:63:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
```

Nämä ilmoitukset koskevat funktioita `add_game` ja `update_game`, joilla on 8 argumenttia. Pelillä on monta kenttää (otsikko, kuvaus, päivämäärä, kellonaika, sijainti, pelaajamäärä, käyttäjä, taitotaso), jotka kaikki on luonnollista välittää funktiolle erillisinä argumentteina. Argumenttien määrän vähentäminen esimerkiksi sanakirjalla ei kehittäjän näkemyksen mukaan parantaisi koodin luettavuutta tässä tilanteessa.
