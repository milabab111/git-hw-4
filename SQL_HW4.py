
CREATE TABLE IF NOT EXISTS Singer (
	id SERIAL PRIMARY KEY, 
	singer name VARCHAR(40) NOT null
);


CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	genre name VARCHAR(40) NOT null
);

CREATE TABLE IF NOT EXISTS SingerGenre (
	singer_id integer references Singer(id), 
	genre_id integer references genres(id), 
	constraint pk primary key (singer_id, genre_id
); 

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	album name VARCHAR(60) NOT NULL, 
	release year INTEGER CHECK (release > 0)
); 


CREATE TABLE IF NOT EXISTS SingerAlbum (
	singer_id integer references Singer(id), 
	album_id integer references Album(id), 
	constraint pk primary key (singer_id, album_id)
); 

CREATE TABLE IF NOT EXISTS Songs (
	id SERIAL PRIMARY KEY,
	song name VARCHAR(60) NOT NULL,
	duration INTEGER CHECK (duration > 0),
	album id INTEGER REFERENCES Album (id))
);


CREATE TABLE IF NOT EXISTS Compilation (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL, 
	release_year INTEGER CHECK (release > 0)
);

CREATE TABLE IF NOT EXISTS CompilationSongs (
	compilation_id integer references Compilation(id), 
	songs_id integer references Songs(id), 
	constraint pk primary key (compilation_id, songs_id)
); 


INSERT INTO Singer
	VALUES (1, Bruno Mars);

INSERT INTO Singer
	VALUES (2, Britney Spears);

INSERT INTO Singer
	VALUES (3, Scorpions);

INSERT INTO Singer
	VALUES (4, Madonna); 

INSERT INTO Singer
	VALUES (5, Sting); 

INSERT INTO Singer
	VALUES (6, Adele);

INSERT INTO Singer
	VALUES (7, Beatles); 

INSERT INTO Singer
	VALUES (8, George Michael); 

INSERT INTO genres
	VALUES (1, R&B); 

INSERT INTO genres
	VALUES (2, Pop);

INSERT INTO genres
	VALUES (3, Rock);


INSERT INTO genres
	VALUES (4, Blues);


INSERT INTO genres
	VALUES (5, Funk);

INSERT INTO SingerGenre
	VALUES (1,5);

INSERT INTO SingerGenre
	VALUES (2,2);

INSERT INTO SingerGenre
	VALUES (3,3);

INSERT INTO SingerGenre
	VALUES (4,2);

INSERT INTO SingerGenre
	VALUES (5,2);

INSERT INTO SingerGenre
	VALUES (6,4);

INSERT INTO SingerGenre
	VALUES (7,5);

INSERT INTO SingerGenre
	VALUES (8,3);

INSERT INTO Album
	VALUES (1, Blackout, 2020);

INSERT INTO Album
	VALUES (2, Crazy World, 1988);

INSERT INTO Album
	VALUES (3, 24k Magic, 1999);

INSERT INTO Album
	VALUES (4, Music, 1995);

INSERT INTO Album
	VALUES (5, Abbey Road, 2005);

INSERT INTO Album
	VALUES (6, Faith, 2004);

INSERT INTO Album
	VALUES (7,Memories, 2010);

INSERT INTO Album
	VALUES (8,The Last Ship, 1980);

INSERT INTO SingerAlbum
	VALUES (1,2);
INSERT INTO SingerAlbum
	VALUES (2,3);
INSERT INTO SingerAlbum
	VALUES (3,1);
INSERT INTO SingerAlbum
	VALUES (4,5);
INSERT INTO SingerAlbum
	VALUES (5,4);
INSERT INTO SingerAlbum
	VALUES (6,8);

INSERT INTO SingerAlbum
	VALUES (7,6);
INSERT INTO SingerAlbum
	VALUES (8,7);

INSERT INTO Songs
	VALUES (1,1, Womaniser, 2);

INSERT INTO Songs
	VALUES (2,1, Englishman in New York, 3);

INSERT INTO Songs
	VALUES (3,2, Material Girl, 4);

INSERT INTO Songs
	VALUES (4,2, Careless Whisper, 5);

INSERT INTO Songs
	VALUES (5,3, Finesse, 2);

INSERT INTO Songs
	VALUES (6,3, Hello,3 );

INSERT INTO Songs
	VALUES (7,4, Come Together,) 4;

INSERT INTO Songs
	VALUES (8,5, Send me an Angel, 4);

INSERT INTO Songs
	VALUES (9,6, Toxic, 3);

INSERT INTO Songs
	VALUES (10,7,Uptown Funk, 3);

INSERT INTO Songs
	VALUES (11,8, Shape of my heart,4);

INSERT INTO Songs
	VALUES (12,5, Hung Up, 6);

INSERT INTO Songs
	VALUES (13,7, Vogue, 5);

INSERT INTO Songs
	VALUES (14,8, Rolling in the deep, 4);

INSERT INTO Songs
	VALUES (15,5, Jesus to a child, 2);

INSERT INTO Compilation
	VALUES (1, Sbornik1, 2002);

INSERT INTO Compilation
	VALUES (2, Hits, 2000);

INSERT INTO Compilation
	VALUES (3, Compile2, 2003);

INSERT INTO Compilation
	VALUES (4, Greatest, 1990);

INSERT INTO Compilation
	VALUES (5, Pop, 2002);

INSERT INTO Compilation
	VALUES (6, Best Artists, 2010);

INSERT INTO Compilation
	VALUES (7, 90s, 1998);

INSERT INTO Compilation
	VALUES (8, Megahits, 2022);

INSERT INTO CompilationSongs
	VALUES (1,1);

INSERT INTO CompilationSongs
	VALUES (2,2);

INSERT INTO CompilationSongs
	VALUES (3,1);

INSERT INTO CompilationSongs
	VALUES (4,3);

INSERT INTO CompilationSongs
	VALUES (5,4);

INSERT INTO CompilationSongs
	VALUES (6,5);

INSERT INTO CompilationSongs
	VALUES (7,6);

INSERT INTO CompilationSongs
	VALUES (8,7);

INSERT INTO CompilationSongs
	VALUES (9,8);

INSERT INTO CompilationSongs
	VALUES (10,7);

INSERT INTO CompilationSongs
	VALUES (11,6);

INSERT INTO CompilationSongs
	VALUES (12,5);

INSERT INTO CompilationSongs
	VALUES (13,4);

INSERT INTO CompilationSongs
	VALUES (14,3);

INSERT INTO CompilationSongs
	VALUES (15,2);


SELECT album name, release year FROM Album
	WHERE release year = 2018; 

SELECT song name, duration FROM Songs
	ORDER BY duration DESC
	LIMIT 1; 


SELECT song name FROM Songs
	WHERE duration >= 3.5;

SELECT name FROM Compilation
	WHERE release_year BETWEEN 2018 AND 2020; 


SELECT singer name FROM Singer
	WHERE singer name LIKE ‘_’;


SELECT song name FROM Songs
	WHERE song name LIKE ‘%my%’; 
