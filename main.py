import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
new={row.letter:row.code for(index,row) in data.iterrows()}
name=input("Enter any word : ").upper()
output=[new[i] for i in name]
print(output)