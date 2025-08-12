---
layout: publication
title: Neighborhood Sensitive Mapping For Zero-shot Classification Using Independently
  Learned Semantic Embeddings
authors: Gaurav Singh, Fabrizio Silvestri, John Shawe-Taylor
conference: Arxiv
year: 2016
bibkey: singh2016neighborhood
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.08242'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Gaurav Singh, Fabrizio Silvestri, John Shawe-Taylor
---
In a traditional setting, classifiers are trained to approximate a target
function \(f:X \rightarrow Y\) where at least a sample for each \(y \in Y\) is
presented to the training algorithm. In a zero-shot setting we have a subset of
the labels \(\hat\{Y\} \subset Y\) for which we do not observe any corresponding
training instance. Still, the function \(f\) that we train must be able to
correctly assign labels also on \(\hat\{Y\}\). In practice, zero-shot problems are
very important especially when the label set is large and the cost of
editorially label samples for all possible values in the label set might be
prohibitively high. Most recent approaches to zero-shot learning are based on
finding and exploiting relationships between labels using semantic embeddings.
We show in this paper that semantic embeddings, despite being very good at
capturing relationships between labels, are not very good at capturing the
relationships among labels in a data-dependent manner. For this reason, we
propose a novel two-step process for learning a zero-shot classifier. In the
first step, we learn what we call a *property embedding space* capturing
the "*learnable*" features of the label set. Then, we exploit the learned
properties in order to reduce the generalization error for a linear nearest
neighbor-based classifier.