# Käyttöohje


## Käyttäjän toiminnallisuudet

### Käyttäjän luominen
Uusi käyttäjä luodaan sovelluksen yläpalkissa olevasta Sign up -napin takaa löytyvästä näkymästä. Rekisteröitymisen onnistuessa käyttäjä kirjataan automaattisesti sisään.

### Oman kokoelman tarkastelu
Käyttäjän kokoelma näkyy My collection -näkymässä. Painamalla List items with low ink -nappia kokoelmasta suodattuu tuotteet, joihin käyttäjä on merkinnyt musteen olevan alhainen. Tuotteen mustestatus voidaan vaihtaa painamalla tuotetta vastaavan rivin oikeassa reunassa olevaa Low ink -nappia. List items by date added listaa tuotteet lisäysjärjestyksessä, vanhin ensin. Tätä seuraavana on värikoodihaku, josta lisää myöhemmin tässä dokumentissa. Clear filters -nappia painamalla hakusuodattimet katoavat, ja tavarat listataan oletusasetuksilla (aakkosjärjestys värikoodin mukaan).

### Tuotteen lisääminen ja poistaminen omasta kokoelmasta
Käyttäjät voivat lisätä tietokannassa olevia tuotteita Add an item to my collection -näkymässä. Dropdown-valikoissa on näkyvillä kaikki tietokantaan valmiiksi kirjatut värikoodit sekä tuotetyypit. Käyttäjä valitsee oikean yhdistelmän, ja painaa lopuksi Add a new Item-nappia. Jos valittu yhdistelmä, eli tuote, on olemassa, niin uusi tuote lisätään käyttäjän nimiin, ja näkyy käyttäjän listassa. Ohjelma ei salli duplikaatteja. Tuote poistetaan painamalla tuotetta vastaavan rivin Delete item -nappia My collection-näkymässä.


### Käyttäjän ja adminin toiminnallisuudet

### View products
Näyttää tietokantaan lisätyt tuotteet. Adminina kirjautuneelle listassa on Delete-nappi tuotteen poistamista varten. Most popular colorcodes listaa värikoodit suosituimmasta vähiten suosituimpaan kaikkien käyttäjien kesken: lasketaan jokaisen värikoodin esiintymiskerrat Item-taulussa. Colorcodes only listaa tietokannassa olevat värikoodit, Product types only tekee saman product typeillä. Adminit voivat poistaa värikoodeja ja product typejä vastaavissa näkymissä. 

### Värikoodihaku
Värikoodihaun avulla etsitään... värikoodeja. Haun Inclusive-checkbox hakee värikoodit, jotka sisältävät annetun hakutermin. Esimerkiksi:
* Hakutermi G hakee kaikki G-alkuiset, eli vihreät värikoodit
* Hakutermi BG hakee kaikki BG-alkuiset, eli sinivihreät värikoodit
* Hakutermi G + Inclusive hakee kaikki G-merkin sisältävät värikoodit, eli YG, G ja BG -alkuiset koodit.
* Hakutermi R2 hakee R2-alkuiset värikoodit, palauttaa esimerkiksi R24, R29.
* Hakutermi V0 + Inclusive hakee V0-merkkijonon sisältävät värikoodit, palauttaa esimerkiksi BV02, V000, RV06

## Admin-oikeudella varustetut käyttäjät
Admineilla vasta hauskaa onkin. Adminit voivat lisätä tuotteita tietokantaan, joita käyttäjät voivat lisätä omiin kokoelmiinsa. Lisäksi adminit voivat lisätä uusia tuotetyyppejä. List users' items -näkymässä adminit näkevät kaikkien käyttäjien tavarat.


### Värikoodin lisääminen ja poistaminen tietokannasta
Uudet tuotetyypit lisätään Add to database -näkymässä Colorcode-kohdassa. Ohjelma ei hyväksy tyhjiä kenttiä eikä duplikaatteja. Annetun nimen täytyy olla 1-25 merkkiä pitkä. Värikoodi poistetaan View products -näkymän Colorcodes only -näkymän kautta.


### Tuotetyypin lisääminen ja poistaminen tietokannasta
Uudet tuotetyypit lisätään Add to database -näkymässä Product type -kohdassa. Ohjelma ei hyväksy tyhjiä kenttiä eikä duplikaatteja. Annetun nimen täytyy olla 2-25 merkkiä pitkä.


### Tuotteen lisääminen tietokantaan
Tietokantaan lisätään uusi tuote Add to database -näkymän Item-kohdassa. Dropdowneista valitaan haluttu värikoodi ja tuotetyyppi ja painetaan Add Item -nappia. Ohjelma ilmoittaa duplikaateista, eikä hyväksy niitä. Ei-duplikaatit lisätään rivi Cc_Ptype-liitostauluun. Tämän taulun rivit ovat tuotteita, joita käyttäjät voivat lisätä listoilleen. Cc_ptype-taulun sisältö näkyy View products -näkymässä. 


### Tuotteen poistaminen tietokannasta
Tuote poistetaan tietokannasta View products -näkymässä klikkaamalla poistettavan tuotteen riviltä Delete item -nappia. Tämä poistaa tuotteen kaikilta käyttäjiltä, jotka omistavat tuotteen.


## Copic-kannan elämän alussa
Tietokantaan lisätään ensin vähintään yksi tuotetyyppi, värikoodi ja tuote.


## Tiedettyjä rajoituksia ja ongelmia
Tietokanta ei salli käyttäjän omistaa enempää kuin yhden kappaleen tiettyä tuotetta, vaikka käytännössä kahden saman tuotteen omistaminen on mahdollista.


## Tulevia toiminnallisuuksia
* Hienostuneempi värihaku nappuloilla, seuraavaan tapaan:
![colorsearch](https://github.com/ikylios/copic-kanta/blob/master/documentation/colorsearch.png)
* Varjostussävyjen merkitseminen
* Toivelista
* Etusivu, jolla näkyvät uudet tietokantaan lisätyt tuotteet
* Listauksien suodatinnappien muokkaaminen siten, että aktiivisen suodattimen nappi on "active"
