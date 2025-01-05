import sqlite3

con = sqlite3.connect("cultural_bridge.db")
cur = con.cursor()

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Cultures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Meanings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT
)WITHOUT ROWID; """)
    
cur.execute("""CREATE TABLE IF NOT EXISTS Expressions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type TEXT,
    language_id INT,
    country_id INT,
    culture_id INT,
    description TEXT,
    meaning_id INT,
    FOREIGN KEY(language_id) REFERENCES Languages(id),
    FOREIGN KEY(country_id) REFERENCES Countries(id),
    FOREIGN KEY(culture_id) REFERENCES Cultures(id),
    FOREIGN KEY(meaning_id) REFERENCES Meanings(id)
)WITHOUT ROWID; """) 

# Example Data Generation Function
def add_data(cursor, table, values):
  try:
    placeholders = ', '.join('?' for _ in values)
    cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", values)
  except Exception as e:
    print(f"Error inserting into table {table} with values {values}: {e}")
    raise

languages = [
    (2, 'Spanish'),
    (3, 'French'),
    (4, 'German'),
    (5, 'Japanese'),
    (6, 'Mandarin'),
    (7, 'Arabic'),
    (8, 'Hindi'),
    (9, 'Portuguese'),
    (10, 'Russian'),
    (11, 'Italian'),
    (12, 'Swahili'),
    (13, 'Korean'),
    (14, 'Dutch'),
    (15, 'Swedish'),
    (16, 'Turkish'),
    (17, 'Polish'),
    (18, 'Vietnamese'),
    (19, 'Thai'),
    (20, 'Greek'),
]
for lang_id, lang_name in languages:
    add_data(cur, 'Languages', (lang_id, lang_name))

countries = [
    (2, 'Spain'),
    (3, 'France'),
    (4, 'Germany'),
    (5, 'Japan'),
    (6, 'China'),
    (7, 'Egypt'),
    (8, 'India'),
    (9, 'Brazil'),
    (10, 'Russia'),
    (11, 'Italy'),
    (12, 'Kenya'),
    (13, 'South Korea'),
    (14, 'Netherlands'),
    (15, 'Sweden'),
    (16, 'Turkey'),
    (17, 'Poland'),
    (18, 'Vietnam'),
    (19, 'Thailand'),
     (20, 'Greece'),
     (21, 'Canada'),
     (22, 'Mexico'),
     (23, 'Australia'),
     (24, 'Argentina'),
      (25, 'Nigeria'),
      (26, 'Ireland'),
       (27, 'Denmark'),
       (28, 'Switzerland'),
       (29, 'Indonesia'),
       (30, 'Norway'),
      (31, 'Scotland'),

]
for country_id, country_name in countries:
    add_data(cur, 'Countries', (country_id, country_name))

cultures = [
    (2, 'Spanish'),
    (3, 'French'),
    (4, 'German'),
    (5, 'Japanese'),
    (6, 'Chinese'),
    (7, 'Egyptian'),
    (8, 'Indian'),
    (9, 'Brazilian'),
    (10, 'Russian'),
    (11, 'Italian'),
     (12, 'Kenyan'),
    (13, 'Korean'),
    (14, 'Dutch'),
    (15, 'Swedish'),
    (16, 'Turkish'),
    (17, 'Polish'),
     (18, 'Vietnamese'),
     (19, 'Thai'),
    (20, 'Greek'),
    (21, 'Canadian'),
    (22, 'Mexican'),
    (23, 'Australian'),
    (24, 'Argentinian'),
     (25, 'Nigerian'),
     (26, 'Irish'),
      (27, 'Danish'),
       (28, 'Swiss'),
        (29, 'Indonesian'),
        (30, 'Norwegian'),
       (31, 'Scottish'),
]
for culture_id, culture_name in cultures:
    add_data(cur, 'Cultures', (culture_id, culture_name))

meanings = [
    (2, 'Respect and acknowledgement'),
    (3, 'Hospitality and welcome'),
    (4, 'Formality and politeness'),
    (5, 'Humility and thankfulness'),
    (6, 'Trust and reliability'),
    (7, 'Joy and celebration'),
    (8, 'Mourning and respect for the deceased'),
    (9, 'Greetings and farewells'),
    (10, 'Emphasis and sincerity'),
     (11, 'Rejection or disapproval'),
     (12, 'Privacy and personal space'),
     (13, 'Affection and intimacy'),
     (14, 'Friendship and camaraderie'),
     (15, 'Gratitude and appreciation'),
      (16, 'Agreement and acceptance'),
     (17, 'Disagreement and skepticism'),
     (18, 'Patience and understanding'),
      (19, 'Excitement and enthusiasm'),
     (20, 'Apology and remorse'),
     (21, 'Authority and power'),
      (22, 'Compassion and sympathy'),
       (23, 'Hope and optimism'),
      (24, 'Warning or caution'),
      (25, 'Confusion or uncertainty'),
     (26, 'Surprise and shock'),
      (27, 'Determination and resilience'),
      (28, 'Playfulness and humor'),
      (29, 'Jealousy or envy'),
     (30, 'Longing and nostalgia'),
     (31, 'Curiosity and wonder'),
     (32, 'Embarrassment or shame'),
     (33, 'Indifference or apathy'),
     (34, 'Frustration and anger'),
     (35, 'Peace and tranquility'),
     (36, 'Bravery and courage'),
     (37, 'Creativity and imagination'),
     (38, 'Tradition and heritage'),
     (39, 'Modernity and innovation'),
      (40, 'Indignation and outrage'),
      (41, 'Acceptance of fate'),
      (42, 'Resignation and passivity'),
      (43, 'Sorrow and grief'),
      (44, 'Loneliness and isolation'),
      (45, 'Generosity and altruism'),
      (46, 'Contentment and satisfaction'),
      (47, 'Pride and self-respect'),
    (48, 'Doubt and uncertainty')

]

for meaning_id, meaning_desc in meanings:
  add_data(cur, 'Meanings', (meaning_id, meaning_desc))

expressions = [
    (2, 'Gesture', 2, 2, 2, 'Kissing on both cheeks as a greeting', 3),
    (3, 'Phrase', 3, 3, 3, 'Bonjour', 9),
     (4, 'Gesture', 4, 4, 4, 'Firm handshake with direct eye contact', 2),
     (5, 'Phrase', 5, 5, 5, 'Sumimasen (Excuse me)', 5),
     (6, 'Phrase', 6, 6, 6, 'Ni hao (Hello)', 9),
     (7, 'Gesture', 7, 7, 7, 'Right hand over heart', 2),
     (8, 'Phrase', 8, 8, 8, 'Namaste', 9),
     (9, 'Gesture', 9, 9, 9, 'Nod of the head', 16),
    (10, 'Phrase', 10, 10, 10, 'Privet (Hello)', 9),
     (11, 'Gesture', 11, 11, 11, 'Hand kissing', 13),
     (12, 'Phrase', 12, 12, 12, 'Asante (Thank you)', 15),
    (13, 'Gesture', 13, 13, 13, 'Bowing', 5),
    (14, 'Phrase', 14, 14, 14, 'Hallo (Hello)', 9),
    (15, 'Gesture', 15, 15, 15, 'Placing hand on the heart', 2),
    (16, 'Phrase', 16, 16, 16, 'Merhaba (Hello)', 9),
    (17, 'Phrase', 17, 17, 17, 'Dzień dobry (Good morning)', 9),
    (18, 'Gesture', 18, 18, 18, 'Putting hands together', 5),
    (19, 'Phrase', 19, 19, 19, 'Sawasdee (Hello)', 9),
   (20, 'Gesture', 20, 20, 20, 'Tapping someone on the shoulder', 14),
    (21, 'Phrase', 1, 21, 21, 'How\'s it going?', 9),
    (22, 'Gesture', 22, 22, 22, 'Kiss on one cheek', 3),
    (23, 'Phrase', 23, 23, 23, 'G\'Day Mate', 9),
    (24, 'Gesture', 24, 24, 24, 'A slight bow', 2),
     (25, 'Gesture', 25, 25, 25, 'Clapping to show appreciation', 15),
    (26, 'Phrase', 26, 26, 26, 'Top o\' the mornin\' to ya!', 9),
     (27, 'Phrase', 27, 27, 27, 'Hej', 9),
    (28, 'Phrase', 28, 28, 28, 'Grüezi', 9),
    (29, 'Phrase', 29, 29, 29, 'Selamat pagi', 9),
    (30, 'Phrase', 30, 30, 30, 'Hei', 9),
    (31, 'Phrase', 31, 31, 31, 'Alright pal', 9),
    (32, 'Gesture', 2, 2, 2, 'Shaking a fist to show anger', 34),
    (33, 'Phrase', 3, 3, 3, 'Merci', 15),
    (34, 'Gesture', 4, 4, 4, 'A bow', 2),
    (35, 'Phrase', 5, 5, 5, 'Itadakimasu (Let\'s eat)', 15),
     (36, 'Gesture', 6, 6, 6, 'Pointing with the middle finger is rude', 11),
    (37, 'Phrase', 7, 7, 7, 'Ahlan wa sahlan (Welcome)', 3),
    (38, 'Gesture', 8, 8, 8, 'Touching elders feet to show respect', 2),
     (39, 'Gesture', 9, 9, 9, 'Thumbs up is great', 16),
    (40, 'Phrase', 10, 10, 10, 'Spasibo (Thank you)', 15),
    (41, 'Phrase', 11, 11, 11, 'Ciao (Hello/Goodbye)', 9),
     (42, 'Gesture', 12, 12, 12, 'Handshakes are common', 16),
    (43, 'Phrase', 13, 13, 13, 'Annyeonghaseyo (Hello)', 9),
    (44, 'Phrase', 14, 14, 14, 'Hallo (Hello)', 9),
    (45, 'Gesture', 15, 15, 15, 'Fika is a coffe break with friends', 14),
    (46, 'Phrase', 16, 16, 16, 'Teşekkür ederim (Thank you)', 15),
    (47, 'Phrase', 17, 17, 17, 'Przepraszam (Excuse me/Sorry)', 20),
     (48, 'Gesture', 18, 18, 18, 'Head nodding yes', 16),
    (49, 'Phrase', 19, 19, 19, 'Khop khun (Thank you)', 15),
    (50, 'Phrase', 20, 20, 20, 'Yassas (Hello)', 9),
    (51, 'Gesture', 1, 1, 1, 'Waving hands', 9),
    (52, 'Phrase', 21, 21, 21, 'Eh?', 25),
     (53, 'Gesture', 22, 22, 22, 'Hugging as a greeting', 13),
    (54, 'Phrase', 23, 23, 23, 'How\'s it going mate?', 9),
    (55, 'Phrase', 24, 24, 24, 'Hola', 9),
    (56, 'Gesture', 25, 25, 25, 'Giving money is customary', 45),
    (57, 'Phrase', 26, 26, 26, 'Grand', 16),
   (58, 'Gesture', 27, 27, 27, 'Nodding head down to show respect', 2),
   (59, 'Gesture', 28, 28, 28, 'Waving to get attention', 9),
    (60, 'Gesture', 29, 29, 29, 'The use of hand for food', 3),
   (61, 'Phrase', 30, 30, 30, 'Takk', 15),
   (62, 'Phrase', 31, 31, 31, 'What\'s the story?', 9),
   (63, 'Gesture', 1, 1, 1, 'Clapping is a show of appreciation', 15),
    (64, 'Phrase', 2, 2, 2, 'Buenas Dias', 9),
    (65, 'Gesture', 3, 3, 3, 'A brief hug', 13),
    (66, 'Phrase', 4, 4, 4, 'Guten Tag', 9),
    (67, 'Gesture', 5, 5, 5, 'Shoes off at the door', 2),
    (68, 'Gesture', 6, 6, 6, 'Using both hands when giving', 2),
    (69, 'Phrase', 7, 7, 7, 'Shukran (Thank you)', 15),
    (70, 'Phrase', 8, 8, 8, 'Dhanyavaad (Thank you)', 15),
    (71, 'Gesture', 9, 9, 9, 'Kiss on the cheek for women', 13),
    (72, 'Gesture', 10, 10, 10, 'Always greet the eldest first', 2),
    (73, 'Phrase', 11, 11, 11, 'Grazie (Thank you)', 15),
    (74, 'Phrase', 12, 12, 12, 'Habari (Hello)', 9),
    (75, 'Gesture', 13, 13, 13, 'Always face the elders when speaking to them', 2),
     (76, 'Phrase', 14, 14, 14, 'Goedendag (Hello)', 9),
    (77, 'Gesture', 15, 15, 15, 'The concept of "Lagom" (not too much/ not too little)', 16),
     (78, 'Phrase', 16, 16, 16, 'Lütfen (Please)', 15),
    (79, 'Gesture', 17, 17, 17, 'Handshakes are common', 16),
   (80, 'Phrase', 18, 18, 18, 'Xin chào (Hello)', 9),
    (81, 'Gesture', 19, 19, 19, 'Wai gesture', 2),
    (82, 'Gesture', 20, 20, 20, 'Keeping eye contact is normal', 16),
    (83, 'Phrase', 1, 21, 21, 'How\'s it going, eh?', 9),
    (84, 'Gesture', 22, 22, 22, 'Kiss on both cheeks to show affecion', 13),
    (85, 'Phrase', 23, 23, 23, 'No worries mate', 18),
    (86, 'Gesture', 24, 24, 24, 'Kiss on the cheek between friends', 13),
     (87, 'Phrase', 25, 25, 25, 'Ekaabo (Welcome)', 3),
     (88, 'Phrase', 26, 26, 26, 'Cheers', 9),
     (89, 'Gesture', 27, 27, 27, 'Bowing to show respect', 2),
    (90, 'Gesture', 28, 28, 28, 'Kissing all three cheeks', 13),
     (91, 'Phrase', 29, 29, 29, 'Terima kasih (Thank you)', 15),
     (92, 'Phrase', 30, 30, 30, 'Tusen Takk', 15),
     (93, 'Gesture', 31, 31, 31, 'Handshake with a light bow', 2),
     (94, 'Phrase', 2, 2, 2, 'Como estas?', 9),
      (95, 'Phrase', 3, 3, 3, 'Comment allez-vous?', 9),
     (96, 'Phrase', 4, 4, 4, 'Wie geht es Ihnen?', 9),
     (97, 'Phrase', 5, 5, 5, 'Konnichiwa', 9),
      (98, 'Phrase', 6, 6, 6, 'Nin hao ma?', 9),
     (99, 'Phrase', 7, 7, 7, 'Kayf halak', 9),
    (100, 'Phrase', 8, 8, 8, 'Aap kaise hain?', 9),
    (101, 'Phrase', 9, 9, 9, 'Olá', 9),
    (102, 'Phrase', 10, 10, 10, 'Kak dela?', 9),
    (103, 'Phrase', 11, 11, 11, 'Come stai?', 9)
]
for expr_id, expr_type, expr_lang, expr_country, expr_culture, expr_desc, expr_meaning in expressions:
    add_data(cur, 'Expressions', (expr_id, expr_type, expr_lang, expr_country, expr_culture, expr_desc, expr_meaning))


con.commit()
con.close()
