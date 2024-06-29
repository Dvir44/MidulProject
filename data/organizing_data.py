import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load the original CSV file
df = pd.read_csv('event_log.csv')

# Step 2: Select the first (index 0) and third (index 2) columns
selected_columns = df.iloc[:, [0, 2]].copy()

# New Step: Split the data into train and test sets (70% train, 30% test)
train_df, test_df = train_test_split(selected_columns, test_size=0.3, random_state=42)

# Step 3: Create a dictionary to map words to group identifiers
word_to_group = {}
next_group = 'a'

def get_group(word):
    global next_group
    # Check if the word is already in the dictionary
    if word not in word_to_group:
        # Assign the next available group identifier to the new word
        word_to_group[word] = next_group
        # Increment the group identifier for the next unique word
        next_group = chr(ord(next_group) + 1)
    # Return the group identifier for the word
    return word_to_group[word]

# Step 4: Apply the function to the words column using .loc for both train and test sets
train_df.loc[:, train_df.columns[1]] = train_df.iloc[:, 1].apply(get_group)
test_df.loc[:, test_df.columns[1]] = test_df.iloc[:, 1].apply(get_group)

# Step 5: Group by the 'id' column and concatenate the words for both train and test sets
grouped_train_df = train_df.groupby(train_df.columns[0])[train_df.columns[1]].apply(''.join).reset_index()
grouped_test_df = test_df.groupby(test_df.columns[0])[test_df.columns[1]].apply(''.join).reset_index()

# Step 6: Save the resulting DataFrames to new CSV files
grouped_train_df.to_csv('traces_train.csv', index=False)
grouped_test_df.to_csv('traces_test.csv', index=False)

# Step 7: Create a DataFrame that counts the occurrences of each unique trace in the train set
trace_counts_train = grouped_train_df.iloc[:, 1].value_counts().reset_index()
trace_counts_train.columns = ['trace', 'count']

# Save the resulting DataFrame to a new CSV file
trace_counts_train.to_csv('trace_counts_train.csv', index=False)

# Step 8: Create a DataFrame that counts the occurrences of each unique trace in the test set
trace_counts_test = grouped_test_df.iloc[:, 1].value_counts().reset_index()
trace_counts_test.columns = ['trace', 'count']

# Save the resulting DataFrame to a new CSV file
trace_counts_test.to_csv('trace_counts_test.csv', index=False)

# Optional: Save the word_to_group dictionary to a CSV file for reference
word_to_group_df = pd.DataFrame(list(word_to_group.items()), columns=['Word', 'Group'])
word_to_group_df.to_csv('letters_meaning.csv', index=False)

