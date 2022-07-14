#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

ad_listesi = []
soyad_listesi = []
okul_no_listesi = []
sinav_puani_listesi = []
gecme_kalma_durumu = []
harf_notu = []


def girdiler(ad, soyad, okul_no, sinav_puani):
    if sinav_puani >= 60:
        gecme_kalma_durumu.append("Geçti")
        if (sinav_puani >= 90) & (sinav_puani <= 100):
            harf_notu.append("AA")
        elif (sinav_puani >= 82) & (sinav_puani <= 89):
            harf_notu.append("BA")
        elif (sinav_puani >= 73) & (sinav_puani <= 81):
            harf_notu.append("BB")
        elif (sinav_puani >= 65) & (sinav_puani <= 72):
            harf_notu.append("CB")
        elif (sinav_puani >= 57) & (sinav_puani <= 64):
            harf_notu.append("CC")
        elif (sinav_puani >= 48) & (sinav_puani <= 56):
            harf_notu.append("DC")
        elif (sinav_puani >= 40) & (sinav_puani <= 47):
            harf_notu.append("DD")
    else:
        gecme_kalma_durumu.append("Kaldı")
        harf_notu.append("FF")

    ad_listesi.append(ad)
    soyad_listesi.append(soyad)
    okul_no_listesi.append(okul_no)
    sinav_puani_listesi.append(sinav_puani)



girdiler("ayşe", "asasd", 4527, 61)
girdiler("ali", "asasd", 4527, 40)
girdiler("yasin", "asasd", 4527, 90)
girdiler("bahar", "adsasd", 483, 70)
################################################################################

ad_listesi = pd.Series(ad_listesi)
soyad_listesi = pd.Series(soyad_listesi)
okul_no_listesi = pd.Series(okul_no_listesi)
sinav_puani_listesi = pd.Series(sinav_puani_listesi)
gecme_kalma_durumu = pd.Series(gecme_kalma_durumu)
harf_notu = pd.Series(harf_notu)
################################################################################

puan_tablosu = pd.concat([ad_listesi, soyad_listesi, okul_no_listesi, sinav_puani_listesi, gecme_kalma_durumu, harf_notu], axis=1)

df = pd.DataFrame(puan_tablosu)
################################################################################

columns_ = ["Ad", "Soyad", "Okul No", "Sınav puanı", "geçme-kalma durumu", "harf notu"]
df.columns = columns_

################################################################################
df.head()
################################################################################

sinav_notlari= df.to_excel("C:/Users/90538/Desktop/sınav_notları.xlsx", sheet_name="Matematik", index= False)


# In[5]:


df


# In[ ]:




