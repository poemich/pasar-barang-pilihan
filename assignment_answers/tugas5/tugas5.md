# Pasar Barang Pilihan

## TUGAS 5

**WEBSITE**: <http://muhammad-fadhlan31-pasarbarangpilihan.pbp.cs.ui.ac.id/>

---

# Pertanyaan

### 1. **Urutan Prioritas CSS Selector**
   CSS memiliki tiga cara utama untuk diterapkan pada elemen HTML, yaitu melalui **inline CSS**, **internal CSS**, dan **external CSS**. Prioritas penentuan style (specificity) dari yang tertinggi hingga terendah adalah sebagai berikut:

   1. **Inline CSS**: CSS yang ditulis langsung di elemen HTML, seperti `<div style="color: red;">`. Inline style memiliki prioritas tertinggi karena langsung diterapkan ke elemen individu.
      - **Contoh**: `<div style="color: red;">Contoh</div>`.
   
   2. **Internal CSS**: CSS yang ditulis di dalam tag `<style>` pada bagian `<head>` dari halaman HTML. Style ini hanya berlaku pada halaman tersebut, dan memiliki prioritas lebih rendah dari inline style, tetapi lebih tinggi dari external CSS.
      - **Contoh**:
        ```html
        <style>
          div {
            color: blue;
          }
        </style>
        ```
   
   3. **External CSS**: CSS yang ditulis di dalam file terpisah dengan ekstensi `.css` dan dihubungkan ke halaman HTML menggunakan tag `<link>`. External CSS memiliki prioritas terendah dibandingkan inline dan internal CSS.
      - **Contoh**:
        ```html
        <link rel="stylesheet" href="styles.css">
        ```

   Jika elemen HTML memiliki beberapa style dari ketiga sumber ini, style dari **inline CSS** akan diterapkan terlebih dahulu, diikuti oleh **internal CSS**, dan terakhir **external CSS** jika tidak ada conflict.

### 2. **Pentingnya Responsive Design**
   **Responsive design** merupakan pendekatan desain web di mana halaman web dapat beradaptasi dengan berbagai ukuran layar dan perangkat. Ini sangat penting karena:
   - **Peningkatan Pengguna Mobile**: Saat ini, banyak orang mengakses web melalui perangkat mobile seperti smartphone dan tablet. Jika desain web hanya berfokus pada layar desktop, pengalaman pengguna di perangkat mobile akan buruk, seperti teks yang terlalu kecil atau elemen yang tidak sesuai.
   - **SEO (Search Engine Optimization)**: Google dan mesin pencari lainnya memberi peringkat lebih tinggi pada situs yang mobile-friendly, meningkatkan visibilitas situs dalam hasil pencarian.
   - **Pengalaman Pengguna (UX)**: Dengan desain yang responsif, pengguna dapat mengakses dan berinteraksi dengan situs tanpa harus memperbesar atau menggulir berlebihan, sehingga meningkatkan kenyamanan pengguna.
   - **Efisiensi Biaya dan Waktu**: Daripada membuat versi terpisah untuk mobile dan desktop, responsive design memungkinkan satu kode HTML digunakan untuk semua perangkat, yang berarti pengembangan dan pemeliharaan lebih efisien.

   **Contoh aplikasi yang sudah menerapkan responsive design**:
   - **YouTube**: Situs video terbesar ini menyesuaikan tata letak dan ukuran video berdasarkan ukuran layar pengguna, memastikan pengalaman yang optimal baik di desktop maupun mobile.
   - **Twitter**: Aplikasi jejaring sosial ini juga menampilkan tata letak yang responsif, dengan navigasi yang berubah menjadi hamburger menu di perangkat mobile.
   
   **Contoh aplikasi yang belum menerapkan responsive design**:
   - **Beberapa situs pemerintahan lama**: Beberapa situs web pemerintah yang belum dioptimalkan untuk perangkat mobile akan mengalami masalah tata letak ketika diakses dari layar kecil, seperti teks yang sulit dibaca dan gambar yang meluap keluar dari layar.

### 3. **Perbedaan Margin, Border, dan Padding**
   Dalam CSS, **margin**, **border**, dan **padding** adalah bagian dari **CSS Box Model**, yang mendefinisikan bagaimana ruang di sekitar elemen diatur. Berikut perbedaan dan cara mengimplementasikannya:
   
   - **Margin**: Ruang di luar elemen yang memisahkannya dari elemen lainnya. Margin bersifat transparan dan tidak memiliki warna atau garis.
     ```css
     div {
       margin: 20px;  /* Menambahkan jarak 20px di luar elemen */
     }
     ```
   - **Border**: Garis pembatas yang mengelilingi elemen, terletak di antara padding dan margin. Border memiliki warna dan ketebalan yang bisa diatur.
     ```css
     div {
       border: 2px solid black;  /* Border berwarna hitam dengan ketebalan 2px */
     }
     ```
   - **Padding**: Ruang di dalam elemen, antara konten dan border. Padding juga transparan dan digunakan untuk memberi jarak antara konten dan batas elemen.
     ```css
     div {
       padding: 10px;  /* Menambahkan jarak 10px di dalam elemen */
     }
     ```

   **Visualisasi Urutan CSS Box Model**
```
   +-----------------------------+
   |           margin            |
   |   +----------------------+  |
   |   |       border         |  |
   |   |  +----------------+  |  |
   |   |  |    padding     |  |  |
   |   |  |  +----------+  |  |  |
   |   |  |  | content  |  |  |  |
   |   |  |  +----------+  |  |  |
   |   |  +----------------+  |  |
   |   +----------------------+  |
   +-----------------------------+
   ```

### 4. **Konsep Flexbox dan Grid Layout**
   - **Flexbox** (Flexible Box Layout) adalah layout model satu dimensi yang digunakan untuk menyusun elemen secara fleksibel dalam satu arah (baik baris atau kolom). Flexbox sangat berguna untuk membuat layout yang responsif dan mudah diatur.
     - **Kegunaan**: Menyusun elemen dalam satu baris atau kolom, membuat elemen secara otomatis menyesuaikan ruang yang tersedia.
     - **Contoh**:
       ```css
       .container {
         display: flex;
         justify-content: space-around; /* Membuat elemen tersebar dengan jarak seimbang */
       }
       ```
       Dalam flexbox, properti seperti `justify-content` dan `align-items` digunakan untuk mengatur posisi elemen.

   - **Grid Layout** adalah layout model dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Grid layout memberikan kontrol yang lebih besar terhadap tata letak halaman yang kompleks.
     - **Kegunaan**: Digunakan untuk membuat layout yang terdiri dari beberapa kolom dan baris, seperti layout majalah atau dashboard.
     - **Contoh**:
       ```css
       .container {
         display: grid;
         grid-template-columns: 1fr 2fr;  /* Membuat dua kolom dengan proporsi 1:2 */
         grid-gap: 20px;  /* Memberi jarak antara kolom */
       }
       ```
       Dengan grid layout, properti seperti `grid-template-columns` dan `grid-template-rows` digunakan untuk menentukan struktur grid.

### 5. **Implementasi Checklist Step-by-Step**
   Berikut adalah langkah-langkah implementasi checklist dalam tugas ini:
   - **Implementasi Fitur Edit dan Delete Produk**: Saya menambahkan dua button pada setiap card produk untuk mengedit dan menghapus produk. Fungsi ini diimplementasikan dengan membuat URL khusus untuk fitur edit dan delete, dan memanggil fungsi view yang mengelola operasi edit dan delete produk di database.
     ```python
     def delete_product(request, pk):
         product = get_object_or_404(Product, pk=pk)
         product.delete()
         return redirect('main:product_list')
     ```
   - **Kustomisasi Halaman Login, Register, dan Tambah Produk**: Untuk mempercantik halaman login, register, dan tambah produk, saya menggunakan Tailwind CSS. Saya menerapkan berbagai utility classes untuk membuat tampilan yang clean dan modern.
     - **Halaman Login**: Form login dikustomisasi dengan tampilan responsif, menggunakan Tailwind untuk styling input field dan tombol submit.
     - **Halaman Register**: Form pendaftaran didesain agar lebih user-friendly dengan bantuan Tailwind, sehingga elemen form seperti input dan pesan error terlihat lebih jelas.
     - **Halaman Tambah Produk**: Form untuk menambah produk didesain dengan tampilan minimalis menggunakan Tailwind, termasuk penempatan label dan input field yang konsisten.
   - **Kustomisasi Halaman Daftar Produk**: Saya membuat layout card untuk setiap produk yang ditampilkan. Jika tidak ada produk yang tersedia, halaman akan menampilkan gambar placeholder dan pesan yang menyatakan tidak ada produk. Card menggunakan border dan shadow untuk memberikan efek elevasi dan tombol edit dan delete ditempatkan di dalam card tersebut.
   - **Responsive Navbar**: Navbar diimplementasikan agar responsif di berbagai ukuran layar. Saya menggunakan `md:hidden` dan `block` untuk menyesuaikan tampilan antara versi mobile dan desktop. Pada versi mobile, navbar berubah menjadi hamburger menu yang dapat di-toggle.
        ```html
        <button class="mobile-menu-button">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        </button>
        <div class="mobile-menu hidden md:hidden">
        <!-- Menu untuk mobile -->
        </div>
        ```

### **Referensi**

- **Slide Scele**: 
   - [06 - Web Design Using HTML5 and CSS3File](https://scele.cs.ui.ac.id/mod/resource/view.php?id=179306)

- **CSS Specificity**: 
   - [MDN Web Docs - Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

- **Responsive Design**: 
   - [Google Developers - Responsive Web Design Basics](https://developers.google.com/web/fundamentals/design-and-ux/responsive)

- **CSS Box Model**:
   - [MDN Web Docs - CSS Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

- **Flexbox**:
   - [CSS Tricks - A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

- **Grid Layout**:
   - [CSS Tricks - A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)