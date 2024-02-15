#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl 
import folium
import branca
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import Dash, html
import base64


# In[2]:


# load data
df_sale = pd.read_csv("Sale_prices_Austria.csv")
df_rent = pd.read_csv("Rent_prices_Austria.csv")


# In[3]:


# add new column and merge datasets
type_s = "sale"
type_r = "rent"
df_sale["type"] = type_s
df_rent["type"] = type_r
frames = [df_sale, df_rent]
df = pd.concat(frames)


# In[4]:


# strip unwanted characters
df = df.replace("€", "", regex=True)
df = df.replace("Zi.", "", regex=True)
df = df.replace("m²", "", regex=True)
df = df.replace("location", "", regex=True)


# In[5]:


# define and correct entries
df = df.replace("Wien(Stadt) (Innere Stadt)", "Wien (Innere Stadt)")

checkLeopoldstadt = df["location"].str.contains("Leopoldstadt")
df["location"] = np.where(checkLeopoldstadt, "Wien (Leopoldstadt)", df["location"])

checkLandstrasse = df["location"].str.contains("Landstraße")
df["location"] = np.where(checkLandstrasse, "Wien (Landstraße)", df["location"])

checkWieden = df["location"].str.contains("Wieden")
df["location"] = np.where(checkWieden, "Wien (Wieden)", df["location"])

checkMargareten = df["location"].str.contains("Margareten")
df["location"] = np.where(checkMargareten, "Wien (Margareten)", df["location"])

checkMariahilf = df["location"].str.contains("Mariahilf")
df["location"] = np.where(checkMariahilf, "Wien (Mariahilf)", df["location"])

checkNeubau = df["location"].str.contains("Neubau")
df["location"] = np.where(checkNeubau, "Wien (Neubau)", df["location"])

checkJosefstadt = df["location"].str.contains("Josefstadt")
df["location"] = np.where(checkJosefstadt, "Wien (Josefstadt)", df["location"])

checkAlsergrund = df["location"].str.contains("Alsergrund")
df["location"] = np.where(checkAlsergrund, "Wien (Alsergrund)", df["location"])

checkFavoriten = df["location"].str.contains("Favoriten")
df["location"] = np.where(checkFavoriten, "Wien (Favoriten)", df["location"])

checkSimmering = df["location"].str.contains("Simmering")
df["location"] = np.where(checkSimmering, "Wien (Simmering)", df["location"])

checkMeidling = df["location"].str.contains("Meidling")
df["location"] = np.where(checkMeidling, "Wien (Meidling)", df["location"])

checkHietzing = df["location"].str.contains("Hietzing")
df["location"] = np.where(checkHietzing, "Wien (Hietzing)", df["location"])

checkPenzing = df["location"].str.contains("Penzing")
df["location"] = np.where(checkPenzing, "Wien (Penzing)", df["location"])

checkRudolfsheimfünfhaus = df["location"].str.contains("Rudolfsheim-Fünfhaus")
df["location"] = np.where(checkRudolfsheimfünfhaus, "Wien (Rudolfsheim-Fünfhaus)", df["location"])

checkOttakring = df["location"].str.contains("Ottakring")
df["location"] = np.where(checkOttakring, "Wien (Ottakring)", df["location"])

checkHernals = df["location"].str.contains("Hernals")
df["location"] = np.where(checkHernals, "Wien (Hernals)", df["location"])

checkWähring = df["location"].str.contains("Währing")
df["location"] = np.where(checkWähring, "Wien (Währing)", df["location"])

checkDöbling = df["location"].str.contains("Döbling")
df["location"] = np.where(checkDöbling, "Wien (Döbling)", df["location"])

checkBrigittenau = df["location"].str.contains("Brigittenau")
df["location"] = np.where(checkBrigittenau, "Wien (Brigittenau)", df["location"])

checkFloridsdorf = df["location"].str.contains("Floridsdorf")
df["location"] = np.where(checkFloridsdorf, "Wien (Floridsdorf)", df["location"])

checkDonaustadt = df["location"].str.contains("Donaustadt")
df["location"] = np.where(checkDonaustadt, "Wien (Donaustadt)", df["location"])

checkLiesing = df["location"].str.contains("Liesing")
df["location"] = np.where(checkLiesing, "Wien (Liesing)", df["location"])

checkKlagenfurt = df["location"].str.contains("Klagenfurt")
df["location"] = np.where(checkKlagenfurt, "Klagenfurt", df["location"])

checkInnsbruck = df["location"].str.contains("Innsbruck")
df["location"] = np.where(checkInnsbruck, "Innsbruck", df["location"])

checkSalzburg = df["location"].str.contains("Salzburg")
df["location"] = np.where(checkSalzburg, "Salzburg", df["location"])

checkGraz = df["location"].str.contains("Graz")
df["location"] = np.where(checkGraz, "Graz", df["location"])

checkLinz = df["location"].str.contains("Linz")
df["location"] = np.where(checkLinz, "Linz", df["location"])

checkVillach = df["location"].str.contains("Villach")
df["location"] = np.where(checkVillach, "Villach", df["location"])

checkPölten = df["location"].str.contains("Pölten")
df["location"] = np.where(checkPölten, "SLinz", df["location"])

checkLeopoldstadt = df["location"].str.contains("Leopoldstadt")
df["location"] = np.where(checkLeopoldstadt, "Wien (Leopoldstadt)", df["location"])

checkLandstrasse = df["location"].str.contains("Landstraße")
df["location"] = np.where(checkLandstrasse, "Wien (Landstraße)", df["location"])

checkWieden = df["location"].str.contains("Wieden")
df["location"] = np.where(checkWieden, "Wien (Wieden)", df["location"])

checkMargareten = df["location"].str.contains("Margareten")
df["location"] = np.where(checkMargareten, "Wien (Margareten)", df["location"])

checkMariahilf = df["location"].str.contains("Mariahilf")
df["location"] = np.where(checkMariahilf, "Wien (Mariahilf)", df["location"])

checkNeubau = df["location"].str.contains("Neubau")
df["location"] = np.where(checkNeubau, "Wien (Neubau)", df["location"])

checkJosefstadt = df["location"].str.contains("Josefstadt")
df["location"] = np.where(checkJosefstadt, "Wien (Josefstadt)", df["location"])

checkAlsergrund = df["location"].str.contains("Alsergrund")
df["location"] = np.where(checkAlsergrund, "Wien (Alsergrund)", df["location"])

checkFavoriten = df["location"].str.contains("Favoriten")
df["location"] = np.where(checkFavoriten, "Wien (Favoriten)", df["location"])

checkSimmering = df["location"].str.contains("Simmering")
df["location"] = np.where(checkSimmering, "Wien (Simmering)", df["location"])

checkMeidling = df["location"].str.contains("Meidling")
df["location"] = np.where(checkMeidling, "Wien (Meidling)", df["location"])

checkHietzing = df["location"].str.contains("Hietzing")
df["location"] = np.where(checkHietzing, "Wien (Hietzing)", df["location"])

checkPenzing = df["location"].str.contains("Penzing")
df["location"] = np.where(checkPenzing, "Wien (Penzing)", df["location"])

checkRudolfsheimfünfhaus = df["location"].str.contains("Rudolfsheim-Fünfhaus")
df["location"] = np.where(checkRudolfsheimfünfhaus, "Wien (Rudolfsheim-Fünfhaus)", df["location"])

checkOttakring = df["location"].str.contains("Ottakring")
df["location"] = np.where(checkOttakring, "Wien (Ottakring)", df["location"])

checkHernals = df["location"].str.contains("Hernals")
df["location"] = np.where(checkHernals, "Wien (Hernals)", df["location"])

checkWähring = df["location"].str.contains("Währing")
df["location"] = np.where(checkWähring, "Wien (Währing)", df["location"])

checkDöbling = df["location"].str.contains("Döbling")
df["location"] = np.where(checkDöbling, "Wien (Döbling)", df["location"])

checkBrigittenau = df["location"].str.contains("Brigittenau")
df["location"] = np.where(checkBrigittenau, "Wien (Brigittenau)", df["location"])

checkFloridsdorf = df["location"].str.contains("Floridsdorf")
df["location"] = np.where(checkFloridsdorf, "Wien (Floridsdorf)", df["location"])

checkDonaustadt = df["location"].str.contains("Donaustadt")
df["location"] = np.where(checkDonaustadt, "Wien (Donaustadt)", df["location"])

checkLiesing = df["location"].str.contains("Liesing")
df["location"] = np.where(checkLiesing, "Wien (Liesing)", df["location"])

checkKlagenfurt = df["location"].str.contains("Klagenfurt")
df["location"] = np.where(checkKlagenfurt, "Klagenfurt", df["location"])

checkInnsbruck = df["location"].str.contains("Innsbruck")
df["location"] = np.where(checkInnsbruck, "Innsbruck", df["location"])

checkSalzburg = df["location"].str.contains("Salzburg")
df["location"] = np.where(checkSalzburg, "Salzburg", df["location"])

checkGraz = df["location"].str.contains("Graz")
df["location"] = np.where(checkGraz, "Graz", df["location"])

checkLinz = df["location"].str.contains("Linz")
df["location"] = np.where(checkLinz, "Linz", df["location"])

checkVillach = df["location"].str.contains("Villach")
df["location"] = np.where(checkVillach, "Villach", df["location"])

checkPölten = df["location"].str.contains("Pölten")
df["location"] = np.where(checkPölten, "SLinz", df["location"])

checkLeopoldstadt = df["location"].str.contains("Leopoldstadt")
df["location"] = np.where(checkLeopoldstadt, "Wien (Leopoldstadt)", df["location"])

checkLandstrasse = df["location"].str.contains("Landstraße")
df["location"] = np.where(checkLandstrasse, "Wien (Landstraße)", df["location"])

checkWieden = df["location"].str.contains("Wieden")
df["location"] = np.where(checkWieden, "Wien (Wieden)", df["location"])

checkMargareten = df["location"].str.contains("Margareten")
df["location"] = np.where(checkMargareten, "Wien (Margareten)", df["location"])

checkMariahilf = df["location"].str.contains("Mariahilf")
df["location"] = np.where(checkMariahilf, "Wien (Mariahilf)", df["location"])

checkNeubau = df["location"].str.contains("Neubau")
df["location"] = np.where(checkNeubau, "Wien (Neubau)", df["location"])

checkJosefstadt = df["location"].str.contains("Josefstadt")
df["location"] = np.where(checkJosefstadt, "Wien (Josefstadt)", df["location"])

checkAlsergrund = df["location"].str.contains("Alsergrund")
df["location"] = np.where(checkAlsergrund, "Wien (Alsergrund)", df["location"])

checkFavoriten = df["location"].str.contains("Favoriten")
df["location"] = np.where(checkFavoriten, "Wien (Favoriten)", df["location"])

checkSimmering = df["location"].str.contains("Simmering")
df["location"] = np.where(checkSimmering, "Wien (Simmering)", df["location"])

checkMeidling = df["location"].str.contains("Meidling")
df["location"] = np.where(checkMeidling, "Wien (Meidling)", df["location"])

checkHietzing = df["location"].str.contains("Hietzing")
df["location"] = np.where(checkHietzing, "Wien (Hietzing)", df["location"])

checkPenzing = df["location"].str.contains("Penzing")
df["location"] = np.where(checkPenzing, "Wien (Penzing)", df["location"])

checkRudolfsheimfünfhaus = df["location"].str.contains("Rudolfsheim-Fünfhaus")
df["location"] = np.where(checkRudolfsheimfünfhaus, "Wien (Rudolfsheim-Fünfhaus)", df["location"])

checkOttakring = df["location"].str.contains("Ottakring")
df["location"] = np.where(checkOttakring, "Wien (Ottakring)", df["location"])

checkHernals = df["location"].str.contains("Hernals")
df["location"] = np.where(checkHernals, "Wien (Hernals)", df["location"])

checkWähring = df["location"].str.contains("Währing")
df["location"] = np.where(checkWähring, "Wien (Währing)", df["location"])

checkDöbling = df["location"].str.contains("Döbling")
df["location"] = np.where(checkDöbling, "Wien (Döbling)", df["location"])

checkBrigittenau = df["location"].str.contains("Brigittenau")
df["location"] = np.where(checkBrigittenau, "Wien (Brigittenau)", df["location"])

checkFloridsdorf = df["location"].str.contains("Floridsdorf")
df["location"] = np.where(checkFloridsdorf, "Wien (Floridsdorf)", df["location"])

checkDonaustadt = df["location"].str.contains("Donaustadt")
df["location"] = np.where(checkDonaustadt, "Wien (Donaustadt)", df["location"])

checkLiesing = df["location"].str.contains("Liesing")
df["location"] = np.where(checkLiesing, "Wien (Liesing)", df["location"])

checkKlagenfurt = df["location"].str.contains("Klagenfurt")
df["location"] = np.where(checkKlagenfurt, "Klagenfurt", df["location"])

checkInnsbruck = df["location"].str.contains("Innsbruck")
df["location"] = np.where(checkInnsbruck, "Innsbruck", df["location"])

checkSalzburg = df["location"].str.contains("Salzburg")
df["location"] = np.where(checkSalzburg, "Salzburg", df["location"])

checkGraz = df["location"].str.contains("Graz")
df["location"] = np.where(checkGraz, "Graz", df["location"])

checkLinz = df["location"].str.contains("Linz")
df["location"] = np.where(checkLinz, "Linz", df["location"])

checkVillach = df["location"].str.contains("Villach")
df["location"] = np.where(checkVillach, "Villach", df["location"])

checkPölten = df["location"].str.contains("Pölten")
df["location"] = np.where(checkPölten, "St. Pölten", df["location"])

checkKrems = df["location"].str.contains("Krems")
df["location"] = np.where(checkKrems, "Krems an der Donau", df["location"])

checkSteyr = df["location"].str.contains("Steyr")
df["location"] = np.where(checkSteyr, "Steyr", df["location"])

checkVelden = df["location"].str.contains("Velden")
df["location"] = np.where(checkVelden, "Velden am Wörthersee", df["location"])

checkWaidhofen = df["location"].str.contains("Waidhofen")
df["location"] = np.where(checkWaidhofen, "Waidhofen an der Ybbs", df["location"])

checkWels = df["location"].str.contains("Wels")
df["location"] = np.where(checkWels, "Wels", df["location"])

df = df.replace("Sankt Georgen ob Murau / Sankt Lorenzen ob Murau", "Sankt Lorenzen ob Murau")
df = df.replace("AURACH", "Aurach bei Kitzbühel")
df = df.replace("Aigen / Staudach", "Aigen")
df = df.replace("Arzl (Arzl)", "Innsbruck")
df = df.replace("Aschau, lertal", "Aschau")
df = df.replace("Attnang Puchheim", "Attnang-Puchheim")
df = df.replace("Blumau Neurißof", "Blumau-Neurißof")
df = df.replace("Bruck an der Glocknerstraße", "Bruck an der Großglocknerstraße")
df = df.replace("Christkindl (Christkindl)", "Christkindl")
df = df.replace("Deutsch Wagram", "Deutsch-Wagram")
df = df.replace("ELLMAU", "Ellmau")
df = df.replace("Ebensee am Traunsee", "Ebensee")
df = df.replace("Eisenstadt(Stadt) (Eisenstadt)", "Eisenstadt")
df = df.replace("Eisenstadt (Eisenstadt)", "Eisenstadt")
df = df.replace("GOING", "Going")
df = df.replace("Glasenbach (Aigen I)", "Glasenbach")
df = df.replace("Gneixendorf (Krems an der Donau)", "Krems an der Donau")
df = df.replace("Going am Wilden Kaiser", "Going")
df = df.replace("Gois (Maxglan)", "Salzburg")
df = df.replace("Hoch-Liebenfels (Lend)", "Lend")
df = df.replace("Hofstetten, Pielach", "Hofstetten")
df = df.replace("Hötting (Hötting)", "Innsbruck")
df = df.replace("Igls (Igls)", "Igls")
df = df.replace("Innerschwand am Mondsee / Au", "Innerschwand")
df = df.replace("Kematen/Ybbs", "Kematen an der Ybbs")
df = df.replace("Kleinkirchheim / Bach", "Kleinkirchheim")
df = df.replace("Leogang / Rain", "Leogang")
df = df.replace("Mannersdorf/Leithagebirge", "Mannersdorf am Leithagebirge")
df = df.replace("Maria Wörth / Dellach", "Maria Wörth")
df = df.replace("Mühlau (Mühlau)", "Innsbruck")
df = df.replace("Pottenbrunn (Pottenbrunn)", "Pottenbrunn")
df = df.replace("SCHEFFAU", "Scheffau")
df = df.replace("ST. ULRICH", "St. Ulrich")
df = df.replace("Sankt Johann im Pongau / Plankenau", "Sankt Johann im Pongau")
df = df.replace("Schwarzach", "Schwarzach im Pongau")
df = df.replace("Schwechat / Kledering", "Schwechat")
df = df.replace("Schärding Innere Stadt", "Schärding")
df = df.replace("Seeboden am Millstätter See", "Seeboden")
df = df.replace("Seefeld in Tirol", "Seefeld")
df = df.replace("Seefeld in Tirol / Mösern", "Seefeld")
df = df.replace("St. Stefan", "St. Stefan ob Leoben")
df = df.replace("Stattegg (Andritz)", "Stattegg")
df = df.replace("Stein an der Donau (Stein an der Donau)", "Stein an der Donau")
df = df.replace("Steinach am Brenner / Mauern", "Steinach am Brenner")
df = df.replace("Viktring (Viktring)", "Klagenfurt")
df = df.replace("Wien / Innere Stadt (Innere Stadt)", "Wien (Innere Stadt)")
df = df.replace("Wien, Innere Stadt (Innere Stadt)", "Wien (Innere Stadt)")
df = df.replace("Wien, Innere Stadt / Wien 1., Innere Stadt (Innere Stadt)", "Wien (Innere Stadt)")
df = df.replace("Wien,Innere Stadt (Innere Stadt)", "Wien (Innere Stadt)")
df = df.replace("Wiener Neutstadt", "Wiener Neustadt")
df = df.replace("Wildschönau-Niederau", "Wildschönau")
df = df.replace("Wr. Neudorf", "Wiener Neudorf")
df = df.replace("Zelll am See", "Zell am See")
df = df.replace("KIRCHBERG", "Kirchberg")
df = df.replace("KITZBÜHEL", "Kitzbühel")
df = df.replace("Linz (Linz)", "Linz")
df = df.replace("St. Anton a/A", "St. Anton")
df = df.replace("Krems an der Donau (Krems an der Donau)", "Krems an der Donau")
df = df.replace("Velden am Wörther See / Augsdorf", "Velden am Wörther See")
df = df.replace("SLinz", "Linz")
df = df.replace("Eisenstadt (Sankt Georgen am Leithagebirge)", "Eisenstadt")
df = df.replace("", "")
df = df.replace("Wien(Stadt) (Innere Stadt)", "Wien (Innere Stadt)")


# In[6]:


# identify units with no values
df = df.replace("NaN", np.nan)
df = df.replace("auf Anfrage", np.nan)


# In[7]:


# delete false values
df = df.reset_index()
df = df.drop([18011, 19354, 16463, 2726, 10247, 19085])
df = df.reset_index()
df = df.dropna()
df = df.drop(df[df["location"] == "checkteil- oder vollrenoviert, Kelleranteil"].index)
df = df.drop(df[df["location"] == "l"].index)


# In[8]:


# change the data types
df["price"] = df["price"].str.replace(".", "").str.replace(",", ".").astype(float)
df["rooms"] = df["rooms"].astype(float)
df["area"] = df["area"].astype(float)


# In[9]:


# add new column
df["price per m2"] = df["price"] / df["area"]
df = df.round(2)


# In[10]:


# add new column and assign regions
region_mapping = {
    "Eisenstadt": ("Burgenland", "Eisenstadt (Stadt)"),
    "Donnerskirchen": ("Burgenland", "Eisenstadt-Umgebung"),
    "Mörbisch": ("Burgenland", "Eisenstadt-Umgebung"),
    "Oggau am Neusiedler See": ("Burgenland", "Eisenstadt-Umgebung"),
    "Purbach am Neusiedler See": ("Burgenland", "Eisenstadt-Umgebung"),
    "Siegendorf": ("Burgenland", "Eisenstadt-Umgebung"),
    "Wimpassing an der Leitha": ("Burgenland", "Eisenstadt-Umgebung"),
    "Stegersbach": ("Burgenland", "Güssing"),
    "Jennersdorf": ("Burgenland", "Jennersdorf"),
    "Minihof-Liebau": ("Burgenland", "Jennersdorf"),
    "Rudersdorf": ("Burgenland", "Jennersdorf"),
    "Forchtenstein": ("Burgenland", "Mattersburg"),
    "Mattersburg": ("Burgenland", "Mattersburg"),
    "Neudörfl": ("Burgenland", "Mattersburg"),
    "Pöttsching": ("Burgenland", "Mattersburg"),
    "Wiesen": ("Burgenland", "Mattersburg"),
    "Apetlon": ("Burgenland", "Neusiedl am See"),
    "Bruckneudorf": ("Burgenland", "Neusiedl am See"),
    "Gols": ("Burgenland", "Neusiedl am See"),
    "Mönchhof": ("Burgenland", "Neusiedl am See"),
    "Neusiedl am See": ("Burgenland", "Neusiedl am See"),
    "Podersdorf am See": ("Burgenland", "Neusiedl am See"),
    "Tadten": ("Burgenland", "Neusiedl am See"),
    "Weiden am See": ("Burgenland", "Neusiedl am See"),
    "Winden am See": ("Burgenland", "Neusiedl am See"),
    "Draßmarkt": ("Burgenland", "Oberpullendorf"),
    "Lutzmannsburg": ("Burgenland", "Oberpullendorf"),
    "Litzelsdorf": ("Burgenland", "Oberwart"),
    "Loipersdorf-Kitzladen": ("Burgenland", "Oberwart"),
    "Markt Neuhodis": ("Burgenland", "Oberwart"),
    "Oberwart": ("Burgenland", "Oberwart"),
    "Stadtschlaining": ("Burgenland", "Oberwart"),
    "Wolfau": ("Burgenland", "Oberwart"),
    "Klagenfurt": ("Kärnten", "Klagenfurt (Stadt)"),
    "Villach": ("Kärnten", "Villach (Stadt)"),
    "Lesachtal": ("Kärnten", "Hermagor"),
    "Ferlach": ("Kärnten", "Klagenfurt Land"),
    "Köttmannsdorf": ("Kärnten", "Klagenfurt Land"),
    "Krumpendorf am Wörthersee": ("Kärnten", "Klagenfurt Land"),
    "Maria Saal": ("Kärnten", "Klagenfurt Land"),
    "Maria Wörth": ("Kärnten", "Klagenfurt Land"),
    "Pörtschach am Wörther See": ("Kärnten", "Klagenfurt Land"),
    "Schiefling am Wörthersee": ("Kärnten", "Klagenfurt Land"),
    "Techelsberg am Wörther See": ("Kärnten", "Klagenfurt Land"),
    "Velden am Wörthersee": ("Kärnten", "Villach Land"),
    "Friesach": ("Kärnten", "Sankt Veit an der Glan"),
    "Micheldorf": ("Kärnten", "Sankt Veit an der Glan"),
    "Mölbling": ("Kärnten", "Sankt Veit an der Glan"),
    "St. Veit an der Glan": ("Kärnten", "Sankt Veit an der Glan"),
    "Bad Kleinkirchheim": ("Kärnten", "Spittal an der Drau"),
    "Dellach im Drautal": ("Kärnten", "Spittal an der Drau"),
    "Greifenburg": ("Kärnten", "Spittal an der Drau"),
    "Heiligenblut am Großglockner": ("Kärnten", "Spittal an der Drau"),
    "Lendorf": ("Kärnten", "Spittal an der Drau"),
    "Obervellach": ("Kärnten", "Spittal an der Drau"),
    "Radenthein": ("Kärnten", "Spittal an der Drau"),
    "Spittal an der Drau": ("Kärnten", "Spittal an der Drau"),
    "Krumpendorf": ("Kärnten", "Klagenfurt Land"),
    "Weißensee": ("Kärnten", "Spittal an der Drau"),
    "Winklern": ("Kärnten", "Spittal an der Drau"),
    "Arnoldstein": ("Kärnten", "Villach Land"),
    "Bad Bleiberg": ("Kärnten", "Villach Land"),
    "Millstatt": ("Kärnten", "Spittal an der Drau"),
    "Finkenstein am Faaker See": ("Kärnten", "Villach Land"),
    "Paternion": ("Kärnten", "Villach Land"),
    "Treffen am Ossiacher See": ("Kärnten", "Villach Land"),
    "Eberndorf": ("Kärnten", "Völkermarkt"),
    "Gallizien": ("Kärnten", "Völkermarkt"),
    "St. Kanzian am Klopeiner See": ("Kärnten", "Völkermarkt"),
    "Völkermarkt": ("Kärnten", "Völkermarkt"),
    "Lavamünd": ("Kärnten", "Wolfsberg"),
    "St. Andrä": ("Kärnten", "Wolfsberg"),
    "Wolfsberg": ("Kärnten", "Wolfsberg"),
    "Feldkirchen in Kärnten": ("Kärnten", "Feldkirchen"),
    "Ossiach": ("Kärnten", "Feldkirchen"),
    "Steindorf am Ossiacher See": ("Kärnten", "Feldkirchen"),
    "Bludenz": ("Vorarlberg", "Bludenz"),
    "Bludesch": ("Vorarlberg", "Bludenz"),
    "Bürs": ("Vorarlberg", "Bludenz"),
    "Dalaas": ("Vorarlberg", "Bludenz"),
    "Ludesch": ("Vorarlberg", "Bludenz"),
    "Nenzing": ("Vorarlberg", "Bludenz"),
    "Nüziders": ("Vorarlberg", "Bludenz"),
    "Schruns": ("Vorarlberg", "Bludenz"),
    "Thüringen": ("Vorarlberg", "Bludenz"),
    "Tschagguns": ("Vorarlberg", "Bludenz"),
    "Vandans": ("Vorarlberg", "Bludenz"),
    "Andelsbuch": ("Vorarlberg", "Bregenz"),
    "Bregenz": ("Vorarlberg", "Bregenz"),
    "Egg": ("Vorarlberg", "Bregenz"),
    "Fußach": ("Vorarlberg", "Bregenz"),
    "Hard": ("Vorarlberg", "Bregenz"),
    "Höchst": ("Vorarlberg", "Bregenz"),
    "Hohenweiler": ("Vorarlberg", "Bregenz"),
    "Kennelbach": ("Vorarlberg", "Bregenz"),
    "Langen bei Bregenz": ("Vorarlberg", "Bregenz"),
    "Lauterach": ("Vorarlberg", "Bregenz"),
    "Lochau": ("Vorarlberg", "Bregenz"),
    "Mellau": ("Vorarlberg", "Bregenz"),
    "Mittelberg": ("Vorarlberg", "Bregenz"),
    "Reuthe": ("Vorarlberg", "Bregenz"),
    "Riefensberg": ("Vorarlberg", "Bregenz"),
    "Schröcken": ("Vorarlberg", "Bregenz"),
    "Schwarzenberg": ("Vorarlberg", "Bregenz"),
    "Sulzberg": ("Vorarlberg", "Bregenz"),
    "Wolfurt": ("Vorarlberg", "Bregenz"),
    "Dornbirn": ("Vorarlberg", "Dornbirn"),
    "Hohenems": ("Vorarlberg", "Dornbirn"),
    "Lustenau": ("Vorarlberg", "Dornbirn"),
    "Altach": ("Vorarlberg", "Feldkirch"),
    "Feldkirch": ("Vorarlberg", "Feldkirch"),
    "Frastanz": ("Vorarlberg", "Feldkirch"),
    "Fraxern": ("Vorarlberg", "Feldkirch"),
    "Göfis": ("Vorarlberg", "Feldkirch"),
    "Götzis": ("Vorarlberg", "Feldkirch"),
    "Klaus": ("Vorarlberg", "Feldkirch"),
    "Koblach": ("Vorarlberg", "Feldkirch"),
    "Mäder": ("Vorarlberg", "Feldkirch"),
    "Meiningen": ("Vorarlberg", "Feldkirch"),
    "Rankweil": ("Vorarlberg", "Feldkirch"),
    "Röthis": ("Vorarlberg", "Feldkirch"),
    "Satteins": ("Vorarlberg", "Feldkirch"),
    "Schlins": ("Vorarlberg", "Feldkirch"),
    "Sulz": ("Vorarlberg", "Feldkirch"),
    "Zwischenwasser": ("Vorarlberg", "Feldkirch"),
    "Innsbruck": ("Tirol", "Innsbruck (Stadt)"),
    "Lienz": ("Tirol", "Lienz"),
    "Arzl im Pitztal": ("Tirol", "Imst"),
    "Haiming": ("Tirol", "Imst"),
    "Imst": ("Tirol", "Imst"),
    "Karrösten": ("Tirol", "Imst"),
    "Längenfeld": ("Tirol", "Imst"),
    "Mieming": ("Tirol", "Imst"),
    "Mötz": ("Tirol", "Imst"),
    "Nassereith": ("Tirol", "Imst"),
    "Obsteig": ("Tirol", "Imst"),
    "Oetz": ("Tirol", "Imst"),
    "Rietz": ("Tirol", "Imst"),
    "Roppen": ("Tirol", "Imst"),
    "St. Leonhard im Pitztal": ("Tirol", "Imst"),
    "Silz": ("Tirol", "Imst"),
    "Umhausen": ("Tirol", "Imst"),
    "Absam": ("Tirol", "Innsbruck Land"),
    "Aldrans": ("Tirol", "Innsbruck Land"),
    "Axams": ("Tirol", "Innsbruck Land"),
    "Birgitz": ("Tirol", "Innsbruck Land"),
    "Ellbögen": ("Tirol", "Innsbruck Land"),
    "Fulpmes": ("Tirol", "Innsbruck Land"),
    "Götzens": ("Tirol", "Innsbruck Land"),
    "Grinzens": ("Tirol", "Innsbruck Land"),
    "Inzing": ("Tirol", "Innsbruck Land"),
    "Kematen in Tirol": ("Tirol", "Innsbruck Land"),
    "Kolsass": ("Tirol", "Innsbruck Land"),
    "Lans": ("Tirol", "Innsbruck Land"),
    "Leutasch": ("Tirol", "Innsbruck Land"),
    "Mils": ("Tirol", "Innsbruck Land"),
    "Mutters": ("Tirol", "Innsbruck Land"),
    "Neustift im Stubaital": ("Tirol", "Innsbruck Land"),
    "Pettnau": ("Tirol", "Innsbruck Land"),
    "Reith bei Seefeld": ("Tirol", "Innsbruck Land"),
    "Rum": ("Tirol", "Innsbruck Land"),
    "Schönberg im Stubaital": ("Tirol", "Innsbruck Land"),
    "Sellrain": ("Tirol", "Innsbruck Land"),
    "Sistrans": ("Tirol", "Innsbruck Land"),
    "Hall in Tirol": ("Tirol", "Innsbruck Land"),
    "Steinach am Brenner": ("Tirol", "Innsbruck Land"),
    "Telfes im Stubai": ("Tirol", "Innsbruck Land"),
    "Telfs": ("Tirol", "Innsbruck Land"),
    "Thaur": ("Tirol", "Innsbruck Land"),
    "Tulfes": ("Tirol", "Innsbruck Land"),
    "Völs": ("Tirol", "Innsbruck Land"),
    "Volders": ("Tirol", "Innsbruck Land"),
    "Wattens": ("Tirol", "Innsbruck Land"),
    "Matrei am Brenner": ("Tirol", "Innsbruck Land"),
    "Aurach bei Kitzbühel": ("Tirol", "Kitzbühel"),
    "Brixen im Thale": ("Tirol", "Kitzbühel"),
    "Fieberbrunn": ("Tirol", "Kitzbühel"),
    "Hopfgarten im Brixental": ("Tirol", "Kitzbühel"),
    "Itter": ("Tirol", "Kitzbühel"),
    "Jochberg": ("Tirol", "Kitzbühel"),
    "Seefeld": ("Tirol", "Innsbruck Land"),
    "Kirchberg in Tirol": ("Tirol", "Kitzbühel"),
    "Kirchdorf in Tirol": ("Tirol", "Kitzbühel"),
    "Kitzbühel": ("Tirol", "Kitzbühel"),
    "Kössen": ("Tirol", "Kitzbühel"),
    "Oberndorf in Tirol": ("Tirol", "Kitzbühel"),
    "Reith bei Kitzbühel": ("Tirol", "Kitzbühel"),
    "St. Johann in Tirol": ("Tirol", "Kitzbühel"),
    "Schwendt": ("Tirol", "Kitzbühel"),
    "Westendorf": ("Tirol", "Kitzbühel"),
    "Alpbach": ("Tirol", "Kufstein"),
    "Bad Häring": ("Tirol", "Kufstein"),
    "Brandenberg": ("Tirol", "Kufstein"),
    "Breitenbach am Inn": ("Tirol", "Kufstein"),
    "Brixlegg": ("Tirol", "Kufstein"),
    "Ebbs": ("Tirol", "Kufstein"),
    "Ellmau": ("Tirol", "Kufstein"),
    "Kirchbichl": ("Tirol", "Kufstein"),
    "Kramsach": ("Tirol", "Kufstein"),
    "Kundl": ("Tirol", "Kufstein"),
    "Langkampfen": ("Tirol", "Kufstein"),
    "Münster": ("Tirol", "Kufstein"),
    "Radfeld": ("Tirol", "Kufstein"),
    "Rattenberg": ("Tirol", "Kufstein"),
    "Reith im Alpbachtal": ("Tirol", "Kufstein"),
    "Scheffau am Wilden Kaiser": ("Tirol", "Kufstein"),
    "Schwoich": ("Tirol", "Kufstein"),
    "Söll": ("Tirol", "Kufstein"),
    "Thiersee": ("Tirol", "Kufstein"),
    "Walchsee": ("Tirol", "Kufstein"),
    "Wildschönau": ("Tirol", "Kufstein"),
    "Wörgl": ("Tirol", "Kufstein"),
    "Fließ": ("Tirol", "Landeck"),
    "Flirsch": ("Tirol", "Landeck"),
    "Galtür": ("Tirol", "Landeck"),
    "Grins": ("Tirol", "Landeck"),
    "Landeck": ("Tirol", "Landeck"),
    "Pfunds": ("Tirol", "Landeck"),
    "Prutz": ("Tirol", "Landeck"),
    "Serfaus": ("Tirol", "Landeck"),
    "Assling": ("Tirol", "Lienz"),
    "Kartitsch": ("Tirol", "Lienz"),
    "Matrei in Osttirol": ("Tirol", "Lienz"),
    "Nußdorf-Debant": ("Tirol", "Lienz"),
    "Going": ("Tirol", "Kitzbühel"),
    "Bach": ("Tirol", "Reutte"),
    "Ehrwald": ("Tirol", "Reutte"),
    "Elbigenalp": ("Tirol", "Reutte"),
    "Aschau": ("Tirol", "Schwaz"),
    "Höfen": ("Tirol", "Reutte"),
    "Lechaschau": ("Tirol", "Reutte"),
    "Pflach": ("Tirol", "Reutte"),
    "Reutte": ("Tirol", "Reutte"),
    "Tannheim": ("Tirol", "Reutte"),
    "Kufstein": ("Tirol", "Kufstein"),
    "Achenkirch": ("Tirol", "Schwaz"),
    "Eben am Achensee": ("Tirol", "Schwaz"),
    "Fügen": ("Tirol", "Schwaz"),
    "Fügenberg": ("Tirol", "Schwaz"),
    "Jenbach": ("Tirol", "Schwaz"),
    "Mayrhofen": ("Tirol", "Schwaz"),
    "Igls": ("Tirol", "Innsbruck Land"),
    "Rohrberg": ("Tirol", "Schwaz"),
    "Schlitters": ("Tirol", "Schwaz"),
    "Schwaz": ("Tirol", "Schwaz"),
    "Stans": ("Tirol", "Schwaz"),
    "Uderns": ("Tirol", "Schwaz"),
    "Vomp": ("Tirol", "Schwaz"),
    "Weer": ("Tirol", "Schwaz"),
    "Weerberg": ("Tirol", "Schwaz"),
    "Wiesing": ("Tirol", "Schwaz"),
    "Graz": ("Steiermark", "Graz (Stadt)"),
    "Frauental an der Laßnitz": ("Steiermark", "Deutschlandsberg"),
    "Lannach": ("Steiermark", "Deutschlandsberg"),
    "Pölfing-Brunn": ("Steiermark", "Deutschlandsberg"),
    "Deutschlandsberg": ("Steiermark", "Deutschlandsberg"),
    "Groß Sankt Florian": ("Steiermark", "Deutschlandsberg"),
    "Stainz": ("Steiermark", "Deutschlandsberg"),
    "Gratkorn": ("Steiermark", "Graz-Umgebung"),
    "Hausmannstätten": ("Steiermark", "Graz-Umgebung"),
    "Kumberg": ("Steiermark", "Graz-Umgebung"),
    "Lieboch": ("Steiermark", "Graz-Umgebung"),
    "Peggau": ("Steiermark", "Graz-Umgebung"),
    "Semriach": ("Steiermark", "Graz-Umgebung"),
    "Stattegg": ("Steiermark", "Graz-Umgebung"),
    "Übelbach": ("Steiermark", "Graz-Umgebung"),
    "Vasoldsberg": ("Steiermark", "Graz-Umgebung"),
    "Weinitzen": ("Steiermark", "Graz-Umgebung"),
    "Werndorf": ("Steiermark", "Graz-Umgebung"),
    "Deutschfeistritz": ("Steiermark", "Graz-Umgebung"),
    "Frohnleiten": ("Steiermark", "Graz-Umgebung"),
    "Gratwein-Straßengel": ("Steiermark", "Graz-Umgebung"),
    "Premstätten": ("Steiermark", "Graz-Umgebung"),
    "Allerheiligen bei Wildon": ("Steiermark", "Leibnitz"),
    "Sankt Andrä-Höch": ("Steiermark", "Leibnitz"),
    "Wagna": ("Steiermark", "Leibnitz"),
    "Sankt Georgen an der Stiefing": ("Steiermark", "Leibnitz"),
    "Wildon": ("Steiermark", "Leibnitz"),
    "Eisenerz": ("Steiermark", "Leoben"),
    "Kraubath an der Mur": ("Steiermark", "Leoben"),
    "Leoben": ("Steiermark", "Leoben"),
    "Sankt Michael in Obersteiermark": ("Steiermark", "Leoben"),
    "Traboch": ("Steiermark", "Leoben"),
    "Vordernberg": ("Steiermark", "Leoben"),
    "Trofaiach": ("Steiermark", "Leoben"),
    "Bad Aussee": ("Steiermark", "Liezen"),
    "Gröbming": ("Steiermark", "Liezen"),
    "Grundlsee": ("Steiermark", "Liezen"),
    "Haus": ("Steiermark", "Liezen"),
    "Lödersdorf": ("Steiermark", "Liezen"),
    "Trieben": ("Steiermark", "Liezen"),
    "Admont": ("Steiermark", "Liezen"),
    "Aich": ("Steiermark", "Liezen"),
    "Bad Mitterndorf": ("Steiermark", "Liezen"),
    "Michaelerberg-Pruggern": ("Steiermark", "Liezen"),
    "Mitterberg-Sankt Martin": ("Steiermark", "Liezen"),
    "Öblarn": ("Steiermark", "Liezen"),
    "Rottenmann": ("Steiermark", "Liezen"),
    "Schladming": ("Steiermark", "Liezen"),
    "Stainach-Pürgg": ("Steiermark", "Liezen"),
    "Murau": ("Steiermark", "Murau"),
    "Scheifling": ("Steiermark", "Murau"),
    "Voitsberg": ("Steiermark", "Voitsberg"),
    "Bärnbach": ("Steiermark", "Voitsberg"),
    "Edelschrott": ("Steiermark", "Voitsberg"),
    "Köflach": ("Steiermark", "Voitsberg"),
    "Maria Lankowitz": ("Steiermark", "Voitsberg"),
    "Hofstätten an der Raab": ("Steiermark", "Weiz"),
    "Miesenbach bei Birkfeld": ("Steiermark", "Weiz"),
    "Mitterdorf an der Raab": ("Steiermark", "Weiz"),
    "St. Kathrein am Hauenstein": ("Steiermark", "Weiz"),
    "St. Margarethen an der Raab": ("Steiermark", "Weiz"),
    "Sinabelkirchen": ("Steiermark", "Weiz"),
    "Gleisdorf": ("Steiermark", "Weiz"),
    "Passail": ("Steiermark", "Weiz"),
    "Sankt Ruprecht an der Raab": ("Steiermark", "Weiz"),
    "Weiz": ("Steiermark", "Weiz"),
    "Fohnsdorf": ("Steiermark", "Murtal"),
    "Zeltweg": ("Steiermark", "Murtal"),
    "Judenburg": ("Steiermark", "Murtal"),
    "Knittelfeld": ("Steiermark", "Murtal"),
    "Obdach": ("Steiermark", "Murtal"),
    "Spielberg": ("Steiermark", "Murtal"),
    "Krieglach": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Liezen": ("Steiermark", "Liezen"),
    "Turnau": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Bruck an der Mur": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Kapfenberg": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Kindberg": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Mariazell": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Mürzzuschlag": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Sankt Barbara im Mürztal": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Thörl": ("Steiermark", "Bruck-Mürzzuschlag"),
    "Friedberg": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Hartberg": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Ottendorf an der Rittschein": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Sankt Johann in der Haide": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Ehrenhausen": ("Steiermark", "Südoststeiermark"),
    "Bad Waltersdorf": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Fürstenfeld": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Ilz": ("Steiermark", "Südoststeiermark"),
    "Kaindorf": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Rohr bei Hartberg": ("Steiermark", "Hartberg-Fürstenfeld"),
    "Bad Gleichenberg": ("Steiermark", "Südoststeiermark"),
    "Bad Radkersburg": ("Steiermark", "Südoststeiermark"),
    "Fehring": ("Steiermark", "Südoststeiermark"),
    "Feldbach": ("Steiermark", "Südoststeiermark"),
    "Kirchberg an der Raab": ("Steiermark", "Südoststeiermark"),
    "Mureck": ("Steiermark", "Südoststeiermark"),
    "Paldau": ("Steiermark", "Südoststeiermark"),
    "Riegersburg": ("Steiermark", "Südoststeiermark"),
    "Straden": ("Steiermark", "Südoststeiermark"),
    "Salzburg": ("Salzburg", "Salzburg (Stadt)"),
    "Abtenau": ("Salzburg", "Hallein"),
    "Golling an der Salzach": ("Salzburg", "Hallein"),
    "Hallein": ("Salzburg", "Hallein"),
    "Kuchl": ("Salzburg", "Hallein"),
    "Siezenheim": ("Salzburg", "Hallein"),
    "Oberalm": ("Salzburg", "Hallein"),
    "Puch bei Hallein": ("Salzburg", "Hallein"),
    "Sankt Koloman": ("Salzburg", "Hallein"),
    "Anif": ("Salzburg", "Salzburg-Umgebung"),
    "Bergheim": ("Salzburg", "Salzburg-Umgebung"),
    "Bürmoos": ("Salzburg", "Salzburg-Umgebung"),
    "Ebenau": ("Salzburg", "Salzburg-Umgebung"),
    "Elixhausen": ("Salzburg", "Salzburg-Umgebung"),
    "Elsbethen": ("Salzburg", "Salzburg-Umgebung"),
    "Eugendorf": ("Salzburg", "Salzburg-Umgebung"),
    "Faistenau": ("Salzburg", "Salzburg-Umgebung"),
    "Grödig": ("Salzburg", "Salzburg-Umgebung"),
    "Hallwang": ("Salzburg", "Salzburg-Umgebung"),
    "Henndorf am Wallersee": ("Salzburg", "Salzburg-Umgebung"),
    "Koppl": ("Salzburg", "Salzburg-Umgebung"),
    "Lamprechtshausen": ("Salzburg", "Salzburg-Umgebung"),
    "Mattsee": ("Salzburg", "Salzburg-Umgebung"),
    "Neumarkt am Wallersee": ("Salzburg", "Salzburg-Umgebung"),
    "Obertrum am See": ("Salzburg", "Salzburg-Umgebung"),
    "Sankt Jakob am Thurn": ("Salzburg", "Salzburg-Umgebung"),
    "Plainfeld": ("Salzburg", "Salzburg-Umgebung"),
    "Sankt Gilgen": ("Salzburg", "Salzburg-Umgebung"),
    "Straßwalchen": ("Salzburg", "Salzburg-Umgebung"),
    "Strobl": ("Salzburg", "Salzburg-Umgebung"),
    "Thalgau": ("Salzburg", "Salzburg-Umgebung"),
    "Wals-Siezenheim": ("Salzburg", "Salzburg-Umgebung"),
    "Seekirchen am Wallersee": ("Salzburg", "Salzburg-Umgebung"),
    "Altenmarkt im Pongau": ("Salzburg", "Sankt Johann im Pongau"),
    "Bad Hofgastein": ("Salzburg", "Sankt Johann im Pongau"),
    "Bad Gastein": ("Salzburg", "Sankt Johann im Pongau"),
    "Bischofshofen": ("Salzburg", "Sankt Johann im Pongau"),
    "Dorfgastein": ("Salzburg", "Sankt Johann im Pongau"),
    "Eben im Pongau": ("Salzburg", "Sankt Johann im Pongau"),
    "Filzmoos": ("Salzburg", "Sankt Johann im Pongau"),
    "Flachau": ("Salzburg", "Sankt Johann im Pongau"),
    "Goldegg": ("Salzburg", "Sankt Johann im Pongau"),
    "Kleinarl": ("Salzburg", "Sankt Johann im Pongau"),
    "Mühlbach am Hochkönig": ("Salzburg", "Sankt Johann im Pongau"),
    "Pfarrwerfen": ("Salzburg", "Sankt Johann im Pongau"),
    "Radstadt": ("Salzburg", "Sankt Johann im Pongau"),
    "Sankt Johann im Pongau": ("Salzburg", "Sankt Johann im Pongau"),
    "Sankt Martin am Tennengebirge": ("Salzburg", "Sankt Johann im Pongau"),
    "Schwarzach im Pongau": ("Salzburg", "Sankt Johann im Pongau"),
    "Mariapfarr": ("Salzburg", "Tamsweg"),
    "Mauterndorf": ("Salzburg", "Tamsweg"),
    "St. Michael im Lungau": ("Salzburg", "Tamsweg"),
    "Sankt Margarethen im Lungau": ("Salzburg", "Tamsweg"),
    "Sankt Michael im Lungau": ("Salzburg", "Tamsweg"),
    "Nussdorf am Haunsberg": ("Salzburg", "Salzburg-Umgebung"),
    "Bramberg am Wildkogel": ("Salzburg", "Zell am See"),
    "Bruck an der Großglocknerstraße": ("Salzburg", "Zell am See"),
    "Hollersbach im Pinzgau": ("Salzburg", "Zell am See"),
    "Kaprun": ("Salzburg", "Zell am See"),
    "Lend": ("Salzburg", "Zell am See"),
    "Leogang": ("Salzburg", "Zell am See"),
    "Maishofen": ("Salzburg", "Zell am See"),
    "Mittersill": ("Salzburg", "Zell am See"),
    "Neukirchen am Großvenediger": ("Salzburg", "Zell am See"),
    "Niedernsill": ("Salzburg", "Zell am See"),
    "Piesendorf": ("Salzburg", "Zell am See"),
    "Rauris": ("Salzburg", "Zell am See"),
    "Saalbach-Hinterglemm": ("Salzburg", "Zell am See"),
    "Saalfelden am Steinernen Meer": ("Salzburg", "Zell am See"),
    "Taxenbach": ("Salzburg", "Zell am See"),
    "Unken": ("Salzburg", "Zell am See"),
    "Viehhofen": ("Salzburg", "Zell am See"),
    "Wald im Pinzgau": ("Salzburg", "Zell am See"),
    "Zell am See": ("Salzburg", "Zell am See"),
    "Krems an der Donau": ("Niederösterreich", "Krems an der Donau (Stadt)"),
    "Waidhofen an der Ybbs": ("Niederösterreich", "Waidhofen an der Ybbs (Stadt)"),
    "Wiener Neustadt": ("Niederösterreich", "Wiener Neustadt (Stadt)"),
    "Amstetten": ("Niederösterreich", "Amstetten"),
    "Ernsthofen": ("Niederösterreich", "Amstetten"),
    "Euratsfeld": ("Niederösterreich", "Amstetten"),
    "Kematen an der Ybbs": ("Niederösterreich", "Amstetten"),
    "Neustadtl an der Donau": ("Niederösterreich", "Amstetten"),
    "St. Peter in der Au": ("Niederösterreich", "Amstetten"),
    "St. Valentin": ("Niederösterreich", "Amstetten"),
    "Seitenstetten": ("Niederösterreich", "Amstetten"),
    "Strengberg": ("Niederösterreich", "Amstetten"),
    "Viehdorf": ("Niederösterreich", "Amstetten"),
    "Zeillern": ("Niederösterreich", "Amstetten"),
    "Alland": ("Niederösterreich", "Baden"),
    "Bad Vöslau": ("Niederösterreich", "Baden"),
    "Berndorf": ("Niederösterreich", "Baden"),
    "Ebreichsdorf": ("Niederösterreich", "Baden"),
    "Enzesfeld-Lindabrunn": ("Niederösterreich", "Baden"),
    "Furth an der Triesting": ("Niederösterreich", "Baden"),
    "Hirtenberg": ("Niederösterreich", "Baden"),
    "Kottingbrunn": ("Niederösterreich", "Baden"),
    "Leobersdorf": ("Niederösterreich", "Baden"),
    "Oberwaltersdorf": ("Niederösterreich", "Baden"),
    "Pfaffstätten": ("Niederösterreich", "Baden"),
    "Pottendorf": ("Niederösterreich", "Baden"),
    "Sooß": ("Niederösterreich", "Baden"),
    "Tattendorf": ("Niederösterreich", "Baden"),
    "Teesdorf": ("Niederösterreich", "Baden"),
    "Traiskirchen": ("Niederösterreich", "Baden"),
    "Trumau": ("Niederösterreich", "Baden"),
    "Blumau-Neurißhof": ("Niederösterreich", "Baden"),
    "Bruck an der Leitha": ("Niederösterreich", "Bruck an der Leitha"),
    "Enzersdorf an der Fischa": ("Niederösterreich", "Bruck an der Leitha"),
    "Götzendorf an der Leitha": ("Niederösterreich", "Bruck an der Leitha"),
    "Hof am Leithaberge": ("Niederösterreich", "Bruck an der Leitha"),
    "Mannersdorf am Leithagebirge": ("Niederösterreich", "Bruck an der Leitha"),
    "Ebergassing": ("Niederösterreich", "Bruck an der Leitha"),
    "Fischamend": ("Niederösterreich", "Bruck an der Leitha"),
    "Leopoldsdorf": ("Niederösterreich", "Bruck an der Leitha"),
    "Maria-Lanzendorf": ("Niederösterreich", "Bruck an der Leitha"),
    "Moosbrunn": ("Niederösterreich", "Bruck an der Leitha"),
    "Schwechat": ("Niederösterreich", "Bruck an der Leitha"),
    "Auersthal": ("Niederösterreich", "Gänserndorf"),
    "Deutsch-Wagram": ("Niederösterreich", "Gänserndorf"),
    "Dürnkrut": ("Niederösterreich", "Gänserndorf"),
    "Ebenthal": ("Niederösterreich", "Gänserndorf"),
    "Gänserndorf": ("Niederösterreich", "Gänserndorf"),
    "Groß-Enzersdorf": ("Niederösterreich", "Gänserndorf"),
    "Hofstetten": ("Niederösterreich", "Sankt Pölten Land"),
    "Groß-Schweinbarth": ("Niederösterreich", "Gänserndorf"),
    "Marchegg": ("Niederösterreich", "Gänserndorf"),
    "Strasshof an der Nordbahn": ("Niederösterreich", "Gänserndorf"),
    "Gmünd": ("Niederösterreich", "Gmünd"),
    "Bad Großpertholz": ("Niederösterreich", "Gmünd"),
    "Heidenreichstein": ("Niederösterreich", "Gmünd"),
    "Göllersdorf": ("Niederösterreich", "Hollabrunn"),
    "Haugsdorf": ("Niederösterreich", "Hollabrunn"),
    "Hollabrunn": ("Niederösterreich", "Hollabrunn"),
    "Maissau": ("Niederösterreich", "Hollabrunn"),
    "Gars am Kamp": ("Niederösterreich", "Horn"),
    "Horn": ("Niederösterreich", "Horn"),
    "Japons": ("Niederösterreich", "Horn"),
    "Sigmundsherberg": ("Niederösterreich", "Horn"),
    "Bisamberg": ("Niederösterreich", "Korneuburg"),
    "Ernstbrunn": ("Niederösterreich", "Korneuburg"),
    "Hausleiten": ("Niederösterreich", "Korneuburg"),
    "Korneuburg": ("Niederösterreich", "Korneuburg"),
    "Langenzersdorf": ("Niederösterreich", "Korneuburg"),
    "Spillern": ("Niederösterreich", "Korneuburg"),
    "Stockerau": ("Niederösterreich", "Korneuburg"),
    "Gerasdorf bei Wien": ("Niederösterreich", "Korneuburg"),
    "Gföhl": ("Niederösterreich", "Krems Land"),
    "Langenlois": ("Niederösterreich", "Krems Land"),
    "Mautern an der Donau": ("Niederösterreich", "Krems Land"),
    "St. Leonhard am Hornerwald": ("Niederösterreich", "Krems Land"),
    "Senftenberg": ("Niederösterreich", "Krems Land"),
    "Straß im Straßertale": ("Niederösterreich", "Krems Land"),
    "Weißenkirchen in der Wachau": ("Niederösterreich", "Krems Land"),
    "Hainfeld": ("Niederösterreich", "Lilienfeld"),
    "Hohenberg": ("Niederösterreich", "Lilienfeld"),
    "Kleinzell": ("Niederösterreich", "Lilienfeld"),
    "Lilienfeld": ("Niederösterreich", "Lilienfeld"),
    "St. Aegyd am Neuwalde": ("Niederösterreich", "Lilienfeld"),
    "Traisen": ("Niederösterreich", "Lilienfeld"),
    "Türnitz": ("Niederösterreich", "Lilienfeld"),
    "Artstetten-Pöbring": ("Niederösterreich", "Melk"),
    "Bergland": ("Niederösterreich", "Melk"),
    "Bischofstetten": ("Niederösterreich", "Melk"),
    "Blindenmarkt": ("Niederösterreich", "Melk"),
    "Erlauf": ("Niederösterreich", "Melk"),
    "Hofamt Priel": ("Niederösterreich", "Melk"),
    "Hürm": ("Niederösterreich", "Melk"),
    "Kilb": ("Niederösterreich", "Melk"),
    "Kirnberg an der Mank": ("Niederösterreich", "Melk"),
    "Krummnußbaum": ("Niederösterreich", "Melk"),
    "Loosdorf": ("Niederösterreich", "Melk"),
    "Mank": ("Niederösterreich", "Melk"),
    "Melk": ("Niederösterreich", "Melk"),
    "Neumarkt an der Ybbs": ("Niederösterreich", "Melk"),
    "Nöchling": ("Niederösterreich", "Melk"),
    "Pöchlarn": ("Niederösterreich", "Melk"),
    "St. Leonhard am Forst": ("Niederösterreich", "Melk"),
    "St. Oswald": ("Niederösterreich", "Melk"),
    "Weiten": ("Niederösterreich", "Melk"),
    "Ybbs an der Donau": ("Niederösterreich", "Melk"),
    "Emmersdorf an der Donau": ("Niederösterreich", "Melk"),
    "Bernhardsthal": ("Niederösterreich", "Mistelbach"),
    "Drasenhofen": ("Niederösterreich", "Mistelbach"),
    "Großkrut": ("Niederösterreich", "Mistelbach"),
    "Laa an der Thaya": ("Niederösterreich", "Mistelbach"),
    "Mistelbach": ("Niederösterreich", "Mistelbach"),
    "Staatz": ("Niederösterreich", "Mistelbach"),
    "Wolkersdorf im Weinviertel": ("Niederösterreich", "Mistelbach"),
    "Ottenthal": ("Niederösterreich", "Mistelbach"),
    "Achau": ("Niederösterreich", "Mödling"),
    "Biedermannsdorf": ("Niederösterreich", "Mödling"),
    "Breitenfurt bei Wien": ("Niederösterreich", "Mödling"),
    "Brunn am Gebirge": ("Niederösterreich", "Mödling"),
    "Gießhübl": ("Niederösterreich", "Mödling"),
    "Gumpoldskirchen": ("Niederösterreich", "Mödling"),
    "Guntramsdorf": ("Niederösterreich", "Mödling"),
    "Hinterbrühl": ("Niederösterreich", "Mödling"),
    "Kaltenleutgeben": ("Niederösterreich", "Mödling"),
    "Laab im Walde": ("Niederösterreich", "Mödling"),
    "Laxenburg": ("Niederösterreich", "Mödling"),
    "Maria Enzersdorf": ("Niederösterreich", "Mödling"),
    "Mödling": ("Niederösterreich", "Mödling"),
    "Münchendorf": ("Niederösterreich", "Mödling"),
    "Perchtoldsdorf": ("Niederösterreich", "Mödling"),
    "Vösendorf": ("Niederösterreich", "Mödling"),
    "Wiener Neudorf": ("Niederösterreich", "Mödling"),
    "Breitenau": ("Niederösterreich", "Neunkirchen"),
    "Breitenstein": ("Niederösterreich", "Neunkirchen"),
    "Buchbach": ("Niederösterreich", "Neunkirchen"),
    "Edlitz": ("Niederösterreich", "Neunkirchen"),
    "Gloggnitz": ("Niederösterreich", "Neunkirchen"),
    "Grünbach am Schneeberg": ("Niederösterreich", "Neunkirchen"),
    "Mönichkirchen": ("Niederösterreich", "Neunkirchen"),
    "Neunkirchen": ("Niederösterreich", "Neunkirchen"),
    "Pitten": ("Niederösterreich", "Neunkirchen"),
    "Puchberg am Schneeberg": ("Niederösterreich", "Neunkirchen"),
    "Reichenau an der Rax": ("Niederösterreich", "Neunkirchen"),
    "Ternitz": ("Niederösterreich", "Neunkirchen"),
    "Rotheau": ("Niederösterreich", "Neunkirchen"),
    "Altlengbach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Böheimkirchen": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Eichgraben": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Hafnerbach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Herzogenburg": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Inzersdorf-Getzersdorf": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Kapelln": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Kasten bei Böheimkirchen": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Kirchberg an der Pielach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Kirchstetten": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Loich": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Neulengbach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Ober-Grafendorf": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Prinzersdorf": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Pyhra": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Rabenstein an der Pielach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Statzendorf": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Stössing": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Traismauer": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Wilhelmsburg": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Gablitz": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Mauerbach": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Pressbaum": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Purkersdorf": ("Niederösterreich", "Sankt Pölten(Land)"),
    "Gresten": ("Niederösterreich", "Scheibbs"),
    "Oberndorf an der Melk": ("Niederösterreich", "Scheibbs"),
    "Randegg": ("Niederösterreich", "Scheibbs"),
    "Steinakirchen am Forst": ("Niederösterreich", "Scheibbs"),
    "Wieselburg": ("Niederösterreich", "Scheibbs"),
    "Absdorf": ("Niederösterreich", "Tulln"),
    "Kirchberg am Wagram": ("Niederösterreich", "Tulln"),
    "Königstetten": ("Niederösterreich", "Tulln"),
    "Michelhausen": ("Niederösterreich", "Tulln"),
    "Sieghartskirchen": ("Niederösterreich", "Tulln"),
    "Sitzenberg-Reidling": ("Niederösterreich", "Tulln"),
    "Tulln an der Donau": ("Niederösterreich", "Tulln"),
    "St. Andrä-Wördern": ("Niederösterreich", "Tulln"),
    "Klosterneuburg": ("Niederösterreich", "Tulln"),
    "Baden": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Ebenfurth": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Eggendorf": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Bad Erlach": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Felixdorf": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Gutenstein": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Hochneukirchen-Gschaidt": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Hollenthon": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Katzelsdorf": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Lanzenkirchen": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Lichtenegg": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Lichtenwörth": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Markt Piesting": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Matzendorf-Hölles": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Pernitz": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Pottenbrunn": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Sollenau": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Winzendorf-Muthmannsdorf": ("Niederösterreich", "Wiener Neustadt(Land)"),
    "Bärnkopf": ("Niederösterreich", "Zwettl"),
    "Göpfritz an der Wild": ("Niederösterreich", "Zwettl"),
    "Groß Gerungs": ("Niederösterreich", "Zwettl"),
    "Martinsberg": ("Niederösterreich", "Zwettl"),
    "Bad Traunstein": ("Niederösterreich", "Zwettl"),
    "Linz": ("Oberösterreich", "Linz (Stadt)"),
    "Steyr": ("Oberösterreich", "Steyr (Stadt)"),
    "Wels": ("Oberösterreich", "Wels (Stadt)"),
    "Altheim": ("Oberösterreich", "Braunau"),
    "Aspach": ("Oberösterreich", "Braunau"),
    "Braunau am Inn": ("Oberösterreich", "Braunau"),
    "Eggelsberg": ("Oberösterreich", "Braunau"),
    "Feldkirchen bei Mattighofen": ("Oberösterreich", "Braunau"),
    "Haigermoos": ("Oberösterreich", "Braunau"),
    "Helpfau-Uttendorf": ("Oberösterreich", "Braunau"),
    "Hochburg-Ach": ("Oberösterreich", "Braunau"),
    "Lochen am See": ("Oberösterreich", "Braunau"),
    "Mattighofen": ("Oberösterreich", "Braunau"),
    "Mauerkirchen": ("Oberösterreich", "Braunau"),
    "Munderfing": ("Oberösterreich", "Braunau"),
    "Ostermiething": ("Oberösterreich", "Braunau"),
    "Palting": ("Oberösterreich", "Braunau"),
    "Innerschwand": ("Oberösterreich", "Vöcklabruck"),
    "St. Pantaleon": ("Oberösterreich", "Braunau"),
    "Schalchen": ("Oberösterreich", "Braunau"),
    "Alkoven": ("Oberösterreich", "Eferding"),
    "Eferding": ("Oberösterreich", "Eferding"),
    "Prambachkirchen": ("Oberösterreich", "Eferding"),
    "Freistadt": ("Oberösterreich", "Freistadt"),
    "Grünbach": ("Oberösterreich", "Freistadt"),
    "Gutau": ("Oberösterreich", "Freistadt"),
    "Ebensee": ("Oberösterreich", "Gmunden"),
    "Leopoldschlag": ("Oberösterreich", "Freistadt"),
    "Neumarkt im Mühlkreis": ("Oberösterreich", "Freistadt"),
    "Pierbach": ("Oberösterreich", "Freistadt"),
    "Rainbach im Mühlkreis": ("Oberösterreich", "Freistadt"),
    "Tragwein": ("Oberösterreich", "Freistadt"),
    "Unterweitersdorf": ("Oberösterreich", "Freistadt"),
    "Schörfling": ("Oberösterreich", "Vöcklabruck"),
    "Windhaag bei Freistadt": ("Oberösterreich", "Freistadt"),
    "Altmünster": ("Oberösterreich", "Gmunden"),
    "Bad Goisern am Hallstättersee": ("Oberösterreich", "Gmunden"),
    "Bad Ischl": ("Oberösterreich", "Gmunden"),
    "Gmunden": ("Oberösterreich", "Gmunden"),
    "Laakirchen": ("Oberösterreich", "Gmunden"),
    "Ohlsdorf": ("Oberösterreich", "Gmunden"),
    "Pinsdorf": ("Oberösterreich", "Gmunden"),
    "Traunkirchen": ("Oberösterreich", "Gmunden"),
    "Vorchdorf": ("Oberösterreich", "Gmunden"),
    "Bad Schallerbach": ("Oberösterreich", "Grieskirchen"),
    "Gallspach": ("Oberösterreich", "Grieskirchen"),
    "Geboltskirchen": ("Oberösterreich", "Grieskirchen"),
    "Grieskirchen": ("Oberösterreich", "Grieskirchen"),
    "Natternbach": ("Oberösterreich", "Grieskirchen"),
    "Neumarkt im Hausruckkreis": ("Oberösterreich", "Grieskirchen"),
    "Rottenbach": ("Oberösterreich", "Grieskirchen"),
    "Schlüßlberg": ("Oberösterreich", "Grieskirchen"),
    "Taufkirchen an der Trattnach": ("Oberösterreich", "Grieskirchen"),
    "Waizenkirchen": ("Oberösterreich", "Grieskirchen"),
    "Peuerbach": ("Oberösterreich", "Grieskirchen"),
    "Hinterstoder": ("Oberösterreich", "Kirchdorf"),
    "Nußbach": ("Oberösterreich", "Kirchdorf"),
    "Pettenbach": ("Oberösterreich", "Kirchdorf"),
    "Windischgarsten": ("Oberösterreich", "Kirchdorf"),
    "Ansfelden": ("Oberösterreich", "Linz Land"),
    "Asten": ("Oberösterreich", "Linz Land"),
    "Enns": ("Oberösterreich", "Linz Land"),
    "Hargelsberg": ("Oberösterreich", "Linz Land"),
    "Hörsching": ("Oberösterreich", "Linz Land"),
    "Hofkirchen im Traunkreis": ("Oberösterreich", "Linz Land"),
    "Leonding": ("Oberösterreich", "Linz Land"),
    "St. Florian": ("Oberösterreich", "Linz Land"),
    "Pasching": ("Oberösterreich", "Linz Land"),
    "Piberbach": ("Oberösterreich", "Linz Land"),
    "St. Marien": ("Oberösterreich", "Linz Land"),
    "Traun": ("Oberösterreich", "Linz Land"),
    "Wilhering": ("Oberösterreich", "Linz Land"),
    "Allerheiligen im Mühlkreis": ("Oberösterreich", "Perg"),
    "Katsdorf": ("Oberösterreich", "Perg"),
    "Mauthausen": ("Oberösterreich", "Perg"),
    "Münzbach": ("Oberösterreich", "Perg"),
    "Perg": ("Oberösterreich", "Perg"),
    "Antiesenhofen": ("Oberösterreich", "Ried"),
    "Aurolzmünster": ("Oberösterreich", "Ried"),
    "Eberschwang": ("Oberösterreich", "Ried"),
    "Hohenzell": ("Oberösterreich", "Ried"),
    "Kirchheim im Innkreis": ("Oberösterreich", "Ried"),
    "Lambrechten": ("Oberösterreich", "Ried"),
    "Neuhofen im Innkreis": ("Oberösterreich", "Ried"),
    "Obernberg am Inn": ("Oberösterreich", "Ried"),
    "Ried im Innkreis": ("Oberösterreich", "Ried"),
    "St. Georgen bei Obernberg am Inn": ("Oberösterreich", "Ried"),
    "St. Martin im Innkreis": ("Oberösterreich", "Ried"),
    "Taiskirchen im Innkreis": ("Oberösterreich", "Ried"),
    "Wippenham": ("Oberösterreich", "Ried"),
    "Auberg": ("Oberösterreich", "Rohrbach"),
    "Hofkirchen im Mühlkreis": ("Oberösterreich", "Rohrbach"),
    "Julbach": ("Oberösterreich", "Rohrbach"),
    "Kollerschlag": ("Oberösterreich", "Rohrbach"),
    "Neufelden": ("Oberösterreich", "Rohrbach"),
    "Oberkappel": ("Oberösterreich", "Rohrbach"),
    "Oepping": ("Oberösterreich", "Rohrbach"),
    "Putzleinsdorf": ("Oberösterreich", "Rohrbach"),
    "Sarleinsbach": ("Oberösterreich", "Rohrbach"),
    "Schwarzenberg am Böhmerwald": ("Oberösterreich", "Rohrbach"),
    "Helfenberg": ("Oberösterreich", "Rohrbach"),
    "Andorf": ("Oberösterreich", "Schärding"),
    "Dorf an der Pram": ("Oberösterreich", "Schärding"),
    "Engelhartszell": ("Oberösterreich", "Schärding"),
    "Raab": ("Oberösterreich", "Schärding"),
    "Riedau": ("Oberösterreich", "Schärding"),
    "Schärding": ("Oberösterreich", "Schärding"),
    "Schardenberg": ("Oberösterreich", "Schärding"),
    "Suben": ("Oberösterreich", "Schärding"),
    "Taufkirchen an der Pram": ("Oberösterreich", "Schärding"),
    "Waldkirchen am Wesen": ("Oberösterreich", "Schärding"),
    "Zell an der Pram": ("Oberösterreich", "Schärding"),
    "Adlwang": ("Oberösterreich", "Steyr Land"),
    "Bad Hall": ("Oberösterreich", "Steyr Land"),
    "Garsten": ("Oberösterreich", "Steyr Land"),
    "Sierning": ("Oberösterreich", "Steyr Land"),
    "Alberndorf in der Riedmark": ("Oberösterreich", "Urfahr Umgebung"),
    "Engerwitzdorf": ("Oberösterreich", "Urfahr Umgebung"),
    "Feldkirchen an der Donau": ("Oberösterreich", "Urfahr Umgebung"),
    "Gallneukirchen": ("Oberösterreich", "Urfahr Umgebung"),
    "Goldwörth": ("Oberösterreich", "Urfahr Umgebung"),
    "Gramastetten": ("Oberösterreich", "Urfahr Umgebung"),
    "Hellmonsödt": ("Oberösterreich", "Urfahr Umgebung"),
    "Oberneukirchen": ("Oberösterreich", "Urfahr Umgebung"),
    "Ottensheim": ("Oberösterreich", "Urfahr Umgebung"),
    "Puchenau": ("Oberösterreich", "Urfahr Umgebung"),
    "Reichenau im Mühlkreis": ("Oberösterreich", "Urfahr Umgebung"),
    "Reichenthal": ("Oberösterreich", "Urfahr Umgebung"),
    "Walding": ("Oberösterreich", "Urfahr Umgebung"),
    "Attnang-Puchheim": ("Oberösterreich", "Vöcklabruck"),
    "Desselbrunn": ("Oberösterreich", "Vöcklabruck"),
    "Frankenmarkt": ("Oberösterreich", "Vöcklabruck"),
    "Mondsee": ("Oberösterreich", "Vöcklabruck"),
    "Oberwang": ("Oberösterreich", "Vöcklabruck"),
    "Redlham": ("Oberösterreich", "Vöcklabruck"),
    "St. Georgen im Attergau": ("Oberösterreich", "Vöcklabruck"),
    "Schwanenstadt": ("Oberösterreich", "Vöcklabruck"),
    "Seewalchen am Attersee": ("Oberösterreich", "Vöcklabruck"),
    "Steinbach am Attersee": ("Oberösterreich", "Vöcklabruck"),
    "Tiefgraben": ("Oberösterreich", "Vöcklabruck"),
    "Timelkam": ("Oberösterreich", "Vöcklabruck"),
    "Vöcklabruck": ("Oberösterreich", "Vöcklabruck"),
    "Vöcklamarkt": ("Oberösterreich", "Vöcklabruck"),
    "Zell am Moos": ("Oberösterreich", "Vöcklabruck"),
    "Bad Wimsbach-Neydharting": ("Oberösterreich", "Wels Land"),
    "Holzhausen": ("Oberösterreich", "Wels Land"),
    "Lambach": ("Oberösterreich", "Wels Land"),
    "Marchtrenk": ("Oberösterreich", "Wels Land"),
    "Sattledt": ("Oberösterreich", "Wels Land"),
    "Steinerkirchen an der Traun": ("Oberösterreich", "Wels Land"),
    "Wien (Innere Stadt)": ("Wien", "Wien"),
    "Wien (Leopoldstadt)": ("Wien", "Wien"),
    "Wien (Landstraße)": ("Wien", "Wien"),
    "Wien (Wieden)": ("Wien", "Wien"),
    "Wien (Margareten)": ("Wien", "Wien"),
    "Wien (Mariahilf)": ("Wien", "Wien"),
    "Wien (Neubau)": ("Wien", "Wien"),
    "Wien (Josefstadt)": ("Wien", "Wien"),
    "Wien (Alsergrund)": ("Wien", "Wien"),
    "Wien (Favoriten)": ("Wien", "Wien"),
    "Wien (Simmering)": ("Wien", "Wien"),
    "Wien (Meidling)": ("Wien", "Wien"),
    "Wien (Hietzing)": ("Wien", "Wien"),
    "Wien (Penzing)": ("Wien", "Wien"),
    "Wien (Rudolfsheim-Fünfhaus)": ("Wien", "Wien"),
    "Wien (Ottakring)": ("Wien", "Wien"),
    "Wien (Hernals)": ("Wien", "Wien"),
    "Wien (Währing)": ("Wien", "Wien"),
    "Wien (Döbling)": ("Wien", "Wien"),
    "Wien (Brigittenau)": ("Wien", "Wien"),
    "Wien (Floridsdorf)": ("Wien", "Wien"),
    "Wien (Donaustadt)": ("Wien", "Wien"),
    "Wien (Liesing)": ("Wien", "Wien"),
}


df["region"] = df["location"].apply(region_mapping.get).str[0]
df["district"] = df["location"].apply(region_mapping.get).str[1]


# In[11]:


# seperate the dataset
rent_data = df[df["type"] == "rent"]
sale_data = df[df["type"] == "sale"]


# In[12]:


# drop unnecessary columns
df = df.drop(columns=["level_0", "index"])
rent_data = rent_data.drop(columns=["level_0", "index"])
sale_data = sale_data.drop(columns=["level_0", "index"])


# In[13]:


# data binning
salebins = np.linspace(4526.991304, 7438.788161, 6)
rentbins = np.linspace(11.125937, 20.360861, 6)
salebinsdistricts = np.linspace(1235.29, 7220.12, 6)
rentbinsdistricts = np.linspace(8.193077, 27.235, 6)
salebinsvienna = np.linspace(5403.41, 9591.30, 6)
rentbinsvienna = np.linspace(17.17, 22.08, 6)


# In[14]:


# Austria (sale) - data visualization

austria_map_sale = folium.Map(location=(47.5162, 13), zoom_start=7, min_zoom=7, max_zoom=9,
                         min_lat=45, max_lat=50, min_lon=7, max_lon=20, max_bounds=True,
                         tiles="CartoDB Positron")

austria_geojson = r"oesterreich.json"

def style_function(feature):
    region_name = feature["properties"]["Name"]

    if region_name == "Burgenland":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Kaernten":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Niederoesterreich":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Oberoesterreich":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Salzburg":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Steiermark":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Tirol":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Vorarlberg":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Wien":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(austria_geojson, style_function = style_function, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average sale price"])).add_to(austria_map_sale)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = salebins,
    vmin = salebins[0],
    vmax = salebins[-1],
    caption = "Apartments´ average sale price per m2"
).add_to(austria_map_sale)

austria_map_sale


# In[15]:


# Austria (rent) - data visualization

austria_map_rent = folium.Map(location=(47.5162, 13), zoom_start=7, min_zoom=7, max_zoom=9,
                         min_lat=45, max_lat=50, min_lon=7, max_lon=20, max_bounds=True,
                         tiles="CartoDB Positron")

austria_geojson = r"oesterreich.json"

def style_function(feature):
    region_name = feature["properties"]["Name"]

    if region_name == "Burgenland":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Kaernten":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Niederoesterreich":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Oberoesterreich":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Salzburg":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Steiermark":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Tirol":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Vorarlberg":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Wien":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(austria_geojson, style_function = style_function, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average rent price"])).add_to(austria_map_rent)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = rentbins,
    vmin = rentbins[0],
    vmax = rentbins[-1],
    caption = "Apartments´ average rent price per m2"
).add_to(austria_map_rent)

austria_map_rent


# In[16]:


# Austria - districts (sale) - data visualization

austria_districts_map_sale = folium.Map(location=(47.5162, 13), zoom_start=7, min_zoom=7, max_zoom=9,
                         min_lat=45, max_lat=50, min_lon=7, max_lon=20, max_bounds=True,
                         tiles="CartoDB Positron")

austria_districts_geojson = r"bezirke.json"
    
def style_function_districts(feature):
    district_name = feature["properties"]["Name"]

    if district_name == "Amstetten":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Baden":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bludenz":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Braunau":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bregenz":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bruck an der Leitha":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bruck-Muerzzuschlag":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Deutschlandsberg":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Dornbirn":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eferding":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eisenstadt (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eisenstadt-Umgebung":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Feldkirch":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Feldkirchen":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gmunden":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gmuend":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Graz (Stadt)":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Graz-Umgebung":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Grieskirchen":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gaenserndorf":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hallein":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hartberg-Fuerstenfeld":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hermagor":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hollabrunn":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Horn":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Imst":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Innsbruck (Stadt)":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Innsbruck Land":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Kitzbuehel":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Klagenfurt (Stadt)":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Klagenfurt Land":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Korneuburg":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Krems Land":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Krems an der Donau (Stadt)":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Kufstein":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Landeck":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Leibnitz":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Leoben":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Lienz":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Liezen":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Lilienfeld":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Linz (Stadt)":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Linz Land":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Mattersburg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Melk":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Mistelbach":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Murau":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Murtal":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Moedling":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Neunkirchen":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Neusiedl am See":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Oberpullendorf":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Perg":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Reutte":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Ried":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Salzburg (Stadt)":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Salzburg-Umgebung":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Johann im Pongau":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Poelten Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Veit an der Glan":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Scheibbs":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Schwaz":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Schaerding":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Spittal an der Drau":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Steyr (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Steyr Land":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Suedoststeiermark":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Tamsweg":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Tulln":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Urfahr Umgebung":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Villach (Stadt)":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Villach Land":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Voitsberg":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Voecklabruck":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Waidhofen an der Ybbs (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Weiz":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wels (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wels Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wien":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wiener Neustadt (Stadt)":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wiener Neustadt Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wolfsberg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Zell am See":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Zwettl":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    else:
        return {"fillColor": "gray", "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(austria_districts_geojson, style_function = style_function_districts, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average sale price"])).add_to(austria_districts_map_sale)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = salebinsdistricts,
    vmin = salebinsdistricts[0],
    vmax = salebinsdistricts[-1],
    caption = "Apartments´ average sale price per m2"
).add_to(austria_districts_map_sale)

austria_districts_map_sale


# In[17]:


# Austria - districts (rent) - data visualization

austria_districts_map_rent = folium.Map(location=(47.5162, 13), zoom_start=7, min_zoom=7, max_zoom=9,
                         min_lat=45, max_lat=50, min_lon=7, max_lon=20, max_bounds=True,
                         tiles="CartoDB Positron")

austria_districts_geojson = r"bezirke.json"
    
def style_function_districts(feature):
    district_name = feature["properties"]["Name"]

    if district_name == "Amstetten":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Baden":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bludenz":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Braunau":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bregenz":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bruck an der Leitha":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Bruck-Muerzzuschlag":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Deutschlandsberg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Dornbirn":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eferding":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eisenstadt (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Eisenstadt-Umgebung":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Feldkirch":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Feldkirchen":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gmunden":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gmuend":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Graz (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Graz-Umgebung":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Grieskirchen":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Gaenserndorf":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hallein":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hartberg-Fuerstenfeld":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Hollabrunn":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Horn":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Imst":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Innsbruck (Stadt)":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Innsbruck Land":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Kitzbuehel":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Klagenfurt (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Klagenfurt Land":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Korneuburg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Krems Land":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Krems an der Donau (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Kufstein":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Landeck":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Leibnitz":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Leoben":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Lienz":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Liezen":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Lilienfeld":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Linz (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Linz Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Mattersburg":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Melk":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Mistelbach":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Murtal":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Moedling":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Neunkirchen":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Neusiedl am See":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Oberpullendorf":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Perg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Reutte":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Ried":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Salzburg (Stadt)":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Salzburg-Umgebung":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Johann im Pongau":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Poelten Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Sankt Veit an der Glan":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Scheibbs":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Schwaz":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Schaerding":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Spittal an der Drau":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Steyr (Stadt)":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Steyr Land":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Suedoststeiermark":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Tamsweg":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Tulln":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Urfahr Umgebung":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Villach (Stadt)":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Villach Land":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Voitsberg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Voecklabruck":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Waidhofen an der Ybbs (Stadt)":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Weiz":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wels (Stadt)":
        return {"fillColor": "gren", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wels Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wien":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wiener Neustadt (Stadt)":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wiener Neustadt Land":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Wolfsberg":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Zell am See":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif district_name == "Zwettl":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    else:
        return {"fillColor": "gray", "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(austria_districts_geojson, style_function = style_function_districts, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average rent price"])).add_to(austria_districts_map_rent)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = rentbinsdistricts,
    vmin = rentbinsdistricts[0],
    vmax = rentbinsdistricts[-1],
    caption = "Apartments´ average rent price per m2"
).add_to(austria_districts_map_rent)

austria_districts_map_rent


# In[18]:


# Vienna (sale) - data visualization

vienna_map_sale = folium.Map(location=(48.2082, 16.3719), zoom_start = 11, min_zoom = 11, max_zoom = 13,
               min_lat = 48, max_lat = 48.40, min_lon = 15.95, max_lon = 16.9, max_bounds = True,
               tiles="CartoDB Positron")

vienna_geojson = r"vienna_.geojson"

def style_function(feature):
    region_name = feature["properties"]["Name"]

    if region_name == "Alsergrund":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Brigittenau":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Donaustadt":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Doebling":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Favoriten":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Floridsdorf":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Hernals":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Hietzing":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Innere Stadt":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Josefstadt":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Landstrasse":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Leopoldstadt":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Liesing":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Margareten":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Mariahilf":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Meidling":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Neubau":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Ottakring":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Penzing":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Rudolfsheim-Fuenfhaus":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Simmering":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Wieden":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Waehring":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(vienna_geojson, style_function = style_function, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average sale price"])).add_to(vienna_map_sale)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = salebinsvienna,
    vmin = salebinsvienna[0],
    vmax = salebinsvienna[-1],
    caption = "Apartments´ average sale price per m2"
).add_to(vienna_map_sale)

vienna_map_sale


# In[19]:


# Vienna (rent) - data visualization

vienna_map_rent = folium.Map(location=(48.2082, 16.3719), zoom_start = 11, min_zoom = 11, max_zoom = 13,
               min_lat = 48, max_lat = 48.40, min_lon = 15.95, max_lon = 16.9, max_bounds = True,
               tiles="CartoDB Positron")

vienna_geojson = r"vienna_.geojson"

def style_function(feature):
    region_name = feature["properties"]["Name"]

    if region_name == "Alsergrund":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Brigittenau":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Donaustadt":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Doebling":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Favoriten":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Floridsdorf":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Hernals":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Hietzing":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Innere Stadt":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Josefstadt":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Landstrasse":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Leopoldstadt":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Liesing":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Margareten":
        return {"fillColor": "darkred", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Mariahilf":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Meidling":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Neubau":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Ottakring":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Penzing":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Rudolfsheim-Fuenfhaus":
        return {"fillColor": "orange", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Simmering":
        return {"fillColor": "darkgreen", "fillOpacity": 0.3, "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Wieden":
        return {"fillColor": "green", "color": "black", "weight": 2, "dashArray": "5, 5"}
    elif region_name == "Waehring":
        return {"fillColor": "red", "color": "black", "weight": 2, "dashArray": "5, 5"}

folium.GeoJson(vienna_geojson, style_function = style_function, tooltip = folium.GeoJsonTooltip(fields = ["Name", "Average rent price"])).add_to(vienna_map_rent)

color_map = branca.colormap.LinearColormap(
    colors = ["darkgreen", "green", "yellow", "orange", "red", "darkred"],
    index = rentbinsvienna,
    vmin = rentbinsvienna[0],
    vmax = rentbinsvienna[-1],
    caption = "Apartments´ average rent price per m2"
).add_to(vienna_map_rent)

vienna_map_rent


# In[20]:


# save visualizations

austria_map_sale.save("austria_map_sale.html")
austria_map_rent.save("austria_map_rent.html")
austria_districts_map_sale.save("austria_districts_map_sale.html")
austria_districts_map_rent.save("austria_districts_map_rent.html")
vienna_map_sale.save("vienna_map_sale.html")
vienna_map_rent.save("vienna_map_rent.html")


# In[27]:


# Dashboard

app = dash.Dash(__name__)

image_options = {
    "Austria (regions) - Sale": "austria_map_sale.html",
    "Austria (regions) - Rent": "austria_map_rent.html",
    "Austria (districts) - Sale": "austria_districts_map_sale.html",
    "Austria (districts) - Rent": "austria_districts_map_rent.html",
    "Vienna (districts) - Sale": "vienna_map_sale.html",
    "Vienna (districts) - Rent": "vienna_map_rent.html",
}

app.layout = html.Div([
    html.H1("Apartments' sale and rent prices per m2 in Austria"),
    
    html.P("Data: January 2024"),
    
    html.H3("Choose map:"),
    dcc.Dropdown(
        id='image-dropdown',
        options=[{'label': key, 'value': value} for key, value in image_options.items()],
        value='austria_map_sale.html',
    ),
    
    html.H3("Selected map:"),
    html.Iframe(id='selected-image', width="900px", height="500px"),
])

@app.callback(
    Output('selected-image', 'srcDoc'),
    [Input('image-dropdown', 'value')]
)
def update_selected_image(selected_image):
    with open(selected_image, "r") as file:
        html_content = file.read()
    return html_content

if __name__ == "__main__":
    app.run_server(debug=True)




