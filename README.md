# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tingkat dropout siswa yang tinggi, yang dapat berdampak negatif terhadap reputasi, akreditasi, serta kepercayaan masyarakat terhadap institusi. Dropout siswa juga menyebabkan pemborosan sumber daya dan potensi pendapatan yang hilang. Oleh karena itu, perlu dilakukan deteksi dini terhadap siswa yang berpotensi dropout agar pihak institusi dapat melakukan intervensi secara proaktif.

### Cakupan Proyek
* **Tujuan utama:** Mengembangkan sistem machine learning untuk memprediksi kemungkinan dropout siswa.
* **Cakupan:**
  * Identifikasi faktor-faktor yang mempengaruhi dropout (absensi, nilai, latar belakang ekonomi, dsb)
  * Pengembangan model prediksi dropout berbasis data historis siswa
  * Pembuatan dashboard analitik untuk visualisasi prediksi dan insight
  * Pembuatan prototype sistem yang dapat diakses user (misal: menggunakan Streamlit)

### Persiapan
* **Sumber data:** https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 
* **Setup environment:**
  * Tools dan library yang digunakan:
  ```
  streamlit
  joblib
  pandas
  scikit-learn
  altair
  matplotlib
  seaborn
  plotly
  ```
  * Langkah setup:
  ```
  1. Install dependensi dengan pip install -r requirements.txt
  2. Jalankan aplikasi dashboard dengan streamlit run app.py
  ```
  * Dashboard Metabase:
  ```
  email: root@email.com
  password: root123
  ```

## Business Dashboard
Dashboard dirancang untuk menampilkan insight penting kepada pihak universitas, antara lain:
1. Menampilkan statistik jumlah dropout berdasarkan rata-rata sks yang mahasiswa ambil pada semester 1 dan 2
2. Menampilkan statistik jumlah dropout berdasarkan rata-rata sks yang diselesaikan mahasiswa pada semester 1 dan 2
3. Menampikan faktor-faktor yang menyebabkan mahasiswa dropout.
4. Menampilkan siswa yang berpotensi dropout beserta faktor risikonya


## Menjalankan Sistem Machine Learning
1. Clone repo project (atau download source code)
2. Install dependensi:
   Jalankan perintah berikut di terminal:
  ```
  pip install -r requirements.txt
  ```
3. Jalankan aplikasi Streamlit:
   ```
   streamlit run app.py
   ```
4. Akses dashboard melalui browser pada alamat yang ditampilkan.
5. Masukkan data siswa pada form prediksi.
   
**Link akses:** https://studentprediction-rmlbhe6a4pwrdxjnu7sazu.streamlit.app/

## Conclusion
Proyek ini telah berhasil membangun sistem prediksi dropout berbasis machine learning yang dapat membantu Jaya Jaya Institut mendeteksi siswa berisiko tinggi untuk dropout secara dini. Dengan adanya dashboard analitik, pihak institusi dapat mengambil keputusan yang lebih cepat dan tepat sasaran untuk melakukan intervensi, sehingga diharapkan dapat mengurangi angka dropout dan meningkatkan kualitas lulusan.

### Rekomendasi Action Items
Berdasarkan keseluruhan proses yang telah dilakukan, penulis menemukan beberapa rekomendasi action items yang dapat dijadikan pertimbangan untuk berbagai stakeholders yang ada, seperti:
1. Implementasi Intervensi Dini:
   Terapkan program bimbingan atau konseling khusus bagi siswa yang diprediksi berisiko tinggi oleh sistem.
2. Peningkatan Kualitas Data:
   Lakukan pencatatan data siswa secara lebih lengkap dan berkala untuk meningkatkan akurasi prediksi.
3. Sosialisasi dan Pelatihan:
   Latih staf akademik untuk menggunakan dashboard dan memahami insight yang diberikan model.
4. Monitoring dan Evaluasi:
   Pantau efektivitas sistem secara berkala dan lakukan update model jika diperlukan.
5. Kolaborasi dengan Orang Tua:
   Libatkan orang tua/wali siswa dalam proses intervensi agar penanganan lebih komprehensif.
6. Pengembangan Lanjutan:
   Integrasikan sistem dengan platform akademik internal dan kembangkan fitur notifikasi otomatis.
