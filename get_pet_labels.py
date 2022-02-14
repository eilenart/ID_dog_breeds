#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: EMESE ILDIKO LENART
# DATE CREATED: 09 FEBRUARY, 2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
   
    filenames = listdir(image_dir)  #lists all files
    
    results_dic = dict() #creating emtpy dictionary for results
          
    for name in filenames:
        pet_name = name.lower().split("_")
        full_name = ""
        for word in pet_name:
            if word.isalpha():
                full_name += word + " "
        pet_label = full_name.strip()
        results_dic[name] = [pet_label]
      
    print(results_dic)
    return results_dic
