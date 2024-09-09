---
layout: publication
title: "No Repetition: Fast Streaming with Highly Concentrated Hashing"
authors: Aamand Anders, Das Debarati, Kipouridis Evangelos, Knudsen Jakob B. T., Rasmussen Peter M. R., Thorup Mikkel
conference: Arxiv
year: 2020
bibkey: aamand2020no
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2004.01156"}
tags: ['ARXIV']
---
To get estimators that work within a certain error bound with high probability, a common strategy is to design one that works with constant probability, and then boost the probability using independent repetitions. Important examples of this approach are small space algorithms for estimating the number of distinct elements in a stream, or estimating the set similarity between large sets. Using standard strongly universal hashing to process each element, we get a sketch based estimator where the probability of a too large error is, say, 1/4. By performing $r$ independent repetitions and taking the median of the estimators, the error probability falls exponentially in $r$. However, running $r$ independent experiments increases the processing time by a factor $r$. Here we make the point that if we have a hash function with strong concentration bounds, then we get the same high probability bounds without any need for repetitions. Instead of $r$ independent sketches, we have a single sketch that is $r$ times bigger, so the total space is the same. However, we only apply a single hash function, so we save a factor $r$ in time, and the overall algorithms just get simpler. Fast practical hash functions with strong concentration bounds were recently proposed by Aamand em et al. (to appear in STOC 2020). Using their hashing schemes, the algorithms thus become very fast and practical, suitable for online processing of high volume data streams.