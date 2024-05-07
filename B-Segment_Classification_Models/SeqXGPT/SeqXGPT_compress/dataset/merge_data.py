import pandas as pd

# Load the first dataset (CSV file)
csv_file_path = 'author_data.csv'
csv_data = pd.read_csv(csv_file_path)

# Load the second dataset (TSV file without header)
tsv_file_path = 'sent_level_eval.txt'
tsv_data = pd.read_csv(tsv_file_path, sep='\t', header=None, names=['sentence_text', 'pred_label'])

# Preview the data
csv_data.head(), tsv_data.head()


# Joining the datasets based on the 'sentence_text' field
# We use a left join to keep all rows from the first dataset and add information from the second dataset where available
joined_data = pd.merge(csv_data, tsv_data, on='sentence_text', how='left')

# Checking the first few rows of the joined dataset
print(joined_data.head())
