import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


sets = ['train', 'test', 'val']
wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('data/labels/'):
        os.makedirs('data/labels/')
    image_ids = open('data/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('data/images/%s.jpg\n' % (image_id))
        print('data/images/%s.jpg\n' % (image_id))
        # convert_annotation(image_id)
        in_file = open('data/Annotations/%s.xml' % (image_id))



    list_file.close()


