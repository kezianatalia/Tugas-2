Screenshot Postman:
- html
![postman html](https://user-images.githubusercontent.com/112607944/191626354-d8e29a45-13ec-45ef-a961-596f6e7a045a.png)

- xml 
![postman xml](https://user-images.githubusercontent.com/112607944/191626537-4d4c0dab-842e-46a7-acd4-f714e9166522.png)

- json
![postman json](https://user-images.githubusercontent.com/112607944/191626468-c8c67b8c-5521-4244-8fcd-ccbdd4befc79.png)


1. Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON atau JavaScript Object Notation adalah salah satu format yang digunakan untuk menyimpan dan mentransfer data. JSON terdiri dari dua struktur. Yang petama yaitu kumpulan value yang saling berpasangan (contohnya object), dan yang kedua adalah kumpulan value yang berurutan (contohnya array). Sintaks JSON merupakan turunan dari object JavaScript. Biasanya, file JSON berisikan teks dan ekstensinya adalah .json. JSON menyimpan elemennya secara efisien tetapi tidak terlihat rapi.

XML atau eXtensible Markup Language juga merupakan format untuk menyimpan dan mentransfer data. XML banyak digunakan pada aplikasi web dan mobile. XML biasanya juga berisi teks dan ekstensi filenya adalah .xml. didesain untuk menyimpan elemen-elemennya dengan rapi sehinga mudah dibaca manusia, tetapi kurang efisien jika dibandingkan JSON. 

HTML atau Hypertext Markup Language adalah bahasa pemrograman untuk pembuatan halaman web. Berbeda dengan JSON dan XML, fungsi utama HTML adalah untuk membangun struktur sebuah laman web dan menampilkan data. Pada XML, kita bisa menggunakan tag apapun, sedangkan HTML membutuhkan tag-tag khusus untuk menjalankan fungsinya. 


2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita perlu mengirimkan data-data dari satu stack ke stack lain ketika mengimplementasikan sebuah platform. Terdapat bermacam-macam jenis dan bentuk data yang dikirimkan. Contoh dari format data yang umum digunakan adalah HTML, XML, dan JSON, yaitu format-format yang telah kita pelajari pada sesi tutorial.


3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
Membuat django-app bernama mywatchlist dengan perintah "python manage.py startapp mywatchlist". Lalu tambahkan aplikasi mywatchlist ke list aplikasi di INSTALLED_APPS pada settings.py.

- Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
Mengisi urls.py pada aplikasi mywatchlist dengan 'mywatchlist' pada app_name dan menambahkan path pada urlpatterns untuk menampilkan mywatchlist.

- Membuat sebuah model MyWatchList yang memiliki atribut-atribut
Membuat class MyWatchList pada models.py, dan membuat atribut sesuai petunjuk di soal, yaitu watched, titile, rating, release_date, dan review. Kemudian lakukan migrasi untuk menerapkan skema model yang dibuat ke database Django lokal.

- Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
Membuat file initial_mywatchlist_data.json pada folder fixtures, kemudian isi data sesuai dengan atribut yang terdapat di model. Kemudian lakukan load data agar data masuk ke database Django lokal.

- Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
HTML : membuat sebuah fungsi show_mywatchlist yang menerima parameter request, kemudian buat variabel di dalam fungsi yang menyimpan hasil query dari seluruh data yang ada pada MyWatchList
XML : membuat fungsi show_xml yang menerima parameter request, kemudian buat variabel di dalam fungsi yang menyimpan hasil query dari seluruh data yang ada pada MyWatchList, dan return berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML
JSON : membuat fungsi show_json yang menerima parameter request, kemudian buat variabel di dalam fungsi yang menyimpan hasil query dari seluruh data yang ada pada MyWatchList, dan return berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON

- Membuat routing sehingga data di atas dapat diakses melalui URL
Membuat file urls.py di dalam aplikasi mywatchlist dan buat variabel urlpatterns yang berisi path URL. Buat masing-masing path untuk HTML, XML, dan JSON

- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Karena sudah mengaktifkan automatic deploys di heroku ketika tugas 2 kemarin, maka langkah yang perlu saya lakukan hanyalah melakukan push ke GitHub dan url untuk HTML, XML, dan JSON aplikasi sudah bisa diakses.