---
layout: publication
title: 'Pseudo: Interactive Pattern Search In Multivariate Time Series With Locality-sensitive
  Hashing And Relevance Feedback'
authors: Yuncong Yu, Dylan Kruyff, Tim Becker, Michael Behrisch
conference: Arxiv
year: 2021
bibkey: yu2021pseudo
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14962'}]
tags: ["Datasets", "Efficiency", "Locality-Sensitive-Hashing", "Neural Hashing", "Tree Based ANN"]
short_authors: Yu et al.
---
We present PSEUDo, an adaptive feature learning technique for exploring
visual patterns in multi-track sequential data. Our approach is designed with
the primary focus to overcome the uneconomic retraining requirements and
inflexible representation learning in current deep learning-based systems.
Multi-track time series data are generated on an unprecedented scale due to
increased sensors and data storage. These datasets hold valuable patterns, like
in neuromarketing, where researchers try to link patterns in multivariate
sequential data from physiological sensors to the purchase behavior of products
and services. But a lack of ground truth and high variance make automatic
pattern detection unreliable. Our advancements are based on a novel query-aware
locality-sensitive hashing technique to create a feature-based representation
of multivariate time series windows. Most importantly, our algorithm features
sub-linear training and inference time. We can even accomplish both the
modeling and comparison of 10,000 different 64-track time series, each with 100
time steps (a typical EEG dataset) under 0.8 seconds. This performance gain
allows for a rapid relevance feedback-driven adaption of the underlying pattern
similarity model and enables the user to modify the speed-vs-accuracy trade-off
gradually. We demonstrate superiority of PSEUDo in terms of efficiency,
accuracy, and steerability through a quantitative performance comparison and a
qualitative visual quality comparison to the state-of-the-art algorithms in the
field. Moreover, we showcase the usability of PSEUDo through a case study
demonstrating our visual pattern retrieval concepts in a large meteorological
dataset. We find that our adaptive models can accurately capture the user's
notion of similarity and allow for an understandable exploratory visual pattern
retrieval in large multivariate time series datasets.