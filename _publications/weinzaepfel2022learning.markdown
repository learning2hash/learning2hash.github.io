---
layout: publication
title: Learning Super-features For Image Retrieval
authors: Philippe Weinzaepfel, Thomas Lucas, Diane Larlus, Yannis Kalantidis
conference: Arxiv
year: 2022
bibkey: weinzaepfel2022learning
citations: 13
additional_links: [{name: Code, url: 'https://github.com/naver/FIRe'}, {name: Paper,
    url: 'https://arxiv.org/abs/2201.13182'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation, Memory Efficiency]
short_authors: Weinzaepfel et al.
---
Methods that combine local and global features have recently shown excellent
performance on multiple challenging deep image retrieval benchmarks, but their
use of local features raises at least two issues. First, these local features
simply boil down to the localized map activations of a neural network, and
hence can be extremely redundant. Second, they are typically trained with a
global loss that only acts on top of an aggregation of local features; by
contrast, testing is based on local feature matching, which creates a
discrepancy between training and testing. In this paper, we propose a novel
architecture for deep image retrieval, based solely on mid-level features that
we call Super-features. These Super-features are constructed by an iterative
attention module and constitute an ordered set in which each element focuses on
a localized and discriminant image pattern. For training, they require only
image labels. A contrastive loss operates directly at the level of
Super-features and focuses on those that match across images. A second
complementary loss encourages diversity. Experiments on common landmark
retrieval benchmarks validate that Super-features substantially outperform
state-of-the-art methods when using the same number of features, and only
require a significantly smaller memory footprint to match their performance.
Code and models are available at: https://github.com/naver/FIRe.