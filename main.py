from m3u_parser import M3uParser
pluto_us_url = "https://i.mjh.nz/PlutoTV/us.m3u8"
pluto_uk_url = "https://i.mjh.nz/PlutoTV/gb.m3u8"
stv_uk_url = "https://i.mjh.nz/SamsungTVPlus/gb.m3u8"
stv_us_url = "https://i.mjh.nz/SamsungTVPlus/us.m3u8"
stirr_url = "https://i.mjh.nz/Stirr/all.m3u8"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
pluto_us = M3uParser(timeout=5, useragent=user_agent)
pluto_us.parse_m3u(pluto_us_url)
pluto_removals = [
    "Degrassi", "America's Voice News", "CBS News Chicago", "OAN Plus", "WeatherNation Los Angeles",
    'Faith TV', 'TBN', 'GLORY Kickboxing', 'World Poker Tour', 'PokerGo', 'Golazo Network', 'Logo Pluto TV',
    'Baywatch', 'Star Trek', 'theGrio', '90210', "Bounce XL", 'Shades of Black', 'Heartland', 'Stargate',
    'More Star Trek', 'AspireTV Life', 'Johnny Carson TV', 'The Rifleman', 'Dark Shadows', 'The Carol Burnett Show',
    "Three's Company", 'Family Ties', 'Happy Days', 'The Love Boat', 'Beverly Hillbillies', 'Mission Impossible',
    'Wanted: Dead or Alive', 'The Andy Griffith Show', 'Matlock', 'Gunsmoke', 'Black Classics', 'Perry Mason',
    'The Ed Sullivan Show', 'I Love Lucy', 'Rawhide', 'The Dick Van Dyke Show', 'Gameplay: Roblox',
    'Gameplay: Call of Duty', 'Gameplay: Fortnite', 'Gameplay: Sports', 'Dallas Cowboys Cheerleaders', 'The Challenge',
    'Black Ink Crew', 'Survivor', 'Rescue 911', 'Jersey Shore', 'Bar Rescue', 'Teen Mom', 'Cheaters',
    'Best of Dr. Phil', 'This Old House', 'MinecrafTV', 'BET Pluto TV', 'BET Her', 'Ink Master', 'Black Throwbacks',
    'Julia Child', 'Best of The Drew Barrymore Show', 'MAVTV Select', 'CBS News Los Angeles', 'The Rachael Ray Show',
    'CBS News New York', 'PFL MMA', 'XITE Gospel', 'The First', 'Midsomer Murders', 'Inspector Gadget',
    'Sabrina Teenage Witch', 'Little Baby Bum', 'Morphle', 'Moonbug Kids', 'Arthur', 'Barney & Friends', 'Duck Dynasty',
    'Wicked Tuna', '16 & Pregnant', 'My Strange Addiction', 'Bridezillas', 'Hunter', 'Highway to Heaven',
    'Wild at Heart', 'Hart to Hart', 'When Calls the Heart', 'Party of Five',
    'Rookie Blue'
]
samsung_removals = [
    'Project Runway', 'FailArmy', 'Catfish', 'TalkTV', 'GB News', 'Pluto TV Action', 'Pluto TV Romance',
    'Pluto TV Movies', 'Survivor', 'Are We There Yet?', 'Real Life', 'Bondi Vet', 'The Pet Collective',
    'Pluto TV Classic TV', 'LOL! Network', 'Bridezillas', 'Shades of Black', 'People Are Awesome', 'Baywatch',
    "McLeod's Daughters", 'The Wicked Tuna Channel', 'PBS America', 'Homicide Hunter', 'Pluto TV Crime',
    'Pluto TV Inside', 'Pluto TV Paranormal', 'Pluto TV Conspiracy', 'WaterBear', 'Pluto TV Animals', 'Fashion TV',
    'Pluto TV Food', 'World Poker Tour', 'Horse & Country', 'Strongman Champions League', 'MMA TV', 'CBS News',
    "Real America's Voice", 'TYT Network', 'NBC Bay Area News', 'ABC7 Bay Area', 'WN San Francisco', 'Stories by AMC',
    'TV Land Drama', 'BET Pluto TV', 'Bounce XL', 'Baywatch', 'The Walking Dead Universe', '21 Jump Street', 'Degrassi',
    'Lucky Dog', 'The Bob Ross Channel', 'Nosey', 'Divorce Court', 'Shades of Black', 'Dove Channel', 'Cowboy Way',
    'Fireplace 4K', 'Dr. G: Medical Examiner', 'Dateline 24/7', 'Midsomer Murders', 'CBS Sports HQ', 'beIN SPORTS XTRA',
    'Stadium', 'Origin Sports', 'IMPACT Wrestling', 'SURF NOW TV', 'People Are Awesome', 'Waypoint TV',
    'World Poker Tour', 'Top Gear', 'MAVTV Select', 'PowerNation', 'MotorTrend FAST TV', 'NHRA TV', 'MOTORVISION.TV',
    'Cars', 'Torque', 'Antiques Roadshow', 'This Old House', 'This Old House Makers', 'Home.Made.Nation', 'That Girl',
    'Family Ties', 'Portlandia', 'The Jack Hanna Channel'
]
stirr_removals = [
    'Buzzr', 'Nosey', 'Johnny Carson TV', 'The Carol Burnett Show', 'Shout Factory', 'The Tim Conway Show',
    'Dick Cavett', 'The Bob Ross Channel', 'Comedy Dynamics', 'Bloomberg TV', 'Filmrise Free Movies',
    'News 12 New York', 'The First', 'Cheddar', 'AFV', 'The Pet Collective', 'FailArmy', 'Horse Shopping Channel',
    'So...Real', 'People Are Awesome', 'Dove', 'HSN', 'The Country Network', 'ONTV4U', 'Shop LC', 'beIN Sports Xtra',
    'SportsGrid', 'Racing America', 'MavTv', 'QVC', 'Outdoor America', 'Stingray', 'World Poker Tour', 'Electric Now',

]

stirr_to_keep = [
    ' TBD', ' Swerve Sports', ' STIRR | National', ' Stadium', ' SportsGrid', ' RetroCrush', ' Midnight Pulp', ' Comet',
    ' Docurama', ' Law & Crime', ' LiveXLive', ' Gravitas', ' Electric Now', ' CHARGE', ' EVERGRN'
]
print(f"Pluto US: Loaded {len(pluto_us.get_list())} channels")
pluto_us.remove_by_category("En Español")
pluto_us.remove_by_category("Local News")
pluto_us.remove_by_category("Kids")
pluto_us.filter_by("name", pluto_removals, retrieve=False)
pluto_us.filter_by("name", "48 Hours", retrieve=False)
pluto_us.filter_by("name", "Bloomberg TV", retrieve=False)
pluto_us.filter_by("name", "CBS News", retrieve=False)
pluto_us.filter_by("name", "FailArmy", retrieve=False)
pluto_us.filter_by("name", "Judge Nosey", retrieve=False)
pluto_us.filter_by("name", "MST3K", retrieve=False)
pluto_us.filter_by("name", "Nosey", retrieve=False)
pluto_us.filter_by("name", "QVC", retrieve=False)
pluto_us.filter_by("name", "Sky News", retrieve=False)
pluto_us.filter_by("name", "The Judge Judy Channel", retrieve=False)
pluto_us.filter_by("name", "The New Detectives", retrieve=False)
pluto_us.filter_by("name", "The Pet Collective", retrieve=False)
pluto_us.filter_by("name", "Voyager Documentaries", retrieve=False)
pluto_us.filter_by("name", "Unsolved Mysteries", retrieve=False)
pluto_us.filter_by("name", "The Addams Family", retrieve=False)
pluto_us.filter_by("name", "HSN", retrieve=False)
pluto_us.filter_by("name", "Naruto", retrieve=False)
pluto_us.filter_by("name", "Sailor Moon", retrieve=False)
pluto_us.filter_by("name", "Lupin the 3rd", retrieve=False)
pluto_us.filter_by("name", "One Piece", retrieve=False)
pluto_us.filter_by("name", "Yu-Gi-Oh!", retrieve=False)
pluto_us.filter_by("name", "Tiny House Nation", retrieve=False)
pluto_us.filter_by("name", "Antiques Road Trip", retrieve=False)
pluto_us.filter_by("name", "Naturescape", retrieve=False)
pluto_us.filter_by("name", "Black Cinema", retrieve=False)
pluto_us.filter_by("name", "The Asylum", retrieve=False)
pluto_us.filter_by("name", "Newsmax", retrieve=False)
pluto_us.filter_by("name", "Blaze Live", retrieve=False)
pluto_us.filter_by("name", "TODAY All Day", retrieve=False)
pluto_us.filter_by("name", "VH1 Hip Hop Family", retrieve=False)
pluto_us.filter_by("name", "MTV Dating", retrieve=False)
pluto_us.filter_by("name", "Love & Hip Hop", retrieve=False)
pluto_us.filter_by("name", "Bellator MMA", retrieve=False)
pluto_us.filter_by("name", "PBR RidePass", retrieve=False)
pluto_us.filter_by("name", "Hot Bench", retrieve=False)
pluto_us.filter_by("name", "Home.Made.Nation", retrieve=False)
pluto_us.filter_by("name", "Western TV", retrieve=False)
pluto_us.filter_by("name", "Always Funny Videos", retrieve=False)
pluto_us.filter_by("name", "CSI: NY", retrieve=False)
pluto_us.filter_by("name", "CSI: Miami", retrieve=False)
pluto_us.filter_by("name", "CSI", retrieve=False)
pluto_us.filter_by("name", "Gordon Ramsay's Hell's Kitchen", retrieve=False)
pluto_us.filter_by("name", "Are You Smarter Than A 5th Grader", retrieve=False)
pluto_us.filter_by("name", "Deal or No Deal", retrieve=False)
pluto_us.filter_by("name", "The Price Is Right: The Barker Era", retrieve=False)
pluto_us.filter_by("name", "Let's Make A Deal", retrieve=False)
pluto_us.filter_by("name", "Cats 24/7", retrieve=False)
pluto_us.filter_by("name", "Antiques Roadshow UK", retrieve=False)
pluto_us.filter_by("name", "Fear Factor", retrieve=False)
pluto_us.filter_by("name", "The Amazing Race", retrieve=False)
pluto_us.filter_by("name", "IMPACT Wrestling", retrieve=False)
pluto_us.filter_by("name", "Funny AF", retrieve=False)
pluto_us.filter_by("name", "Awesomeness TV", retrieve=False)
pluto_us.filter_by("name", "The Design Network", retrieve=False)
pluto_us.filter_by("name", "CMT Equal Play", retrieve=False)
pluto_us.filter_by("name", "CMT", retrieve=False)
pluto_us.filter_by("name", "Vevo Country", retrieve=False)
pluto_us.filter_by("name", "Vevo Latino", retrieve=False)
pluto_us.filter_by("name", "All Reality by WE tv", retrieve=False)
pluto_us.filter_by("name", "VH1 I Love Reality", retrieve=False)
pluto_us.sort_by("category")
print(f"{len(pluto_us.get_list())} channels remaining\n")
pluto_us.to_file("pluto_us", "m3u")

pluto_uk = M3uParser(timeout=5, useragent=user_agent)
pluto_uk.parse_m3u(pluto_uk_url)
print(f"Pluto UK: Loaded {len(pluto_uk.get_list())} channels")
pluto_uk.filter_by("name", pluto_removals, retrieve=False)
pluto_uk.filter_by("name", "Anthony Bourdain: Parts Unknown", retrieve=False)
pluto_uk.filter_by("name", "Cheddar", retrieve=False)
pluto_uk.filter_by("name", "Bloomberg TV", retrieve=False)
pluto_uk.filter_by("name", "Catfish", retrieve=False)
pluto_uk.filter_by("name", "Euronews", retrieve=False)
pluto_uk.filter_by("name", "Great British Menu", retrieve=False)
pluto_uk.filter_by("name", "The Asylum Channel", retrieve=False)
pluto_uk.filter_by("name", "CSI: Miami", retrieve=False)
pluto_uk.filter_by("name", "Charlie's Angels", retrieve=False)
pluto_uk.filter_by("name", "CSI: New York", retrieve=False)
pluto_uk.filter_by("name", "Fear Factor", retrieve=False)
pluto_uk.filter_by("name", "Bake with Anna Olson", retrieve=False)
pluto_uk.filter_by("name", "Extreme American Homes", retrieve=False)
pluto_uk.filter_by("name", "10 Years Younger", retrieve=False)
pluto_uk.filter_by("name", "Sarah's House", retrieve=False)
pluto_uk.filter_by("name", "Punk'd", retrieve=False)
pluto_uk.filter_by("name", "Starsky & Hutch/The Shield", retrieve=False)
pluto_uk.filter_by("name", "Transformers", retrieve=False)
pluto_uk.filter_by("name", "Haunt TV", retrieve=False)
pluto_uk.filter_by("name", "Paranormal State", retrieve=False)
pluto_uk.filter_by("name", "Most Haunted", retrieve=False)
pluto_uk.filter_by("name", "Sensing Murder", retrieve=False)
pluto_uk.filter_by("name", "Ghost Dimension", retrieve=False)
pluto_uk.filter_by("name", "Beyond Belief: Fact or Fiction", retrieve=False)
pluto_uk.filter_by("name", "Fifth Gear", retrieve=False)
pluto_uk.filter_by("name", "Ice Pilots", retrieve=False)
pluto_uk.filter_by("name", "Full Custom Garage", retrieve=False)
pluto_uk.filter_by("name", "The New Detectives", retrieve=False)
pluto_uk.sort_by("category")
print(f"{len(pluto_uk.get_list())} channels remaining\n")
pluto_uk.to_file("pluto_uk", "m3u")

samsung_uk = M3uParser(timeout=5, useragent=user_agent)
samsung_uk.parse_m3u(stv_uk_url)
print(f"Samsung UK: Loaded {len(samsung_uk.get_list())} channels")
samsung_uk.filter_by("name", samsung_removals, retrieve=False)
samsung_uk.remove_by_category("Kids")
samsung_uk.remove_by_category("Motoring")
samsung_uk.filter_by("name", "Now 80s", retrieve=False)
samsung_uk.filter_by("name", "5 Cops", retrieve=False)
samsung_uk.filter_by("name", "5 Exploring Britain", retrieve=False)
samsung_uk.filter_by("name", "Haunt TV", retrieve=False)
samsung_uk.filter_by("name", "Hell's Kitchen", retrieve=False)
samsung_uk.filter_by("name", "Tastemade", retrieve=False)
samsung_uk.filter_by("name", "Deal or No Deal US", retrieve=False)
samsung_uk.filter_by("name", "The Design Network", retrieve=False)
samsung_uk.filter_by("name", "Grjngo - Western Movies", retrieve=False)
samsung_uk.filter_by("name", "Unbeaten", retrieve=False)
samsung_uk.filter_by("name", "Pluto Drama", retrieve=False)
samsung_uk.sort_by("category")
print(f"{len(samsung_uk.get_list())} channels remaining\n")
samsung_uk.to_file("samsung_uk", "m3u")

samsung_us = M3uParser(timeout=5, useragent=user_agent)
samsung_us.parse_m3u(stv_us_url)
print(f"Samsung US: Loaded {len(samsung_us.get_list())} channels")
samsung_us.filter_by("name", samsung_removals, retrieve=False)
samsung_us.remove_by_category("Game Shows")
samsung_us.remove_by_category("Reality")
samsung_us.remove_by_category("Latino")
samsung_us.sort_by("category")
print(f"{len(samsung_us.get_list())} channels remaining\n")
samsung_us.to_file("samsung_us", "m3u")

stirr = M3uParser(timeout=5, useragent=user_agent)
stirr.parse_m3u(stirr_url)
print(f"Stirr: Loaded {len(stirr.get_list())} channels")
stirr.get_random_stream()
stirr.filter_by("name", stirr_to_keep, retrieve=True)
print(f"{len(stirr.get_list())} channels remaining\n")
stirr.to_file("stirr", "m3u")

