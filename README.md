# CulturalBridge Database

### Overview
The **CulturalBridge Database** is a relational database designed to address challenges in cross-cultural communication. It stores cultural expressions (including phrases, gestures, and idioms), their context-specific meanings, and associated translations. It aims to improve cross-cultural interactions by providing a comprehensive resource for understanding cultural nuances, reducing misinterpretations, and supporting effective communication in a globalized world.

### Features
- Catalogs various linguistic and cultural expressions, including gestures, phrases, and idioms, across different languages and countries.
- Provides context-specific meanings of gestures and phrases, reducing the likelihood of misinterpretations.
- Easily extensible for integration with AI systems and other applications, such as translation tools and cultural sensitivity training programs.


### Example SQL Queries:
  *   Retrieve all expressions for a specific culture:
  ```sql
  SELECT 
    e.type,
    e.description AS expression_description,
    l.name AS language_name,
    c.name AS country_name,
    cul.name AS culture_name,
    m.description AS meaning_description
FROM Expressions e
JOIN Languages l ON e.language_id = l.id
JOIN Countries c ON e.country_id = c.id
JOIN Cultures cul ON e.culture_id = cul.id
JOIN Meanings m ON e.meaning_id = m.id
WHERE cul.id = 2
  ```
The Result Would be:
![image](https://github.com/user-attachments/assets/174afa0b-87a8-49c4-ab94-26dc45159c05)

*   Find equivalent expressions in another language:
  ```sql
  SELECT
    e.type,
    e.description AS expression_description,
    l.name AS language_name,
    c.name AS country_name,
    cul.name AS culture_name,
    m.description AS meaning_description
FROM Expressions e
JOIN Languages l ON e.language_id = l.id
JOIN Countries c ON e.country_id = c.id
JOIN Cultures cul ON e.culture_id = cul.id
JOIN Meanings m ON e.meaning_id = m.id
WHERE l.id = 2;
  ```
The result would be:
![image](https://github.com/user-attachments/assets/a3c70bb4-5061-4f5e-bcd3-a42ab081d793)

These queries can be used to retrieve specific types of information from the database.

Example python usage to retrieve and display information from the database:

```python
import sqlite3
from tabulate import tabulate #not necessary, but makes the output look prettier

connection = sqlite3.connect('culture_lib.db')
cursor = connection.cursor()

query = """
SELECT
    e.type,
    e.description AS expression_description,
    l.name AS language_name,
    c.name AS country_name,
    cul.name AS culture_name,
    m.description AS meaning_description
FROM Expressions e
JOIN Languages l ON e.language_id = l.id
JOIN Countries c ON e.country_id = c.id
JOIN Cultures cul ON e.culture_id = cul.id
JOIN Meanings m ON e.meaning_id = m.id
WHERE c.id = 3;
"""
cursor.execute(query)

results = cursor.fetchall()
headers = ["Type", "Description", "Language", "Country", "Culture", "Meaning"]
print(tabulate(results, headers=headers, tablefmt="grid"))

connection.close()

```
And the output would be:


An ER diagram to help visualize better:

![cultural_diagram](https://github.com/user-attachments/assets/f0a33a93-04f7-4761-b7a6-858358adaab6)
ER Diagram of the CulturalBridge Database. 
Generated using dbdiagram.io (https://dbdiagram.io).


### Data Population
Currently, the database contains synthetic data for testing purposes. Additional data can be incorporated by:

Manually extracting cultural insights (phrases, gestures, and their meanings) from peer-reviewed academic papers related to linguistics and anthropology.

Conducting structured polls and surveys to gather cultural insights from native speakers. These surveys would capture the context, nuances, and intended meanings of various expressions,

Ensuring the data is in the specified format outlined in the README.md file to ensure proper integration.

### Future Work
Expand the database with real-world data sourced from ethnographic studies, academic databases, and community contributions.

Integrate with AI systems to enable real-time cross-cultural communication analysis and provide contextual translations.

Develop a user-friendly web interface for broader accessibility, allowing users to search, contribute to, and explore cultural expressions in the database easily.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.
