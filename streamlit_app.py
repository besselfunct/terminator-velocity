import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.title("Terminator Velocity")

a = 6378137 # meters
b = 6356752.314245 # meters
f = 1/298.257223563

def find_radius(theta, a, b):
  r = ((b - a)/(np.pi/2)) * theta + a
  return r

def find_circumference_radius(theta, radius):
  circum_radius = np.cos(theta) * radius
  return circum_radius

theta_range = np.arange(0, np.pi/2, 10 * np.pi/180)

accumulator = []
for angle in theta_range:
  r = find_radius(angle, a, b)
  circum_radius = find_circumference_radius(angle, r)
  circumference = 2 * np.pi * circum_radius
  accumulator.append(circumference)

st.write(accumulator)
st.write(theta_range)
