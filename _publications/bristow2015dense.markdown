---
layout: publication
title: Dense Semantic Correspondence Where Every Pixel Is A Classifier
authors: Hilton Bristow, Jack Valmadre, Simon Lucey
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: bristow2015dense
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.04143'}]
tags: ["ICCV"]
short_authors: Hilton Bristow, Jack Valmadre, Simon Lucey
---
Determining dense semantic correspondences across objects and scenes is a
difficult problem that underpins many higher-level computer vision algorithms.
Unlike canonical dense correspondence problems which consider images that are
spatially or temporally adjacent, semantic correspondence is characterized by
images that share similar high-level structures whose exact appearance and
geometry may differ.
  Motivated by object recognition literature and recent work on rapidly
estimating linear classifiers, we treat semantic correspondence as a
constrained detection problem, where an exemplar LDA classifier is learned for
each pixel. LDA classifiers have two distinct benefits: (i) they exhibit higher
average precision than similarity metrics typically used in correspondence
problems, and (ii) unlike exemplar SVM, can output globally interpretable
posterior probabilities without calibration, whilst also being significantly
faster to train.
  We pose the correspondence problem as a graphical model, where the unary
potentials are computed via convolution with the set of exemplar classifiers,
and the joint potentials enforce smoothly varying correspondence assignment.