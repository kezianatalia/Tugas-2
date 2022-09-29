Link aplikasi : https://tugas2-kezia.herokuapp.com/todolist 

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