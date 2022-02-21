#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: EMESE ILDIKO LENART   
# DATE CREATED: 21 FEBRUARY, 2022                            
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
# 
def calculates_results_stats(results_dic):                  #defining function and parameter
          
    results_stats_dic = dict()                              #creating empty dictionary for results_stats_dic
    
    results_stats_dic["n_dogs_img"] = 0                     #setting all counters to 0 for correct incrementation during processing
    results_stats_dic["n_match"] = 0
    results_stats_dic["n_correct_dogs"] = 0
    results_stats_dic["n_correct_notdogs"] = 0
    results_stats_dic["n_correct_breed"] = 0       
    
    
    for key in results_dic:                                 #processing the data in the results dictionary
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1               #counts number of pet image label and classifier label matches
        if results_dic[key][3] == 1 and results_dic[key][2] == 1: 
                results_stats_dic["n_correct_breed"] +=1    #counts instances where pet image label is indicating dog, and matches classifier label as well
        if results_dic[key][3] == 1:
            results_stats_dic["n_dogs_img"] += 1            #counts number of pet image labels indicating dogs     
        if results_dic[key][4] == 1:
                results_stats_dic["n_correct_dogs"] += 1    #counts number of classifier labels indicating dogs
        else:
                results_stats_dic["n_correct_notdogs"] +=1  #count number of classifier labels indicating NOT dogs
             
    #The statistics below are calculated based on the results above.      
    
    results_stats_dic["n_images"] = len(results_dic)        #calculating number of total images
  
    #calculating number of NOT dog images by substracting the dog images from the total number
    results_stats_dic["n_notdogs_img"] = (results_stats_dic["n_images"] - results_stats_dic["n_dogs_img"])
                                                            
    #correctly matched images in % 
    results_stats_dic["pct_match"] = ((results_stats_dic["n_match"]/results_stats_dic["n_images"])*100.0)                
    
    #correctly identified as dogs in %
    results_stats_dic["pct_correct_dogs"] = ((results_stats_dic["n_correct_dogs"]/results_stats_dic["n_dogs_img"])*100.0) 

    #correctly classified breeds in %
    results_stats_dic["pct_correct_breed"] = ((results_stats_dic["n_correct_breed"]/results_stats_dic["n_dogs_img"])*100.0) 

    
    if results_stats_dic["n_notdogs_img"] > 0:      #to avoid zero division error in case no NOT dog images were submitted
        
        #correctly identified NOT dog images
        results_stats_dic["pct_correct_notdogs"] = (results_stats_dic["n_correct_notdogs"]/results_stats_dic["n_notdogs_img"]*100.0) 
        
        #if no NOT dog images were submitted, this number is 0
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0 

        #returning results
    return results_stats_dic

