    # Implementasi Otomasi Proses ML dengan Makefile

    Tugas ini bertujuan untuk memberikan pengalaman kepada mahasiswa dalam mengotomatisasi alur kerja machine learning menggunakan Makefile. Mahasiswa akan membuat Makefile untuk mengelola berbagai tahapan dalam siklus hidup machine learning,termasuk pengumpulan data, pemrosesan data, pelatihan model, evaluasi model, dan deployment model. Seluruh proses ini akan dijalankan secara manual di komputer lokal masing-masing.

    ## Pengumpulan dan Persiapan Data:

    - Download dataset publik (misalnya, dataset Iris atau Titanic) dari sumber online.
    - Lakukan pre-processing data seperti pembersihan data, pengisian nilai hilang, dan normalisasi fitur.
    ## Pelatihan Model:

    - Kembangkan model machine learning sederhana menggunakan Python (misalnya, model Logistic Regression atau Decision Tree).
    - Buat skrip Python untuk melatih model menggunakan dataset yang telah diproses.

    ## valuasi Model:

    - Evaluasi performa model menggunakan metrik evaluasi standar (misalnya, akurasi, precision, recall, F1-score).
    - Simpan hasil evaluasi model dalam format yang mudah dibaca (misalnya, file teks atau JSON).

    ## Deployment Model:

    - Simulasikan deployment model dengan menyimpan model yang sudah terlatih ke dalam format serialisasi (misalnya, menggunakan joblib atau pickle).

    ## Makefile untuk Otomatisasi:

    Buat Makefile yang mendefinisikan berbagai perintah untuk menjalankan setiap langkah dalam siklus hidup machine learning:

    1. make data untuk pengumpulan dan persiapan data.
    2. make train untuk pelatihan model.
    3. make evaluate untuk evaluasi model.
    4. make deploy untuk menyimpan model yang terlatih.

    # Langkah-langkah tugas:

    ## Menyiapkan Lingkungan Kerja:

    - Buat direktori proyek baru di komputer lokal.
    - Siapkan struktur folder untuk memisahkan kode, data, dan hasil (misalnya, folder data/, scripts/, models/).

    ## Menulis Skrip Python:

    - Buat skrip Python untuk setiap tahap dalam siklus machine learning: data_prep.py, train_model.py, evaluate_model.py, deploy_model.py.
    - Skrip harus berfungsi untuk melakukan tugas-tugas yang terkait dengan namanya (misalnya, data_prep.py harus mengunduh dan memproses data).

    ## Menyusun Makefile:

    Tulis Makefile dengan target berikut:

    - data: Mengunduh dan memproses data.
    - train: Melatih model menggunakan data yang telah diproses.
    - evaluate: Mengevaluasi performa model.
    - deploy: Menyimpan model yang terlatih ke format serialisasi.

    ## Menyiapkan Lingkungan Kerja:

    - Buat direktori proyek baru di komputer lokal.
    - Siapkan struktur folder untuk memisahkan kode, data, dan hasil (misalnya, folder data/, scripts/, models/).

    ## Menulis Skrip Python:

    - Buat skrip Python untuk setiap tahap dalam siklus machine learning: data_prep.py, train_model.py, evaluate_model.py, deploy_model.py.
    - Skrip harus berfungsi untuk melakukan tugas-tugas yang terkait dengan namanya (misalnya, data_prep.py harus mengunduh dan memproses data).

    ## Menyusun Makefile:

    Tulis Makefile dengan target berikut:

    1. data: Mengunduh dan memproses data.
    2. train: Melatih model menggunakan data yang telah diproses.
    3. evaluate: Mengevaluasi performa model.
    4. deploy: Menyimpan model yang terlatih ke format serialisasi.
