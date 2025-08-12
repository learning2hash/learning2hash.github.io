---
layout: publication
title: 'Deeptoppush: Simple And Scalable Method For Accuracy At The Top'
authors: "V\xE1clav M\xE1cha, Luk\xE1\u0161 Adam, V\xE1clav \u0160m\xEDdl"
conference: Arxiv
year: 2020
bibkey: "m\xE1cha2020deeptoppush"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.12293'}]
tags: []
short_authors: "V\xE1clav M\xE1cha, Luk\xE1\u0161 Adam, V\xE1clav \u0160m\xEDdl"
---
Accuracy at the top is a special class of binary classification problems
where the performance is evaluated only on a small number of relevant (top)
samples. Applications include information retrieval systems or processes with
manual (expensive) postprocessing. This leads to minimizing the number of
irrelevant samples above a threshold. We consider classifiers in the form of an
arbitrary (deep) network and propose a new method DeepTopPush for minimizing
the loss function at the top. Since the threshold depends on all samples, the
problem is non-decomposable. We modify the stochastic gradient descent to
handle the non-decomposability in an end-to-end training manner and propose a
way to estimate the threshold only from values on the current minibatch and one
delayed value. We demonstrate the excellent performance of DeepTopPush on
visual recognition datasets and two real-world applications. The first one
selects a small number of molecules for further drug testing. The second one
uses real malware data, where we detected 46% malware at an extremely low
false alarm rate of \(10^\{-5\}\).