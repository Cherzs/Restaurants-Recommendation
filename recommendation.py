# -*- coding: utf-8 -*-
"""Recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t68PUpWxNI3UxzaA1qjA6-YMdPpTi2xC

#Muhammad Zhafran Ghaly

**M183X0348**

**M02 | Machine Learning and Front-End**

Import Library
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('always')
import os
import matplotlib.pyplot as plt
import seaborn as sns
from os.path import join
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle

"""Disini saya menggunakan Dataset dari kaggle : https://www.kaggle.com/datasets/absin7/zomato-bangalore-dataset"""

!kaggle datasets download -d absin7/zomato-bangalore-dataset

!unzip zomato-bangalore-dataset.zip

df = pd.read_csv ('/content/zomato.csv')
df.head(5)

"""#Eksploratory Data Analysis"""

df.info()

"""Mengecek Nilai Null pada dataset"""

df.isnull().sum()

print('Null : ', df.isnull().sum().sum())

"""Menangani Null dengan drop"""

df.isnull().sum()
df.dropna(how='any',inplace=True)

print('Null : ', df.isnull().sum().sum())

"""Tahap ini saya menghapus elemen yang tidak saya perlukan"""

df2 = df.drop([
  'url', 'dish_liked', 'phone'
], axis = 1)

"""Menghapus nilai yang duplikat"""

df2.duplicated().sum()
df2.drop_duplicates(inplace = True)

df2.columns

"""Mengubah nama kolom dan tipe data"""

df2 = df2.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type', 'listed_in(city)':'city'})

df2['cost'] = df2['cost'].astype(str) 
df2['cost'] = df2['cost'].apply(lambda x: x.replace(',','.')) 
df2['cost'] = df2['cost'].astype(float)

"""Menghilangkan slash 5(/5) dari Rates"""

df2 = df2.loc[df2.rate !='NEW']
df2 = df2.loc[df2.rate !='-'].reset_index(drop=True)
remove_slash = lambda x: x.replace('/5', '') if type(x) == np.str else x
df2.rate = df2.rate.apply(remove_slash).str.strip().astype('float')

"""Menyesuakan nama kolom """

df2.name = df2.name.apply(lambda x:x.title())
df2.online_order.replace(('Ya','Tidak'),(True, False),inplace=True)
df2.book_table.replace(('Ya','Tidak'),(True, False),inplace=True)

"""Menghitung Rata-rata dari rating"""

restaurants = list(df2['name'].unique())
df2['Nilai Rating'] = 0

for i in range(len(restaurants)):
    df2['Nilai Rating'][df2['name'] == restaurants[i]] = df2['rate'][df2['name'] == restaurants[i]].mean()
    

scaler = MinMaxScaler(feature_range = (1,5))
df2[['Nilai Rating']] = scaler.fit_transform(df2[['Nilai Rating']]).round(2)

"""Mengeliminasi/menghapus kolom yang tidak diperlukan"""

df2 = df2.drop(['address','rest_type', 'type', 'menu_item', 'votes'],axis=1)

"""Sampel secara acak 60% dari kerangka data yang digunakan"""

df_percent = df2.sample(frac=0.5)

"""#Data Preprocessing"""

plt.figure(figsize=(25,25))
sns.countplot(y=df2['location'])
plt.show()

"""Terlihat bahwa lokasi restaurant yang memiliki pengunjung terbanyak adalah Koramangala 5th Black

#Modeling

TF-IDF (Term Frequency-Inverse Document Frequency) vektor untuk setiap dokumen. Ini akan memberi Anda matriks di mana setiap kolom mewakili sebuah kata dalam kosakata umum dan setiap kolom mewakili sebuah restoran, seperti sebelumnya.

TF-IDF adalah metode statistik untuk menilai arti kata dalam dokumen tertentu. Sekarang, saya akan menggunakan vektorisasi TF-IDF pada dataset:
"""

df_percent.set_index('name', inplace=True)
indices = pd.Series(df_percent.index)

# Membuat tf-idf matrix
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_percent['reviews_list'])

cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

"""Ukuran dari Matrix TF-IDF"""

tfidf_matrix.shape

"""Membuat daftar untuk menempatkan restoran teratas kemudian mencari indeks restoran yang dimasukkan. Mencari restoran dengan nilai cosinus yang sama dari nomor besar. Mengekstrak 40 indeks restoran teratas dengan nilai cosinus yang serupa. Dilanjut membuat kumpulan data baru untuk menampilkan restoran serupa dan buat 40 restoran serupa teratas dengan beberapa kolomnya. setelah itu Drop restoran bernama sama dan urutkan hanya 10 teratas berdasarkan peringkat tertinggi"""

def recommend(name, cosine_similarities = cosine_similarities):

    recommend_restaurant = []
    idx = indices[indices == name].index[0]
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    top40_indexes = list(score_series.iloc[0:41].index)
    
    for each in top40_indexes:
        recommend_restaurant.append(list(df_percent.index)[each])
    
    df3 = pd.DataFrame(columns=['cuisines', 'Nilai Rating', 'cost'])

    for each in recommend_restaurant:
        df3 = df3.append(pd.DataFrame(df_percent[['cuisines','Nilai Rating', 'cost']][df_percent.index == each].sample()))
    
    
    df3 = df3.drop_duplicates(subset=['cuisines','Nilai Rating', 'cost'], keep=False)
    df3 = df3.sort_values(by='Nilai Rating', ascending=False).head(10)
    
    print('Top %s Restoran Serupa %s dengan review yang mirip: ' % (str(len(df3)), name))
    
    return df3
recommend('Jalsa')

recommend('Grand Village')