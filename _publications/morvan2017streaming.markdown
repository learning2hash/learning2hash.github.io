---
layout: publication
title: Streaming Binary Sketching Based On Subspace Tracking And Diagonal Uniformization
authors: "Anne Morvan, Antoine Souloumiac, C\xE9dric Gouy-Pailler, Jamal Atif"
conference: Arxiv
year: 2017
bibkey: morvan2017streaming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.07661'}]
tags: ["Compact Codes", "Datasets", "Similarity Search"]
short_authors: Morvan et al.
---
In this paper, we address the problem of learning compact
similarity-preserving embeddings for massive high-dimensional streams of data
in order to perform efficient similarity search. We present a new online method
for computing binary compressed representations -sketches- of high-dimensional
real feature vectors. Given an expected code length \(c\) and high-dimensional
input data points, our algorithm provides a \(c\)-bits binary code for preserving
the distance between the points from the original high-dimensional space. Our
algorithm does not require neither the storage of the whole dataset nor a
chunk, thus it is fully adaptable to the streaming setting. It also provides
low time complexity and convergence guarantees. We demonstrate the quality of
our binary sketches through experiments on real data for the nearest neighbors
search task in the online setting.