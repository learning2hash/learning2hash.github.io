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
onlyfiles=[join("./unbal_train/", f) for f in listdir("./unbal_train/") if isfile(join("./unbal_train/", f))]  # location of the unbalanced training dataset TFRecords
train_features_filename=path.join("./train_features.npy") # numpy file containing the features
train_metadata_filename=path.join("./train_metadata.csv") # numpy file containing the metadata e.g. video_id, class labels
valid_features_filename=path.join("./valid_features.npy") # numpy file containing the features
valid_metadata_filename=path.join("./valid_metadata.csv") # numpy file containing the features e.g. video_id, class labels

train_memmap=np.memmap(train_features_filename, dtype='float32', mode='w+', shape=(20131970,128)) # Memory map for the training featureset (saves loading into memory and exhausting RAM)
valid_memmap=np.memmap(vaid_features_filename, dtype='float32', mode='w+', shape=(2013197,128)) # Memory map for the validation featureset

'''
Uncomment the following line to generate the query dataset (our query set)
'''
#onlyfiles=[join("./eval/", f) for f in listdir("./eval/") if isfile(join("./eval/", f))]  # location of the unbalanced training dataset TFRecords
#test_features_filename=path.join("./test_features.npy") # numpy file containing the features
#test_metadata_filename=path.join("./test_metadata.csv") # numpy file containing the metadata e.g. video_id, class labels
#test_memmap=np.memmap(test_features_filename, dtype='float32', mode-'w+', shape=(202439,128)) # Memory map for the test featureset

write_valid=True
VALID_ROWS=2013196 # validation features are 10% of the training features

with open(train_metadata_filename, 'w') as f1, open(valid_metadata_filename, 'w') as f2: 

     train_writer = csv.writer(f1, lineterminator='\n')
     valid_writer = csv.writer(f2, lineterminator='\n')
     row=0

     for file in onlyfiles:

         record_iterator=tf.python_io.tf_record_iterator(file)

         for string_record in record_iterator:

            metadata=[]

            example = tf.train.SequenceExample()
            sample.ParseFromString(string_record)

            start_time_seconds = example.context.feature['start_time_seconds'].float_list.values[0]
            end_time_seconds = example.context.feature['end_time_seconds'].float_list.values[0]

            '''
            Keep only segments that are 10 seconds in duration
            '''
            if end_time_seconds-start_time_seconds != 10:
                continue
	     
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

                if write_valid:

                    valid_memmap[row,:]=embedding

                    if row % 100000 == 0:
                        valid_memmap.flush()

                    valid_writer.writerow(metadata)

                    if row==VALID_ROWS:
                        row=-1
                        write_valid=False
                        valid_memmap.flush()

                else:

                    train_memmap[row,:]=embedding

                    if row % 100000 == 0:
                        train_memmap.flush()

                    train_writer.writerow(metadata)
		    
                row+=1

train_memmap.flush()
valid_memmap.flush()
del train_memmap
del valid_memmap
