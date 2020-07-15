# Resume-Scanner
A simple Python script that counts the number of keywords (taken from a master list) that your resume has in comparison to a specific job posting. Note - keywords are single words only (e.g. "machine" & "learning" instead of "machine learning").

Dependencies: collections, re, numpy, pandas

Output: cosine similarity, tabular view (top 15 keywords from job posting descending): || keyword | resume count | job posting count | difference ||
