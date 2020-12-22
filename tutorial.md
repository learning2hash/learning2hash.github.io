---
layout: default
title: Tutorial
comments: true
---
In this tutorial we explore a learning to hash model and compare its performance to Locality Sensitive Hashing (LSH). 

Specifically we will implement [Graph Regularised Hashing (GRH)](https://sjmoran.github.io/pdfs/grh_ecir15.pdf) of Moran and Lavrenko, a simple but empirically effective model for learning to hash. The citation bibtex can be found [here](https://sjmoran.github.io/bib/grh.bib).

The original Matlab code supplied by the authors is [here](https://github.com/sjmoran/GRH). We will code up a version of the model in Python 3. This tutorial will train the model on the CIFAR-10 dataset and benchmark retrieval effectiveness against LSH (random projections).

First step is to instantiate a virtual environment for Python3:

<pre>
python3 -m venv ./hashing_tutorial
source hashing_tutorial/bin/activate
</pre>

We retrieve and pre-process the CIFAR-10 dataset as follows:

<pre>
import scipy.io
import os
import requests

url='https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=1'
response = requests.get(url)
with open(os.path.join("./", "Gist512CIFAR10.mat"), 'wb') as f:
    f.write(response.content)

mat = scipy.io.loadmat('./Gist512CIFAR10.mat')

data = mat['X']
classes = mat['X_class']
</pre>

The above code should download and save the CIFAR-10 dataset pre-processed into GIST features to the current directory. We will now generate 16 random hyperplanes and project one image onto these hyperplanes, generating the hashcode:

<pre>
import numpy as np

num_classes = 10
n_vectors = 32
dim = 512

np.random.seed(0)
random_vectors = np.random.randn(dim, n_vectors)
print(random_vectors)

print('dimension:', data[0,:].shape)
bin_indices_bits = data[0,:].dot(random_vectors) >= 0

print(bin_indices_bits)

# [False  True False  True False  True False False False False  True  True True False False False]

</pre>

The last line of code prints out the hashcode assigned to this image. Images with the exact same hashcode will collide in the same hashtable bucket. We would like these colliding images to be semantically similar i.e. have the same class label.

We now convert the boolean representation above into an integer representation that will denote the bin indices:

<pre>
# https://wiki.python.org/moin/BitwiseOperators
# x << y is the same as multiplying x by 2 ** y
powers_of_two = 1 << np.arange(n_vectors - 1, -1, step=-1)
print(powers_of_two)
# [32768 16384  8192  4096  2048  1024   512   256   128    64    32    16    8     4     2     1]

bin_indices = bin_indices_bits.dot(powers_of_two)
print(bin_indices)
# 21560
</pre>

The example image will hash into hashtable bucket with index 21560. Now we will hash the entire dataset using matrix operations:

<pre>
bin_indices_bits = data.dot(random_vectors) >= 0
print(bin_indices_bits.shape)
bin_indices = bin_indices_bits.dot(powers_of_two)
bin_indices.shape
</pre>

bin_indices now contains 60,000 bin indices, one for each of the 60,000 images in the CIFAR-10 dataset. We now insert these images into a hashtable and inspect the duplicates:

<pre>
from collections import defaultdict

table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
	table[bin_index].append(idx)

for bucket,images in table.items():
	if len(images)>1:
        print(images)
</pre>

The code above will print out the buckets of the hashtable with at least two images and the associated IDs (i.e. row numbers in the original .mat file) of the images in each bucket. The average bin count is ~51 images, so there has been many collisions of images into buckets. Next we will inspect some of the buckets to gain an understanding of the quality of the hashing with LSH:

<pre>
# We take this bucket and inspect the images:
# [46262, 46488, 47724, 59147, 59462, 59572]

print(classes.shape)
print(classes[:,46262])   # 3
print(classes[:,46488])   # 8
print(classes[:,47724])   # 7
print(classes[:,59147])   # 9
print(classes[:,59462])   # 2
print(classes[:,59572])   # 8
</pre>

On this particular example we can see that LSH does fairly poorly, with only two semantically related images (class 8), colliding in the same bucket. We will inspect another bucket before moving on:

<pre>
# We take this bucket and inspect the images:
# [16380, 18515, 27324, 33419, 43442, 46613, 54356]

print(classes.shape)
print(classes[:,16380])   # 0
print(classes[:,18515])   # 8
print(classes[:,27324])   # 0
print(classes[:,33419])   # 0
print(classes[:,43442])   # 0
print(classes[:,46613])   # 0
print(classes[:,54356])   # 0
</pre>

In this case we see that LSH performs very well, with most of the collding images coming from the same class label (0). We now quantify the performance of LSH using the precision and recall metrics:

Reminscent of the expectation maximisation algorithm (EM), the model consists of two steps, performed in a loop: learning of the hashing hyperplanes followed by smoothing of the predicted bits based on the image relationship graph defined by the labels.

<pre>
ALPHA = 0.9
bitsGRH = ALPHA.*(affinity * bitsGRH) + (1-ALPHA).*bitsSBQ(RunObj.data.affinityInd,:);

bitsGRH(bitsGRH>=0)=1;
bitsGRH(bitsGRH<0)=-1;

bitsGRHTemp=[];
dataProj=[];
predictedScores={};
predictedLabels={};
svmModel={};

for k=1:size(bitsGRH,2)
    
    labels=bitsGRH(:,k);
    
    nPosLabels=size(find(labels==1),1);
    nNegLabels=size(find(labels==-1),1);
  
    svmModel{k} =train(labels,sparse(data),['-s 1 -c ',num2str(RunObj.params.C),' -w1 ',num2str(ceil(w1)),' -w-1 ',num2str(ceil(w2))]);
   
    data=RunObj.data.dataValidParFor;
    predictedLabels={};
    
    [predictedLabels, accuracy, predictedScores]=predict(ones(size(data,1),1), sparse(data{), svmModel{k});
    
    bitsGRHTemp(:,k)=predictedLabels;

    dataProj=[dataProj,predictedScores];
end

bitsGRH=bitsGRHTemp;

% Quantise projections
bitsGRH(bitsGRH>0)=1;
bitsGRH(bitsGRH<=0)=0;

[RunObj,pAtR2GRHValid, mAPGRHValid]=eval_bits(RunObj, bitsGRH, 1);

disp(sprintf('%s\t%f\n','mAPGRHValid: ',mAPGRHValid))

bitsGRH(bitsGRH==0)=-1;
</pre>

Parts of this tutorial were inspired by the text-based LSH tutorial [here](http://ethen8181.github.io/machine-learning/recsys/content_based/lsh_text.html).
