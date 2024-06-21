# script.rpy

define e = Character("Narrator")
define characterSampingan = Character("Jaka")
define kucing = Character("Tom")
define pohon = Character("Groot")


init python:
    # Initialize the linked list and add nodes
    from Cerita import LinkedList

    # Urutan Node
    story = LinkedList()
    story.add("start")    # 0
    story.add("scene1")    # 1
    story.add("scene2")    # 2
    story.add("scene1A")   # 3
    story.add("scene1B")   # 4
    story.add("scene2A")   # 5
    story.add("scene2B")   # 6
    story.add("scene1A1")  # 7
    story.add("scene1A2")  # 8
    story.add("scene1B1")  # 9
    story.add("scene1B2")  # 10
    story.add("scene2A1")  # 11
    story.add("scene2A2")  # 12
    story.add("scene2B1")  # 13
    story.add("scene2B2")  # 14
    story.add("scene1A1A") # 15
    story.add("scene1A1B") # 16
    story.add("scene1A2A") # 17
    story.add("scene1A2B") # 18
    story.add("scene1B1A") # 19
    story.add("scene1B1B") # 20
    story.add("scene1B2A") # 21
    story.add("scene1B2B") # 22
    story.add("scene2A1A") # 23
    story.add("scene2A1B") # 24
    story.add("scene2A2A") # 25
    story.add("scene2A2B") # 26
    story.add("scene2B1A") # 27
    story.add("scene2B1B") # 28
    story.add("scene2B2A") # 29
    story.add("scene2B2B") # 30
    story.add("goodending1")#31
    story.add("badending1")#32
    story.add("goodending2")#33
    story.add("canonending1")#34
    story.add("secretending1")#35
    story.add("badending2")#36
    story.add("goodending3")#37
    story.add("goodending4")#38
    story.add("secretending2")#39
    story.add("canonending2")#40
    story.add("goodending5")#41
    story.add("worstending")#42
 
# The game starts here.
label start:
    play music "audio/Sate.mp3" volume 0.3

    scene bg class
    with fade 
    e "Jaka, seorang pemuda yang suka petualangan, suatu hari menemukan pintu misterius di dalam lemari tuanya. Karena penasaran, dia memutuskan untuk masuk ke dalam pintu tersebut."
    e "Tiba-tiba, dia menemukan dirinya di dunia lain yang penuh dengan makhluk aneh dan lucu."

    $ current_node = 0
    menu:
        "Jaka melihat seekor kucing yang bisa berbicara.":
            $ current_node = 1
            jump expression story.get(current_node)
        "Jaka melihat pohon yang sedang menari.":
            $ current_node = 2
            jump expression story.get(current_node)

#Definisikan isi Node 
label scene1:
    
    show bg hutan

    show jaka ss at left
    e "Jaka terkejut melihat seekor kucing yang sedang membaca buku dan bisa berbicara."
    e "Kucing itu menyapa Jaka dengan ramah."
    hide jaka ss

    show tom samurai
    kucing "Halo, manusia! Namaku Tom. Apa yang membawamu ke sini?"
    hide tom samurai
    menu:
        "Jaka bertanya kepada kucing tentang dunia ini.":
            $ current_node = 3
            jump expression story.get(current_node)
        "Jaka meminta kucing menunjukkan jalan keluar.":
            $ current_node = 4
            jump expression story.get(current_node)

label scene2:
    show bg dancingtree

    show jaka ss
    e "Jaka terpukau melihat pohon yang menari mengikuti irama musik yang entah berasal dari mana."
    hide jaka ss

    show groot idle
    e "Tiba-tiba, pohon itu berhenti dan menyapanya."
    pohon "Halo, manusia! Namaku Groot. Apa yang membawamu ke sini?"
    e ""
    hide groot idle
    menu:
        "Jaka bertanya kepada pohon tentang dunia ini.":
            $ current_node = 5
            jump expression story.get(current_node)
        "Jaka meminta pohon menunjukkan jalan keluar.":
            $ current_node = 6
            jump expression story.get(current_node)

label scene1A:
    show bg 1a

    show jaka content
    characterSampingan "Tom, bisa ceritakan tentang dunia ini?"
    hide jaka content

    show tom samurai
    kucing "Ini adalah Dunia Lucu, tempat di mana segala sesuatu bisa terjadi. Kamu ingin mencoba sesuatu yang menarik?"
    hide tom samurai
    menu:
        "Aku ingin mencoba makanan ajaib.":
            $ current_node = 7
            jump expression story.get(current_node)
        
        "Aku ingin mencoba terbang dengan sayap kucing.":
            $ current_node = 8
            jump expression story.get(current_node)

label scene1B:
    show bg 1b

    show jaka perplexed
    characterSampingan "Tom, bisa tunjukkan jalan keluar dari sini?"
    hide jaka perplexed
    show tom samurai
    kucing "Tentu, tapi kamu harus menjawab teka-teki dulu. Apa yang memiliki ekor tapi bukan hewan?"
    hide tom samurai
    menu:
        "layang-layang":
            $ current_node = 9
            jump expression story.get(current_node)
        
        "cacing":
            $ current_node = 10
            jump expression story.get(current_node)

label scene2A:
    show bg toys

    show jaka question
    characterSampingan "Groot, bisa ceritakan tentang dunia ini?"
    hide jaka question

    show tom samurai
    kucing "Ini adalah Dunia Lucu, tempat di mana pohon bisa menari dan manusia bisa berbicara dengan pohon. Kamu ingin mencoba sesuatu yang menarik?"
    hide tom samurai
    menu:
        "Aku ingin menari dengan pohon.":
            $ current_node = 11
            jump expression story.get(current_node)
        
        "Aku ingin memetik buah ajaib dari pohon.":
            $ current_node = 12
            jump expression story.get(current_node)

label scene2B:
    show bg lushforest

    show jaka perplexed
    characterSampingan "Groot, bisa tunjukkan jalan keluar dari sini?"
    hide jaka perplexed

    show tom samurai
    kucing "Tentu, tapi kamu harus menjawab teka-teki dulu. Apa yang selalu di depanmu tetapi tidak pernah bisa kamu lihat?"
    hide tom samurai
    menu:
        "Masa depan.":
            $ current_node = 13
            jump expression story.get(current_node)
        
        "Bayangan.":
            $ current_node = 14
            jump expression story.get(current_node)

label scene1A1:
    show bg witcher
    
    show tom cake
    kucing "Baiklah, cobalah kue ini. Setiap gigitan akan membuatmu merasa seperti tokoh kartun!"
    hide tom cake

    show jaka cursed
    e "Jaka mencoba kue itu dan tiba-tiba badannya mulai berubah menjadi kartun, tangannya bisa melar seperti karet dan kepalanya bisa berputar."
    hide jaka cursed
    
    menu:
        "Jaka senang dan ingin mencoba lebih banyak makanan ajaib.":
            $ current_node = 15
            jump expression story.get(current_node)
        
        "Jaka panik dan meminta bantuan Tom.":
            $ current_node = 16
            jump expression story.get(current_node)

label scene1A1A: #Good Ending 1
    show bg kue

    show jaka ss
    characterSampingan "Wah, ini luar biasa! Aku ingin mencoba lebih banyak makanan ajaib!"
    hide jaka ss

    show tom cakes
    kucing "Bagus! Aku punya banyak makanan lain yang bisa kamu coba."
    hide tom cakes
    
    e "Kucing itu memberikan Jaka berbagai macam makanan ajaib. Setiap makanan memberikan kekuatan kartun yang berbeda. Jaka sangat senang dan menghabiskan waktu seharian bermain dengan kekuatan barunya."
    e "Akhirnya, Jaka menemukan makanan yang bisa mengembalikannya ke wujud normal. Ia menyimpan makanan ajaib lainnya untuk digunakan di kemudian hari."
    e "Jaka pulang ke rumah dengan hati gembira, siap untuk petualangan baru di masa depan dengan kekuatan barunya."
    $ current_node = 31
    jump expression story.get(current_node)

label scene1A1B: #Bad Ending 1
    show bg cakeman

    characterSampingan "Oh tidak, apa yang terjadi padaku? Tom! Tolong aku!"
    e "Jaka panik dan berlari mencari Tom. Ketika menemukan Tom, ia menjelaskan apa yang terjadi."
    kucing "Tenang Jaka, aku akan membantumu."
    e "Tom mencoba berbagai cara untuk mengembalikan Jaka ke wujud normal, tetapi tidak ada yang berhasil. Jaka mulai putus asa."
    e "Hari demi hari berlalu, dan Jaka harus belajar hidup dengan tubuh kartunnya. Meski pada awalnya sulit, lambat laun Jaka mulai menerima kenyataan dan menemukan cara untuk menggunakan kekuatannya untuk membantu orang lain."
    e "Walau Jaka tidak pernah bisa kembali sepenuhnya seperti semula, ia menemukan makna baru dalam hidupnya dengan membantu orang lain dengan kekuatan kartunnya."
    $ current_node = 32
    jump expression story.get(current_node)

label scene1A2:
    show bg kontol
    kucing "Baiklah, pegang ini!"
    e "Tom memberikan sayap ajaib kepada Jaka."
    e "Jaka memasang sayap tersebut dan tiba-tiba dia bisa terbang seperti burung."
    menu:
        "Jaka terbang tinggi dan menjelajahi dunia dari atas":
            $ current_node = 17
            jump expression story.get(current_node)
        
        "Jaka terbang rendah dan mencoba mendarat di tempat aman.":
            $ current_node = 18
            jump expression story.get(current_node)

label scene1A2A: #Good Ending 2
    show bg sky
    e "Jaka terbang tinggi ke langit, menjelajahi dunia dari atas. Pemandangan yang ia lihat sangat menakjubkan; gunung, lautan, dan kota-kota terlihat begitu kecil dari ketinggian."
    e "Jaka merasa sangat bebas dan bahagia, melayang di udara seperti burung."
    characterSampingan "Ini luar biasa! Aku bisa melihat seluruh dunia dari sini!"
    e "Setelah beberapa jam menikmati pemandangan, Jaka memutuskan untuk kembali ke tanah. Dia menemukan tempat yang aman untuk mendarat."
    e "Ketika mendarat, sayap ajaibnya menghilang dengan perlahan."
    kucing "Bagaimana rasanya terbang, Jaka?"
    characterSampingan "Itu pengalaman yang tak terlupakan. Terima kasih!"
    e "Jaka pulang dengan hati yang penuh kebahagiaan dan kenangan indah dari petualangannya di langit. Dia tahu bahwa dia selalu bisa mengandalkan kucing untuk petualangan ajaib di masa depan."
    $ current_node = 33
    jump expression story.get(current_node)

label scene1B1:
    show bg goodending2b
    kucing "Betul! Layang-layang punya ekor tapi bukan hewan. Ayo, ikut aku!"
    e "Tom membawa Jaka ke sebuah pintu yang bisa membawanya pulang ke rumah."
    e " Jaka memasang sayap tersebut dan tiba-tiba dia bisa terbang seperti burung."
    menu:
        "Jaka pulang ke rumah dan membawa pulang Miau sebagai teman.":
            $ current_node = 19
            jump expression story.get(current_node)
        
        "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu.":
            $ current_node = 20
            jump expression story.get(current_node)

label scene1B1A: #Canon Ending 1
    show bg goodending2bs
    e "Jaka memutuskan untuk pulang ke rumah. Sebelum pergi, kucing itu memberikan Miau, seekor kucing kecil yang lucu, sebagai teman."
    characterSampingan "Terima kasih atas semuanya! Aku akan merindukan tempat ini, tapi aku senang bisa membawa Miau bersamaku."
    kucing "Jangan khawatir, Jaka. Kamu selalu bisa kembali ke Dunia Lucu kapan saja."
    hide bg goodending2bs

    show bg portal
    e "Jaka berjalan melalui pintu dan tiba-tiba dia berada di kamarnya sendiri. Miau mengikuti di belakangnya."
    e "Dengan Miau di sisinya, Jaka merasa lebih bahagia dan tidak pernah merasa kesepian lagi. Mereka berdua menjadi sahabat yang tak terpisahkan."
    e "Setiap kali Jaka ingin petualangan baru, ia tahu bahwa Dunia Lucu selalu menunggunya."
    e "Jaka menjalani hidupnya dengan penuh keceriaan dan kenangan indah dari Dunia Lucu."
    $ current_node = 34
    jump expression story.get(current_node)

label scene1B1B: #Secret Ending 1
    show bg secret1s
    e "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu. Tempat itu penuh dengan keajaiban dan petualangan yang tak ada habisnya."
    characterSampingan "Aku ingin menjelajahi lebih banyak tempat di Dunia Lucu. Terlalu banyak yang belum aku lihat."
    kucing "Bagus sekali, Jaka! Mari kita mulai petualangan baru!"
    e "Kucing itu membawa Jaka ke berbagai tempat yang menakjubkan. Mereka bertemu makhluk-makhluk aneh dan menikmati petualangan yang luar biasa."
    e "Suatu hari, Jaka menemukan sebuah gua tersembunyi yang belum pernah dilihat oleh siapapun sebelumnya. Di dalamnya, dia menemukan harta karun dan artefak ajaib."
    characterSampingan "Ini luar biasa! Tempat ini penuh dengan misteri dan keajaiban."
    e "Jaka memutuskan untuk menjadikan Dunia Lucu sebagai rumah keduanya. Setiap hari adalah petualangan baru, dan dia belajar banyak hal tentang dunia dan dirinya sendiri."
    e "Dalam hatinya, Jaka tahu bahwa dia telah menemukan tempat yang benar-benar ajaib, di mana impian menjadi kenyataan."
    $ current_node = 35
    jump expression story.get(current_node)


label scene1B2:
    show bg lushforest
    show tom samurai
    kucing "Salah! Tapi tidak apa-apa, kamu masih punya satu kesempatan lagi. Apa yang selalu di depanmu tetapi tidak pernah bisa kamu lihat?"
    hide tom samurai
    menu:
        "Masa depan":
            $ current_node = 21
            jump expression story.get(current_node)
        
        "Bayangan":
            $ current_node = 22
            jump expression story.get(current_node)

label scene1B2A: #Bad Ending 2 
    show bg dsforest
    e "Jaka berpikir keras dan akhirnya menjawab."
    show jaka perplexed
    characterSampingan "Masa depan!"
    hide jaka perplexed
    show tom samurai
    kucing "Salah lagi, Jaka! Jawabannya bukan itu."
    hide tom samurai
    e "Tiba-tiba, lantai di bawah Jaka terbuka dan dia jatuh ke dalam kegelapan yang dalam."
    show jaka ss
    characterSampingan "Aaaahhh!"
    hide jaka ss
    e "Jaka terjebak di dunia yang suram dan penuh dengan ketakutan. Dia mencoba mencari jalan keluar, tapi setiap langkah hanya membawanya lebih dalam ke dalam kegelapan."
    e "Meski berusaha keras, Jaka tidak bisa menemukan jalan kembali ke dunia nyata. Dia terjebak selamanya dalam dunia teka-teki yang tak berujung."
    $ current_node = 36
    jump expression story.get(current_node)

label scene1B2B: #Good Ending 3
    show bg good3s
    e "Jaka berpikir keras dan akhirnya menjawab."
    show jaka question
    characterSampingan "Bayangan!"
    hide jaka question
    show tom samurai
    kucing "Betul sekali! Kamu memang pintar, Jaka."
    e "Pintu besar muncul di depan Jaka, memancarkan cahaya terang yang menyilaukan."
    kucing "Lewat pintu ini, kamu bisa kembali ke rumah."
    hide tom samurai
    e "Jaka tersenyum lega dan melangkah melalui pintu. Seketika, dia menemukan dirinya kembali di kamarnya, aman dan sehat."
    characterSampingan "Terima kasih, kucing! Aku tidak akan melupakan petualangan ini."
    e "Dengan kenangan indah dari Dunia Lucu, Jaka menjalani hari-harinya dengan lebih ceria dan penuh semangat. Dia tahu bahwa kapan saja dia merasa bosan atau kesepian, petualangan selalu menunggunya di suatu tempat yang ajaib."
    $ current_node = 37
    jump expression story.get(current_node)

label scene2A1:
    show bg lushforest
    show grood idle
    pohon "Ayo, mari kita menari!"
    hide groot idle
    e "Jaka dan Groot mulai menari bersama dan Jaka merasa sangat senang, ternyata menari dengan pohon sangat menyenangkan."
    menu:
        "Jaka ingin terus menari dengan Groot.":
            $ current_node = 23
            jump expression story.get(current_node)
        
        "Jaka lelah dan ingin mencari petualangan lain.":
            $ current_node = 24
            jump expression story.get(current_node)

label scene2A1A: #Good Ending 1
    e "Jaka memutuskan untuk terus menari dengan Groot. Mereka menari sepanjang hari, dan setiap gerakan membuat Jaka semakin bahagia."
    characterSampingan "Ini benar-benar menyenangkan, Groot!"
    e "Groot tersenyum lebar, menandakan bahwa ia juga senang."
    pohon "Aku senang kamu menikmatinya, Jaka!"
    e "Tiba-tiba, dari dalam Groot, muncul buah-buahan ajaib yang berkilauan. Groot memberikannya kepada Jaka."
    pohon "Ini adalah buah persahabatan. Makanlah, dan kamu akan merasakan kekuatan persahabatan selamanya."
    e "Jaka memakan buah itu dan merasa hangat di dalam hatinya. Dia merasa lebih kuat dan lebih bahagia daripada sebelumnya."
    e "Jaka tahu bahwa dia telah menemukan teman sejati di Groot, dan persahabatan mereka akan bertahan selamanya."
    e "Dengan hati yang penuh kebahagiaan, Jaka kembali ke rumah dengan kenangan indah dan kekuatan baru dari buah persahabatan."
    $ current_node = 31 
    jump expression story.get(current_node)

label scene2A1B: #Secret Ending 1
    e "Jaka merasa lelah setelah menari begitu lama. Dia berpikir untuk mencari petualangan lain."
    characterSampingan "Terima kasih, Groot! Menari denganmu sangat menyenangkan, tapi aku ingin melihat petualangan lainnya di sini."
    pohon "Tentu, Jaka. Aku akan selalu ada di sini jika kamu ingin menari lagi."
    e "Jaka melanjutkan perjalanannya, dan tak lama kemudian dia menemukan sebuah gua misterius yang dipenuhi dengan cahaya berkilauan."
    characterSampingan "Apa ini? Sepertinya gua ini menyembunyikan sesuatu yang istimewa."
    e "Dengan hati-hati, Jaka masuk ke dalam gua dan menemukan sebuah portal rahasia. Portal itu tampak seperti pintu menuju dunia lain."
    e "Tanpa ragu, Jaka melangkah melalui portal dan menemukan dirinya di sebuah dunia ajaib yang penuh dengan makhluk-makhluk langka dan keajaiban yang belum pernah ia lihat sebelumnya."
    e "Di dunia baru ini, Jaka menemukan banyak rahasia dan harta karun yang tak ternilai. Setiap sudut dunia baru ini membawa petualangan dan penemuan yang menakjubkan."
    e "Jaka merasa seperti penjelajah sejati, dan dia tahu bahwa dunia ini menyimpan banyak rahasia yang menunggu untuk diungkap."
    e "Dengan semangat dan rasa ingin tahu yang tak pernah padam, Jaka memulai petualangan barunya di dunia yang penuh dengan keajaiban dan misteri."
    $ current_node = 35
    jump expression story.get(current_node)

label scene2A2:
    pohon "Baiklah, ini dia buah ajaibnya. Satu gigitan akan membuatmu bisa berbicara dengan semua makhluk di sini."
    e "Jaka memetik buah tersebut dan memakannya."
    menu:
        "Jaka mencoba berbicara dengan makhluk lain.":
            $ current_node = 25
            jump expression story.get(current_node)
        
        "Jaka ingin mencoba buah ajaib lainnya.":
            $ current_node = 26
            jump expression story.get(current_node)

label scene2A2A: #Good Ending 4
    e "Jaka merasakan perubahan aneh setelah memakan buah ajaib itu. Tiba-tiba, dia bisa mengerti dan berbicara dengan semua makhluk di sekitarnya."
    characterSampingan "Halo, teman-teman! Aku bisa berbicara dengan kalian sekarang."
    e "Semua makhluk di sekitar Jaka mulai berbicara dan menyambutnya dengan antusias. Mereka berbagi cerita dan pengalaman mereka."
    burung "Selamat datang, Jaka! Kami sangat senang bisa berbicara denganmu."
    e "Jaka merasa sangat senang dan terhubung dengan makhluk-makhluk di dunia ini. Dia belajar banyak dari mereka dan merasa seperti bagian dari komunitas."
    e "Hari-hari Jaka dipenuhi dengan petualangan dan pengetahuan baru. Dia menemukan teman-teman sejati dan merasa sangat bahagia."
    e "Ketika tiba saatnya untuk pulang, Jaka merasa berat hati untuk pergi, tapi dia tahu bahwa dia selalu bisa kembali."
    pohon "Kami akan selalu merindukanmu, Jaka. Jangan lupa kembali lagi."
    characterSampingan "Aku pasti akan kembali. Terima kasih atas semuanya!"
    e "Dengan kenangan indah dan hati yang penuh kebahagiaan, Jaka pulang ke rumah, siap untuk petualangan lain di masa depan."
    $ current_node = 38
    jump expression story.get(current_node)

label scene2A2B: #Secret Ending 2
    e "Jaka merasa penasaran dengan buah-buahan ajaib lainnya. Dia meminta pohon untuk mencoba yang lain."
    characterSampingan "Aku ingin mencoba buah ajaib lainnya, pohon."
    pohon "Baiklah, Jaka. Ini adalah buah petualangan. Satu gigitan akan membawamu ke tempat yang paling ajaib di dunia ini."
    e "Jaka memetik buah itu dan menggigitnya. Seketika, dia merasa tubuhnya melayang dan dikelilingi oleh cahaya yang berkilauan."
    e "Dia tiba di sebuah tempat yang luar biasa indah, dengan air terjun berkilauan, padang bunga yang luas, dan makhluk-makhluk ajaib."
    characterSampingan "Wow, tempat ini luar biasa!"
    e "Jaka menjelajahi tempat itu dan menemukan banyak rahasia serta keajaiban. Dia bertemu dengan makhluk legendaris dan belajar tentang sejarah dunia tersebut."
    e "Di tengah petualangannya, Jaka menemukan sebuah artefak kuno yang memiliki kekuatan besar. Artefak itu memberinya kemampuan untuk memanggil portal ke Dunia Lucu kapan saja."
    characterSampingan "Dengan artefak ini, aku bisa kembali kapan saja aku mau!"
    e "Jaka merasa sangat beruntung dan bersyukur atas petualangan yang menakjubkan ini. Dia tahu bahwa dunia ini selalu terbuka untuknya, dan dia bisa kembali kapan saja."
    e "Dengan artefak di tangannya dan hati penuh kegembiraan, Jaka pulang ke rumah, siap untuk petualangan lainnya kapan saja dia inginkan."
    $ current_node = 39
    jump expression story.get(current_node)


label scene2B1:
    pohon "Betul! Masa depan selalu di depanmu tetapi tidak pernah bisa kamu lihat. Ayo, ikut aku!"
    e "Groot membawa Jaka ke sebuah pintu yang bisa membawanya pulang ke rumah."
    menu:
        "Jaka pulang ke rumah dan membawa pulang Groot sebagai teman.":
            $ current_node = 27
            jump expression story.get(current_node)
        
        "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu.":
            $ current_node = 28
            jump expression story.get(current_node)

label scene2B1A: #Canon Ending 2
    e "Jaka memutuskan untuk pulang ke rumah. Sebelum pergi, Groot memutuskan untuk ikut bersamanya sebagai teman."
    characterSampingan "Terima kasih, Groot! Aku akan sangat senang kalau kamu ikut denganku."
    pohon "Aku juga senang bisa bersamamu, Jaka. Mari kita pulang."
    e "Mereka berjalan melalui pintu dan tiba-tiba Jaka berada di kamarnya sendiri. Groot berdiri di sampingnya."
    e "Dengan Groot di sisinya, Jaka merasa lebih berani dan tidak pernah merasa kesepian lagi. Mereka berdua menjadi sahabat yang tak terpisahkan."
    e "Setiap kali Jaka ingin petualangan baru, ia tahu bahwa Groot akan selalu bersamanya."
    e "Jaka menjalani hidupnya dengan penuh keceriaan dan kenangan indah dari Dunia Lucu, dan dia tahu bahwa persahabatannya dengan Groot akan bertahan selamanya."
    $ current_node = 40
    jump expression story.get(current_node)

label scene2B1B: #Good Ending 5
    e "Jaka memutuskan untuk tinggal lebih lama di Dunia Lucu. Tempat itu penuh dengan keajaiban dan petualangan yang tak ada habisnya."
    characterSampingan "Aku ingin menjelajahi lebih banyak tempat di Dunia Lucu. Terlalu banyak yang belum aku lihat."
    pohon "Bagus sekali, Jaka! Mari kita mulai petualangan baru!"
    e "Groot membawa Jaka ke berbagai tempat yang menakjubkan. Mereka bertemu makhluk-makhluk aneh dan menikmati petualangan yang luar biasa."
    e "Suatu hari, Jaka menemukan sebuah gua tersembunyi yang belum pernah dilihat oleh siapapun sebelumnya. Di dalamnya, dia menemukan harta karun dan artefak ajaib."
    characterSampingan "Ini luar biasa! Tempat ini penuh dengan misteri dan keajaiban."
    e "Jaka memutuskan untuk menjadikan Dunia Lucu sebagai rumah keduanya. Setiap hari adalah petualangan baru, dan dia belajar banyak hal tentang dunia dan dirinya sendiri."
    e "Dalam hatinya, Jaka tahu bahwa dia telah menemukan tempat yang benar-benar ajaib, di mana impian menjadi kenyataan."
    $ current_node = 41
    jump expression story.get(current_node)

label scene2B2:
    pohon "Salah! Tapi tidak apa-apa, kamu masih punya satu kesempatan lagi. Apa yang memiliki ekor tapi bukan hewan?"
    menu:
        "layang-layang":
            $ current_node = 29
            jump expression story.get(current_node)
        
        "cacing":
            $ current_node = 30
            jump expression story.get(current_node)

label scene2B2A: #Worst Ending
    e "Jaka berpikir keras dan akhirnya menjawab."
    characterSampingan "Layang-layang!"
    pohon "Betul! Layang-layang memiliki ekor tapi bukan hewan. Tapi jawaban yang benar tidak cukup kali ini."
    e "Tiba-tiba, dunia di sekitar Jaka mulai berubah menjadi gelap dan mengerikan."
    characterSampingan "Apa yang terjadi?"
    pohon "Kamu telah menjawab dengan benar, tapi kamu telah menghabiskan semua kesempatanmu. Dunia ini bukan untukmu."
    e "Jaka merasa tubuhnya ditarik ke dalam kegelapan yang pekat. Dia berteriak, tapi suaranya tidak terdengar."
    e "Dia terjebak dalam dunia yang suram dan penuh dengan ketakutan. Tidak ada jalan keluar, tidak ada harapan."
    e "Jaka tersesat selamanya dalam kegelapan, tanpa ada yang bisa menolongnya."
    $ current_node = 42
    jump expression story.get(current_node)

label scene2B2B: #Worst Ending
    e "Jaka berpikir keras dan akhirnya menjawab."
    characterSampingan "Cacing!"
    pohon "Salah lagi! Jawaban yang benar adalah layang-layang. Tapi sekarang sudah terlambat."
    e "Tiba-tiba, tanah di bawah Jaka mulai retak dan dia jatuh ke dalam lubang yang dalam."
    characterSampingan "Aaaahhh!"
    e "Jaka jatuh ke dalam jurang yang gelap dan penuh dengan bayangan yang menakutkan."
    e "Dia mencoba memanjat keluar, tapi dindingnya terlalu licin dan tinggi. Jaka merasa putus asa."
    e "Dia terjebak di dalam jurang itu, tanpa ada yang bisa menolongnya. Tidak ada jalan keluar, tidak ada harapan."
    e "Jaka tersesat selamanya dalam kegelapan, tanpa ada yang bisa menolongnya."
    $ current_node = 42
    jump expression story.get(current_node)

label goodending1: 
    show bg goodending1
    e "Good Ending 1"
    with fade
    return 
    #31 gambar goodending 1A1A & 2A1A

label badending1: 
    show bg kutuk
    e "Bad Ending 1"
    with fade
    #32 gambar 1A1B
    
label goodending2: #33
    show bg goodending2
    e "Good Ending 2"
    with fade
    return
    #gambar goodending 1A2A & 1A2B

label canonending1: #34
    show bg canon1
    e "Canon Ending 1"
    with fade
    return
    #gambar canonending 1B1A

label secretending1: #35
    show bg secret1
    e "Secret Ending 1"
    with fade
    return
    #gambar secretending1B1B

label badending2: #36
    show bg bad2
    e "Bad Ending 2"
    with fade
    return
    #gambar bad ending 1B2A

label goodending3: #37  
    show bg good3
    e "Good Ending 3"
    with fade
    return
    #gambar good ending 1B2B

label goodending4: #38
    show bg witcher
    e "Good Ending 4"
    with fade
    return
    #gambar good ending 2A2A
    
label secretending2: #39
    show bg witcher
    e "Secret Ending 2"
    with fade
    return
    #gambar secret ending 2A2B

label canonending2: #40
    show bg witcher
    e "Canon Ending 2"
    with fade
    return
    #gambar canon ending 2B1A

label goodending5: #41
    show bg witcher
    e "Good Ending 5"
    with fade
    return
    #gambar goodending 2B1B

label worstending: #42
    show bg witcher
    e "Worst Ending"
    with fade
    return
    #gambar worst ending 2B2A & 2B2B ending