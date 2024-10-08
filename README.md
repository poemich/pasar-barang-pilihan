# Pasar Barang Pilihan

## TUGAS 6

**WEBSITE**: <http://muhammad-fadhlan31-pasarbarangpilihan.pbp.cs.ui.ac.id/>

---

# Pertanyaan

### 1. **Manfaat penggunaan JavaScript dalam pengembangan aplikasi web**:

JavaScript merupakan bahasa pemrograman utama untuk pengembangan web interaktif. Dengan JavaScript, kita dapat membuat halaman web yang lebih **dinamis** dan **responif** tanpa perlu memuat ulang seluruh halaman. Hal ini meningkatkan **usability** dan **efisiensi**. Misalnya, ketika menggunakan **AJAX**, JavaScript dapat mengirim dan menerima data dari server di latar belakang, memungkinkan pembaruan bagian halaman tertentu tanpa perlu memuat ulang seluruh halaman.

Pada implementasi tugas ini, saya menggunakan **AJAX** untuk mendapatkan data produk menggunakan `fetch()` dan memperbarui konten tanpa reload halaman:

```javascript
async function refreshProductEntries() {
  const productEntries = await getProductEntries();
  // memuat ulang data produk tanpa refresh halaman penuh
}
```

### 2. **Fungsi penggunaan `await` ketika menggunakan `fetch()`**:

Penggunaan `await` berfungsi untuk menunggu hasil dari operasi **asinkronus**, seperti `fetch()`. `await` memastikan bahwa eksekusi kode berikutnya tidak berjalan sampai `fetch()` menyelesaikan pengambilan data. Tanpa `await`, eksekusi kode berikutnya akan berjalan **sebelum** data diambil dari server, yang dapat menyebabkan **error** atau data tidak valid. Contoh penggunaannya adalah pada saat mengambil data produk:

```javascript
const productEntries = await getProductEntries();
```

Tanpa `await`, misalnya:

```javascript
const productEntries = getProductEntries(); // Akan mengembalikan promise, bukan data
```

### 3. **Mengapa perlu menggunakan decorator `csrf_exempt` pada view untuk AJAX POST?**:

Django memiliki mekanisme **CSRF (Cross-Site Request Forgery)** untuk mencegah request berbahaya. Pada request AJAX POST, token CSRF tidak selalu disertakan secara otomatis, yang menyebabkan Django menolak request tersebut. Oleh karena itu, decorator `@csrf_exempt` digunakan untuk menonaktifkan proteksi CSRF pada view yang menerima request AJAX POST, seperti pada fungsi `add_product_entry_ajax`:

```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    # Menambahkan produk baru ke database melalui AJAX POST
```

Ini memastikan bahwa AJAX POST dapat berjalan tanpa error terkait CSRF, khususnya jika token CSRF tidak dikirim oleh JavaScript.

### 4. **Mengapa pembersihan data input pengguna dilakukan di backend, bukan di frontend saja?**:

Validasi dan pembersihan input di **backend** sangat penting karena data yang dikirim dari frontend dapat dengan mudah dimanipulasi oleh pengguna yang tidak jujur. Serangan seperti **XSS (Cross-Site Scripting)** dapat terjadi jika input yang diterima tidak dibersihkan dari tag berbahaya. Melakukan pembersihan di backend memberikan lapisan keamanan tambahan yang tidak dapat dilewati pengguna. Pada implementasi ini, pembersihan dilakukan di backend dengan menggunakan fungsi `strip_tags` untuk menghapus tag HTML dari input pengguna:

```python
def clean_name(self):
    name = self.cleaned_data["name"]
    return strip_tags(name)  # Membersihkan tag HTML
```

Pembersihan data input seperti ini mencegah serangan XSS yang dapat membahayakan keamanan aplikasi.

### 5. **Implementasi checklist secara step-by-step**:

- **1: Implementasi AJAX GET**  
   Langkah pertama yang saya lakukan adalah mengubah pengambilan data produk agar menggunakan AJAX GET. Tujuannya adalah mengambil data dari server secara asinkronus tanpa me-refresh halaman utama.

  Saya memulai dengan menambahkan fungsi `getProductEntries()` dan `refreshProductEntries()` di dalam berkas HTML, yang bertanggung jawab untuk mengambil data produk dalam format JSON dari endpoint `/json/`. Fungsi ini menggunakan API `fetch()` untuk mengambil data secara asinkronus dan kemudian memperbarui elemen DOM untuk menampilkan produk di halaman tanpa reload penuh.

  Contoh implementasinya:

  ```javascript
  async function getProductEntries() {
    return fetch("{% url 'main:show_json' %}") // Mengambil data dari endpoint JSON
      .then((res) => res.json()); // Parsing data ke format JSON
  }

  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = ""; // Bersihkan elemen HTML
    const productEntries = await getProductEntries(); // Menunggu data produk

    let htmlString = "";
    if (productEntries.length === 0) {
      htmlString = `
              <div>
                  <p>No products available.</p>
              </div>`;
    } else {
      productEntries.forEach((item) => {
        htmlString += `
                  <div>
                      <h3>${item.fields.name}</h3>
                      <p>${item.fields.description}</p>
                      <p>Price: ${item.fields.price}</p>
                  </div>`;
      });
    }
    document.getElementById("product_entry_cards").innerHTML = htmlString; // Update elemen DOM
  }

  refreshProductEntries(); // Memanggil fungsi untuk memuat data produk pertama kali
  ```

  Kode ini memungkinkan produk yang disimpan di database dapat ditampilkan di halaman utama tanpa memuat ulang seluruh halaman, meningkatkan performa dan UX.

- **2: Implementasi AJAX POST**  
   Langkah kedua adalah menambahkan produk baru menggunakan AJAX POST. Saya membuat form modal yang dapat di-trigger oleh tombol "Add New Product Entry by AJAX". Modal ini memuat form input untuk nama produk, deskripsi, dan harga.

  Setelah form di-submit, data produk dikirim ke server melalui AJAX POST dan form kemudian dibersihkan serta modal ditutup secara otomatis. Fungsi untuk mengirim data produk menggunakan `fetch()` dengan method `POST`:

  ```javascript
  function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST", // Menggunakan metode POST untuk mengirim data
      body: new FormData(document.querySelector("#productEntryForm")), // Mengambil data form
    }).then((response) => refreshProductEntries()); // Setelah berhasil, refresh produk yang ditampilkan

    document.getElementById("productEntryForm").reset(); // Bersihkan form input
    hideModal(); // Tutup modal setelah submit
  }

  document.getElementById("submitProductEntry").onclick = addProductEntry; // Memanggil fungsi saat tombol submit ditekan
  ```

  Pada view di Django, saya menambahkan fungsi `add_product_entry_ajax()` untuk menangani request POST dan menyimpan produk baru ke database. Fungsi ini berada di `views.py` dan terlihat seperti ini:

  ```python
  @csrf_exempt
  @require_POST
  def add_product_entry_ajax(request):
      name = strip_tags(request.POST.get("name"))  # Pembersihan input
      description = strip_tags(request.POST.get("description"))
      price = request.POST.get("price")
      user = request.user

      # Membuat objek produk baru
      new_product = ProductEntry(
          name=name,
          description=description,
          price=price,
          user=user
      )
      new_product.save()

      return HttpResponse(b"CREATED", status=201)  # Mengembalikan status sukses
  ```

  Dengan ini, produk baru yang ditambahkan melalui form AJAX POST akan tersimpan ke database dan ditampilkan secara dinamis tanpa reload halaman.

- **3: Penutupan modal dan pembersihan form**  
   Setelah pengguna menambahkan produk baru, modal ditutup secara otomatis dan form di-reset agar siap digunakan lagi untuk input baru. Implementasinya menggunakan JavaScript:

  ```javascript
  function hideModal() {
    const modal = document.getElementById("crudModal");
    const modalContent = document.getElementById("crudModalContent");

    modalContent.classList.remove("opacity-100", "scale-100");
    modalContent.classList.add("opacity-0", "scale-95");

    setTimeout(() => {
      modal.classList.add("hidden");
    }, 150); // Animasi penutupan modal
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal); // Tutup modal jika tombol "Cancel" ditekan
  ```

  Setelah submit, form di-reset dengan:

  ```javascript
  document.getElementById("productEntryForm").reset();
  ```

  Dan modal ditutup menggunakan fungsi `hideModal()`.

### **Referensi**

- **Web Interactivity**:

  - [07 - Web Interactivity - Fakultas Ilmu Komputer UI](https://scele.cs.ui.ac.id/pluginfile.php/239466/mod_resource/content/1/07%20-%20Web%20Interactivity-NC-300924-v1.pdf)

- **AJAX Introduction**:

  - [W3Schools - AJAX Introduction](https://www.w3schools.com/js/js_ajax_intro.asp)

- **Fetch API**:

  - [JavaScript Tutorial - Fetch API](https://www.javascripttutorial.net/web-apis/javascript-fetch-api/)

- **JSON Objects**:
  - [W3Schools - JSON Objects](https://www.w3schools.com/js/js_json_objects.asp)
