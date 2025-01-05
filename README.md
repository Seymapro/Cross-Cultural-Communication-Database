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
  SELECT * FROM Expressions WHERE culture_id = 1;
  ```
*   Find equivalent expressions in another language:
  ```sql
  SELECT * FROM Expressions WHERE language_id = 2;
  ```
*   Retrieve meanings associated with a particular ID:
  ```sql
  SELECT description FROM Meanings WHERE id= 2;
  ```
  These queries can be used to retrieve specific types of information from the database.

Example python usage to retrieve and display information from the database:

```python
import sqlite3
from tabulate import tabulate # use it to make the output look prettier

conn = sqlite3.connect('culture_lib.db')
cursor = conn.cursor()

# Example query
cursor.execute("SELECT * FROM Expressions WHERE culture_id = 1")
rows = cursor.fetchall()

headers = ["ID", "Type", "Language", "Country", "Culture", "Description", "Meaning"]

print(tabulate(rows, headers=headers, tablefmt="grid"))

conn.close()
````

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
