Link aplikasi : https://tugas2-kezia.herokuapp.com/todolist 

# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
crsf atau cross site request forgery adalah salah satu serangan siber pada website yang menyebabkan website mengeksekusi perintah yang seharusnya tidak diizinkan, namun output yang dihasilkan tetap sesuai dengan seharusnya. Salah satu cara untuk mencegah hal ini adalah dengan csrf token. csrf token merupakan sebuah random string yang di-generate setiap kali halaman form muncul. csrf token membuat penyerang tidak mungkin melakukan permintaan http yang sepenuhnya valid karena penyerang tidak dapat memprediksi nilai token csrf pengguna. 
Jika tidak ada potongan kode csrf token, maka website bisa saja diserang dan diakses oleh orang lain tanpa kita sadari.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, kita dapat membuatnya. Membuat form secara manual dapat menggunakan method POST dengan csrf token. Kita dapat membuat tabel terlebih dahulu dengan tag table, dan di dalamnya berikan tag input sesuai dengan tipe input yang diinginkan. Setelah disubmit, kita bisa mengakses data yang di-input dengan method request.POST.get() dengan argumen nama dari data yang di-input. 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna meng-input data ke dalam form, pengguna dapat mengakses data tersebut dengan request.POST.get() dengan argumen nama data yang di-input. Setelah itu, data akan disimpan ke dalam django database dalam bentuk object, maka kita perlu membuat object terlebih dahulu dengan Task.objects.create(data input). Untuk menampilkannya menggunakan fungsi show_todolist pada views.py yang berguna untuk mengakses data, memasukkan ke dalam context, lalu me-render nya ke dalam file html. Di dalam file html, kita bisa mengambil data yang telah di-render dengan sintaks django yaitu double curly brackets ({{ }}) dan for loop untuk mengakses objects satu per satu.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Membuat django-app bernama todolist dengan perintah "python manage.py startapp mywatchlist". Lalu tambahkan aplikasi todolist ke list aplikasi INSTALLED_APPS pada settings.py di folder project_django.

2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Tambahkan path todolist/ pada urls.py di folder project_django. Kemudian buat fungsi show_todolist untuk me-render data ke file html. Lalu buat file urls.py pada folder aplikasi todolist dan tambahkan path dari fungsi show_todolist di dalam variabel urlpatterns.

3. Membuat sebuah model Task
Membuat class Task pada models.py dengan atribut sesuai petunjuk di soal, yaitu user, date, title, dan description. Kemudian lakukan migrasi untuk menerapkan skema model yang dibuat ke database Django lokal.

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
Membuat fungsi register, login, dan logout pada views.py. Kemudian buat bagian tampilannya, yaitu file html di folder templates untuk login dan registrasi akun.

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Membuat file todolist.html pada folder templates dan mengimplementasikan elemen-elemen yang perlu ditampilkan, yaitu judul, tabel todolist, button logout, dan button untuk menambahkan task. Untuk mengambil data, gunakan sintaks django yaitu dengan double curly brackets. 

6. Membuat halaman form untuk pembuatan task
Membuat fungsi create_task pada views.py yang bertujuan untuk membuat object task baru. Selain itu, diperlukan juga membuat halaman html baru (add_task.html) untuk tampilannya. Lalu tambahkan juga path create_task pada urls.py. Data yang masuk di form pembuatan task nantinya akan ditampilkan pada tabel di todolist.html.

7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL
Mengimport fungsi-fungsi dari views ke urls.py pada folder aplikasi todolist, dan menambahkan path fungsi-fungsi tersebut ke dalam variabel urlpatterns.

8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Melakukan push ke GitHub. Saya telah menyambungkan aplikasi heroku dengan akun GitHub, maka ketika kode di repository GitHub ter-update, aplikasi saya akan langsung di-deploy.

9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Setelah aplikasi ter-deploy, jalankan aplikasi dengan akun dan data sesuai keinginan kita.

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework
##  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline CSS 
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Tiap elemennya memiliki atribut style, dan disitulah inline CSS dimasukkan. Kelebihannya yaitu dapat membantu ketika ingin menguji dan melihat perubahan satu elemen dan memparbarui kode dengan cepat. Kelebihan lainnya yaitu proses request HTTP membuat loading lebih cepat karena lebih kecil. Kekurangannya yaitu tidak efisien karena hanya bisa diterapkan dalam satu elemen HTML.
- Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML yang ditulis di header file HTML. Kelebihan internal CSS adalah class dan ID nya bisa digunakan oleh internal stylesheet, perubahannya hanya berlaku di satu halaman, dan tidak perlu mengupload banyak file karena HTML dan CSS berada di satu file. Kekurangannya yaitu kurang efisien jika ingin menggunakan CSS yang sama di beberapa file dan dapat membuat performa website lambat karena website akan selalu meload ulang ketika ganti halaman. 
- External CSS
External CSS adalah kode CSS yang ditulis terpisah dengan HTML. Terdapat file khusus untuk menulis external CSS, yaitu file dengan ekstensi .css. File ini biasanya diletakkan di header halaman HTML. Kelebihannya yaitu lebih mudah dan sederhana untuk menambahkan kode CSS di tiap elemen HTML, ukuran halaman lebih kecil dan rapi, dan loading website lebih cepat. Kekurangannya yaitu jika file CSS gagal dipanggil oleh HTML, tampilan website akan berantakan.

## Jelaskan tag HTML5 yang kamu ketahui.
- <!doctype html> : mendeklarasikan sebuah dokumen agar menjadi file HTML
- <html> : tag pembuka dokumen HTML
- <head> : menampung informasi meta dari dokumen
- <title> : membuat judul halaman yang akan ditampilkan di web
- <p> : membuat paragraf
- <br> : membuat baris baru
- <style> : atribut untuk elemen styling pada HTML
- <form> : membuat formulir untuk mengumpulan input
- <input> : membuat tipe inputran form
- <label> : memberikan label pada input
- <button> : membuat button
- <table> : membuat tabel
- <tr> : membuat baris pada tabel
- <td> : membuat kolom pada tabel
- <option> : mendefinisikan opsi-opsi
- <select> : membuat input dengan pilihan berbentuk list dropdown

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Selektor Tag : selektor yang memilih berdasarkan tag.
- Selektor Class : selektor yang memilih elemen berdasarkan nama class yang diberikan
- Selektor ID : selektor ID mirip dengan selektor class namun ID nya bersifat unik. 
- Selektor atribut : selektor yang memilih elemen berdasarkan atribut, selektor ini mirip dengan selektor ID.
- Selektor universal : selektor untuk menyeleksi semua elemen pada suatu scope (jangkauan)
- Pseudo selektor : selektor untuk memilih elemen semu seperti state di elemen, elemen before dan after, dsb.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Kustomisasi template untuk halaman login, register, dan create-task semenarik mungkin.
Menghubungkan tailwind dengan file HTML dengan memasukkan url di head html, kemudian lakukan kustomisasi sesuai keinginan
- Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
Mengubah file HTML yang tadinya menampilkan todo dengan tabel menjadi menggunakan cards
- Membuat keempat halaman yang dikustomisasi menjadi responsive.
Menambahkan kode pada tag style agar website menjadi responsif