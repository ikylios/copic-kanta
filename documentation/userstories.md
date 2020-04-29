## Toiminnallisuuksia

* Haluan nähdä listan kaikista Copic-tuotteista, jotta voin suunnitella toivelistaani.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Colorcode.id, Ptype.id"
                " FROM Cc_ptype"
                " JOIN Colorcode ON Cc_ptype.colorcode_id = Colorcode.id"
                " JOIN Ptype ON Cc_ptype.ptype_id = Ptype.id"
                " ORDER BY Colorcode.code"
```


* Haluan listata esineet, joiden muste on alhainen, jotta tiedän mitä minun tulee ostaa lisää.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                        " FROM Item"
                        " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                        " JOIN Ptype ON Item.ptype_id = Ptype.id"
                        " WHERE Item.account_id = " + user_id +
                        " AND Item.lowink = '1'"
                        " ORDER BY Colorcode.code"
```


* Haluan pystyä tarkistamaan, omistanko jonkin tietyn värikoodin esineitä, etten osta vahingossa duplikaatteja.
```
SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.id"
                        " FROM Item"
                        " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                        " JOIN Ptype ON Item.ptype_id = Ptype.id"
                        " WHERE Colorcode.code LIKE UPPER('%" + searchterm + "%')"
                        " AND Item.account_id = " + user_id +
                        " ORDER BY Colorcode.code"
```

* Haluan merkitä lempisävyni, jotta voin ottaa nämä kynät heti esille.


* Haluan nähdä suosituimmat värikoodit, jotta voin inspiroitua muiden käyttäjien vaikutuksesta.
```
"SELECT Colorcode.code, Colorcode.name, COUNT(Colorcode.id)"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " GROUP BY Colorcode.id"
```

