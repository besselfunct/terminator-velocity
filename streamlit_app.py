import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.title("Terminator Velocity")

a = 6378137 # meters
b = 6356752.314245 # meters
f = 1/298.257223563

def radius(theta, a, b):
  r = ((b - a)/(np.pi/2)) * theta + a

