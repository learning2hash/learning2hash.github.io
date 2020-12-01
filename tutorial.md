---
layout: default
title: Tutorial
comments: true
---
In this tutorial we explore a learning to hash model and compare its performance to Locality Sensitive Hashing (LSH). 

Specifically we will implement [Graph Regularised Hashing (GRH)](https://sjmoran.github.io/pdfs/grh_ecir15.pdf), a simple but effecitive model for learning to hash.

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
