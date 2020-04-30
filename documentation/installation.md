# Asennusohje

### Heroku (pilvi)

Herokun sivuilla ohjelma käynnistyy klikkaamalla GitHubin etusivulla olevaa Heroku-linkkiä, tai [tästä](https://copic-kanta.herokuapp.com).


### Paikallisesti

1. Lataa projekti tietokoneellesi. 
2. Koodihaun toimimintaan paikallisesti täytyy muokata hieman koodia. Kansiossa `~/copic-kanta/application/colorcode` on tiedosto `models.py`. Rivi 92 on kommentoitu ulos #-merkillä rivin alussa. Poista tämä merkki. Tämän jälkeen kommentoi rivi 93 samaan tapaan ulos: laita risuaita rivin alkuun. Toista tämä prosessi kansiossa `~copic-kanta/application/items` tiedostossa models.py, rivi 125 ja 126. Nyt koodihaku osaa suorittaa SQL-komennon sqlitelle sopivalla syntaksilla.
3. Laitetaan ohjelma käyntiin. Siirry komentorivillä kansioon `/copic-kanta-master/` ja suorita komento `python3 run.py`. Älä sulje komentoriviä. 
4. Avaa selain ja kirjoita osoitekenttään osoite `http://localhost:5000`
5. Suorita copic-tarpeitasi. 


Ohjelma suljetaan komennolla `Ctrl+C` selainta suorittavalla komentorivillä.
