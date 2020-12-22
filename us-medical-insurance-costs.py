#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[1]:


#import libraries that will be used for the project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math


# In[2]:


#define function to round up when decimal value is 0.5 or greater
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


# In[3]:


#load data into a pandas dataframe
df = pd.read_csv('insurance.csv')

#convert age datatype to integer and bmi/charges to float --> originally, these were string values
df.age = df.age.astype(dtype='int')
df.bmi = df.bmi.astype(dtype='float')
df.charges = df.charges.astype(dtype='float')

print(df.head(5))


# In[4]:


#as alternative to dataframe, here we open the csv and convert it to a python dictionary
csv_info = open('insurance.csv')
csv_dict = csv.DictReader(csv_info)
#atke a look at what the csv_dict looks like
for row in csv_dict:
    print(row)


# In[22]:


#create empty lists for each field in the dataframe
variables = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
values = [ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges]
dictionary = {variable: value for variable, value in zip(variables, values)}
print(dictionary)
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# In[23]:


#create function to load the csv data into a list for each variable
def load_list_data(data_dict, csv_file):
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            for variable in data_dict:
                data_dict[variable].append(row[variable])
        return data_dict


# In[26]:


# look at the data in insurance_csv_dict
all_insurance_data_dict = load_list_data(dictionary, 'insurance.csv')
#load_list_data(sexes, 'insurance.csv', 'sex')
#load_list_data(bmis, 'insurance.csv', 'bmi')
#load_list_data(num_children, 'insurance.csv', 'children')
#load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
#load_list_data(regions, 'insurance.csv', 'region')
#load_list_data(insurance_charges, 'insurance.csv', 'charges')

print(all_insurance_data_dict['charges'])


# In[34]:


#use pandas dataframe to look at the summary statistics of our different variables
avg_age = round(df.age.mean(), 2)
#ages = [int(age) for age in ages]
#def Average(lst):
 #   avg = sum(lst)/len(lst)
  #  return round(avg, 2)
#print(Average(ages))

#avg male bmi
df_males = df.loc[df['sex'] == 'male']
avg_male_bmi = df_males.bmi.mean()

#avg female bmi
df_females = df.loc[df['sex'] == 'female']
avg_female_bmi = df_females.bmi.mean()

print("Avg. female bmi: " + str(round(avg_female_bmi, 2)))
print("Avg. male bmi: " + str(round(avg_male_bmi, 2)))
print("Average age of patients: " + str(avg_age))


# In[35]:


#How many people from each region?
df.region.value_counts().reset_index()
#looks like a pretty even distribution, although teh southeast region is slightly more highly represented


# In[37]:


#Do smokers have higher charges on average?

#Calculate average charges for people who do(n't) smoke and round to 2 decimals
avg_smoker_charges = df.loc[df['smoker'] == 'yes'].charges.mean()
avg_nonsmoker_charges = df.loc[df['smoker'] == 'no'].charges.mean()
round_smoker_charges = round(avg_smoker_charges, 2)

#Round the calculation of difference between charges to two decimal places
smoker_charge_diff = df.loc[df['smoker'] == 'yes'].charges.mean() - df.loc[df['smoker'] == 'no'].charges.mean()
round_smoker_charge_diff = round(smoker_charge_diff, 2)

#Print conclusion
print("On average, smokers are charged an average of $" + str(round_smoker_charges) + 
      ", which is "+ " $" + str(round_smoker_charge_diff) 
      + " more in medical costs than what non-smokers are charged.")


# In[97]:


#Let's graph this difference as a bar chart
fig, ax = plt.subplots()
x = ['non-smokers', 'smokers']
y = df.groupby('smoker').charges.mean()
y_ticks = list(range(0, 45000, 5000))
ax.bar(x, y, width = 0.6, edgecolor = 'black', linewidth=1.2)
ax.set_ylabel('insurance charges ($)')
ax.set_yticks(y_ticks)
ax.set_title("Smokers  charged way more than non-smokers")
#for index, value in enumerate(y):
 #   plt.text(value, index, str(value))

#add labels to the bars in the bar graphs for the mean charge values
#rects = ax.patches
#labels = ["$"+str(i) for i in list(round(df.groupby('smoker').charges.mean(), 2))]
#for rect, label in zip(rects, labels):
 #   height = rect.get_height()
  #  ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
   #         ha='center', va='bottom')

#trying new functin from stackoverflow
def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "${:.2f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.


# Call the function above. All the magic happens there.
add_value_labels(ax)
plt.show()

#df.groupby('smoker').charges.mean().plot.bar()


# In[134]:


#What does the age distribution look like?
#Let's build a histogram to find out.

fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot()
n_bins = [i for i in range(min(df.age.unique()), max(df.age.unique()+4), 4)]
x = df.age

# We can set the number of bins with the `bins` kwarg
n, real_bins, patches = ax.hist(x, bins=n_bins, edgecolor='black', linewidth=1.2)
plt.title('Age distribution')
ax.set_xlabel("age")
ax.set_ylabel("frequency")
ax.set_xticks(bins)
plt.xticks(bins, rotation=45)
plt.show()
print("The most well-represented age demographic in our sample is 18-22.")


# In[138]:


#How are age and medical costs related?
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot()
ax.set_xlabel("age")
ax.set_ylabel("medical charges")
plt.title("medical charges vs age")
plt.scatter(df.age, df.charges, alpha=0.2, color='purple')
plt.show()

#round correlation coefficient to 2 decimal places
rounded_corr = "{:.2f}".format(np.corrcoef(df.age, df.charges)[0,1])

#print  the results
print("The correlation coefficient between age and charges is " + str(rounded_corr)
       + " suggesting positive but not very strong correlation. There seem to be three groups here: low, medium, and high charges. Perhaps this means there's another highly influential variable. Since most people are in the low category, maybe more rare health conditions cause a minority of patients to be in the medium and high categories.")


# In[144]:


#Group charges by age
charges_by_age = df.charges.groupby(df.age)
xticks = [i for i in range(min(df.age), max(df.age), 4)]
#How are age and medical costs related?
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot()
ax.set_xlabel("age group")
ax.set_ylabel("average medical charges")
ax.set_xticks(xticks)
plt.title("average medical charges vs age")
ax.plot(charges_by_age.mean(), color='purple')
plt.show()


# In[31]:


#round correlation coefficient to 2 decimal places
rounded_corr = "{:.2f}".format(np.corrcoef(df.age.unique(), charges_by_age.mean())[0,1])

#print  the results
print("The correlation coefficient between age and average charges is " + str(rounded_corr)
       + " suggesting positive but not very strong correlation.")


# In[79]:


#create function to calculate difference from average overall cost for each person
def diff_from_average(dataframe, index):
    higher_or_lower = []
    
    differences = []
    for i in range(len(dataframe)):
        differences.append(df.charges[i] - df.charges.mean())
    for j in range(len(dataframe)):
        if differences[j] > 0:
            higher_or_lower.append("higher than") 
        elif differences[j] < 0:
                higher_or_lower.append("lower than")
        else:
            higher_or_lower.append("equal to")
    return "Patient id# " + str(index) + "'s medical charges are $" + str("{:.2f}".format(abs(differences[index]))) + " " + higher_or_lower[index] + " average."
print(diff_from_average(df, 1))


# In[ ]:




