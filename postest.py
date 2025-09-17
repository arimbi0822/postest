# Class Mahasiswa
class Mahasiswa:
    def __init__(self, NIM="", nama_mahasiswa="", kode_jurusan="", tempat_lahir="", 
                 tanggal_lahir="", jenis_kelamin="", agama="", alamat="", telepon="", 
                 status="", pembimbing_akademik=""):
        self.NIM = NIM
        self.nama_mahasiswa = nama_mahasiswa
        self.kode_jurusan = kode_jurusan
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.jenis_kelamin = jenis_kelamin
        self.agama = agama
        self.alamat = alamat
        self.telepon = telepon
        self.status = status
        self.pembimbing_akademik = pembimbing_akademik

    def tambah(self):
        pass

    def simpan(self):
        pass


# Class Dosen
class Dosen:
    def __init__(self, NIDN="", nama_dosen="", tempat_lahir="", tanggal_lahir="", 
                 jenis_kelamin="", agama="", alamat="", telepon="", status=""):
        self.NIDN = NIDN
        self.nama_dosen = nama_dosen
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.jenis_kelamin = jenis_kelamin
        self.agama = agama
        self.alamat = alamat
        self.telepon = telepon
        self.status = status

    def tambah(self):
        pass

    def simpan(self):
        pass


# Class MataKuliah
class MataKuliah:
    def __init__(self, kode_matkul="", nama_matkul="", semester="", sks=0):
        self.kode_matkul = kode_matkul
        self.nama_matkul = nama_matkul
        self.semester = semester
        self.sks = sks

    def tambah(self):
        pass

    def simpan(self):
        pass


# Class KHS
class KHS:
    def __init__(self, NIM="", semester="", kode_matkul="", nilai_akhir=0, ips=0):
        self.NIM = NIM
        self.semester = semester
        self.kode_matkul = kode_matkul
        self.nilai_akhir = nilai_akhir
        self.ips = ips

    def tambah(self):
        pass
    def simpan(self):
        pass


# Class KRS
class KRS:
    def __init__(self, NIM="", tanggal_registrasi="", tahun_akademik="", kode_matkul=""):
        self.NIM = NIM
        self.tanggal_registrasi = tanggal_registrasi
        self.tahun_akademik = tahun_akademik
        self.kode_matkul = kode_matkul

    def tambah(self):
        pass
    def simpan(self):
        pass


# Class Nilai
class Nilai:
    def __init__(self, NIM="", NIDN="", semester="", kode_matkul="", nilai_kuis=0, 
                 nilai_uts=0, nilai_uas=0, nilai_akhir=0):
        self.NIM = NIM
        self.NIDN = NIDN
        self.semester = semester
        self.kode_matkul = kode_matkul
        self.nilai_kuis = nilai_kuis
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_akhir = nilai_akhir

    def tambah(self):
        pass
    def simpan(self):
        pass


# Class Jadwal Kuliah
class JadwalKuliah:
    def __init__(self, kode_matkul="", tahun_akademik="", hari="", jam="", NIDN=""):
        self.kode_matkul = kode_matkul
        self.tahun_akademik = tahun_akademik
        self.hari = hari
        self.jam = jam
        self.NIDN = NIDN

    def tambah(self):
        pass

    def simpan(self):
        pass


# Class Transkrip Nilai
class TranskripNilai:
    def __init__(self, NIM="", kode_matkul="", nilai_akhir=0, IPK=0):
        self.NIM = NIM
        self.kode_matkul = kode_matkul
        self.nilai_akhir = nilai_akhir
        self.IPK = IPK

    def tambah(self):
        pass
    def simpan(self):
        pass


# Class Registrasi Ulang
class RegistrasiUlang:
    def __init__(self, NIM="", tanggal_registrasi="", tahun_akademik=""):
        self.NIM = NIM
        self.tanggal_registrasi = tanggal_registrasi
        self.tahun_akademik = tahun_akademik

    def tambah(self):
        pass

    def simpan(self):
        pass


# Class Pembimbing Akademik
class PembimbingAkademik:
    def __init__(self, NIDN="", NIM=""):
        self.NIDN = NIDN
        self.NIM = NIM

    def tambah(self):
        pass

    def simpan(self):
        pass