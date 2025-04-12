import pandas as pd

# Load data
df = pd.read_csv('../data/student_assessments.csv')

# Basic cleaning
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
# Flag low scores
df['Intervention_Needed'] = (df['ELA_Score'] < 70) | (df['Math_Score'] < 70)

# Save cleaned data
df.to_csv('../output/cleaned_assessments.csv', index=False)
