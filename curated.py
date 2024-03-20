from m3u_parser import M3uParser

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

pluto_us_url = "https://i.mjh.nz/PlutoTV/us.m3u8"
pluto_uk_url = "https://i.mjh.nz/PlutoTV/gb.m3u8"
stv_uk_url = "https://i.mjh.nz/SamsungTVPlus/gb.m3u8"
stv_us_url = "https://i.mjh.nz/SamsungTVPlus/us.m3u8"
stirr_url = "https://i.mjh.nz/Stirr/all.m3u8"
roku_url = "https://i.mjh.nz/Roku/all.m3u8"

pluto_gb_channels = ["Pluto TV Movies", "Pluto TV Action", "Pluto TV Sci-Fi", "Pluto TV Comedy Movies",
                     "Pluto TV Cult Films", "Pluto TV Thrillers", "Pluto TV Horror", "Pluto TV Westerns",
                     "Pluto TV Family Movie Club", "Pluto TV Sci-fi Series", "More TV Sci-fi", "5 Cops",
                     "Pluto TV Tough Jobs", "Pluto TV Cops & Convicts", "5 Emergency Rescue", "UKTV Play Heroes",
                     "Pluto TV Adventure", "Pluto TV Motor", "UKTV Play Full Throttle", "Extreme Channel",
                     "Come Dine with Me", "Judge Judy", "Hell's Kitchen", "Auction Hunters", "1 vs 100", "Pointless",
                     "Mythbusters", "Pimp my Ride", "Undercover Boss Global", "Pluto TV Trash to Cash", "Fear Factor",
                     "Pluto TV Crime", "Pluto TV Investigation", "More TV Crime", "Inside Crime", "Aftershock",
                     "FBI Files", "48 Hours", "Pluto TV Reality", "MTV Reality", "NextUp LIVE Comedy Channel",
                     "UKTV Play Laughs", "Pluto TV Sitcoms", "Pluto TV Classic TV", "Pluto TV Stand Up", "Wipeout",
                     "Just for Laughs", "Pluto TV Food", "South Park", "Great British Menu", "Bake with Anna Olson",
                     "Homes Under Hammer", "Location, location, location", "Pluto TV Animals", "Pluto TV Space",
                     "Pluto TV Conspiracy", "Pluto TV Science", "Pluto TV History", "5 Britain at War", "World War TV",
                     "UKTV Play Uncovered", "Voyager Documentaries", "Get.factual", "World's Greatest",
                     "5 Exploring Britain", "Pluto TV Big Builds", "Pluto TV Music", "MTV Classic",
                     "Yo! MTV Raps Classic", "MTV Movie Hits", "MTV Love", "Pluto TV K-Pop", "MTV Rocks",
                     "Pluto TV Animation"]
pluto_us_channels = ["Pluto TV Spotlight", "Pluto TV Icons", "Pluto TV Reaction", "Pluto TV Drama", "Pluto TV Fantastic",
                     "Pluto TV Romance", "Pluto TV Staff Picks", "MovieSphere by Lionsgate", "Pluto TV Documentaries",
                     "70s Cinema", "80s Rewind", "90s Throwback", "00s Replay", "Paramount Movie Channel",
                     "Classic Movies Channel", "Pluto TV Cult Films", "Flicks of Fury", "Hallmark Movies & More",
                     "Sitcom Legends", "TV Land Sitcoms", "More TV Sitcoms", "Comedy Central Pluto TV",
                     "Comedy Central Animation", "Stand-Up TV", "Slightly Off IFC", "British Comedy",
                     "Classic TV Comedy", "Classic TV: Families", "Classic TV Drama", "Classic TV Crime Drama",
                     "Classic TV Variety", "TokuSHOUTsu", "Pluto TV Crime Drama", "More Crime Drama", "TV Land Drama",
                     "More TV Drama", "Action Drama", "Stories by AMC", "BritBox Mysteries", "British Drama",
                     "Pluto TV Suspense", "Pluto TV Drama Life", "Court TV", "Crime 360", "Spike Pluto TV",
                     "Pluto TV Lives", "Xtreme Outdoor Presented by HISTORY", "Real Disaster Channel", "Pluto TV Cars",
                     "Top Gear", "Paramount+ Picks", "Showtime Selects", "ION", "K-Content by CJ ENM",
                     "Live Music Replay", "BUZZR", "Pluto TV Game Shows", "The Price Is Right", "Family Feud Classic",
                     "More TV Game Shows", "Game Show Central", "CBS Sports HQ", "FOX Sports", "NFL Channel", "MLB",
                     "Golazo Network", "Pluto TV Sports", "Fight", "beIN SPORTS XTRA", "Antiques Roadshow UK",
                     "BBC Home & Garden", "Food TV", "Warner Bros. TV Sweet Escapes", "The Jamie Oliver Channel",
                     "Iron Chef", "BBC Food", "Smithsonian Channel Selects", "Pluto TV Travel", "PBS Nature", "IGN",
                     "Anime All Day", "Vevo Holiday", "Vevo '70s", "Vevo '80s", "Vevo '90s", "Vevo 2K",
                     "XITE Classic Country", "Vevo Country", "Vevo True School Hip-Hop", "Vevo R&B", "Vevo Retro Rock",
                     "XITE Rock", "Vevo Pop", "MTV Spankin' New", "MTV Biggest Pop", "Vevo Latino", "Vevo Reggaeton & Trap"]
samsung_uk_channels = ["Entertainment Hub", "Comedy Hub", "Comedy Movies - Rakuten TV", "America's Got Talent",
                       "Real Series - Rakuten TV", "Comedy Dynamics", "Sky Mix", "World Drama by ITV Studios",
                       "Radical Docs", "Documentaries - Rakuten TV", "INWONDER", "INFAST", "PBS History", "INWILD",
                       "CNN FAST", "FRANCE 24 FAST", "Bloomberg Originals", "FIFA+", "Red Bull TV", "Trace UK", "GIGS",
                       "Tennis Channel International", "Origin Sports", "INTROUBLE", "Trace UK", "Qwest TV",
                       "Deluxe Lounge HD", "Qello Concerts by Stingray", "Clubbing TV", "Romance Movies - Rakuten TV",
                       "wedo movies", "MovieSphere", "GREAT! movies", "GREAT! romance", "Top Movies - Rakuten TV",
                       "Drama Movies - Rakuten TV", "Action Movies - Rakuten TV", "Crime Network",
                       "The Graham Norton Show", "Horizons", "Super Anime", "GIGS", "Trace Urban", "XITE Hits",
                       "Pointless UK: 'Powered by Banijay'", "Challenge", "Wipeout Xtra Powered by Banijay"]
samsung_us_channels = ["History 365", "ION Plus", "VICE", "MHz Now", "The Rotten Tomatoes Channel",
                       "ION Mystery", "fubo Sports Network", "Tastemade Home", "Tastemade Travel", "Journy",
                       "Hungry", "Kitchen Nightmares", "Conan O'Brien TV", "Dry Bar Comedy", "RiffTrax", "FilmRise",
                       "Samsung Wild Life", "TED", "PBS Digital Studios", "XITE Icons", "XITE Rock On",
                       "XITE Just Chill", "FilmRise Action", "Documentary+", "NEW KMOVIES", "The Preview Channel"]
stirr_channels = ["Swerve Sports", "CHARGE", "COMET", "TBD", "Electric Now", "Midnight Pulp", "RetroCrush", "LiveXLive",
                  "PursuitUp", "The T", "It's Showtime at the Apollo", "SOAR"]
roku_channels = ["NBC Sports", "Women's Sports Network", "Stadium", "For The Fans", "Swerve Combat", "DAZN Ringside",
                 "Torque", "SPORTSGRID", "Redbox Romance", "REDBOX FREE MOVIES", "FilmRise British TV",
                 "Rakuten Viki", "AsianCrush", "Crunchyroll", "FilmRise Sci-Fi", "WMX Hip Hop", "WMX Pop", "WMX Rock"]

pluto_uk = M3uParser(timeout=5, useragent=user_agent)
pluto_uk.parse_m3u(pluto_uk_url)
print(f"Pluto UK: Loaded {len(pluto_uk.get_list())} channels")
pluto_uk.filter_by("name", pluto_gb_channels, retrieve=True)
pluto_uk.to_file("pluto_uk_curated", "m3u")

stv_uk = M3uParser(timeout=5, useragent=user_agent)
stv_uk.parse_m3u(stv_uk_url)
print(f"SS UK: Loaded {len(stv_uk.get_list())} channels")
stv_uk.filter_by("name", samsung_uk_channels, retrieve=True)
stv_uk.to_file("ss_uk_curated", "m3u")

stv_us = M3uParser(timeout=5, useragent=user_agent)
stv_us.parse_m3u(stv_us_url)
print(f"SS US: Loaded {len(stv_us.get_list())} channels")
stv_us.filter_by("name", samsung_us_channels, retrieve=True)
stv_us.to_file("ss_us_curated", "m3u")

stirr = M3uParser(timeout=5, useragent=user_agent)
stirr.parse_m3u(stirr_url)
print(f"Stirr: Loaded {len(stirr.get_list())} channels")
stirr.filter_by("name", stirr_channels, retrieve=True)
stirr.to_file("stirr_curated", "m3u")

roku = M3uParser(timeout=5, useragent=user_agent)
roku.parse_m3u(roku_url)
print(f"Roku: Loaded {len(roku.get_list())} channels")
roku.filter_by("name", roku_channels, retrieve=True)
roku.to_file("roku_curated", "m3u")

pluto_us = M3uParser(timeout=5, useragent=user_agent)
pluto_us.parse_m3u(pluto_us_url)
print(f"Pluto US: Loaded {len(pluto_us.get_list())} channels")
pluto_us.filter_by("name", pluto_us_channels, retrieve=True)
pluto_us.to_file("pluto_us_curated", "m3u")




print()