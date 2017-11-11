---
layout: publication
title: "Learning Multiple Layers of Features from Tiny Images"
authors: A. Krizhevsky
conference: University of Toronto
year: 2009
bibkey: cifar2009learning
additional_links:
   - {name: "PDF", url: "https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf"}
   - {name: "URL", url: "https://www.cs.toronto.edu/~kriz/cifar.html"}
   - {name: "Features", url: "https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=0&m="}
---
Groups at MIT and NYU have collected a dataset of millions of tiny colour images from the web. It
is, in principle, an excellent dataset for unsupervised training of deep generative models, but previous
researchers who have tried this have found it difficult to learn a good set of
filters from the images.
We show how to train a multi-layer generative model that learns to extract meaningful features which
resemble those found in the human visual cortex. Using a novel parallelization algorithm to distribute
the work among multiple machines connected on a network, we show how training such a model can be
done in reasonable time.
A second problematic aspect of the tiny images dataset is that there are no reliable class labels
which makes it hard to use for object recognition experiments. We created two sets of reliable labels.
The CIFAR-10 set has 6000 examples of each of 10 classes and the CIFAR-100 set has 600 examples of
each of 100 non-overlapping classes. Using these labels, we show that object recognition is significantly
improved by pre-training a layer of features on a large set of unlabeled tiny images.
