## Toiminnallisuuksia

* Haluan nähdä listan kaikista Copic-tuotteista.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Colorcode.id, Ptype.id"
                " FROM Cc_ptype"
                " JOIN Colorcode ON Cc_ptype.colorcode_id = Colorcode.id"
                " JOIN Ptype ON Cc_ptype.ptype_id = Ptype.id"
                " ORDER BY Colorcode.code"
```

* Haluan listata omat esineeni.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.favorite, Item.date_created, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " ORDER BY Item.date_created"
```

* Haluan listata esineeni, joiden muste on alhainen, jotta tiedän mitä minun tulee ostaa lisää.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.favorite, Item.date_created, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " AND Item.lowink = '1'"
                    " ORDER BY Colorcode.code"
```

* Haluan listata lempisävyni.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.favorite, Item.date_created, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " AND Item.favorite = '1'"
                    " ORDER BY Colorcode.code"
```

* Haluan pystyä tarkistamaan, omistanko jonkin tietyn värikoodin esineitä, etten osta vahingossa duplikaatteja.
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.favorite, Item.date_created, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " AND Colorcode.code " + condition +
                    " ORDER BY Colorcode.code"
```

* Haluan listata esineeni uutuusjärjestyksessä. 
```
"SELECT Colorcode.code, Colorcode.name, Ptype.name, Item.lowink, Item.favorite, Item.date_created, Item.id"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " JOIN Ptype ON Item.ptype_id = Ptype.id"
                    " WHERE Item.account_id = " + user_id +
                    " ORDER BY Item.date_created DESC"
```

* Haluan nähdä suosituimmat värikoodit, jotta voin inspiroitua muiden käyttäjien vaikutuksesta.
```
"SELECT Colorcode.code, Colorcode.name, COUNT(Colorcode.id)"
                    " FROM Item"
                    " JOIN Colorcode ON Item.colorcode_id = Colorcode.id"
                    " GROUP BY Colorcode.id"
```

