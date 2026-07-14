import seaborn as sns
import matplotlib.pyplot as plt

# Load a small sample dataset
df = sns.load_dataset("penguins")

# Simple scatterplot
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", hue="species", data=df)

plt.show()
