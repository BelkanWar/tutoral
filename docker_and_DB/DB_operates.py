import pymysql
from sklearn import datasets

# DB connecting 
db = pymysql.connect(host='localhost', user='root',password='123456')
cursor = db.cursor()

# create a database
cursor.execute("CREATE DATABASE myDB")

# create a table 
cursor.execute(
    """
    CREATE TABLE myDB.iris (
        id INT NOT NULL AUTO_INCREMENT, 
        species VARCHAR(30) NOT NULL,
        sepal_length FLOAT NOT NULL ,
        sepal_width FLOAT NOT NULL,
        petal_length FLOAT NOT NULL,
        petal_width FLOAT NOT NULL,
        timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
        PRIMARY KEY (id)
    )
    """
)

cursor.execute(
    """
    CREATE INDEX Species 
    ON myDB.iris (species)
    """
)

# insert some data
iris = datasets.load_iris()

for row in range(iris.data.shape[0]):
    species = iris.target_names[iris.target[row]].tolist()
    sepal_len, sepal_width, petal_len, petal_width = iris.data[row].tolist()

    cursor.execute(
        """
        INSERT INTO myDB.iris (species, sepal_length, sepal_width, petal_length, petal_width)
        VALUES (%s, %s, %s, %s, %s)
        """, (species, sepal_len, sepal_width, petal_len, petal_width))
    db.commit()

# retrieve some data
cursor.execute(
    """
    SELECT 
        id, species, sepal_length, timestamp
    FROM myDB.iris
        WHERE species = %s
    """, ('setosa'))

data = cursor.fetchall()

# counting data 
cursor.execute(
    """
    SELECT 
        COUNT(id)
    FROM myDB.iris
        WHERE species = %s
    """, ('versicolor'))

count = cursor.fetchall()

# grouping
cursor.execute(
    """
    SELECT 
        species, AVG(sepal_length), SUM(sepal_width) 
    FROM myDB.iris
        GROUP BY species
    """)

data = cursor.fetchall()

# disconnect
db.close()