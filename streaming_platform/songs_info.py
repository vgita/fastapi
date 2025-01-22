# Define a list of song information

songs_info = [
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "genre": "Pop",
        "album": {
            "title": "÷ (Divide)",
            "release_year": 2017,
        },
        "views_per_country": {
            "US": 50_000_001,
            "UK": 30_000_002,
            "France": 20_000_003,
            "Italy": 10_000_004,
            "Germany": 15_000_005,
        },
    },
    {
        "title": "Despacito",
        "artist": "Luis Fonsi ft. Daddy Yankee",
        "album": {
            "title": "Despacito & Mis Grandes Éxitos",
            "release_year": 2017,
        },
        "genre": "latin pop",
        "views_per_country": {
            "India": 50_000_006,
            "UK": 35_000_007,
            "Mexico": 60_000_008,
            "Spain": 40_000_009,
            "Germany": 15_000_010,
        },
    },
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "genre": "R&B",
        "album": {
            "title": "After Hours",
            "release_year": 2020,
        },
        "views_per_country": {
            "US": 20_000_011,
            "UK": 15_000_012,
            "France": 10_000_013,
            "Italy": 5_000_014,
            "Germany": 15_000_015,
        },
    },
    {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "genre": "classic rock",
        "album": {
            "title": "A Night at the Opera",
            "release_year": 1975,
        },
        "views_per_country": {
            "US": 10_000_016,
            "UK": 20_000_017,
            "Germany": 15_000_018,
            "Italy": 5_000_019,
        },
    },
    {
        "title": "Hips Don't Lie",
        "artist": "Shakira ft. Wyclef Jean",
        "genre": "Latin Pop",
        "album": {
            "title": "Oral Fixation, Vol. 2",
            "release_year": 2006,
        },
        "views_per_country": {
            "US": 10_030_020,
            "UK": 15_000_021,
            "France": 10_000_022,
            "Germany": 5_000_023,
            "Italy": 5_000_024,
        },
    },
    {
        "title": "Dance Monkey",
        "artist": "Tones and I",
        "genre": "Pop",
        "album": {
            "title": "The Kids Are Coming",
            "release_year": 2019,
        },
        "views_per_country": {
            "US": 30_000_025,
            "UK": 20_000_026,
            "France": 15_000_027,
            "Italy": 10_000_028,
            "Australia": 50_000_029,
            "Germany": 15_000_030,
        },
    },
    {
        "title": "Old Town Road",
        "artist": "Lil Nas X ft. Billy Ray Cyrus",
        "genre": "country Rap",
        "album": {
            "title": "7",
            "release_year": 2019,
        },
        "views_per_country": {
            "US": 30_000_031,
            "UK": 20_000_032,
            "France": 15_000_033,
            "Italy": 10_000_034,
            "Australia": 50_000_035,
            "Germany": 15_000_036,
        },
    },
    {
        "title": "Someone You Loved",
        "artist": "Lewis Capaldi",
        "genre": "Pop",
        "album": {
            "title": "Divinely Uninspired to a Hellish Extent",
            "release_year": 2019,
        },
        "views_per_country": {
            "US": 30_000_037,
            "UK": 20_000_038,
            "France": 15_000_039,
            "Italy": 10_000_040,
            "Australia": 50_000_041,
            "Germany": 15_000_042,
        },
    },
    {
        "title": "Uptown Funk",
        "artist": "Mark Ronson ft. Bruno Mars",
        "genre": "Funk/pop",
        "album": {
            "title": "Uptown Special",
            "release_year": 2014,
        },
        "views_per_country": {
            "US": 30_000_043,
            "UK": 20_000_044,
            "France": 15_000_045,
            "Italy": 10_000_046,
            "Australia": 50_000_047,
            "Germany": 15_000_048,
        },
    },
    {
        "title": "Cheap Thrills",
        "artist": "Sia ft. Sean Paul",
        "genre": "Pop",
        "album": {
            "title": "This Is Acting",
            "release_year": 2016,
        },
        "views_per_country": {
            "US": 30_000_049,
            "UK": 20_000_050,
            "France": 15_000_051,
            "Italy": 10_000_052,
            "Australia": 50_000_053,
            "Germany": 15_000_054,
        },
    },
    {
        "title": "7 Rings",
        "artist": "Ariana Grande",
        "genre": "Pop",
        "album": {
            "title": "Thank U, Next",
            "release_year": 2019,
        },
        "views_per_country": {
            "US": 30_000_055,
            "UK": 20_000_056,
            "Germany": 15_000_057,
            "Italy": 10_000_058,
            "Australia": 50_000_059,
            "France": 15_000_060,
        },
    },
    {
        "title": "SICKO MODE",
        "artist": "Travis Scott",
        "genre": "Hip-Hop",
        "album": {
            "title": "Astroworld",
            "release_year": 2018,
        },
        "views_per_country": {
            "US": 30_000_061,
            "UK": 20_000_062,
            "France": 15_000_063,
            "Italy": 10_000_064,
            "Australia": 50_000_065,
            "Germany": 15_000_066,
        },
    },
    {
        "title": "God's Plan",
        "artist": "Drake",
        "genre": "Hip-Hop",
        "album": {
            "title": "Scorpion",
            "release_year": 2018,
        },
        "views_per_country": {
            "US": 30_000_067,
            "UK": 20_000_068,
            "France": 15_000_069,
            "Italy": 10_000_070,
            "Australia": 50_000_071,
            "Germany": 15_000_072,
        },
    },
    {
        "title": "WAP",
        "artist": "Cardi B ft. Megan Thee Stallion",
        "genre": "Hip-Hop",
        "album": {
            "title": "WAP (feat. Megan Thee Stallion)",
            "release_year": 2020,
        },
        "views_per_country": {
            "US": 30_000_073,
            "UK": 20_000_074,
            "France": 15_000_075,
            "Italy": 10_000_076,
            "Australia": 50_000_077,
            "Germany": 15_000_078,
        },
    },
    {
        "title": "Gangnam Style",
        "artist": "PSY",
        "genre": "K-Pop",
        "album": {
            "title": "PSY 6 (Six Rules), Part 1",
            "release_year": 2012,
        },
        "views_per_country": {
            "US": 30_000_079,
            "UK": 20_000_080,
            "France": 15_000_081,
            "Italy": 10_000_082,
            "Australia": 50_000_083,
            "Germany": 15_000_084,
        },
    },
    {
        "title": "Rolling in the Deep",
        "artist": "Adele",
        "genre": "Pop",
        "album": {
            "title": "21",
            "release_year": 2011,
        },
        "views_per_country": {
            "US": 30_000_085,
            "UK": 20_000_086,
            "France": 15_000_087,
            "Italy": 10_000_088,
            "Australia": 50_000_089,
            "Germany": 15_000_090,
        },
    },
    {
        "title": "Radioactive",
        "artist": "Imagine Dragons",
        "genre": "alternative Rock",
        "album": {
            "title": "Night Visions",
            "release_year": 2012,
        },
        "views_per_country": {
            "US": 30_000_091,
            "UK": 20_000_092,
            "France": 15_000_093,
            "Italy": 10_000_094,
            "Australia": 50_000_095,
            "Germany": 15_000_096,
        },
    },
    {
        "title": "Can't Stop the Feeling!",
        "artist": "Justin Timberlake",
        "genre": "Pop",
        "album": {
            "title": "Trolls: Original Motion Picture Soundtrack",
            "release_year": 2016,
        },
        "views_per_country": {
            "US": 30_000_097,
            "UK": 20_000_098,
            "France": 15_000_099,
            "Italy": 10_000_100,
            "Australia": 50_000_101,
            "Germany": 15_000_102,
        },
    },
    {
        "title": "Rockstar",
        "artist": "Post Malone ft. 21 Savage",
        "genre": "Hip-Hop",
        "album": {
            "title": "Beerbongs & Bentleys",
            "release_year": 2018,
        },
        "views_per_country": {
            "US": 30_000_103,
            "UK": 20_000_104,
            "France": 15_000_105,
            "Italy": 10_000_106,
            "Australia": 50_000_107,
            "Germany": 15_000_108,
        },
    },
    {
        "title": "Hello",
        "artist": "Adele",
        "genre": "Pop",
        "album": {
            "title": "25",
            "release_year": 2015,
        },
        "views_per_country": {
            "US": 30_000_109,
            "UK": 20_000_110,
            "France": 15_000_111,
            "Italy": 10_000_112,
            "Australia": 50_000_113,
            "Germany": 15_000_114,
        },
    },
    {
        "title": "Thunder",
        "artist": "Imagine Dragons",
        "genre": "Alternative Rock",
        "album": {
            "title": "Evolve",
            "release_year": 2017,
        },
        "views_per_country": {
            "US": 30_000_115,
            "UK": 20_000_116,
            "France": 15_000_117,
            "Italy": 10_000_118,
            "Australia": 50_000_119,
            "Germany": 15_000_120,
        },
    },
    {
        "title": "Hotline Bling",
        "artist": "Drake",
        "genre": "Hip-Hop",
        "album": {
            "title": "Views",
            "release_year": 2016,
        },
        "views_per_country": {
            "US": 30_000_121,
            "UK": 20_000_122,
            "France": 15_000_123,
            "Italy": 10_000_124,
            "Australia": 50_000_125,
            "Germany": 15_000_126,
        },
    },
    {
        "title": "Closer",
        "artist": "The Chainsmokers ft. Halsey",
        "genre": "EDM/Pop",
        "album": {
            "title": "Collage",
            "release_year": 2016,
        },
        "views_per_country": {
            "US": 30_000_127,
            "UK": 20_000_128,
            "France": 15_000_129,
            "Italy": 10_000_130,
            "Australia": 50_000_131,
            "Germany": 15_000_132,
        },
    },
    {
        "title": "Love Yourself",
        "artist": "Justin Bieber",
        "genre": "Pop",
        "album": {
            "title": "Purpose",
            "release_year": 2015,
        },
        "views_per_country": {
            "US": 30_000_133,
            "UK": 20_000_134,
            "France": 15_000_135,
            "Italy": 10_000_136,
            "Australia": 50_000_137,
            "Germany": 15_000_138,
        },
    },
    {
        "title": "The Hills",
        "artist": "The Weeknd",
        "genre": "R&B",
        "album": {
            "title": "Beauty Behind the Madness",
            "release_year": 2015,
        },
        "views_per_country": {
            "US": 30_000_139,
            "UK": 20_000_140,
            "France": 15_000_141,
            "Italy": 10_000_142,
            "Australia": 50_000_143,
            "Germany": 15_000_144,
        },
    },
    {
        "title": "Sucker",
        "artist": "Jonas Brothers",
        "genre": "Pop",
        "album": {
            "title": "Happiness Begins",
            "release_year": 2019,
        },
        "views_per_country": {
            "US": 30_000_145,
            "UK": 20_000_146,
            "France": 15_000_147,
            "Italy": 10_000_148,
            "Australia": 50_000_149,
            "Germany": 15_000_150,
        },
    },
    {
        "title": "Sorry",
        "artist": "Justin Bieber",
        "genre": "Pop",
        "album": {
            "title": "Purpose",
            "release_year": 2015,
        },
        "views_per_country": {
            "US": 30_000_151,
            "UK": 20_000_152,
            "France": 15_000_153,
            "Italy": 10_000_154,
            "Australia": 50_000_155,
            "Germany": 15_000_156,
        },
    },
    {
        "title": "Stressed Out",
        "artist": "Twenty One Pilots",
        "genre": "Alternative/Indie",
        "album": {
            "title": "Blurryface",
            "release_year": 2015,
        },
        "views_per_country": {
            "US": 30_000_157,
            "UK": 20_000_158,
            "France": 15_000_159,
            "Italy": 10_000_160,
            "Australia": 50_000_161,
            "Germany": 15_000_162,
        },
    },
    {
        "title": "Djadja",
        "artist": "Aya Nakamura",
        "genre": "Afrobeat/R&B",
        "album": {
            "title": "Nakamura",
            "release_year": 2018,
        },
        "views_per_country": {
            "US": 40_000_163,
            "UK": 10_000_164,
            "France": 150_000_165,
            "Italy": 10_000_166,
            "Australia": 50_000_167,
            "Germany": 15_000_168,
        },
    },
    {
        "title": "Virtual Insanity",
        "artist": "Jamiroquai",
        "genre": "Funk/Disco",
        "album": {
            "title": "Travelling Without Moving",
            "release_year": 1996,
        },
        "views_per_country": {
            "US": 40_000_169,
            "UK": 40_010_170,
            "France": 10_000_171,
            "Italy": 10_000_172,
            "Australia": 50_000_173,
            "Germany": 15_000_174,
        },
    },
    {
        "title": "Formidable",
        "artist": "Stromae",
        "genre": "Hip-Hop/World",
        "album": {
            "title": "Racine Carrée",
            "release_year": 2013,
        },
        "views_per_country": {
            "France": 50_040_175,
            "Belgium": 20_300_176,
            "Germany": 10_000_177,
            "Switzerland": 5_000_178,
            "Italy": 10_000_179,
            "Australia": 50_000_180,
        },
    },
]