---
layout: publication
title: MTFH A Matrix Tri45;factorization Hashing Framework For Efficient Cross45;modal Retrieval
authors: Liu Xin, Hu Zhikai, Ling Haibin, Cheung Yiu-ming
conference: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
year: 2018
bibkey: liu2018mtfh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1805.01963"}
tags: ['Cross Modal', 'Independent', 'TPAMI']
---
Hashing has recently sparked a great revolution in cross45;modal retrieval because of its low storage cost and high query speed. Recent cross45;modal hashing methods often learn unified or equal45;length hash codes to represent the multi45;modal data and make them intuitively comparable. However such unified or equal45;length hash representations could inherently sacrifice their representation scalability because the data from different modalities may not have one45;to45;one correspondence and could be encoded more efficiently by different hash codes of unequal lengths. To mitigate these problems this paper exploits a related and relatively unexplored problem encode the heterogeneous data with varying hash lengths and generalize the cross45;modal retrieval in various challenging scenarios. To this end a generalized and flexible cross45;modal hashing framework termed Matrix Tri45;Factorization Hashing (MTFH) is proposed to work seamlessly in various settings including paired or unpaired multi45;modal data and equal or varying hash length encoding scenarios. More specifically MTFH exploits an efficient objective function to flexibly learn the modality45;specific hash codes with different length settings while synchronously learning two semantic correlation matrices to semantically correlate the different hash representations for heterogeneous data comparable. As a result the derived hash codes are more semantically meaningful for various challenging cross45;modal retrieval tasks. Extensive experiments evaluated on public benchmark datasets highlight the superiority of MTFH under various retrieval scenarios and show its competitive performance with the state45;of45;the45;arts.
