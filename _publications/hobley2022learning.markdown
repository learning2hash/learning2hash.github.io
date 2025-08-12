---
layout: publication
title: 'Learning To Count Anything: Reference-less Class-agnostic Counting With Weak
  Supervision'
authors: Michael Hobley, Victor Prisacariu
conference: Arxiv
year: 2022
bibkey: hobley2022learning
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.10203'}]
tags: []
short_authors: Michael Hobley, Victor Prisacariu
---
Current class-agnostic counting methods can generalise to unseen classes but
usually require reference images to define the type of object to be counted, as
well as instance annotations during training. Reference-less class-agnostic
counting is an emerging field that identifies counting as, at its core, a
repetition-recognition task. Such methods facilitate counting on a changing set
composition. We show that a general feature space with global context can
enumerate instances in an image without a prior on the object type present.
Specifically, we demonstrate that regression from vision transformer features
without point-level supervision or reference images is superior to other
reference-less methods and is competitive with methods that use reference
images. We show this on the current standard few-shot counting dataset FSC-147.
We also propose an improved dataset, FSC-133, which removes errors,
ambiguities, and repeated images from FSC-147 and demonstrate similar
performance on it. To the best of our knowledge, we are the first
weakly-supervised reference-less class-agnostic counting method.