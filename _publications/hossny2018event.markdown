---
layout: publication
title: 'Event Detection In Twitter: A Keyword Volume Approach'
authors: Ahmad Hany Hossny, Lewis Mitchell
conference: 2018 IEEE International Conference on Data Mining Workshops (ICDMW)
year: 2018
bibkey: hossny2018event
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.00570'}]
tags: []
short_authors: Ahmad Hany Hossny, Lewis Mitchell
---
Event detection using social media streams needs a set of informative
features with strong signals that need minimal preprocessing and are highly
associated with events of interest. Identifying these informative features as
keywords from Twitter is challenging, as people use informal language to
express their thoughts and feelings. This informality includes acronyms,
misspelled words, synonyms, transliteration and ambiguous terms. In this paper,
we propose an efficient method to select the keywords frequently used in
Twitter that are mostly associated with events of interest such as protests.
The volume of these keywords is tracked in real time to identify the events of
interest in a binary classification scheme. We use keywords within word-pairs
to capture the context. The proposed method is to binarize vectors of daily
counts for each word-pair by applying a spike detection temporal filter, then
use the Jaccard metric to measure the similarity of the binary vector for each
word-pair with the binary vector describing event occurrence. The top n
word-pairs are used as features to classify any day to be an event or non-event
day. The selected features are tested using multiple classifiers such as Naive
Bayes, SVM, Logistic Regression, KNN and decision trees. They all produced AUC
ROC scores up to 0.91 and F1 scores up to 0.79. The experiment is performed
using the English language in multiple cities such as Melbourne, Sydney and
Brisbane as well as the Indonesian language in Jakarta. The two experiments,
comprising different languages and locations, yielded similar results.