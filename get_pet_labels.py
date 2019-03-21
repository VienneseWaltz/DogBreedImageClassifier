#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Stella S. 
# DATE CREATED: 3/8/19                                  
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

filename_list = listdir("pet_images/")

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(images_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Creates a list of files in directory from pet images directory
    in_files = listdir(images_dir)
    
    # Process each of the files such that the created dictionary would have
    # key = filename and the value = picture label
    
    # Create an empty dictionary to hold pet labels
    petlabels_dic = dict()
    
    
    
    for idx in range(0, len(in_files), 1): 
        if in_files[idx][0] != ".":
            pet_image_name = in_files[idx].split("_")
            # Check if the first character is uppercase letter. If it is, then lowercase that first character
            if pet_image_name[0].isupper() : 
                pet_image_name = pet_image_name.lower()
            # Create a temporary label variable to hold pet label name
            pet_label = " "
            
            # Process each of the character strings(words) split by '_' in 
            # the list pet_image_name
            for word in pet_image_name: 
                if word.isalpha():
                    pet_label += word + " "
                    pet_label = pet_label.strip()
            if in_files[idx] not in petlabels_dic:
                petlabels_dic[in_files[idx]] = [pet_label]
            else: 
                print(" Warning: Duplicate files exist in dictionary", in_files[idx])
                    
                
    # Return dictionary of pet lables
    return(petlabels_dic)
