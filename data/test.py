import pandas as pd

people = pd.read_csv('people.csv')
places = pd.read_csv('places.csv')

merged_df = people.merge(
    places,
    left_on='place_of_birth',
    right_on='city',
    how='left'
)

print(merged_df.head())

summary = merged_df.groupby('country').size().reset_index(name='count')
print(summary)
