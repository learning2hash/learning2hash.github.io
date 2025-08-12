---
layout: publication
title: Few-shot Learning With Embedded Class Models And Shot-free Meta Training
authors: Avinash Ravichandran, Rahul Bhotika, Stefano Soatto
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: ravichandran2019few
citations: 165
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.04398'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Avinash Ravichandran, Rahul Bhotika, Stefano Soatto
---
We propose a method for learning embeddings for few-shot learning that is
suitable for use with any number of ways and any number of shots (shot-free).
Rather than fixing the class prototypes to be the Euclidean average of sample
embeddings, we allow them to live in a higher-dimensional space (embedded class
models) and learn the prototypes along with the model parameters. The class
representation function is defined implicitly, which allows us to deal with a
variable number of shots per each class with a simple constant-size
architecture. The class embedding encompasses metric learning, that facilitates
adding new classes without crowding the class representation space. Despite
being general and not tuned to the benchmark, our approach achieves
state-of-the-art performance on the standard few-shot benchmark datasets.