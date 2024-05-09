from itertools import permutations

class Peta:
    def __init__(self):
        # Inisialisasi untuk menyimpan daftar kota dan jalur
        self.city_List = {}

    def printPeta(self):
        # Mencetak daftar kota beserta jalurnya
        for city in self.city_List:
            print(city, ":", self.city_List[city])

    def add_city(self, nama_city):
        # Menambahkan kota baru ke dalam peta jika belum ada
        if nama_city not in self.city_List:
            self.city_List[nama_city] = {}
            return True
        return False

    def delete_city(self, deleted_city):
        # Cek apakah kota yang ingin dihapus ada di list
        if deleted_city in self.city_List:
            # Iterasi kepada setiap kota lain untuk menghapus kota yang akan dihapus
            for another_city in self.city_List:
                # Cek apakah kota yang ingin dihapus ada jalannya ke kota lain
                if deleted_city in self.city_List[another_city]:
                    del self.city_List[another_city][deleted_city]
            del self.city_List[deleted_city]
            return True
        return False

    def add_path(self, city1, city2, path):
        # Mengecek apakah kota1 dan kota2 ada dalam list
        if city1 in self.city_List and city2 in self.city_List:
            # Tambahkan kota2 ke daftar kota1 dan sebaliknya
            self.city_List[city1][city2] = path
            self.city_List[city2][city1] = path
            return True
        return False

    def delete_path(self, city1, city2):
        # Mengecek apakah kota1 dan kota2 ada dalam list
        if city1 in self.city_List and city2 in self.city_List:
            # Hapus jalur antara dua kota
            if city2 in self.city_List[city1]:
                del self.city_List[city1][city2]
            if city1 in self.city_List[city2]:
                del self.city_List[city2][city1]
            return True
        return False

    def djikstra(self, source):
        # Membuat map untuk melacak jarak dari setiap kota ke sumber
        distance = {}
        for city in self.city_List:
            distance[city] = float('inf')
        # Tentukan jarak ke sumber = 0
        distance[source] = 0

        # Membuat sebuah set untuk melacak kota yang belum dikunjungi
        unvisited_cities = set(self.city_List.keys())

        # Membuat perulangan selama kota yang belum dikunjungi masih ada isinya
        while unvisited_cities:
            # Mencari kota terdekat dengan jarak minimum
            closest_city = min(unvisited_cities, key=lambda city: distance[city])

            # Menghapus vertex u dari kota yang belum dikunjungi
            unvisited_cities.remove(closest_city)

            # Update nilai jarak dari semua vertex yang berdekatan
            for neighbor, dist in self.city_List[closest_city].items():
                # Jika jarak kota terdekat + bobot lebih kecil daripada jarak di distance, maka ubah nilai distance
                dist_neighbor = distance[closest_city] + dist
                if dist_neighbor < distance[neighbor]:
                    distance[neighbor] = dist_neighbor

        return distance

# Contoh penggunaan
peta = Peta()

peta.add_city("Bytow")
peta.add_city("Koscierzyna")
peta.add_city("Sopot")
peta.add_city("Gdansk")
peta.add_city("Czersk")
peta.add_city("Starogard Gdanski")
peta.add_city("Tczew")
peta.add_city("Nowy Dwor Gdanski")
peta.add_city("Elblag")
peta.add_city("Malbork")
peta.add_city("Sztum")
peta.add_city("Krynica Morska")

peta.add_path("bytow","koscierzyna",36)
peta.add_path("bytow","czersk",62)
peta.add_path("koscierzyna","czersk",50)
peta.add_path("koscierzyna","sopot",71)
peta.add_path("koscierzyna","Gdansk",58)
peta.add_path("Sopot", "Gdansk", 12)
peta.add_path("Gdansk", "Tczew", 39)
peta.add_path("Gdansk", "Nowy Dwor Gdanski", 38)
peta.add_path("Gdansk", "Starogard Gdanski", 56)
peta.add_path("Czersk", "Starogard Gdanski", 42)
peta.add_path("Starogard Gdanski", "Tczew", 26)
peta.add_path("Tczew", "Nowy Dwor Gdanski", 43)
peta.add_path("Nowy Dwor Gdanski", "Krynica Morska", 37)
peta.add_path("Nowy Dwor Gdanski", "Elblag", 24)
peta.add_path("Elblag", "Malbork", 34)
peta.add_path("Malbork", "Sztum", 17)
peta.add_path("Malbork", "Tczew", 28)

peta.printPeta()

print("----------------------------------------------------------------")

#Tambahan

find_distance = input("Apakah Anda ingin melihat jarak total sebuah kota dengan kota lain? (y/n): ")

if find_distance.lower() == "y":
    print('-------------------------------------------------------------------')
    src_city = input("Kota apa yang ingin Anda jadikan acuan? ")
    
    # Periksa apakah kota tersebut ada dalam peta
    if src_city in peta.city_List:
        # Dapatkan jarak dari kota acuan ke semua kota lainnya
        path_from_src = peta.djikstra(src_city)
        print("Jarak kota berikut dari", src_city, "adalah:")
        for city, distance in path_from_src.items():
            print(city, " adalah ", distance, " KM")
        print("----------------------------------------------------------------")
        
        find_permutations = input("Apakah Anda ingin melihat permutasi dari kota-kota yang terhubung dengan kota tertentu? (y/n): ")
        
        if find_permutations.lower() == "y":
            # Periksa kembali kota acuan
            if src_city in peta.city_List:
                # Dapatkan daftar kota yang terhubung dengan kota acuan
                connected_cities = list(peta.city_List[src_city].keys())
                
                # Dapatkan semua permutasi dari kota-kota yang terhubung
                all_permutations = list(permutations(connected_cities))
                
                # Tampilkan semua permutasi
                print("Semua permutasi kota yang terhubung dengan", src_city, "adalah:")
                for perm in all_permutations:
                    print(perm)
            else:
                print("Kota yang Anda masukkan tidak ditemukan dalam peta.")
    else:
        print("Kota yang Anda masukkan tidak ditemukan dalam peta.")
