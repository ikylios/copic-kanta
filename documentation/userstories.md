Käyttäjänä haluan nähdä listan kaikista Copic-tuotteista, jotta voin suunnitella toivelistaani.


Käyttäjänä haluan listata esineet, joiden muste on alhainen, jotta tiedän mitä minun tulee ostaa lisää.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                        " FROM Item"
                        " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                        " JOIN Ptype ON Item.ptype_id = Ptype.id"
                        " WHERE Item.account_id = " + user_id +
                        " AND Item.lowink = '1'"
                        " ORDER BY Colorcode.code"
```


Käyttäjänä haluan pystyä tarkistamaan, omistanko jonkin tietyn värikoodin esineitä, etten osta vahingossa duplikaatteja.
```
SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                        " FROM Item"
                        " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                        " JOIN Ptype ON Item.ptype_id = Ptype.id"
                        " WHERE Colorcode.code LIKE UPPER('%" + searchterm + "%')"
                        " AND Item.account_id = " + user_id +
                        " ORDER BY Colorcode.code"
```

Käyttäjänä haluan merkitä lempisävyni, jotta voin ottaa nämä kynät heti esille.



Käyttäjänä haluan merkitä varjostussävyt, jotta en harhaudu käyttämään vääriä värejä paperille."




