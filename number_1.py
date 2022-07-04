import numpy as np
from math import *

# step one - get the data
vec1 = [60, 45]
vec2 = [40, 20]
vec3 = [50, 30]

def analysis_vectors(vec1, vec2, vec3):
    # step two - calculate i and j
    vec1_i = int(vec1[0])*(cos(vec1[1]*pi/180))
    vec1_j = int(vec1[0])*(sin(vec1[1]*pi/180))

    vec2_i = int(vec2[0])*(cos(vec2[1]*pi/180))
    vec2_j = int(vec2[0])*(sin(vec2[1]*pi/180))

    vec3_i = int(vec3[0])*(cos(vec3[1]*pi/180))
    vec3_j = int(vec3[0])*(sin(vec3[1]*pi/180))

    # step three - calculate the total vector
    total_i = vec1_i + vec2_i + vec3_i
    total_j = vec1_j + vec2_j + vec3_j

    # step four - calculate the average vector
    value = sqrt(total_i**2 + total_j**2)
    degree = atan2(total_j, total_i)*180/pi

    print(f"The average vector is {value} and {degree} degrees")
    

analysis_vectors(vec1, vec2, vec3)