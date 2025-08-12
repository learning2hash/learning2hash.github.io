---
layout: publication
title: K-nearest Neighbour Classification Of Datasets With A Family Of Distances
authors: Stan Hatko
conference: Arxiv
year: 2015
bibkey: hatko2015k
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.00001'}]
tags: ["Datasets", "Supervised"]
short_authors: Stan Hatko
---
The \(k\)-nearest neighbour (\(k\)-NN) classifier is one of the oldest and most
important supervised learning algorithms for classifying datasets.
Traditionally the Euclidean norm is used as the distance for the \(k\)-NN
classifier. In this thesis we investigate the use of alternative distances for
the \(k\)-NN classifier.
  We start by introducing some background notions in statistical machine
learning. We define the \(k\)-NN classifier and discuss Stone's theorem and the
proof that \(k\)-NN is universally consistent on the normed space \(R^d\). We then
prove that \(k\)-NN is universally consistent if we take a sequence of random
norms (that are independent of the sample and the query) from a family of norms
that satisfies a particular boundedness condition. We extend this result by
replacing norms with distances based on uniformly locally Lipschitz functions
that satisfy certain conditions. We discuss the limitations of Stone's lemma
and Stone's theorem, particularly with respect to quasinorms and adaptively
choosing a distance for \(k\)-NN based on the labelled sample. We show the
universal consistency of a two stage \(k\)-NN type classifier where we select the
distance adaptively based on a split labelled sample and the query. We conclude
by giving some examples of improvements of the accuracy of classifying various
datasets using the above techniques.