import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):
    h,w = gray.shape
    hist = np.zeros([256]),dty