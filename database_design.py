import sys
import sqlite3
# -*- coding: utf-8 -*-

con = sqlite3.connect('transport.db')


cursor = con.cursor()


def newtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS CITIES (  Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "CityName TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS COMPANIES (Id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   " CompanyName TEXT, "
                   " CompanyContact TEXT,"
                   " CompanyCity TEXT,"
                   " CompanyPhone TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS GOODS (Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   " GoodsName TEXT,"
                   " GoodsFeatures TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS TRUCKS (Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "TuckName TEXT, "
                   "TruckPlate TEXT, "
                   "TruckCapacity INT, "
                   "TruckFeatures TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS DRIVERS (Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "DriverName TEXT, "
                   "DriverAddress TEXT, "
                   "DriverCity TEXT, "
                   "DriverPhone)")
    cursor.execute("CREATE TABLE IF NOT EXISTS BUSINESS (Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "BusinessName TEXT, "
                   "BusinessOrigin TEXT, "
                   "BusinessDestination TEXT, "
                   "BusinessGoods TEXT, "
                   "BusinessWeight INT, "
                   "BusinessInvoices INT, "
                   "BusinessStartingDate TEXT, "
                   "BusinessEndDate TEXT)")


def newvalue():
    #cursor.execute("INSERT INTO CITY VALUES (NULL, 'Ankara')")
    con.commit()
    con.close()


newtable()
#newvalue()






