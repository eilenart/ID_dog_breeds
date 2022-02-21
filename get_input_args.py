#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: EMESE ILDIKO LENART           
# DATE CREATED: 09 FEBRUARY, 2022                                
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#

import argparse                         #imports relevant python module
 
def get_input_args():                   #defines parsing function using argument parser
    
    parser = argparse.ArgumentParser()  #defines the 3 required arguments with defaults and help lines
    parser.add_argument("--dir", type = str, default = "pet_images/", 
                        help="Path to folder containing the images")
    parser.add_argument("--arch", type = str, default = "vgg", help = "The CNN model architecture applied" )
    parser.add_argument("--dogfile", type = str, default = "dognames.txt", help = "Path to the folder containing the dog names" )
     
    return parser.parse_args()          #returns results
