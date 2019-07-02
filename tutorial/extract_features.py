'''
Code to read the Google Audioset dataset TFRecord format and create numpy feature files and csv formatted metadata files for the training and test splits.

To use this script please extract unbal_train and eval TFRecords to ./unbal_train and ./eval directories within the same directory as this script.
'''

import tensorflow as tf
from os import listdir
from os.path import isfile, join
import numpy as np
import os.path as path
import csv

'''
Uncomment the following line to generate the unbalanced training dataset (our database)
'''
#onlyfiles=[join("./unbal_train/", f) for f in listdir("./unbal_train/") if isfile(join("./unbal_train/", f))]
#csv_file="./train_metadata.csv"
#features_filename=path.join("./train_features.npy")
#metadata_filename=path.join("./train_metadata.csv")
#fp1=np.memmap(features_filename, dtype='float32', mode-'w+', shape=(20326484,128))

'''
Uncomment the following line to generate the query dataset (our query set)
'''
onlyfiles=[join("./eval/", f) for f in listdir("./eval/") if isfile(join("./eval/", f))]
csv_file="./eval_metadata.csv"
features_filename=path.join("./eval_features.npy")
metadata_filename=path.join("./eval_metadata.csv")
fp1=np.memmap(features_filename, dtype='float32', mode='w+', shape=(202439,128))

with open(csv_file, 'w') as f:

     writer = csv.writer(f, lineterminator='\n')
     row=0

     for file in onlyfiles:

         record_iterator=tf.python_io.tf_record_iterator(file)

         for string_record in record_iterator:

            metadata=[]
            example = tf.train.SequenceExample()
            sample.ParseFromString(string_record)

            start_time_seconds = example.context.feature['start_time_seconds'].float_list.values[0]
            end_time_seconds = example.context.feature['end_time_seconds'].float_list.values[0]
            labels = example.context.feature['labels'].int64_list.value
            video_id = example.context.feature['video_id'].bytes_list.value[0].decode("utf-8")
            num_segment = len(example.feature_lists.feature_list['audio_embedding'].feature)

            metadata.append(str(video_id))
            metadata.append(start_time_seconds)
            metadata.append(end_time_seconds)

            '''
            The rest of metadata (after the first 3 elements, are the class labels (1 or more)
            '''
            for label in labels:
                metadata.append(label)

            '''
            Decoding the raw audio features (128 dimensional) associated with the video. 
	        '''
            embedding=[]
            for i in range(0,num_segment):
                hexembed=example.feature_lists.feature_list['audio_embedding'].feature[i].bytes_list.value[0].hex()
                embedding=[int(hexembed[i:i+2],16) for i in range (0, len(hexembed),2)]
                fp1[row,:]=embedding      # this writes the embedding to the feature .npy file
                writer.writerow(metadata) # this writes the metadata to the metadata .csv file
                row+=1
                print(row)
                
del fp1     # flush the data to disk
