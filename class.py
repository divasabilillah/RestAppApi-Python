class Orang:
	def __init__(self):
		pass

class Anak:
	def __init__(self):
		pass

class Mahasiswa(Orang,Anak):
	def __init__(self):
		self.nama = ''
		self.kelas = ''

	def mengerjakan_tugas(self):
		print('kerjakan tugas')	

mhs = Mahasiswa()
mhs.nama = 'Diva'
mhs.kelas = '4C'

