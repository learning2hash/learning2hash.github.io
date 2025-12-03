---
layout: publication
title: 'An Analysis On The Use Of Autoencoders For Representation Learning: Fundamentals,
  Learning Task Case Studies, Explainability And Challenges'
authors: "David Charte, Francisco Charte, Mar\xEDa J. del Jesus, Francisco Herrera"
conference: Neurocomputing
year: 2020
bibkey: charte2020an
citations: 60
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.10516'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Neural Hashing"]
short_authors: Charte et al.
---
In many machine learning tasks, learning a good representation of the data
can be the key to building a well-performant solution. This is because most
learning algorithms operate with the features in order to find models for the
data. For instance, classification performance can improve if the data is
mapped to a space where classes are easily separated, and regression can be
facilitated by finding a manifold of data in the feature space. As a general
rule, features are transformed by means of statistical methods such as
principal component analysis, or manifold learning techniques such as Isomap or
locally linear embedding. From a plethora of representation learning methods,
one of the most versatile tools is the autoencoder. In this paper we aim to
demonstrate how to influence its learned representations to achieve the desired
learning behavior. To this end, we present a series of learning tasks: data
embedding for visualization, image denoising, semantic hashing, detection of
abnormal behaviors and instance generation. We model them from the
representation learning perspective, following the state of the art
methodologies in each field. A solution is proposed for each task employing
autoencoders as the only learning method. The theoretical developments are put
into practice using a selection of datasets for the different problems and
implementing each solution, followed by a discussion of the results in each
case study and a brief explanation of other six learning applications. We also
explore the current challenges and approaches to explainability in the context
of autoencoders. All of this helps conclude that, thanks to alterations in
their structure as well as their objective function, autoencoders may be the
core of a possible solution to many problems which can be modeled as a
transformation of the feature space.