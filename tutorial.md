---
layout: default
title: Tutorial
comments: true
---
In this tutorial we explore a learning to hash model and compare its performance to Locality Sensitive Hashing (LSH). 

Specifically we will implement [Graph Regularised Hashing (GRH)](https://sjmoran.github.io/pdfs/grh_ecir15.pdf), a simple but empirically effective model for learning to hash.

<pre>
@incollection
{ 
year={2015}, 
isbn={978-3-319-16353-6}, 
booktitle={Advances in Information Retrieval}, 
volume={9022}, 
series={Lecture Notes in Computer Science}, 
editor={Hanbury, Allan and Kazai, Gabriella and Rauber, Andreas and Fuhr, Norbert}, 
doi={10.1007/978-3-319-16354-3_15}, 
title={Graph Regularised Hashing}, 
url={http://dx.doi.org/10.1007/978-3-319-16354-3_15}, 
publisher={Springer International Publishing}, author={Moran, Sean and Lavrenko, Victor}, pages={135-146}, 
language={English} 
}
</pre>

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

The above code should download and save the CIFAR-10 dataset pre-processed into GIST features to the current directory. We will now generate 32 random hyperplanes and project one image onto these hyperplanes, generating the hashcode:

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

</pre>

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
