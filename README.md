# Laporan Proyek Machine Learning - Muhammad Zhafran Ghaly

## Kategori Proyek 
Kategori yang saya pilih pada proyek ini adalah sistem rekomendasi Restoran di Bangalore, India pada situs Zomato

## Latar Belakang
Pertumbuhan teknologi pesat dalam pengumpulan data telah membawa ke era baru dunia yang digerakkan oleh data. Data digunakan untuk membuat sistem yang lebih efisien dan di situlah sistem pemberi rekomendasi masuk.

Sistem rekomendasi adalah jenis sistem penyaringan informasi karena meningkatkan kualitas hasil pencarian dan menyediakan elemen yang lebih relevan dengan item pencarian atau yang terkait dengan riwayat pencarian pengguna.

Ini adalah sistem penyaringan informasi aktif yang mempersonalisasi informasi yang diberikan kepada pengguna berdasarkan minat mereka, relevansi informasi, dll. Sistem rekomendasi banyak digunakan untuk merekomendasikan film, item, restoran, tempat untuk dikunjungi, item untuk dibeli, dll. Dengan menggunakan metode onten based filtering yang menggunakan fitur item untuk merekomendasikan item lain yang serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit.

## Business Understanding
### Problem Statements
Dari uraian latar belakang yang telah dijabarkan diatas, dapat dirumuskan masalah sebagai berikut:
- Bagaimana cara kerja sistem rekomendasi restauran? 
- Metode apa yang digunakan?

### Goals

Tujuan:
- Memberikan rekomendasi yang menggunakan fitur item untuk merekomendasikan item lain yang serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit.
- Metode yang digunakan adalah konten user based filtering yang gmenggunakan fitur item untuk merekomendasikan item lain yang serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit. 

### Solution statements
- Menghilangkan nilai yang hilang pada kolom 
- Meneliti dataset seperi menghilangkan kolom yang tidak perlu kita gunakan dan kita menghapusnya. Kemudian menghilangkan item yang memiliki nama serupa.

## Data Understanding
Dataset yang digunakan pada proyek kali ini adalah Zomato Bangalore Dataset dari [Kaggle](https://www.kaggle.com/datasets/absin7/zomato-bangalore-dataset) yang memiliki ukuran 89 mb dan memiliki 17 kolom dan 51716 baris.
Berikut informasi mengenai variabel dari dataset:  
- url : Merupakan alamat restoran dari website zomato.
- address : Merupakan alamat pada restoran.
- name : Nama dari restoran
- online_order : Keterangan restoran bisa dipesan melalui online atau tidak
- book_table : Keterangan apakah restoran bisa memesan meja atau tidak
- rate : Nilai dari restoran yang diberi oleh pelanggan
- votes : Jumlah pelanggan yang memilih restoran
- phone : Nomor telepon restoran
- location : lokasi pada Bangalore
- rest_type : Tipe dari restoran
- dish_liked : Sajian yang disukai
- cuisines : Jenis masakan yang dibuat
- approx_cost(for two people) : Perkiraan biaya untuk 2 orang
- reviews_list : Daftar ulasan
- menu item : Menu Item
- listed_in(type) : Jenis sajian restoran seperti ambil sendiri atau dilayani
- listed_in(city) : Lokasi cabang restoran yang ada


## Exploratory Data Analysis
Drop kolom yang tidak digunakan pada dataset ini yaitu 'url', 'dish_liked', 'phone', 'address','rest_type', 'type', 'menu_item', 'votes'. Kolom yang tersisa setelah didrop sejumlah 10 kolom dan 23043 baris. Kemudian kolom yang digunakan hanya 'cuisines',	'Nilai Rating' yang diubah dari kolom 'rates' dan 'cost'. Sedangkan baris yang digunakan hanya 23043 dari 51716.

Kemudian menangani Nilai yang hilang pada dataset dengan menghapusnya menggunakan drop hingga tak tersisa. 
- Visualisasi dari lokasi restoran terlaris.
Restoran yang memiliki rating tinggi diberi penilaian oleh pengguna yang sudah mengunjunginya.

![lok](https://user-images.githubusercontent.com/76243151/195944993-893ab362-280b-4de9-9906-ed695003dcc0.png)

Gambar.1 Visualisasi lokasi 

Pada gambar .1 kita bisa lihat bahwa Koramangala 5th Black adalah lokasi restoran terlaris dan terpadat

## Data Preparation
### Menghapus Kolom
Pada tahap ini saya melakukan penghapusan pada kolom yang tidak kita gunakan seperti yang saya lakukan pada dataset yaitu 'url', 'dish_liked', 'phone', 'address','rest_type', 'type', 'menu_item' dan'votes'. Dengan mengdrop kolom yang kita rasa tidak perlu.
### Penanganan Nilai Hilang
Pada tahap ini saya memiliki nilai 37700 yang hilang, namun dengan mengdrop data yang hilang tersebut maka saya bisa melanjutkan modelling tanpa masalah. 
Metode yang saya gunakan adalah dengan menghapus data yang hilang menggunakan drop, 

df.isnull().sum()
df.dropna(how='any',inplace=True)

## Modeling

### Content Based Filtering
Content based filtering menggunakan fitur item untuk merekomendasikan item lain yang serupa dengan apa yang disukai pengguna, berdasarkan tindakan mereka sebelumnya atau umpan balik eksplisit..
Pada tahap ini saya membuat variabel baru untuk mengerucutkan apa saja yang saya akan tampilkan, seperti 'cuisines', 'Nilai Rating', dan 'cost'. Dari situ kita bisa menggunakan kata kunci nama restoan yang berasal untuk mencari rekomendasi restoran 40 teratas yang memiliki nilai relevan seperti rating dan biaya yang diberikan oleh pengguna. Dan disitu saya mengerucutkannya lagi yang hanya menampilkan 10 restoran teratas dengan kategori 'Nilai Rating' dan 'cost' atau biaya.
- Kelebihannya tidak memerlukan proses pembentukan neighborhood.
- Kelemahan dari user based filtering adalah ketika pengujian dilakukan dengan pengukuran error menggunakan normalized mean absolute error (NMAE), hasil yang diperoleh NMAE cukup tinggi.

### Hasil Modelling
Hasil dari rekomendasi beberapa restoran yang serupa dengan nama restoran 'Jalsa' :

Pada Tabel.1 merekomendasikan restoran yang memiliki kemiripan seperti restoran Jalsa

|index|cuisines|Nilai Rating|cost|
|---|---|---|---|
|The Black Pearl|North Indian, European, Mediterranean|4\.78|1\.4|
|Communiti|Continental, BBQ, Salad|4\.67|1\.5|
|Hammered|North Indian, Thai, Japanese, Continental, Cafe|4\.65|1\.3|
|The Pallet|Continental, Mediterranean, Italian, North Indian, Finger Food, Asian, Momos|4\.48|1\.6|
|The Globe Grub|Continental, North Indian, Asian, Italian|4\.48|1\.3|
|Jalsa Gold|North Indian, Mughlai, Italian|4\.48|1\.3|
|Brooks And Bonds Brewery|Continental, Mediterranean, North Indian, Chinese, Finger Food|4\.45|1\.6|
|Delhi Highway|North Indian|4\.41|1\.2|
|Deja Vu Resto Bar|North Indian, Italian|4\.35|900\.0|
|The Fisherman'S Wharf|Seafood, Goan, North Indian, Continental, Asian|4\.3|1\.4|

Tabel.1 Hasil Rekomendasi dari "Jalsa"



## Evaluation
Saya mengambil sampel satu lagi untuk memastikan bahwa sistem rekomendasinya berjalan dengan baik yaitu Grand Village.

Berikut hasil dari Restoran Grand Village:

Pada Tabel.2 terlihat bahwa rekomendasi dari restoran yang serupa dengan Grand Villge

|index|cuisines|Nilai Rating|cost|
|---|---|---|---|
|Village - The Soul Of India|North Indian, Lucknowi, Gujarati, Maharashtrian, South Indian, Bengali|3\.85|1\.1|
|Shanthi Sagar|South Indian, North Indian, Chinese|3\.72|400\.0|
|Shanthi Sagar|South Indian, North Indian, Chinese, Juices|3\.72|250\.0|
|Cinnamon|North Indian, Chinese, Biryani|3\.71|550\.0|
|Madeena Hotel|North Indian, Mughlai, Biryani|3\.71|400\.0|
|Red Chilliez|North Indian, South Indian, Chinese, Seafood|3\.26|550\.0|
|Red Chilliez|North Indian, Chinese, Seafood, Mangalorean|3\.26|650\.0|
|Konaseema Grand|North Indian, Mughlai, Andhra, Biryani|2\.87|1\.0|
|Melange - Hotel Ekaa|North Indian, Chinese, Continental, Mangalorean|2\.81|900\.0|
|Kabab Treat|North Indian, Chinese|2\.29|500\.0|

Tabel.2 Hasil Rekomendasi dari "Grand Village"



Rumus untuk Content-Based Filtering : 

P =(  # of our recommendations that are relevant) / (# of items we recommended)

Untuk p = 1, karena rekomendasi yang relevan dibagi dengan item yang kita rekomendasikan
yang mana untuk rekomendasi relevan = 10, item yang direkomendasi = 10.

Maka, 10/10 = 1

Dengan rumus diatas, kita bisa merekomendasikan dengan sangat baik.

Referensi:
- Google Developers, https://developers.google.com/machine-learning/recommendation/content-based/basics#:~:text=Content%2Dbased%20filtering%20uses%20item,previous%20actions%20or%20explicit%20feedback.
- Sistem rekomendasi-Content Based, Binus University (17 Nov 2020) https://mti.binus.ac.id/2020/11/17/sistem-rekomendasi-content-based/
