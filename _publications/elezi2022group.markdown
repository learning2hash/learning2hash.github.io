---
layout: publication
title: 'The Group Loss++: A Deeper Look Into Group Loss For Deep Metric Learning'
authors: Ismail Elezi, Jenny Seidenschwarz, Laurin Wagner, Sebastiano Vascon, Alessandro
  Torcinovich, Marcello Pelillo, Laura Leal-Taixe
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: elezi2022group
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.01509'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval", "Tools & Libraries"]
short_authors: Elezi et al.
---
Deep metric learning has yielded impressive results in tasks such as
clustering and image retrieval by leveraging neural networks to obtain highly
discriminative feature embeddings, which can be used to group samples into
different classes. Much research has been devoted to the design of smart loss
functions or data mining strategies for training such networks. Most methods
consider only pairs or triplets of samples within a mini-batch to compute the
loss function, which is commonly based on the distance between embeddings. We
propose Group Loss, a loss function based on a differentiable label-propagation
method that enforces embedding similarity across all samples of a group while
promoting, at the same time, low-density regions amongst data points belonging
to different groups. Guided by the smoothness assumption that "similar objects
should belong to the same group", the proposed loss trains the neural network
for a classification task, enforcing a consistent labelling amongst samples
within a class. We design a set of inference strategies tailored towards our
algorithm, named Group Loss++ that further improve the results of our model. We
show state-of-the-art results on clustering and image retrieval on four
retrieval datasets, and present competitive results on two person
re-identification datasets, providing a unified framework for retrieval and
re-identification.