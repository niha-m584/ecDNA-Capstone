import matplotlib.pyplot as plt
from IPython.display import Image
import os
import cv2
from sklearn.cluster import KMeans
from matplotlib.pyplot import imshow
import skimage
import numpy as np
import networkx as nx
from pathlib import Path

def count(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Canny(img,25,200)
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    output_folder = 'annotated/' + image
    output_filename = 'a_' + image

    path = Path(output_folder)
    path.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_folder + output_filename, format='tif')

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours



