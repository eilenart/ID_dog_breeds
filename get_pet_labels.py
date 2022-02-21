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

from os import listdir                          #importing the relevant python function
 
def get_pet_labels(image_dir):                  #defining function and parameter
   
    files = listdir(image_dir)                  #lists all files
    
    results_dic = dict()                        #creating emtpy dictionary for results
          
    for name in files:                          #processing through the files
        if name[0] != ".":                      #skips names starting with dot
            pet_name = name.lower().split("_")  #formatting pet name to the required format
            full_name = ""                      #creating variable for full name
            for word in pet_name:               #processing pet names
                if word.isalpha():              #if the word is alphanumeric
                    full_name += word + " "     #add word to full_name
            pet_label = full_name.strip()       #defining pet label as stripped full name
            results_dic[name] = [pet_label]     #storing pet labels in name
      
    return results_dic                          #returns results
