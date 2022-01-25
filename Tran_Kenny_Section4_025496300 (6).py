#Kenny Tran 025496300
#CECS229 Lab 6
#4/19/21
import matplotlib.pyplot as plt
import pandas as pd

filename = "birthweight.csv"

df = pd.read_csv(filename,sep=',')

#Plot 1 : Birthweight VS Gestation
plt.xlabel("Birthweight")
plt.ylabel("Gestation")
plt.title("Birthweight VS Gestation")

np_xbirth = df['Birthweight'].to_numpy()
np_ygest = df['Gestation'].to_numpy()
x = np_xbirth
y = np_ygest
gestplot = plt.scatter(x, y, color="red", marker='.')
plt.show()

#Plot 2 : Birthweight VS Mother's Age
plt.xlabel("Birthweight")
plt.ylabel("Mother's Age")
plt.title("Birthweight VS Mother's Age")

np_xbirth = df['Birthweight'].to_numpy()
np_ymage = df['mage'].to_numpy()
x = np_xbirth
y = np_ymage
mageplot = plt.scatter(x, y, color='orange', marker='.')
plt.show()

#Plot 3 : Birthweight VS # of Cigarettes
plt.xlabel("Birthweight")
plt.ylabel("# of Cigarettes")
plt.title("Birthweight VS # of Cigarettes")

np_xbirth = df['Birthweight'].to_numpy()
np_ycig = df['mnocig'].to_numpy()
x = np_xbirth
y = np_ycig
mnocig = plt.scatter(x, y, color='gray', marker='.')
plt.show()

#Plot 4 : Birthweight VS Mother's Height
plt.xlabel("Birthweight")
plt.ylabel("Mother's Height")
plt.title("Birthweight VS Mother's Height")

np_xbirth = df['Birthweight'].to_numpy()
np_yheight = df['mheight'].to_numpy()
x = np_xbirth
y = np_yheight
mageplot = plt.scatter(x, y, color='green', marker='.')
plt.show()

#Plot 5 : Birthweight VS Mother's Pre-Pregnancy Weight
plt.xlabel("Birthweight")
plt.ylabel("Mother's Pre-Pregnancy Weight")
plt.title("Birthweight VS Mother's Pre-Pregnancy Weight")

np_xbirth = df['Birthweight'].to_numpy()
np_ymppwt = df['mppwt'].to_numpy()
x = np_xbirth
y = np_ymppwt
mnocig = plt.scatter(x, y, color='blue', marker='.')
plt.show()

#Plot 6 : Birthweight VS Father's Age
plt.xlabel("Birthweight")
plt.ylabel("Father's Age")
plt.title("Birthweight VS Father's Age")

np_xbirth = df['Birthweight'].to_numpy()
np_yfage = df['fage'].to_numpy()
x = np_xbirth
y = np_yfage
mnocig = plt.scatter(x, y, color='indigo', marker='.')
plt.show()

#Plot 7 : Birthweight VS Father's Years of Education
plt.xlabel("Birthweight")
plt.ylabel("Father's Years of Education")
plt.title("Birthweight VS Father's Years of Education")

np_xbirth = df['Birthweight'].to_numpy()
np_yfedyrs = df['fedyrs'].to_numpy()
x = np_xbirth
y = np_yfedyrs
mnocig = plt.scatter(x, y, color='purple', marker='.')
plt.show()

#Plot 8 : Birthweight VS # of Cigarettes/Day smoked by Father
plt.xlabel("Birthweight")
plt.ylabel("# of Cigarettes/Day smoked by Father")
plt.title("Birthweight VS # of Cigarettes/Day smoked by Father")

np_xbirth = df['Birthweight'].to_numpy()
np_yfnocig = df['fnocig'].to_numpy()
x = np_xbirth
y = np_yfnocig
mnocig = plt.scatter(x, y, color='black', marker='.')
plt.show()

#Plot 9 : Birthweight VS Father's Height
plt.xlabel("Birthweight")
plt.ylabel("Father's Height")
plt.title("Birthweight VS Father's Height")

np_xbirth = df['Birthweight'].to_numpy()
np_yfheight = df['fheight'].to_numpy()
x = np_xbirth
y = np_yheight
mnocig = plt.scatter(x, y, color='cyan', marker='.')
plt.show()
