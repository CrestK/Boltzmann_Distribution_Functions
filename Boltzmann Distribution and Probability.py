#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import mpld3
mpld3.enable_notebook()


# In[2]:


E = [12,122,12222] # these are the possible energy states that can be occupied
T = np.linspace(0.01,20000,1000) # This is temperature range and resolution


# In[3]:


# Function of e^-E/RT
def Boltzmann_Probability(E,T):
    R = 8.3144
    return np.exp(-E/(R*T))


# In[4]:


# Canonical Partition Function
def Q(E,T):
    q = 0
    for i in range(len(E)):
        q = q + Boltzmann_Probability(E[i],T)
    return q


# In[5]:


# Probability of Energy States
def probability_of_an_energy_state(S, E, T):
    return "The probability of the specified energy state is", Boltzmann_Probability(S,T)/(Q(E,T))


# In[6]:


# Probability of All Energy States outputed per energy state
def all_probabilities(E, T):
    for i in range(len(E)):
        print("The Probability for Energy State", i , "is", probability_of_an_energy_state(E[i],E, T)[1])


# In[7]:


def graph(E):
    for i in range(len(E)):
        plt.plot(T, (probability_of_an_energy_state(E[i],E, T))[1])
        plt.title("Probability of Each Energy State as a Function of Temperature")
        plt.xlabel("Temperature in Kelvin")
        plt.ylabel("Probability")


# ### Set Temperature Range and Energy States,

# In[10]:


E = [12,122,12222] # these are the possible energy states that can be occupied
T = np.linspace(0.01,20000,1000) # This is temperature range and resolution


# # Examples

# ## Graphing

# ### You can graph the function by just specifying the list of energy states the molecule can occupy. The interactive graph function of the matplot library is enable by default to allow scrolling.

# In[11]:


graph(E)


# ## Find out the specific probability of an energy state at a specified temperature

# ### First type the specific energy state you desire, if you know its index in a list you can use that. Then the reference list of energy states, then the temperature.  If you just desire the number then index it like the next example

# In[12]:


probability_of_an_energy_state(E[1], E, 200)


# In[13]:


probability_of_an_energy_state(E[1], E, 200)[1]


# ### If you want a list of all the probabilities, then and in the energy states then the temperature in which you desire the list of probabilities

# In[14]:


all_probabilities(E, 300)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




