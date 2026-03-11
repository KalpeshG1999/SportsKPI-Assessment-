import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "SportsKPI_Kabaddi_Dataset_for_Assessment_.xlsx"
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()
#print("Dataset Loaded Successfully\n")

# 2a) Overall Raiding Team’s Total Raids and Successful Raids
print("------ Question 2a ------")
total_raids = len(df)
successful_raids = df[df["Outcome"] == "Successful"].shape[0]
print("Total Raids:", total_raids)
print("Successful Raids:", successful_raids)
print("\n")

# 2b) Overall Defending Team’s Total Tackles and Successful Tackles
print("------ Question 2b ------")
total_tackles = df[df["Outcome"] != "Empty"].shape[0]
successful_tackles = df[df["Outcome"] == "Unsuccessful"].shape[0]
print("Total Tackles:", total_tackles)
print("Successful Tackles:", successful_tackles)
print("\n")

# 2c) Raiding Team’s Successful Raids against 6-7 Defenders ONLY
print("------ Question 2c ------")
successful_raids_6_7 = df[
    (df["Outcome"] == "Successful") &
    (df["Number_of_Defenders"].isin([6, 7]))
]
count_success_6_7 = successful_raids_6_7.shape[0]
print("Successful Raids against 6-7 Defenders:", count_success_6_7)
print("\n")

# 2d) Defending Team’s Successful Tackles against 1-2-3 Defenders ONLY
print("------ Question 2d ------")
successful_tackles_1_3 = df[
    (df["Outcome"] == "Unsuccessful") &
    (df["Number_of_Defenders"].isin([1, 2, 3]))
]
count_success_tackles_1_3 = successful_tackles_1_3.shape[0]
print("Successful Tackles with 1-2-3 Defenders:", count_success_tackles_1_3)
print("\n")

# 2e) Raiding Team’s Do-or-Die Raids Success Rate
print("------ Question 2e ------")
do_or_die_raids = df[df["Team_Raid_Number"] == 3]
successful_do_or_die = do_or_die_raids[
    do_or_die_raids["Outcome"] == "Successful"
]
total_do_or_die = len(do_or_die_raids)
success_do_or_die = len(successful_do_or_die)
success_rate = success_do_or_die / total_do_or_die if total_do_or_die > 0 else 0
print("Total Do or Die Raids:", total_do_or_die)
print("Successful Do or Die Raids:", success_do_or_die)
print("Do or Die Success Rate:", round(success_rate * 100, 2), "%")
print("\n")


#Q3 Visualizations

# 3a) Distribution of Raids (counts and percentage) for any Raider
raider_name = "HIMANSHU"
raider_df = df[df['Raider_Name'] == raider_name]
raid_outcomes = raider_df['Outcome'].value_counts()

def label_formatter(pct, allvals):
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"
plt.figure(figsize=(7, 7))
plt.pie(raid_outcomes, labels=raid_outcomes.index, 
        autopct=lambda pct: label_formatter(pct, raid_outcomes), 
        startangle=140, colors=['#66b3ff','#99ff99','#ff9999'])
plt.title(f'3a) Raid Distribution for {raider_name}')
plt.savefig('3a_raider_distribution.png')
plt.show()

# 3b) Distribution of Tackles (counts and percentage) for any Defender
defender_name = "GAURAV CHILLAR"
defender_df = df[df['Defender_1_Name'] == defender_name].copy()
tackle_map = {
    'Unsuccessful': 'Successful Tackle', 
    'Successful': 'Unsuccessful Tackle', 
    'Empty': 'Empty Raid'
}
defender_df['Tackle_Outcome'] = defender_df['Outcome'].map(tackle_map)
tackle_outcomes = defender_df['Tackle_Outcome'].value_counts()
def label_fmt(pct, allvals):
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

my_colors = ['#99ff99', '#ff9999', '#66b3ff'] 
plt.figure(figsize=(8, 8))
plt.pie(tackle_outcomes, 
        labels=tackle_outcomes.index, 
        autopct=lambda pct: label_fmt(pct, tackle_outcomes), 
        startangle=140, 
        colors=my_colors, 
        pctdistance=0.85)

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title(f'3b) Tackle Distribution for {defender_name}')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('3b_defender_distribution.png')
plt.show()

# 3c) Attacking Skills Distribution for any Raider
raider_skills = raider_df[
    (raider_df['Attacking_Skill'].notnull()) & 
    (raider_df['Attacking_Skill'].str.strip() != '')
]['Attacking_Skill'].value_counts().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
raider_skills.plot(kind='barh', color='skyblue')
plt.title(f'3c) Attacking Skills Distribution for {raider_name}')
plt.xlabel('Counts')
plt.ylabel('Skill Name')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('3c_raider_skills.png')
plt.show()

# 3d) Defensive Skills Distribution for any Defender
defender_skills = defender_df[
    (defender_df['Defensive_Skill'].notnull()) & 
    (defender_df['Defensive_Skill'].str.strip() != '')
]['Defensive_Skill'].value_counts().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
defender_skills.plot(kind='bar', color='salmon')
plt.title(f'3d) Defensive Skills Distribution for {defender_name}')
plt.xlabel('Skill Name')
plt.xticks(rotation=0, ha='center')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('3d_defender_skills.png')
plt.show()