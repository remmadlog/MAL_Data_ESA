"""
In this file we are going to create plots for the analysis of the studio, genre and theme entries
We are mainly going to create barplots and heatmaps
We also provide a few tables

Nothing major here, just the usual creating of DataFrames and plotting.


PROBLEMS/QUESTIONS:
- sns.set(font_scale=.75)
- - I thought this is ment to scale to font of labels for the heatmaps in import seaborn as sns
- - it has an impact on the looks of the barh plots
- - - WHY
- - it scales things differently
- - - somtimes the font is smaller even though the heatmap/plot was created in the same for loop
- - todo: what is happening


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Genres:
['Drama', 'Sports', 'Avant Garde', 'Comedy', 0, 'Adventure', 'Slice of Life', 'Award Winning', 'Fantasy', 'Action', 'Sci-Fi', 'Romance', 'Hentai', 'Mystery', 'Supernatural', 'Horror', 'Ecchi', 'Suspense', 'Boys Love', 'Girls Love', 'Erotica', 'Gourmet']
Studios:
['Tokyo Movie Shinsha', 0, 'Kuri Jikken Manga Koubou', 'Toei Animation', 'Knack Productions', 'Takun Manga Box', 'Mushi Production', 'Tatsunoko Production', 'Tokyo TV Douga', 'Eiken', 'Otogi Production', 'Tezuka Productions', 'Asahi Production', 'Tokyo Movie', 'Shanghai Animation Film Studio', 'Animation Staff Room', 'Nippon TV Douga', 'Makino Production', 'Sunrise', 'Nippon Animation', 'TMS Entertainment', 'Madhouse', 'Studio Zero', 'Group TAC', 'Topcraft', 'Studio Live', 'Ashi Productions', 'Shin-Ei Animation', 'Academy Productions', 'DAX Production', 'Telecom Animation Film', 'Pierrot', 'Tsuchida Productions', 'Visual 80', 'Gainax', 'Sanrio', 'Studio Korumi', 'Studio Deen', 'Tama Production', 'Studio Cockpit', 'Oh! Production', 'SEK Studios', 'Kokusai Eigasha', 'Meruhensha', 'Artmic', 'Shaft', 'Daewon Media', 'Kitty Film Mitaka Studio', 'Kaname Productions', 'Toyo Links Corporation', 'Gallop', 'Magic Bus', 'Idol', 'AIC', 'APPP', 'MK Pictures', 'Ajia-do', 'Higashinaka Studio', 'Artland', 'Filmlink International', 'Bebow', 'Yamamura Animation, Inc.', 'Production Reed', 'Anime R', 'Studio Comet', 'Zero-G Room', 'Production Wave', 'Studio World', 'Aubec', 'Studio Ghibli', 'animate Film', 'Studio Unicorn', 'Hiro Media', 'Grouper Productions', 'Tokyo Media Connections', 'Circus Production', 'Kusama Art', 'Panmedia', 'Network Kouenji Studio', 'Big Bang', 'Phoenix Entertainment', 'J.C.Staff', 'Agent 21', 'Nakamura Production', 'Telescreen', 'Studio G7', 'Triangle Staff', 'D.A.S.T Corporation', 'Kino Production', 'Gakken', 'Ginga Teikoku', 'ACC Production', 'Wako Productions', 'Mook Animation', 'K-Factory', 'Studio Fantasia', 'Studio 88', 'Production I.G', 'Daume', 'Doga Kobo', '3D Co.', 'Studio Junio', 'Polygon Pictures', 'Studio Sign', 'NHK', 'Animaruya', 'Takahashi Studio', 'Tokyo Kids', 'Urban Product', 'Studio Core', 'Studio Signal', 'Suna Kouhou', 'Watanabe Promotion', 'Deck', 'Animation 21', 'Hanho Heung-Up', 'Dongwoo A&E', 'Animation 501', 'Pastel', 'Darts', 'Azeta Pictures', 'MI', 'Project Team Muu', 'Studio Hibari', 'Studio Hakk', 'MAT', 'SIDO LIMITED', 'Life Work', 'Kyoto Animation', 'Three-d', 'Studio Wombat', 'Studio Coa', 'OB Planning', 'Studio 4°C', 'Tsuburaya Productions', 'Mippei Eigeki Kiryuukan', 'ONIRO', 'Studio Kikan', 'Studio Kyuuma', 'E&G Films', 'Dynamic Planning', 'Egg', 'Minami Machi Bugyousho', 'Bee Media', 'Nippon Ramayana Film Co.', 'KSS', 'Sanctuary', 'Animation Studio Wagumi', 'OutSide Directors Company', 'Hand to Mouse.', 'Image Kei', 'JCF', 'Studio Gazelle', 'Arms', 'Hero', 'Triple X', 'TEC', 'Horannabi', 'Studio Take Off', 'Echo', '81 Produce', 'Robot Communications', 'OLM', 'I.Toon', 'Studio OX', 'Momoi Planning', 'Xebec', 'Dangun Pictures', 'Sofix', 'Wise Guy', 'N&G Production', 'C and R', 'Atorie A.B.C.', 'Twenty First', 'Chaos Project', 'Project Team Sarah', 'General Entertainment', 'Vega Entertainment', 'Office AO', 'PP Project', 'Rikuentai', 'Annapuru', 'Movic', 'Front Line', 'HAL Film Maker', 'Shelty', 'Radix', 'Plum', 'Y.O.U.C', 'Trans Arts', 'Ripple Film', 'Studio B&M', 'ANIDO FILM', 'Studio Meditation With a Pencil', 'Studio Bogey', 'Public & Basic', "Brain's Base", 'Gonzo', 'Tamura Shigeru Studio', 'Four Some', 'Bee Train', 'GAV Video', 'Image Studio 109', 'Studio Z5', 'Studio March', 'Production D.M.H', 'dwarf', 'Seoul Movie', 'RG Animation Studios', 'pH Studio', 'Meltdown', 'Kent House', 'Zexcs', 'P core', 'Anon Pictures', 'Milky Cartoon', 'Garyuu Studio', 'JOF', 'Venet', 'VAP', 'Satelight', 'Actas', 'TCJ', 'Zuiyo', 'Yumeta Company', 'SBS TV Production', 'Tomoyasu Murata Company', 'Bones', 'M&M', 'G.P Entertainment', 'Studio D-Volt', 'Sovat Theater', 'Studio Flag', 'TNK', 'Dream Entertainment', 'Anima', 'ORADA COMPANY', 'Alice Production', 'Studio Jin', 'AT-2', 'Onion Studio', 'Mikimoto Production', 'Sonsan Kikaku', 'KKC Animation Production', 'Ishikawa Pro', 'M.S.C', 'Kojiro Shishido Animation Works', 'Guo Pengzi Studio', 'Office Take Off', 'Shinkuukan', 'Atti Production', 'Executive Decision', 'Idea Factory', 'Digital Dream Studios', 'Studio Jam', 'A-Line', 'Blue Cat', 'Creators Dot Com', 'teevee graphics', 'Square Pictures', 'Studio Rikka', 'Datama Film', 'Shindeban Film', 'Studio Dolphin Night', 'T.P.O', 'EOEO System', 'Sanrio Digital', 'Opera House', 'Japan Vistec', 'Studio G-1Neo', 'Imagin', 'Arcturus', 'AMGA', 'Aiti St.', 'Buyuu', 'CoMix Wave Films', 'Studio Matrix', 'Palm Studio', 'A.C.G.T.', 'Romanov Films', 'Himajin Planning', 'Soeishinsha', 'Concept Films', 'Shura', 'Image House', 'Shinjukuza', 'Ai Yume Mai', 'Synergy Japan', 'GANSIS', 'T-Rex', 'Tsubo Production', 'IKK Room', 'Media Factory', 'ufotable', 'ACiD FiLM', 'Studio Egg', 'I-move', 'C&S Production', 'Studio Guts', 'Viewworks', 'Picture Magic', 'Potato House', 'Mirai Film', 'Nippon Columbia', 'Manglobe', 'foodunited.', 'Liberty Animation Studio', 'Kamikaze Douga', 'Studio 9 Maiami', 'Studio Kelmadick', 'Tryforce', 'cogitoworks', 'feel.', 'Planet', 'Seven Arcs', 'Kyushu Network Animation', 'Itasca Studio', 'J.K.I', 'Marine Entertainment', 'OLM Digital', 'DR Movie', 'CCTV Animation', 'Creatures Inc.', 'AIC ASTA', 'Big Wing', 'Maboroshi Koubou', 'No Side', 'Axis', 'Trinet Entertainment', 'Enjin Productions', 'Arcs Create', 'G&G Direction', 'AIC Spirits', 'WAO World', 'Piko Studio', 'Aiko', 'Blue Note', 'Schoolzone', 'DLE', 'Digital Frontier', 'G&G Entertainment', 'Anime Antenna Iinkai', 'Studio Ranmaru', 'Studio Kajino', 'CinePix', 'Yamato Works', 'Sugar Boy', 'Studio Soul', 'Studio A-CAT', 'Nomad', 'Silver', 'Studio Ten', 'Lead', 'B&T', 'Ocon Studio', 'Animation Planet', 'Plus Heads', 'Studio Crocodile', 'Karaku', 'J.C.F.', 'The Answer Studio', 'Trash Studio', 'SynergySP', 'asread.', 'Shogakukan Music & Digital Entertainment', 'Suzuki Mirano', 'Enzo Animation', 'Eshoya Honpo', 'Studio Bingo', 'AYCO', 'Dyna Method', 'Square Enix Visual Works', 'XEBEC M2', 'PPM', 'Wang Film Productions', 'Flavors Soft', 'Sunny Side Up', 'Kazuki Production', 'Graphinica', 'Studio Barcelona', 'Lyrics', 'Kanaban Graphics', 'Inugoya', 'DOGA Productions', 'Hong Ying Animation', 'Puzzle Animation Studio Limited', 'D & D Pictures', 'Marvelous Entertainment', 'Ginga Ya', 'Remic', 'Gonzino', 'A-1 Pictures', 'Digital Media Lab', 'RAMS', 'Sumomo Film', 'Toei Video', 'Durufix', 'Ishimori Entertainment', 'Fanworks', 'BeSTACK', 'Sunwoo Entertainment', 'Mook DLE', 'Sparkly Key Animation Studio', 'Kenji Studio', 'San-X', 'KAGAYA Studio', 'GARDEN LODGE', 'Iyasakadou Film', 'TUBA', 'Hutoon Animation', 'Cafe de Jeilhouse', 'Yuhodo', 'Cutie Bee', 'JM Animation', 'Alpha Animation', 'Moss Design Unit', 'Khara', 'Diomedéa', 'Oxybot', 'Beat Frog', 'Office TakeOut', 'Melissa', 'Space-X', 'Iconix Entertainment', 'Spooky graphic', 'Shirogumi', 'PrimeTime', 'CyberConnect2', 'Studio Eromatick', 'Imagica', 'Kaeruotoko Shokai', 'Echoes', 'Studio Placebo', 'P.A. Works', 'Anpro', 'Shikachan Studio', 'Imagestone Inc.', 'Kate Arrow', 'Oz Inc.', 'Jinnis Animation Studios', 'Gunners', 'Studio Dadashow', 'I was a Ballerina', 'Studio Animal', 'Pierrot Plus', 'Olive Studio', 'Studio Pastoral', 'Amarcord', 'AIC PLUS+', 'Pink Cat', 'Nihikime no Dozeu', 'Studio Ten Carat', 'Studio Moriken', 'Marza Animation Planet', 'Kami Kukan', 'Sugata Creative & Design', 'TYMOTE', 'Marvy Jack', 'White Fox', 'SILVER LINK.', 'David Production', 'Kinema Citrus', 'Code', 'TYO Animations', 'Barnum Studio', 'Kachidoki Studio', 'GoHands', 'Heewon Entertainment', 'NHK Enterprises', 'PoRO', 'Encourage Films', 'W+K Tokyo', 'Creative Power Entertaining', 'Hoods Entertainment', '8bit', 'KeyEast', 'REALTHING', 'Picograph', 'Studio Boogie Nights', 'Mouse', 'Indeprox', 'Saigo no Shudan', 'Minakata Laboratory', 'Twilight Town', 'Panda Factory', 'G-Lam', 'Studio PuYUKAI', 'Gathering', 'Stingray', 'Mirai Fusion', 'Decovocal', 'Qianqi Animation', 'P.I.C.S.', 'Hananona Studio', 'Misogo Animation Studio', 'Rising Force', 'Future Planet', 'Beijing Huihuang Animation Company', 'Le-joy Animation Studio', 'Shanghai Hippo Animation', 'Super Brain', 'Studio Vandal', 'Brians Film', 'Ascension', 'Ordet', 'Bridge', 'ChuChu', 'Primastea', 'Public Enemies', 'Zyc', 'Office No. 8', 'MooGoo', 'Welz Animation Studios', 'Sunny Gapen', 'Studio Gale', 'Wong Ping Animation Lab', 'CMAY Animation', 'SAMG Entertainment', 'AIC Build', 'Studio Gokumi', 'Purple Cow Studio Japan', 'AIC Takarazuka', 'Studio Blanc.', 'Kantou Douga Kai', 'Comma Studio', 'Transistor Studio', 'Project No.9', 'Fantawild Animation', 'AIC Classic', 'Studio Gram', 'Valkyria', 'HMCH', 'Earth Design Works', 'Taikong Works', 'Hu Po Donghua', 'Seven', 'Studio Ppuri', 'Yaoyorozu', 'Pollyanna Graphics', 'TOHO animation', 'Onionskin', 'HIDEHOMARE', 'Studio Goindol', 'Lerche', 'Collaboration Works', 'Rabbit Gate', 'Odolttogi', 'Wolf Smoke Studio', 'Office DCI', 'Pops Inc.', 'Studio Binzo', 'Majin', 'StudioRF Inc.', 'LMD', 'uzupiyo Animation & Digital Works', 'Transcendence Picture', 'SANZIGEN', 'Okumaza', 'Studio Izena', 'MAPPA', 'Rocen', 'Mad Box', 'B.CMAY PICTURES', 'Ekura Animal', 'Studio Nuck', 'LandQ studios', 'Tomason', 'Hotline', 'C2C', 'Frontier Works', 'Maxilla', 'Seven Stone Entertainment', 'Sparky Animation', 'Studio Chizu', 'Studio Kai', 'Marone', 'lxtl', 'Jumondo', 'Studio Prokion', 'Sola Digital Arts', 'AIC Frontier', 'HOTZIPANG', 'KOO-KI', 'MontBlanc Pictures', 'L²Studio', 'Next Media Animation', 'Oddjob', 'Trigger', 'Fifth Avenue', 'Bandai Namco Pictures', 'teamKG', 'Passione', 'Larx Entertainment', 'Studio 1st', 'Kazami Gakuen Koushiki Douga-bu', 'Charaction', 'Automatic Flowers Studio', 'Soft Garage', 'Shueisha', 'HS Pictures Studio', 'Husio Studio', 'LIDENFILMS', 'Ishibashi Planning', 'An DerCen', 'Piso Studio', 'Calf Studio', 'Wit Studio', 'Seven Arcs Pictures', 'Orange', 'Peak Hunt', 'Assez Finaud Fabric', 'qmotri', 'Animation Do', 'ILCA', 'happyproject', 'Pie in the sky', 'Drawing and Manual', 'DandeLion Animation Studio', 'Connect', 'Studio Colorido', "Steve N' Steven", 'Studio Gadget', 'Haoliners Animation League', 'Colored Pencil Animation', 'Foch Film', 'drop', 'LAN Studio', 'Yamiken', 'Tecarat', 'trenova', 'NAZ', 'Production IMS', 'Ultra Super Pictures', 'Circle Tribute', 'Lay-duce', 'Creators in Pack', '10Gauge', 'Shimogumi', 'Cyclone Graphics', 'MMDGP', 'Taomee', 'Light Chaser Animation Studios', 'Studio UGOKI', 'JJJOY Animation Studios', 'VCRWORKS', 'Studio Artegg', 'C-Station', 'BreakBottle', 'Sprite Animation Studios', 'Poncotan', 'TROYCA', 'Fuji TV', 'Tri-Slash', 'Jumonji', 'Mili Pictures', 'Rockwell Eyes', 'Vasoon Animation', 'Delpic', 'Sankaku', 'Pmats9 studio', 'Studio 3Hz', 'StealthWorks', 'CloverWorks', 'Drive', 'Ijigen Tokyo', 'Nexus', 'Dynamo Pictures', 'Studio BAZOOKA', 'Keyring', 'Oyster', '2:10 Animation', 'Shuka', 'I.Gzwei', 'New Generation', 'MB planning', 'CG Year', 'Usagi Ou', 'Uguisu Kobo', 'Studio Yona', 'GARDEN Culture', 'EMT Squared', 'Millepensee', 'Studio! Cucuri', 'A-Real', 'W-Toon Studio', 'Studio Ponoc', 'studio YOG', 'THREE IS A MAGIC NUMBER', 'Studio VOLN', 'PRA', 'Wawayu Animation', 'Team YokkyuFuman', 'October Media', 'Spoon', 'YHKT Entertainment', 'FOREST Hunting One', 'Science SARU', 'MARK', 'Tomovies', 'Signal.MD', 'Kyotoma', 'Office Nobu', 'Sakura Create', 'Neft Film', 'Gaina', 'Dazzling Star', 'Takara Tomy A.R.T.S', 'Central Animation Studio', 'AXsiZ', "Ryuu M's", 'PINE JAM', 'domerica', 'MoMo Production', 'Fortes', 'Issen', 'Buemon', 'Teatro Nishi Tokyo Studio', 'AIC Project', 'Super Normal Studio', 'Dancing CG Studio', 'Rabbit Machine', 'Tonko House', 'Asura Film', 'Studio Nanahoshi', 'Qualia Animation', 'Lapin Track', 'Joker Films', 'Composition Inc.', 'Thundray', '7doc', 'Happy Elements', 'ANYZAC', 'Egg Firm', 'GEMBA', 'Platinum Vision', 'Namu Animation', 'Zero-G', 'Bouncy', 'KIZAWA Studio', 'HORNETS', 'BUILD DREAM', 'Original Force', 'Craftar Studios', 'TriF Studio', 'Studio Button', 'Koinrush Studio', 'Blade', 'Tengu Kobo', 'Samsara Animation Studio', 'Sotsu', 'Yokohama Animation Laboratory', 'Studio Tumble', 'Yudubai Animation', 'LIGHTAIR Inc.', 'TOCSIS', 'TrioPen Studio', 'Boyan Pictures', 'WHOPPERS', 'Hurray!', 'STUDIO 8 DOGS', 'sugarsaltpepper', 'Nut', 'Typhoon Graphics', 'Geno Studio', 'Studio M2', 'Success Corp.', 'Sunflowers', 'XFLAG Pictures', 'Will Palette', 'Karasfilms', 'Tsukimidou', 'Ripromo', 'Kamio Japan', 'The Village of Marchen', 'Angle', 'Slow Studio', 'Steamworks', 'Shykeumo Animation Studio', 'Imagineer', 'Lesprit', 'Ruo Hong Culture', 'Chiptune', 'CUKA', 'Gyorai Eizo Inc.', 'Studio Gohan', 'G-angle', 'Eallin', 'CGCG Studio', 'DMM.futureworks', 'Big Firebird Culture', 'CygamesPictures', 'ABJ COMPANY', 'Flat Studio', 'Motion Magic', 'iDRAGONS Creative Studio', 'Studio Khronos', 'Bibury Animation Studios', 'Akatsuki', 'Nice Boat Animation', 'Revoroot', 'Sega Interactive', 'Coastline Animation Studio', 'Studio Pivote', 'MAINCONCEPT', 'Hezmon Animation', 'Kobito', 'Felix Film', 'production doA', 'Studio CA', 'Mokai Technology', 'Maro Studio', 'Live2D Creative Studio', 'HeART-BIT', 'Fenz', 'Yinhe Changxing Culture', 'studio2 Animation Lab', 'Emon', 'Studio Flad', 'LICO', 'Red Dog Culture House', 'helo.inc', 'Picona', 'Studio KeepFire', 'Strawberry Meets Pictures', 'ASK Animation Studio', 'Imagica Imageworks', 'Directions', 'Marui Group', 'Goto Inc.', '6pucks', 'Sharefun Studio', 'AHA Entertainment', 'Studio Lings', 'EKACHI EPILKA', 'Anime Beans', 'Pb Animation Co. Ltd.', 'Space Neko Company', 'Dawn Animation', 'Brio Animation', 'Shion', 'CLAP', 'Grom', 'Aurum Production', 'Yi Chen Animation', 'Studio Palette', 'Tong Ming Xuan', 'UWAN Pictures', '33 Collective', 'Studio Kingyoiro', 'NHK Art', 'CUEBiC Inc.', 'Ezόla', 'Production GoodBook', 'GRIZZLY', 'Ark', 'Tear Studio', 'aNCHOR', 'DRAWIZ', 'monofilmo', 'Qiyuan Yinghua', 'Zelico Film', 'Blue bread', 'Studio GOONEYS', 'Shengying Animation', 'PERIMETRON', 'BYMENT', 'Sublimation', 'Arvo Animation', 'THINKR', 'Acca effe', 'Making Animation', 'Chosen', 'Studio W.Baba', 'Painting Dream', 'Studio Himalaya', 'Magia Doraglier', 'Saetta', 'IMAGICA Lab.', 'Geek Toys', 'Okuruto Noboru', 'Ankama Animations', 'MASTER LIGHTS', 'Guton Animation Studio', 'SELFISH', 'Hololive Production', 'Suspenders', 'New Deer', 'Speed Inc.', 'Studio Shelter', 'Locus Corporation', 'Kitchen Ltd.', 'Studio A. Craft', 'Asmik Ace', 'Lide', 'Suoyi Technology', 'XFLAG', 'Fukushima Gaina', 'CUCURI', 'Digital Network Animation', 'Point Pictures', 'Nekonigashi Inc.', 'Keica', 'Griot Groove', 'OTOIRO', 'Flying Ship Studio', 'Ekakiya', 'Ice Butter', 'Particlefield', 'Escape Velocity Animation', 'Think Corporation', 'Twilight Studio', 'Giga Production', 'MMT Technology', 'Twin Engine', 'Enishiya', 'FILMONY', 'Project Studio Q', 'AQUA ARIS', 'Bakken Record', 'Green Monster Team', 'StoryRiders Co. Ltd.', 'East Fish Studio', 'Maho Film', 'Xiaoming Taiji', 'Pony Canyon', 'Kaca Entertainment', 'Genco', '717 Animation Studio', 'Taiko Studios', 'Congrong Film', 'Studio Hokiboshi', 'I & A', 'Nur', "D'ART Shtajio", 'Grayscale Arts', 'Arch', 'LX Animation Studio', "Monster's Egg", 'MORIE Inc.', 'Animation Lab Japan', 'V-sign', 'Cocktail Media', 'ENGI', 'Anima&Co.', 'Sunrise Beyond', 'Nihon Ad Systems', 'Yostar Pictures', 'Gainax Kyoto', 'Planet Nemo Animation', 'Cloud Art', 'l-a-unch・BOX', 'Studio DURIAN', 'Yonago Gainax', 'Caviar', 'Youku', "Children's Playground Entertainment", 'Studio Signpost', "Rock'n Roll Mountain", 'Albacrow', 'Studio CANDY BOX', 'Blaze Studio', 'Artner', 'VROOOOM', 'Pancake', 'Studio Bind', 'ROLL2', 'SPEED', 'Benlai Pictures', 'Borutong', 'Gosay Studio', 'Mimoid', 'team Yamahitsuji', 'Ai Si Animation Studio', 'Chongzhuo Animation', 'A4A Inc.', 'KWANED', 'Wolfsbane', 'Studio Elle', 'Djinn Power', 'Toho Interactive Animation', 'Wonder Cat Animation', 'Flint Sugar', 'Spell Bound', 'Wei Chuang Jiang Xin', 'DC Impression Vision', 'Ten Tails Animation', '1IN', 'LB Commerce', 'HoriPro', 'STUDIOK110', 'Adonero', 'Team TillDawn', 'Ether Kitten', 'Lingsanwu Animation', 'Beijing Enlight Pictures', 'Hai An Xian Donghua Gongzuo Shi', 'TANOsim', 'Atelier Tuki', 'Visual Flight', 'Magma Studio', 'PONOS Corporation', 'ORENDA', 'Poly Animation', 'Xuni Ying Ye', 'Jichitai Anime', 'Tsumugi Akita Animation Lab', 'Xanthus Media', 'TthunDer Animation', 'Miyu Productions', 'Elias', 'Qubic Pictures', 'GIFTanimation', 'Studio Jemi', 'Studio Daisy', 'Paper Plane Animation Studio', 'Colored Pencil Animation Japan', 'Mousou Senka', 'studio MOTHER', 'Wulifang', 'Year Young Culture', 'Delight Animation', 'FIREBUG', 'Noovo', 'Brick Studio', 'Atelier Pontdarc', 'Studio Kafka', 'Cloud Hearts', 'Quebico', 'yell', 'Village Studio', 'The Monk Studios', 'SJYNEXCUS', 'Gambit', 'Nostalook', 'Volca', 'Qzil.la', 'Au Praxinoscope', 'Bigcat Studio', 'Alpha Group', 'Flagship Line', 'Indivision', 'Kung Fu Frog Animation', 'ARECT', 'Joicy Studio', 'Paper Animation', 'Story Effect', 'Gravity Well', 'Scooter Films', 'Myung Films', 'YURUPPE Inc.', 'Stereotype', 'Khaki', 'OZ', 'Quad', 'Production +h.', 'Kigumi', 'Staple Entertainment', 'Oriental Creative Color', 'Jinnan Studio', 'd00r works', 'Tang Kirin Culture', 'Ga-Crew', 'HuaDream', "STUDIO6'oN", 'Xing Yi Kai Chen', 'Kuai Ying Hu Yu', 'AION Studio', 'Imagica Digitalscape', 'Qiying Animation', 'ARCUS', 'StudioXD', 'FUNNY MOVIE', 'Shadow Steps', 'Bibury Animation CG', 'Planet Cartoon', 'Fever Creations', 'Shenman Entertainment', 'Frontier One', 'Passion Paint Animation', 'Amineworks', 'Windy Studio', 'Infinity Vision', 'EDP graphic works', 'Miota', '924 Studio', 'studio NAGURI', 'flag Co.', 'Mainichi Eigasha', 'Panda Tower Studio', 'Studio Massket', 'Tonari Animation', 'CMC Media', 'High Energy Studio', 'Studio Sota', 'HuaMei Animation', 'Aurora Animation', 'GUMBLAB', 'Euluca Lab', 'SIGNIF', 'CANON RECORDINGS', 'CHOCOLATE', 'Avaco Creative Studios', 'Outline', 'Studio Mir', 'Alfred Imageworks', '5 Inc.', 'UchuPeople', 'Qingxiang Culture', 'Pure Arts', 'Quyue Technology', 'TypeZero', 'THINGS.', 'Studio Matomo', 'Haneda xR Studio', 'Makaria', 'NANON CREATIVE', 'Laftel', 'CANOPUS', 'Million Volt', 'Shadow Pond Studio', 'Liber', 'Heart & Soul Animation', 'Bandai Namco Filmworks', 'TOHO animation STUDIO', 'Contrail', 'Starry Cube', 'Gekkou', 'Saber Project', 'studio hb', 'miHoYoAnime', 'Liyu Culture', 'Studio HUIT', 'Shengguang Knight Culture', 'soket', 'maroyaka', 'Fengyun Animation', 'Studio Lemon', 'Youliao Studio', 'R11R', 'ASTROBROS.', 'Studio Moe', 'CELAVIE', 'Flying Monkeys Production', 'BUG FILMS', 'PHANTOM', 'BUDDHA INC.', 'Medo', 'INTERFACEDOGS', 'Cloud Culture', 'CompTown', 'Unend', 'Studio Fusion', 'Fugaku', 'evg', 'MOJO Animation', 'ORCEN', 'Painted Blade Studio', 'Kassen', 'Infinity Animations', 'Manaa Animation', 'Studio Add', 'E&H Production', 'Studio Polon', 'BloomZ', 'ILCASHIPS', 'Konami animation', 'Studio Eight Color', 'Gear Studio', 'Andraft', 'Team OneOne', '100studio', 'Anime Tokyo', 'Alke', 'BlueArc Animation Studios', 'studio ALBLE', 'Studio N', 'Shogakukan-Shueisha Productions', 'Creative House Pocket', 'Production HASU', 'Imagica Infos', 'EOTA', 'Imageworks Studio', 'Nagomi', 'Studio Outrigger', 'Studio Harutonari', 'Pierrot Films', 'Rhythmos', 'FAB', 'Whatever Co.', 'Tsumupapa', 'DEFT', 'Hayabusa Film', 'Voil', 'SAFEHOUSE', 'Reirs', 'Manga Productions', 'Tianshi Wenhua', 'Shuiniu Dongman', 'AOI Pro.']
Themes:
['Team Sports', 0, 'Parody', 'Psychological', 'Combat Sports', 'Music', 'Historical', 'Martial Arts', 'Samurai', 'Mythology', 'Super Power', 'Educational', 'Military', 'Racing', 'Adult Cast', 'Gag Humor', 'School', 'Anthropomorphic', 'Pets', 'Mahou Shoujo', 'Mecha', 'Space', 'Detective', 'Visual Arts', 'Vampire', 'Crossdressing', 'Strategy Game', 'Time Travel', 'Otaku Culture', 'Video Game', 'Childcare', 'Isekai', 'Organized Crime', 'Idols (Female)', 'Love Polygon', 'Performing Arts', 'Gore', 'Medical', 'Delinquents', 'Workplace', 'Showbiz', 'Magical Sex Shift', 'Idols (Male)', 'Reverse Harem', 'Iyashikei', 'Harem', 'Reincarnation', 'Survival', 'CGDCT', 'High Stakes Game', 'Urban Fantasy', 'Love Status Quo', 'Villainess']
"""


import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# use for saving a plt as it is, transparent and as SVG
def plt_save(name):
    plt.savefig('Plots/SGT/'  + name + '.png', dpi=350)
    plt.savefig('Plots/SGT/transparent_png/' + name + '.png', dpi=350, transparent=True)
    plt.savefig('Plots/SGT/SVG/' + name + '.svg', dpi=350, transparent=True)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # loading filed
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Open the created merged tables
#  table_merged
dfm = pd.read_excel('xlsx_tables/S_1970_2024_merged.xlsx').fillna(0)
# table_merged_unique
dfmu = pd.read_excel('xlsx_tables/S_1970_2024_merged_unique.xlsx').fillna(0)

# reset file for printed tables
with open("sgt_table_markdowns.txt", "w") as f:
    f.close()


# prepare loaded tables:
# we usually only consider entries that have scores:
dfm = dfm[dfm["score"]>0]
dfmu = dfmu[dfmu["score"]>0]

# in addition, we should only consider entries that are NOT airing currently
# # we do this episode amount and duration per episode is very unclear (sometimes just 0)
dfm = dfm[dfm["status"] == "Finished Airing"]
dfmu = dfmu[dfmu["status"] == "Finished Airing"]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # complementing data
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# adding TimeFrame (TF) || adding DurationFrame (DF) || adding EpisodeFrame (EF)
for table in [dfm,dfmu]:
    table["TF"] = np.where(
        table["year"] < 2000, "1970-1999", np.where(
            table["year"] < 2015, "2000-2014", np.where(
                table["year"] < 2025, "2015-2024", "2025")
        )
    )
    
    table["DF"] = np.where(
        table["duration"] < 5, "< 005min", np.where(
            table["duration"] < 10, "< 010min", np.where(
                table["duration"] < 20, "< 020min", np.where(
                    table["duration"] < 30, "< 030min", np.where(
                        table["duration"] < 45, "< 045min", np.where(
                            table["duration"] < 60, "< 060min", np.where(
                                table["duration"] < 90, "< 090min", np.where(
                                    table["duration"] < 120, "< 120min", np.where(
                                        table["duration"] < 150, "< 150min", np.where(
                                            table["duration"] < 160, "< 160min", ">= 160min")
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    table["EF"] = np.where(
        table["episodes"] < 4, "< 004 Ep", np.where(
            table["episodes"] < 10, "< 010 Ep", np.where(
                table["episodes"] < 14, "< 014 Ep", np.where(
                    table["episodes"] < 21, "< 021 Ep", np.where(
                        table["episodes"] < 25, "< 025 Ep", np.where(
                            table["episodes"] < 60, "< 060 Ep", np.where(
                                table["episodes"] < 100, "< 100 Ep", np.where(
                                    table["episodes"] < 200, "< 200 Ep", np.where(
                                        table["episodes"] < 300, "< 300 Ep", np.where(
                                            table["episodes"] < 500, "< 500 Ep", ">= 500 Ep")
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- genre/theme amount per year
- - what was most used
- - what combination was most used
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# table that gives the amount of each genre per year
temp_table = dfm[(dfm["genre"] != 0)].groupby(["year","genre"]).size()
# get genre with most entries
# .groupby(level=0)
# # grouby "year"
# .idxmax()
# # per group in temp_table get the max value e.g. (1970, 'Sports') and return a table: year|([year],[genre])
# .values
# # get an array of the form: (1970, 'Sports'), (1971, 'Comedy'), (1972, 'Adventure')...
temp = temp_table.groupby(level=0).idxmax().values
# from temp_table get the rows corresponding to entries in temp
# # e.g. (1970, 'Sports') gives us the row: 1970 | Sports | 12
max_genre_years = temp_table.loc[temp]


# do the same for studio and theme
# # studio
temp_table = dfm[(dfm["studio"] != 0)].groupby(["year","studio"]).size()
temp = temp_table.groupby(level=0).idxmax().values
max_studio_years = temp_table.loc[temp]


# # theme
temp_table = dfm[(dfm["theme"] != 0)].groupby(["year","theme"]).size()
temp = temp_table.groupby(level=0).idxmax().values
max_theme_years = temp_table.loc[temp]


# todo: visualization
# go for a table
# genre
max_genre_years = max_genre_years.reset_index()
max_genre_years.columns = ["year", "genre.max", "amount"]
print(max_genre_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max genre per year\n")
    f.write(max_genre_years.to_markdown(index=False))
    f.write("\n\n")

# theme
max_studio_years = max_studio_years.reset_index()
max_studio_years.columns = ["year", "studio.max", "amount"]
print(max_studio_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max studio per year\n")
    f.write(max_studio_years.to_markdown(index=False))
    f.write("\n\n")

# studio
max_theme_years = max_theme_years.reset_index()
max_theme_years.columns = ["year", "theme.max", "amount"]
print(max_theme_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max theme per year\n")
    f.write(max_theme_years.to_markdown(index=False))
    f.write("\n\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Now we do this for combinations -- todo: This is not super interesting
# # genre
temp_table = dfmu[(dfmu["genre"] != 0)].groupby(["year","genre"]).size()
temp = temp_table.groupby(level=0).idxmax().values
max_genre_years = temp_table.loc[temp]
# # studio
temp_table = dfmu[(dfmu["studio"] != 0)].groupby(["year","studio"]).size()
temp = temp_table.groupby(level=0).idxmax().values
max_studio_years = temp_table.loc[temp]
# # theme
temp_table = dfmu[(dfmu["theme"] != 0)].groupby(["year","theme"]).size()
temp = temp_table.groupby(level=0).idxmax().values
max_theme_years = temp_table.loc[temp]


# todo: visualization (went for table)
# genre
max_genre_years = max_genre_years.reset_index()
max_genre_years.columns = ["year", "genre.max", "amount"]
print(max_genre_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max genre combination per year\n")
    f.write(max_genre_years.to_markdown(index=False))
    f.write("\n\n")

# theme
max_studio_years = max_studio_years.reset_index()
max_studio_years.columns = ["year", "studio.max", "amount"]
print(max_studio_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max studio combination per year\n")
    f.write(max_studio_years.to_markdown(index=False))
    f.write("\n\n")

# studio
max_theme_years = max_theme_years.reset_index()
max_theme_years.columns = ["year", "theme.max", "amount"]
print(max_theme_years.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Max theme combination per year\n")
    f.write(max_theme_years.to_markdown(index=False))
    f.write("\n\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- GT in relation to scores over time
- - no combination
- - no studio cause not interesting imo
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# get average score per year per genre -- do not look at genre = "Award Winning"
temp_table = dfm[(dfm["genre"] != 0) & (dfm["genre"] != "Award Winning")].groupby(["year","genre"])["score"].mean()
# towards getting the highest average score per year
temp = temp_table.groupby(level=0).idxmax().values
# table with best reforming genre per year
best_genre = temp_table.loc[temp]

# get the amount of genres (again)
temp = dfm[(dfm["genre"] != 0)].groupby(["year","genre"]).size().to_frame().reset_index()
temp.columns = ["year", "genre", "amount"]
# merge best_genre and temp (amount genre per year) to get the best performing genres per year and their amount
table_merge_best_genre_size = pd.merge(best_genre, temp, on=["year","genre"])

# todo: visualization (went for table)
print(table_merge_best_genre_size.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Best genre per year\n")
    f.write(table_merge_best_genre_size.to_markdown(index=False))
    f.write("\n\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# do the same for theme
temp_table = dfm[(dfm["theme"] != 0)].groupby(["year","theme"])["score"].mean()
temp = temp_table.groupby(level=0).idxmax().values
best_theme = temp_table.loc[temp]
# again going for the merge
temp = dfm[(dfm["theme"] != 0)].groupby(["year","theme"]).size().to_frame().reset_index()
temp.columns = ["year", "theme", "amount"]
table_merge_best_theme_size = pd.merge(best_theme, temp, on=["year","theme"])

# todo: visualization (went for table)
print(table_merge_best_theme_size.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Best theme per year\n")
    f.write(table_merge_best_theme_size.to_markdown(index=False))
    f.write("\n\n")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# do the same for studio
temp_table = dfm[(dfm["studio"] != 0)].groupby(["year","studio"])["score"].mean()
temp = temp_table.groupby(level=0).idxmax().values
best_studio = temp_table.loc[temp]
# again going for the merge
temp = dfm[(dfm["studio"] != 0)].groupby(["year","studio"]).size().to_frame().reset_index()
temp.columns = ["year", "studio", "amount"]
table_merge_best_studio_size = pd.merge(best_studio, temp, on=["year","studio"])

# todo: visualization (went for table)
print(table_merge_best_studio_size.to_markdown(index=False))
with open("sgt_table_markdowns.txt", "a") as f:
    f.write("Best studio per year\n")
    f.write(table_merge_best_studio_size.to_markdown(index=False))
    f.write("\n\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Barplots for genre and theme (amount overall)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# GENRE
temp_table = dfm[(dfm["genre"] != 0)].groupby(["genre"]).size().to_frame()
temp_table.columns = ["amount"]

plt.figure(figsize=(20, 10))
# this, I do NOT know why, results in very pretty bar plots!
# also results in tiny font for the heatmaps so we have to account for that
sns.set(font_scale=1)
plt.barh(temp_table.index,temp_table["amount"])

plt.title("Amount per genre")
# plt.show()

plt_save("bar_genre_amount")
plt.clf(), plt.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THEME
temp_table = dfm[(dfm["theme"] != 0)].groupby(["theme"]).size().to_frame()
temp_table.columns = ["amount"]

plt.figure(figsize=(20, 10))
# this, I do NOT know why, results in very pretty bar plots!
# also results in tiny font for the heatmaps so we have to account for that
sns.set(font_scale=1)
plt.barh(temp_table.index,temp_table["amount"])

plt.title("Amount per theme")
# plt.show()

plt_save("bar_theme_amount")
plt.clf(), plt.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- SGT in relation to scores
- - no combination
- - - overall
- - - per time frame
- - combinations of SGT? todo: investigate relations between S,G and T
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# GENRE
# # no combination
# # bar plot for average score per genre
table_genre_score = dfm[(dfm["genre"] != 0)].groupby(["genre"])["score"].mean().to_frame()
table_genre_score.columns = ["score_mean"]

plt.figure(figsize=(20, 10))
# this, I do NOT know why, results in very pretty bar plots!
# also results in tiny font for the heatmaps so we have to account for that
sns.set(font_scale=1)
plt.barh(table_genre_score.index,table_genre_score["score_mean"])

plt.xlim(5, 8)
plt.title("Average score per genre")
# plt.show()

plt_save("bar_score_genre")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# heatmap for genre score in TimeTrame
table_genre_score_TF = dfm[(dfm["genre"] != 0)].groupby(["TF","genre"])["score"].mean().to_frame()
table_genre_score_TF = table_genre_score_TF.unstack()
# Now the column names are: "score/" + [theme] -- we want: [theme]
# get the names as a list
name_tuple_list = list(table_genre_score_TF)
new_names = []
for i in range(0,len(name_tuple_list)):
    new_names.append(name_tuple_list[i][1])
table_genre_score_TF.columns = new_names

# todo: name of index shows up in plot: "TF"
plt.figure(figsize=(20, 10))
# heat plot (not %)
hm = sns.heatmap(table_genre_score_TF.transpose(), linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

# set font size for labels
sns.set(font_scale=.75)
plt.title("Average score per genre in time frame")
# plt.show()

plt_save("heatmap_score_genre_TF")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THEME
# # no combination
# # bar plot for average score per genre
table_theme_score = dfm[(dfm["theme"] != 0)].groupby(["theme"])["score"].mean().to_frame()
table_theme_score.columns = ["score_mean"]

plt.figure(figsize=(20, 10))
# this, I do NOT know why, results in very pretty bar plots!
# also results in tiny font for the heatmaps so we have to account for that
sns.set(font_scale=0.5)
plt.barh(table_theme_score.index,table_theme_score["score_mean"])
plt.xlim(5, 8)
plt.title("Average score per theme")
# plt.show()

plt_save("bar_score_theme")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# heatmap for theme score in TimeTrame
table_theme_score_TF = dfm[(dfm["theme"] != 0)].groupby(["TF","theme"])["score"].mean().to_frame()
table_theme_score_TF = table_theme_score_TF.unstack()
# Now the column names are: "score/" + [theme] -- we want: [theme]
# get the names as a list
name_tuple_list = list(table_theme_score_TF)
new_names = []
for i in range(0,len(name_tuple_list)):
    new_names.append(name_tuple_list[i][1])
table_theme_score_TF.columns = new_names

# todo: name of index shows up in plot: "TF"
plt.figure(figsize=(20, 10))
# heat plot (not %)
hm = sns.heatmap(table_theme_score_TF.transpose(), linewidths=0.5, annot=True, cmap = sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

# set font size for labels
sns.set(font_scale=.75)
plt.title("Average score per theme in time frame")
# plt.show()

plt_save("heatmap_score_theme_TF")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# heatmap for theme and genre (what matches) -- amount
table_theme_genre = dfm[(dfm["theme"] != 0) & (dfm["genre"] != 0)].groupby(["genre","theme"]).size().to_frame()
table_theme_genre = table_theme_genre.unstack()
# Now the column names are: "score/" + [theme] -- we want: [theme]
# get the names as a list
name_tuple_list = list(table_theme_genre)
new_names = []
for i in range(0,len(name_tuple_list)):
    new_names.append(name_tuple_list[i][1])
table_theme_genre.columns = new_names

# todo: name of index shows up in plot: "TF"
plt.figure(figsize=(20, 10))
hm = sns.heatmap(table_theme_genre.transpose(), linewidths=0.5, annot=True,fmt='g', cmap = sns.cubehelix_palette(as_cmap=True),annot_kws={'size': 7})
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)

# set font size for labels
sns.set(font_scale=.75)
plt.title("Genre and theme matching (only matches)")
# plt.show()

plt_save("heatmap_genre_theme_matching")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# heatmap for genre x theme -- score
table_genre_combo_score = dfmu[(dfmu["genre"] != 0) & (dfmu["theme"] != 0)].groupby(
    ["genre", "theme"]).size()
table_genre_combo_size = \
dfmu[(dfmu["genre"] != 0) & (dfmu["theme"] != 0)].groupby(["genre", "theme"])["score"].mean()

temp_table = pd.concat([table_genre_combo_score, table_genre_combo_size], axis=1)
temp_table.columns = ["size", "score"]
temp_table = temp_table[temp_table["size"] > 30]
temp_table = temp_table["score"].unstack()

plt.figure(figsize=(20, 10))
hm = sns.heatmap(temp_table, linewidths=0.5, annot=True, cmap=sns.cubehelix_palette(as_cmap=True))
hm.set_yticklabels(hm.get_yticklabels(), rotation=0)
hm.set_xticklabels(hm.get_xticklabels(), rotation=90)

# set font size for labels
sns.set(font_scale=.75)
plt.title("Score of genre+theme combinations with more than 30 entries")
# plt.show()

plt_save("heatmap_score_genre_theme_combo_30entries")
plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Studio and Score
table_studio_score = dfm[(dfm["studio"] != 0)].groupby(["studio"])["score"].mean().to_frame()
table_studio_size = dfm[(dfm["studio"] != 0)].groupby(["studio"]).size().to_frame()
temp_table = pd.concat([table_studio_score, table_studio_size], axis=1)
temp_table.columns = ["score", "amount"]

temp_table = temp_table[temp_table["amount"] > 100].sort_values("score")
# temp_table = temp_table.unstack()

plt.figure(figsize=(20, 10))
# this, I do NOT know why, results in very pretty bar plots!
# also results in tiny font for the heatmaps so we have to account for that
sns.set(font_scale=0.75)
plt.barh(temp_table.index, temp_table["score"])
plt.xlim(5.5, 7.5)
plt.title("Studio average score (more than 100 entries)")
# plt.show()

plt_save("bar_studio_score_min100entries")
plt.clf(), plt.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- SGT - BARPLOTS
- "on_list": "mean",
- "favorites": "mean",
- "duration": "mean",
- "episodes": "mean"
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# GENRE
genre_table = (dfm[(dfm["genre"] != 0)].groupby("genre").agg(
    {"on_list": "mean",
     "favorites": "mean",
     "scored_by": "mean",
     "duration": "mean",
     "episodes": "mean"}
)).sort_index(ascending=False)

# for each item we get one bar plot
for item in ["on_list", "favorites", "scored_by", "duration", "episodes"]:
    plt.figure(figsize=(10, 5))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=0.5)
    plt.barh(genre_table.index, genre_table[item])
    plt.title("average amount of " + item + " per genre")
    # plt.show()

    plt_save("bar_genre_average_"+item)
    plt.clf(), plt.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THEME
theme_table = (dfm[(dfm["theme"] != 0)].groupby("theme").agg(
    {"on_list": "mean",
     "favorites": "mean",
     "scored_by": "mean",
     "duration": "mean",
     "episodes": "mean"}
)).sort_index(ascending=False)

# for each item we get one bar plot
for item in ["on_list", "favorites", "scored_by", "duration", "episodes"]:
    plt.figure(figsize=(10, 5))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=0.5)
    plt.barh(theme_table.index, theme_table[item])
    plt.title("average amount of " + item + " per theme")
    # plt.show()

    plt_save("bar_theme_average_"+item)
    plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# STUDIO
studio_table = (dfm[(dfm["studio"] != 0)].groupby("studio").agg(
    {"on_list": "mean",
     "favorites": "mean",
     "scored_by": "mean",
     "duration": "mean",
     "episodes": "mean",
     "anime_id": "size"}
)).sort_index(ascending=False)

studio_table = studio_table[studio_table["anime_id"]>100]

# for each item we get one bar plot
for item in ["on_list", "favorites", "scored_by", "duration", "episodes"]:
    plt.figure(figsize=(10, 5))
    # this, I do NOT know why, results in very pretty bar plots!
    # also results in tiny font for the heatmaps so we have to account for that
    sns.set(font_scale=0.5)
    plt.barh(studio_table.index, studio_table[item])
    plt.title("average amount of " + item + " per studio")
    # plt.show()

    plt_save("bar_studio_average_"+item)
    plt.clf(), plt.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
- SGT - HEATMAPS
- "source": "size",
- "anime_type": "size",
- "rating": "size",
- "DF": "size",
- "EF": "size"
"""
# todo: STUDIO
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# GENRE
for item in ["source", "anime_type", "rating", "DF", "EF"]:
    for SGT in ["genre", "theme"]:
        item_table = dfm[(dfm[SGT] != 0)].groupby([SGT, item]).size().to_frame()
        item_table = item_table.unstack()

        # Now the column names are: "XYZ/ABC", we only want "ABC"
        # get the names as a list
        name_tuple_list = list(item_table)
        new_names = []
        for i in range(0, len(name_tuple_list)):
            new_names.append(name_tuple_list[i][1])
        item_table.columns = new_names

        item_table.index.name = None

        # get the sum of each row
        sum_row = item_table.sum(axis=1)
        # get the sum of each column
        sum_col = item_table.sum()
        # copy item_table to mean_table
        mean_table = item_table.copy()
        # fill mean_table with nan
        mean_table[:] = np.nan
        # fill item_table with nan were the means will be
        item_table.loc["sum_" + SGT] = np.nan
        item_table["sum_" + item] = np.nan
        # add column and row summ as row and as column
        mean_table.loc["sum_" + SGT] = sum_col
        mean_table["sum_" + item] = sum_row


        # prepare plot
        fig, ax = plt.subplots(figsize=(20, 10))
        # plot item_table
        sns.heatmap(ax=ax, data=item_table, annot=True, fmt='.0f', cmap='Reds', annot_kws={'size': 9})
        # plot mean_table
        sns.heatmap(ax=ax, data=mean_table, annot=True, fmt='.0f', cmap='Blues', annot_kws={'size': 9})

        # set font size for labels
        sns.set(font_scale=.75)

        # title for plot
        plt.title("Amount: " + SGT + "/" + item)
        # # show plot
        # plt.show()
        # save plot
        plt_save("heatmap_" + SGT + "_" + item + "_amount_")
        # close the plot
        plt.clf(), plt.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #






