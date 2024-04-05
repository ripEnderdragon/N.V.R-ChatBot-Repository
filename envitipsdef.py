import random
listoftips = [
    {"Tips1: Kurangi Pemakaian Plastik. Kita sebaiknya mulai saat ini menghindari penggunaan plastik sekali pakai yang sulit terurai. Gantilah dengan penggunaan tas belanja kain, botol air minum yang dapat diisi ulang, dan wadah makanan yang dapat digunakan berulang kali. Daur ulang atau daur ulang plastik jika memungkinkan juga ide yang baik."},
    {"Tips2: Hemat Konsumsi Energi. Hemat penggunaan listrik dengan mematikan peralatan listrik yang tidak digunakan, menggunakan lampu hemat energi, dan memanfaatkan sumber energi terbarukan seperti tenaga matahari atau tenaga angin jika memungkinkan."},
    {"Tips3 : Hindari Penggunaan Bahan Berbahaya. Hindari penggunaan produk yang mengandung bahan kimia berbahaya, seperti pestisida, insektisida, dan bahan pembersih beracun. Beralihlah ke produk yang ramah lingkungan dan alami."}
]

def print_tips():
    # result = ""
    # ran = random.choice(listoftips)
    return random.choices(listoftips)
