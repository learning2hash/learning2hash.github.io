---
layout: publication
title: Optimizing Search API Queries For Twitter Topic Classifiers Using A Maximum
  Set Coverage Approach
authors: Kasra Safari, Scott Sanner
conference: Arxiv
year: 2019
bibkey: safari2019optimizing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.10403'}]
tags: []
short_authors: Kasra Safari, Scott Sanner
---
Twitter has grown to become an important platform to access immediate
information about major events and dynamic topics. As one example, recent work
has shown that classifiers trained to detect topical content on Twitter can
generalize well beyond the training data. Since access to Twitter data is
hidden behind a limited search API, it is impossible (for most users) to apply
these classifiers directly to the Twitter unfiltered data streams ("firehose").
Rather, applications must first decide what content to retrieve through the
search API before filtering that content with topical classifiers. Thus, it is
critically important to query the Twitter API relative to the intended topical
classifier in a way that minimizes the amount of negatively classified data
retrieved. In this paper, we propose a sequence of query optimization methods
that generalize notions of the maximum coverage problem to find the subset of
query terms within the API limits that cover most of the topically relevant
tweets without sacrificing precision. We evaluate the proposed methods on a
large dataset of Twitter data collected during 2013 and 2014 labeled using
manually curated hashtags for eight topics. Among many insights, our analysis
shows that the best of the proposed methods can significantly outperform the
firehose on precision and F1-score while achieving high recall within strict
API limitations.