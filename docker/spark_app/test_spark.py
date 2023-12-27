from pyspark.sql import SparkSession

def word_count():
    # Create a Spark session
    spark = SparkSession.builder.appName("SimpleWordCount").getOrCreate()

    # Define the text data as a Python variable
    text_data = """
    This is a sample text file.
    It contains several lines of text.
    Each line is separated by a newline character.

    Let's use this file for a word count example in Spark.

    Spark is a powerful distributed computing framework.

    We'll count the occurrences of each word in this file.
    """

    # Convert the Python variable to an RDD
    lines = spark.sparkContext.parallelize(text_data.split("\n"))

    # Split each line into words
    words = lines.flatMap(lambda line: line.split(" "))

    # Count the occurrences of each word
    word_counts = words.countByValue()

    # Print the word counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    word_count()
