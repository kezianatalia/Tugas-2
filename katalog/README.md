Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![Bagan](https://user-images.githubusercontent.com/112607944/190235891-5d5ca0c2-f6bb-431a-a953-d244e0584da0.png) 
Ketika user ingin mengakses aplikasi berbasis Django, request dari user akan diterima oleh urls dan diproses untuk masuk ke dalam server Django. Permintaan tersebut kemudian diteruskan ke views yang telah didefinisikan untuk dapat memproses permintaan. Views akan memanggil query ke models dan database akan mengembalikan hasil dari query tersebut ke views. Hal ini terjadi jika permintaan yang masuk melibatkan database. Kemudian, hasil proses akan dipetakan ke dalam HTML dan HTML akan ditampilkan di halaman website yang dilihat oleh user.


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah tool yang berguna untuk menjaga suatu ruang kerja tetap terisolasi agar setiap proyek Django memiliki dependencies, pengaturan, dan package-nya masing-masing. Setiap proyek memiliki kebutuhan yang berbeda-beda, maka virtual environment membantu agar perubahan pada satu proyek tidak memengaruhi proyek lain. 
Pemakaian virtual environment pada pembuatan aplikasi web berbasis Django tidak wajib. Namun, tetap sangat disarankan untuk menggunakan virtual environment agar proyek yang kita buat dapat berjalan dengan baik sesuai kebutuhan modul masing-masing proyek.


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Meng-import models dari class katalog yang telah dibuat sebelumnya ke file views.py. Class ini akan digunakan untuk pengambilan data dari database. Lalu menambahkan kode untuk memanggil fungsi query ke model database dan disimpan ke dalam sebuah variabel. Lalu menambahkan parameter ketiga, yaitu variabel berisi data, pada return fungsi render di fungsi yang telah dibuat sebelumnya.
2.  Untuk membuat routing terhadap fungsi yang telah dibuat pada views.py, kita perlu mendaftarkan katalog pada urlpatterns di file urls.py. Hal ini dilakukan agar halaman HTML dapat ditampilkan di browser.
3. Melakukan iterasi menggunakan for loop terhadap variabel yang berisi data (contoh: variabel list_barang) yang telah di-render ke dalam HTML. 
4. Langkah-langkah untuk melakukan deployment ke Heroku :
- Melakukan add, commit, dan push agar perubahan tersimpan ke dalam repositori GitHub
- Buka dan login ke Heroku, lalu meng-copy API key dari akun Heroku
- Membuat repositori secret baru di GitHub yang berisi nama aplikasi dan API key dari Heroku
- Membuat aplikasi di Heroku sesuai dengan nama aplikasi di GitHub
- Menyambungkan akun Heroku dengan akun GitHub
- Lakukan deployment di Heroku dan link aplikasi sudah dapat diakses