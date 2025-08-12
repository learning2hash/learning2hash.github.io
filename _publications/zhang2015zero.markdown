---
layout: publication
title: Zero-shot Learning Via Semantic Similarity Embedding
authors: Ziming Zhang, Venkatesh Saligrama
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: zhang2015zero
citations: 581
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.04767'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Ziming Zhang, Venkatesh Saligrama
---
In this paper we consider a version of the zero-shot learning problem where
seen class source and target domain data are provided. The goal during
test-time is to accurately predict the class label of an unseen target domain
instance based on revealed source domain side information (\eg attributes) for
unseen classes. Our method is based on viewing each source or target data as a
mixture of seen class proportions and we postulate that the mixture patterns
have to be similar if the two instances belong to the same unseen class. This
perspective leads us to learning source/target embedding functions that map an
arbitrary source/target domain data into a same semantic space where similarity
can be readily measured. We develop a max-margin framework to learn these
similarity functions and jointly optimize parameters by means of cross
validation. Our test results are compelling, leading to significant improvement
in terms of accuracy on most benchmark datasets for zero-shot recognition.