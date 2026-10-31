import pandas as pd
def grade(score):
    if score >= 80:
        return "Distinction"
    elif score >= 50:
          return  "Pass"
    else:
         return "Fail"

df = pd.read_csv("students.csv")
df["result"] = df["score"].apply(grade)

print(df)
print("Average score:", df["score"].mean())

df.to_csv("results.csv",index=False)
