---
layout: publication
title: Learning From Noisy Web Data With Category-level Supervision
authors: Li Niu, Qingtao Tang, Ashok Veeraraghavan, Ashu Sabharwal
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: niu2018learning
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.03857'}]
tags: ["CVPR", "Datasets", "Supervised"]
short_authors: Niu et al.
---
As tons of photos are being uploaded to public websites (e.g., Flickr, Bing,
and Google) every day, learning from web data has become an increasingly
popular research direction because of freely available web resources, which is
also referred to as webly supervised learning. Nevertheless, the performance
gap between webly supervised learning and traditional supervised learning is
still very large, owning to the label noise of web data. To be exact, the
labels of images crawled from public websites are very noisy and often
inaccurate. Some existing works tend to facilitate learning from web data with
the aid of extra information, such as augmenting or purifying web data by
virtue of instance-level supervision, which is usually in demand of heavy
manual annotation. Instead, we propose to tackle the label noise by leveraging
more accessible category-level supervision. In particular, we build our method
upon variational autoencoder (VAE), in which the classification network is
attached on the hidden layer of VAE in a way that the classification network
and VAE can jointly leverage the category-level hybrid semantic information.
The effectiveness of our proposed method is clearly demonstrated by extensive
experiments on three benchmark datasets.