from promptflow import tool
from typing import List
import numpy as np
from numpy.linalg import norm
import json


@tool
def cosine_sim(vectorA: List[float], vectorB: List[float]) -> float:

   # define inputs as np.array
    A = np.array(vectorA)
    B = np.array(vectorB)
    
    # compute cosine similarity
    cosine_sim = np.dot(A,B)/(norm(A)*norm(B))
    
    return cosine_sim