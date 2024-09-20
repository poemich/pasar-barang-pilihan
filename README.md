# Pasar Barang Pilihan

## TUGAS 4

**WEBSITE**: <http://muhammad-fadhlan31-pasarbarangpilihan.pbp.cs.ui.ac.id/>

---

# Pertanyaan

## 1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**:

   - `HttpResponseRedirect()`: Digunakan untuk mengarahkan pengguna ke URL tertentu dengan cara mengembalikan respons HTTP yang berisi status 302 (Found) dan menargetkan URL yang diberikan. Perlu diberikan URL dalam bentuk string absolut atau relatif secara manual.
   
   ```python
   from django.http import HttpResponseRedirect

   def redirect_manual(request):
       return HttpResponseRedirect('/main/')
   ```

   - `redirect()`: Merupakan shortcut dari Django yang lebih efisien karena bisa menerima nama view atau objek, bukan hanya URL. Django akan otomatis melakukan resolving URL menggunakan `reverse()` di balik layar, sehingga lebih fleksibel.

   ```python
   from django.shortcuts import redirect

   def redirect_with_shortcut(request):
       return redirect('main:show_main')
   ```

## 2. **Jelaskan cara kerja penghubungan model `Product` dengan `User`**:

  Hubungan antara `Product` dan `User` dilakukan melalui **ForeignKey**. Seperti yang dijelaskan di kode berikut:

   ```python
   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       name = models.CharField(max_length=100)
       time = models.DateField(auto_now_add=True)
       price = models.IntegerField()
       description = models.TextField()
   ```

   - **ForeignKey** (`user = models.ForeignKey(User, on_delete=models.CASCADE)`) menciptakan relasi **many-to-one** antara model `Product` dan model `User`. Dalam kasus ini, satu pengguna (`User`) bisa memiliki banyak entri produk, tetapi satu entri produk hanya bisa dimiliki oleh satu pengguna.

   - `on_delete=models.CASCADE` berarti jika pengguna dihapus, semua entri produk yang terkait dengan pengguna tersebut juga akan dihapus.

   Dalam view `create_product_entry`, hubungan ini digunakan untuk menyimpan data produk yang dimiliki oleh pengguna yang sedang login:

   ```python
   @login_required
   def create_product_entry(request):
       form = ProductEntryForm(request.POST or None)

       if form.is_valid() and request.method == 'POST':
           product_entry = form.save(commit=False)
           product_entry.user = request.user
           product_entry.save()
           return redirect('main:show_main')

       context = {'form': form}
       return render(request, 'create_product_entry.html', context)
   ```

   Setiap kali pengguna membuat entri produk, `request.user` dihubungkan ke produk yang dibuat.

## 3. **Apa perbedaan antara `authentication` dan `authorization`, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

   - **Authentication**: Proses untuk memverifikasi identitas pengguna. Pada Django, ini biasanya dilakukan dengan menggunakan username dan password. Ketika pengguna melakukan login, `authenticate()` digunakan untuk memverifikasi kredensial mereka, dan `login()` akan menyimpan informasi autentikasi di session:

     ```python
     user = authenticate(request, username=username, password=password)
     if user is not None:
         login(request, user)  # Pengguna login dan session dibuat
     ```

   - **Authorization**: Setelah pengguna berhasil diautentikasi, authorization menentukan hak akses mereka. Apakah pengguna memiliki izin untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu? Django mengatur ini melalui sistem izin (`permissions`), yang bisa diatur di model dan view.

   Saat pengguna login, Django mengelola **session** dengan menyimpan status login di sisi server, dan sesi ini direferensikan melalui cookie di sisi klien. Contoh penggunaannya terlihat dalam view `login_user`:

   ```python
   def login_user(request):
       if request.method == 'POST':
           form = AuthenticationForm(data=request.POST)

           if form.is_valid():
               user = form.get_user()
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main"))
               response.set_cookie('last_login', str(datetime.datetime.now()))  # Menyimpan waktu login terakhir
               return response
   ```

   Ketika pengguna login, cookie `last_login` juga disetel untuk menyimpan informasi kapan pengguna terakhir login.

## 4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**:

   Django mengingat pengguna yang telah login melalui **sessions** dan **cookies**. Setelah login, Django membuat session yang menyimpan informasi pengguna di server. Session ID ini kemudian dikirim ke klien melalui cookie, dan setiap permintaan berikutnya akan menyertakan cookie tersebut untuk mengidentifikasi pengguna yang sedang aktif.

   ```python
   def login_user(request):
       # Login user dan simpan waktu login dalam cookie
       response = HttpResponseRedirect(reverse("main:show_main"))
       response.set_cookie('last_login', str(datetime.datetime.now()))  # Menggunakan cookie untuk menyimpan informasi
   ```

   **Kegunaan lain dari cookies**:
   - **Authentication**: Menyimpan status pengguna yang sudah login, seperti session ID.
   - **User Preferences**: Menyimpan preferensi pengguna, seperti bahasa atau tema.
   - **Tracking**: Bisa digunakan untuk melacak aktivitas pengguna di berbagai halaman atau sesi.

   **Keamanan Cookies**:

   Tidak semua cookies aman digunakan. **Session cookies** lebih aman karena hanya disimpan selama sesi browser aktif dan dihapus setelah browser ditutup. **Persistent cookies** lebih rentan terhadap serangan, karena mereka disimpan lebih lama dan dapat dibaca oleh program lain atau pengguna.

   Untuk meningkatkan keamanan, Django secara default menggunakan **secure cookies** dan **HttpOnly** untuk menghindari akses oleh skrip di klien.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### 1. **Mengimplementasikan Fungsi Registrasi, Login, dan Logout**

   **Registrasi:**

   - Menggunakan `UserCreationForm` dari Django untuk membuat form pendaftaran.
   - Di dalam view `register`, menangani POST request untuk memvalidasi dan menyimpan data pengguna baru jika form sudah valid.
   - Setelah pengguna berhasil mendaftar, mengarahkan mereka ke halaman login menggunakan `redirect()`.

   ```python
   def register(request):
       form = UserCreationForm()

       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
       context = {'form': form}
       return render(request, 'register.html', context)
   ```

   **Login:**

   - Menggunakan `AuthenticationForm` untuk login.
   - Di dalam view `login_user`, menggunakan `authenticate()` untuk memeriksa kredensial pengguna, lalu `login()` untuk menginisialisasi session.
   - Setelah login berhasil, pengguna diarahkan ke halaman utama dengan `HttpResponseRedirect()`, dan cookie `last_login` disimpan untuk mencatat waktu login terakhir.

   ```python
   def login_user(request):
       if request.method == 'POST':
           form = AuthenticationForm(data=request.POST)

           if form.is_valid():
               user = form.get_user()
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main"))
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response

       else:
           form = AuthenticationForm(request)
       context = {'form': form}
       return render(request, 'login.html', context)
   ```

   **Logout:**

   - Di dalam view `logout_user`, memanggil `logout()` untuk menghapus session pengguna.
   - Setelah logout, menghapus cookie `last_login` dengan `response.delete_cookie()` dan mengarahkan pengguna ke halaman login.

   ```python
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
   ```

### 2. **Membuat Dua Akun Pengguna dengan Dummy Data**

   - Membuat dua akun pengguna melalui halaman registrasi yang telah dibuat.
   - Login ke setiap akun dan membuat tiga entri produk dummy untuk setiap akun melalui form `ProductEntryForm` di halaman `create_product_entry`.

   ```python
   def create_product_entry(request):
       form = ProductEntryForm(request.POST or None)

       if form.is_valid() and request.method == 'POST':
           product_entry = form.save(commit=False)
           product_entry.user = request.user  # Menghubungkan ke user yang login
           product_entry.save()
           return redirect('main:show_main')

       context = {'form': form}
       return render(request, 'create_product_entry.html', context)
   ```

### 3. **Menghubungkan Model `Product` dengan `User`**

   - Menambahkan field `user` dengan tipe `ForeignKey(User)` di model `Product`, menghubungkan setiap entri produk dengan pengguna yang membuatnya.
   - Di dalam view `create_product_entry`, memastikan bahwa setiap entri produk yang disimpan terkait dengan `request.user`.

   ```python
   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       name = models.CharField(max_length=100)
       time = models.DateField(auto_now_add=True)
       price = models.IntegerField()
       description = models.TextField()
   ```

### 4. **Menampilkan Detail Informasi Pengguna dan Cookies di Halaman Utama**

   - Di halaman utama (`show_main`), menggunakan `request.user.username` untuk menampilkan nama pengguna yang sedang login.
   - Menambahkan informasi waktu login terakhir dari cookie `last_login`.

   ```python
   @login_required(login_url='/login')
   def show_main(request):
       product_entries = Product.objects.filter(user=request.user)

       context = {
           'name': request.user.username,
           'class': 'PBP F',
           'product_entries': product_entries,
           'last_login': request.COOKIES.get("last_login"),
       }
       return render(request, "main.html", context)
   ```

   Pada template `main.html`, menampilkan detail seperti username dan waktu login terakhir:

   ```html
   <h5>Name: </h5>
   <p>{{ name }}<p>
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```
