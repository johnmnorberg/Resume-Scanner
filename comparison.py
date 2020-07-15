from collections import Counter
import re
import numpy as np
import pandas as pd

# Load the master list of keywords. This list is not specific to any one job
# post.
keywords = pd.read_csv('keywords.csv', sep=',', header=None)

# Convert each master keyword to lowercase for later comparison.
keywords = [x.lower() for x in keywords[0]]

# Collect the user's resume.
resume = input('Paste your resume text here: ')

# Collect the job posting in question.
job = input('Paste the job posting here: ')

# Split resume and job posting inputs into lists of lowercase words
resume_split = re.split(r'\W+', resume.lower())
job_split = re.split(r'\W+', job.lower())

# Count the number
resume_counter = Counter(resume_split)
job_counter = Counter(job_split)

# Remove all counter keys that are not in keywords
reduced_resume_counter = Counter({key : value for key, value in resume_counter.items() if key in keywords})
reduced_job_counter = Counter({key : value for key, value in job_counter.items() if key in keywords})

# Final vectors
resume_vector = np.array([reduced_resume_counter[key] for key in keywords])
job_vector = np.array([reduced_job_counter[key] for key in keywords])

# Cosine similarity
print("\nCosine similarity ~ {:0.3f}".format(np.dot(resume_vector, job_vector) / (np.linalg.norm(resume_vector) * np.linalg.norm(job_vector))), "\n")

# Create dataframe
df = pd.DataFrame({'Keyword': keywords, 'Resume': resume_vector, 'Job Posting': job_vector, 'Difference': resume_vector - job_vector})
df.set_index('Keyword', inplace=True)

# Sort the dataframe by Job Posting in descending order.
df.sort_values(by=['Job Posting'], ascending=False, inplace=True)

# Print top 20 keywords
print("Top 20 keywords from the job posting:\n", df.head(20))
