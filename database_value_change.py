import sys
import database_design

def add_city():
    database_design.cursor.execute("INSERT INTO CITIES VALUES(NULL, 'Izmir')")
    database_design.con.commit()


def add_compay():
    database_design.cursor.execute("INSERT INTO COMPANIES VALUES(NULL, 'Ugur', 'Ayaz', 'Istanbul', '111')")
    database_design.con.commit()


def add_goods():
    database_design.cursor.execute("INSERT INTO GOODS VALUES(NULL, 'Corn', 'Dry')")
    database_design.con.commit()


def add_trucks():
    database_design.cursor.execute("INSERT INTO TRUCKS VALUES(NULL, 'Mercedes', '34DGZ13', '15000', 'Trailer')")
    database_design.con.commit()


def add_drivers():
    database_design.cursor.execute("INSERT INTO DRIVERS VALUES(NULL, 'Yusur', 'Bacilar', 'Istanbul', '555')")
    database_design.con.commit()


def add_businness():
    database_design.cursor.execute("INSERT INTO BUSINESS VALUES(NULL, 'X', 'Bursa', 'Izmir', 'Karpuz', '4000', '1600', '15.01.2017', '17.01.2017')")
    database_design.con.commit()


add_city()
add_compay()
add_goods()
add_trucks()
add_drivers()
add_businness()