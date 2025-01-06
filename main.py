import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sampah(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'Organik\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah Organik🌿')
                await ctx.send('Jenis sampah ini mudah membusuk dan terurai, seperti yang berasal dari tanaman atau makhluk hidup. Misalnya sampah sisa makanan atau daun-daunan.🍀')
                await ctx.send('Sampah ini dapat dengan mudah dibuang, dan beginiliah caranya👌')
                
                await ctx.send(
                "- Pisahkan Sampah🗑️: Gunakan dua tempat sampah, satu untuk sampah organik (sisa makanan, daun) dan satu lagi untuk sampah anorganik (plastik, kaca).\n"
                "- Gunakan Kantong Biodegradable📦: Pakai kantong ramah lingkungan untuk membungkus sampah organik.\n"
                "- Buat Komposter Sederhana🌱: Olah sampah organik menjadi kompos di rumah dengan wadah sederhana.\n"
                "- Gunakan Layanan Pengelolaan Sampah🌍: Manfaatkan layanan pengumpulan sampah organik jika ada.\n"
                "- Sumbangkan Makanan😋: Sumbangkan makanan yang masih layak dimakan.\n")

            elif hasil[0] == 'Anorganik\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah Anorganik🥤')
                await ctx.send('Jenis sampah ini tidak dapat terurai secara alami seperti sampah organik. Nama lain dari sampah jenis ini adalah sampah kering, seperti plastik, besi, dan barang pecah belah.🔍')
                await ctx.send('Sampah ini sebaiknya dibuang dengan baik, dan caranya adalah🔑')
                
                await ctx.send("- Pisahkan Sampah🔰: Gunakan tempat sampah terpisah untuk sampah anorganik (plastik, kaca, logam) dan organik.\n"
                "- Gunakan Tempat Sampah Daur Ulang♻️: Pastikan sampah anorganik dibuang di tempat sampah yang disediakan untuk daur ulang.\n"
                "- Kurangi Penggunaan Plastik🛍️: Gunakan bahan alternatif seperti tas kain atau wadah yang dapat digunakan kembali untuk mengurangi sampah plastik.\n"
                "- Cuci Sampah Sebelum Dibuang💦: Pastikan botol, kaleng, dan kemasan bersih sebelum dibuang agar bisa didaur ulang dengan baik.\n"
                "- Manfaatkan Layanan Daur Ulang🔄: Gunakan layanan daur ulang yang ada di daerahmu jika tersedia.\n")

            elif hasil[0] == 'Sampah B3\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah B3')
                await ctx.send('Sampah jenis ini biasanya berasal dari komponen yang dapat mencemari lingkungan, sehingga tidak bisa Anda buang sembarangan. Misalnya detergen, produk pembersih rumah, hingga zat kimia lainnya.')
                await ctx.send('Sebaiknya sampah ini jangan dibuang bersamaan dengan sampah organik dan anorgantik dan beginilah caranya')

                await ctx.send("- Pisahkan Sampah B3: Pisahkan sampah B3 (baterai, lampu neon, bahan kimia, obat kadaluarsa) dari sampah lainnya.\n"
                "- Gunakan Tempat Sampah Khusus: Pastikan sampah B3 dibuang di tempat sampah yang disediakan untuk bahan berbahaya dan beracun.\n"
                "- Hindari Membuang di Tempat Umum: Jangan buang sampah B3 di tempat sampah biasa atau sembarangan, karena dapat mencemari lingkungan.\n"
                "- Manfaatkan Layanan Pengumpulan B3: Cari tahu apakah ada layanan pengumpulan sampah B3 yang disediakan oleh pemerintah atau lembaga khusus.\n"
                "- Ikuti Petunjuk Pembuangan: Pastikan mengikuti petunjuk pembuangan yang tercantum pada kemasan bahan B3 atau instruksi dari pihak yang berwenang.\n")
    else:
        await ctx.send('Mungkin ambil gambar dengan angle lain lalu sedikit lebih fokus dan jelas')

bot.run("")