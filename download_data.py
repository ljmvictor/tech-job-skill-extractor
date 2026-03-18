from datasets import load_dataset
import pandas as pd

print("Connecting to Hugging Face...")

dataset = load_dataset("lukebarousse/data_jobs", split="train")
print("Dataset downloaded successfully!")

df = dataset.to_pandas()

print("\nHere is a sneak peek at your data:")
print(df[['job_title', 'company_name', 'job_location']].head())

df.head(1000).to_csv("sample_jobs.csv", index=False)
print("\nSaved a sample to sample_jobs.csv!")