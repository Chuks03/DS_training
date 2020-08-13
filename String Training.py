#!/usr/bin/env python
# coding: utf-8

# ## Strings

# In[1]:


# Use quotation marks for defining string

"Michael Jackson"


# In[2]:


# Use single quotation marks for defining string

'Michael Jackson'


# In[3]:


# Digitals and spaces in string

'1 2 3 4 5 6 '


# In[4]:


# Special characters in string

'@#2_#]&*^%$'


# In[5]:


# Print the string

print("hello!")


# In[6]:


# Assign string to variable

Name = "Michael Jackson"
Name


# ## Indexing

# In[7]:


# Print the first element in the string

print(Name[0])


# In[8]:


# Print the element on index 6 in the string

print(Name[6])


# In[9]:


# Print the element on the 13th index in the string

print(Name[13])


# In[10]:


# Print the last element in the string

print(Name[-1])


# In[11]:


# Print the first element in the string

print(Name[-15])


# In[12]:


# Find the length of string

len("Michael Jackson")


# ## Slicing

# In[13]:


# Take the slice on variable Name with only index 0 to index 3

Name[0:4]


# In[14]:


# Take the slice on variable Name with only index 8 to index 11

Name[8:12]


# ## Stride

# In[16]:


# Get every second element. The elments on index 1, 3, 5 ...

Name[::2]


# In[17]:


# Get every second element in the range from index 0 to index 4

Name[0:5:2]


# ## Concatenate Strings

# In[18]:


# Concatenate two strings

Statement = Name + "is the best"
Statement


# In[19]:


# Print the string for 3 times

3 * "Michael Jackson"


# In[20]:


# Concatenate strings

Name = "Michael Jackson"
Name = Name + " is the best"
Name


# ## Escape Sequences

# In[21]:


# New line escape sequence

print(" Michael Jackson \n is the best" )


# In[22]:


# Tab escape sequence

print(" Michael Jackson \t is the best" )


# In[23]:


# Include back slash in string

print(" Michael Jackson \\ is the best" )


# In[24]:


# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )


# ## String Operations

# In[26]:


# Convert all the characters in string to upper case

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)


# In[27]:


# Replace the old substring with the new target substring is the segment has been found in the string

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B


# In[28]:


# Find the substring in the string. Only the index of the first elment of substring in string will be the output

Name = "Michael Jackson"
Name.find('el')


# In[29]:


# Find the substring in the string.

Name.find('Jack')


# In[30]:


# If cannot find the substring in the string

Name.find('Jasdfasdasdf')


# ## Quiz on Strings

# In[31]:


# What is the value of the variable A after the following code is executed?

# Write your code below and press Shift+Enter to execute 

A = "1"
A


# In[32]:


# What is the value of the variable B after the following code is executed?

B = "2"
B


# In[33]:


# What is the value of the variable C after the following code is executed?

# Write your code below and press Shift+Enter to execute 

C = A + B
C


# In[41]:


# Consider the variable D use slicing to print out the first three elements:

# Write your code below and press Shift+Enter to execute

D = "ABCDEFG"

print(D[0:3])


# In[42]:


# Use a stride value of 2 to print out every second character of the string E:

# Write your code below and press Shift+Enter to execute

E = 'clocrkr1e1c1t'
print(E[::2])


# In[49]:


# Print out a backslash:

# Write your code below and press Shift+Enter to execute

print("\\")


# In[60]:


# Convert the variable F to uppercase:

# Write your code below and press Shift+Enter to execute

F = "You are wrong"
F.upper()
F


# In[62]:


# Consider the variable G, and find the first index of the sub-string snow:

G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

G.find("snow")


# In[63]:


# In the variable G, replace the sub-string Mary with Bob:

# Write your code below and press Shift+Enter to execute
G.replace('Mary', 'Bob')


# In[ ]:




