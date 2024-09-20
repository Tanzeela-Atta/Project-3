#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


hotel_dataset=pd.read_csv(r"C:/Users/DELL/Downloads/hotel_booking.csv")


# In[5]:


hotel_dataset.shape


# In[7]:


hotel_dataset.head()


# In[11]:


hotel_dataset.info()


# In[13]:


pd.isnull(hotel_dataset).sum()


# In[15]:


hotel_dataset['company'] = hotel_dataset['company'].fillna(0)


# In[17]:


hotel_dataset['country'] = hotel_dataset['country'].fillna(hotel_dataset['country'].mode()[0])


# In[19]:


hotel_dataset['agent'] = hotel_dataset['agent'].fillna(0)


# In[21]:


hotel_dataset['children'] = hotel_dataset['children'].fillna(0)


# In[23]:


pd.isnull(hotel_dataset).sum()


# # Exploratory Data Analysis

# # Cancellations Analysis

# In[37]:


# Percentage of bookings that were canceled
cancellation_rate = hotel_dataset['is_canceled'].mean() * 100
print(f"Cancellation Rate: {cancellation_rate:.2f}%")

# Visualize cancellation distribution
sns.countplot(data=hotel_dataset, x='is_canceled')
plt.title('Booking Cancellation Distribution')
plt.xlabel('Is Canceled')
plt.ylabel('Count')
plt.show()


# # Lead Time Analysis

# In[62]:


import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the average lead time for canceled and non-canceled bookings
average_lead_time = hotel_dataset.groupby('is_canceled')['lead_time'].mean().reset_index()

# Plot the bar chart
sns.barplot(data=average_lead_time, x='is_canceled', y='lead_time')
plt.title('Average Lead Time by Cancellation Status')
plt.xlabel('Cancellation Status (0: Not Canceled, 1: Canceled)')
plt.ylabel('Average Lead Time (Days)')
plt.show()






# # Seasonality Analysis

# In[45]:


monthly_bookings = hotel_dataset.groupby('arrival_date_month')['hotel'].count().sort_values()
monthly_bookings.plot(kind='bar')
plt.title('Bookings by Month')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Cancellations by month
monthly_cancellations =hotel_dataset[hotel_dataset['is_canceled'] == 1].groupby('arrival_date_month')['is_canceled'].count()
monthly_cancellations.plot(kind='bar', color='red')
plt.title('Cancellations by Month')
plt.xlabel('Month')
plt.ylabel('Number of Cancellations')
plt.xticks(rotation=45)
plt.show()


# # Customer Preference Analysis 

# In[66]:


import seaborn as sns
import matplotlib.pyplot as plt

# Plot for customer type preferences
sns.countplot(data=hotel_dataset, x='customer_type')
plt.title('Customer Type Distribution')
plt.xlabel('Customer Type')
plt.ylabel('Count')
plt.show()



# # Guest Type Analysis

# In[51]:


# Analyze repeated guests vs cancellations
sns.countplot(data=hotel_dataset, x='is_canceled', hue='is_repeated_guest')
plt.title('Cancellations by Repeated Guests')
plt.xlabel('Is Canceled')
plt.ylabel('Count')
plt.show()


# # Distribution by Room Type

# In[54]:


# Analyze cancellations by reserved room type
sns.countplot(data=hotel_dataset, x='reserved_room_type', hue='is_canceled')
plt.title('Cancellations by Reserved Room Type')
plt.xlabel('Reserved Room Type')
plt.ylabel('Count')
plt.show()


# # Conclusion

# In[ ]:


The cancellation rate is 37.04%  with the bookings having longer lead times experiencing higher cancellation rate.
More bookings are done in August and at the same time the more cancellations also occur in August. 
The high number of transient bookings indicates that the majority of customers prefer short-term stays over other types.
Repeated Guest has more more successful bookings than non-repeated. 
Customers of A Room type has less cancellation ratio.

