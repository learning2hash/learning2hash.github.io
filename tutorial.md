---
layout: default
title: Tutorial
comments: true
---
In this tutorial we explore a learning to hash model and compare its performance to Locality Sensitive Hashing (LSH). 

Specifically we will implement [Graph Regularised Hashing (GRH)](https://sjmoran.github.io/pdfs/grh_ecir15.pdf), a simple but effecitive model for learning to hash.

<pre>
@incollection{ 
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
language={English} }
</pre>

The original Matlab code supplied by the authors is [here](https://github.com/sjmoran/GRH). This tutorial will train the model on the CIFAR-10 dataset and benchmark retrieval effectiveness against LSH.

<pre>
unction [bitsGRH, mAPGRHValid, svmModel] = learn_grh(RunObj, affinity, bitsGRH, bitsSBQ)

bitsGRH = RunObj.params.ALPHA.*(affinity * bitsGRH) + (1-RunObj.params.ALPHA).*bitsSBQ(RunObj.data.affinityInd,:);

bitsGRH(bitsGRH>=0)=1;
bitsGRH(bitsGRH<0)=-1;

bitsGRHTemp=[];
dataProj=[];
predictedScores={};
predictedLabels={};
svmModel={};

for k=1:size(bitsGRH,2)
    
    labels=bitsGRH(:,k);
    data=RunObj.data.data(RunObj.data.affinityInd,:);
    
    nPosLabels=size(find(labels==1),1);
    nNegLabels=size(find(labels==-1),1);
    
    if (nPosLabels > nNegLabels)
        w2=nPosLabels/nNegLabels;
        w1=1;
    else
        w1=nNegLabels/nPosLabels;
        w2=1;
    end
    
    if (RunObj.params.KERNEL==3)
        if (abs(sum(labels))==size(data,1))
            labels(1,:)=labels(1,:)*-1;
        end
        svmModel{k} = budgetedsvm_train(labels, data, ['-A 4 -e 5 -L 0.0001 -m 1 -D ',num2str(size(RunObj.data.data,2)),' -v 1 -g ',num2str(RunObj.params.SIGMA),' -B ',num2str(RunObj.params.NLANDMARKS)]);
    elseif(RunObj.params.KERNEL==2)
        svmModel{k} =svmtrain(labels,data,['-t 2 -g ',num2str(RunObj.params.SIGMA),' -c ',num2str(RunObj.params.C),' -s 0 -w1 ',num2str(ceil(w1)),' -w-1 ',num2str(ceil(w2)),' -q']);
    else
        svmModel{k} =train(labels,sparse(data),['-s 1 -c ',num2str(RunObj.params.C),' -w1 ',num2str(ceil(w1)),' -w-1 ',num2str(ceil(w2))]);
    end
    
    data=RunObj.data.dataValidParFor;
    predictedLabels={};
    
    if (RunObj.params.KERNEL==3)
        
        parfor m=1:RunObj.params.NCHUNK
            [errorRate{m}, predictedLabels{m}, predictedScores{m}] = budgetedsvm_predict(ones(size(data{m},1),1), data{m}, svmModel{k});
        end
    elseif (RunObj.params.KERNEL==2)
        parfor m=1:RunObj.params.NCHUNK
            [predictedLabels{m}, accuracy{m}, predictedScores{m}]=svmpredict(ones(size(data{m},1),1), data{m}, svmModel{k});
        end
    else
        parfor m=1:RunObj.params.NCHUNK
            [predictedLabels{m}, accuracy{m}, predictedScores{m}]=predict(ones(size(data{m},1),1), sparse(data{m}), svmModel{k});
        end
    end
    
    bitsTemp=[];
    for m=1:RunObj.params.NCHUNK
        bitsTemp=[bitsTemp;predictedLabels{m}];
    end
    bitsGRHTemp(:,k)=bitsTemp;
    
    dataProjTemp=[];
    
    for m=1:RunObj.params.NCHUNK
        dataProjTemp=[dataProjTemp;predictedScores{m}];
    end
    
    dataProj=[dataProj,dataProjTemp];
end

bitsGRH=bitsGRHTemp;

% Quantise projections
bitsGRH(bitsGRH>0)=1;
bitsGRH(bitsGRH<=0)=0;

[RunObj,pAtR2GRHValid, mAPGRHValid]=eval_bits(RunObj, bitsGRH, 1);

disp(sprintf('%s\t%f\n','mAPGRHValid: ',mAPGRHValid))

bitsGRH(bitsGRH==0)=-1;
</pre>
