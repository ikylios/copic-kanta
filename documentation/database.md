# Tietokannasta


### Tietokantarakenne

![tietokantakaavio](https://github.com/ikylios/copic-kanta/blob/master/documentation/tietokantakaavio.png)


### CREATE TABLE -lauseet
```

CREATE TABLE ptype (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE colorcode (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	code VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
);
CREATE TABLE item (
	id INTEGER NOT NULL, 
	lowink BOOLEAN NOT NULL, 
	favorite BOOLEAN NOT NULL, 
	date_created DATETIME, 
	account_id INTEGER NOT NULL, 
	colorcode_id INTEGER NOT NULL, 
	ptype_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (lowink IN (0, 1)), 
	CHECK (favorite IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(colorcode_id) REFERENCES colorcode (id), 
	FOREIGN KEY(ptype_id) REFERENCES ptype (id)
);
CREATE TABLE cc_ptype (
	colorcode_id INTEGER NOT NULL, 
	ptype_id INTEGER NOT NULL, 
	PRIMARY KEY (colorcode_id, ptype_id), 
	FOREIGN KEY(colorcode_id) REFERENCES colorcode (id), 
	FOREIGN KEY(ptype_id) REFERENCES ptype (id)
);

```


Tärkeää on siis huomata että luokkaa `User` vastaava taulu on nimellä `Account.`
