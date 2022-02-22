#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: EMESE ILDIKO LENART   
# DATE CREATED: 22 FEBRUARY 2022
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
 
def print_results(results_dic, results_stats_dic, model,                                    #defining function and parameters
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    
       
    print("\n\n Results summary for the following CNN model srchitecture: ",model.upper())  #printing result summary statistics
    print("{:20}: {:3d}".format("N Images", results_stats_dic["n_images"]))
    print("{:20}: {:3d}".format("N Dog Images", results_stats_dic["n_dogs_img"]))
    print("{:20}: {:3d}".format("N NOT-Dog Images", results_stats_dic["n_notdogs_img"]))
    
    print(" ")                                                                              #printing percentage summary statistics
    for key in results_stats_dic.items():                                                   #iterating through dictionary
        if key [0] == "p":                                                                  #including only items starting with "p"
            print (results_stats_dic.items(), sep='\n')                                     #prints key-value pairs 
       
                                                                                            #printing out incorrectly classified dogs/nondogs
                                                                                            #when print_incorrect_dogs argument is set to True
    if (print_incorrect_dogs and 
        ((results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"])!= results_stats_dic["n_images"])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:

            if results_dic[key][3] == 1 and results_dic[key][4] == 0 or results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print(results_dic[key][0], results_dic[key][1])
              
                                                                                            #printing out incorrectly classified breeds
                                                                                            #when print_incorrect_breeds argument is set to True
    if (print_incorrect_breed and 
        (results_stats_dic["n_correct_dogs"] != results_stats_dic["n_correct_breed"])):
        print("\nINCORRECT Dog Breed Assignment:")

        for key in results_dic:                                                             #processing through results_dic items
            if (results_dic[key][3] == 1 and results_dic[key][4]==1 and                     #if both pet image label and classifier label are indicating dog
                results_dic[key][2] == 0):                                                  #but the breed is incorrent, print pet image and classifier labels
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],results_dic[key][1]))
                
