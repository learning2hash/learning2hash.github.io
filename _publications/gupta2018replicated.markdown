---
layout: publication
title: Replicated Siamese LSTM In Ticketing System For Similarity Learning And Retrieval
  In Asymmetric Texts
authors: "Pankaj Gupta, Bernt Andrassy, Hinrich Sch\xFCtze"
conference: Arxiv
year: 2018
bibkey: gupta2018replicated
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.02854'}]
tags: [Supervised, Unsupervised]
short_authors: "Pankaj Gupta, Bernt Andrassy, Hinrich Sch\xFCtze"
---
The goal of our industrial ticketing system is to retrieve a relevant
solution for an input query, by matching with historical tickets stored in
knowledge base. A query is comprised of subject and description, while a
historical ticket consists of subject, description and solution. To retrieve a
relevant solution, we use textual similarity paradigm to learn similarity in
the query and historical tickets. The task is challenging due to significant
term mismatch in the query and ticket pairs of asymmetric lengths, where
subject is a short text but description and solution are multi-sentence texts.
We present a novel Replicated Siamese LSTM model to learn similarity in
asymmetric text pairs, that gives 22% and 7% gain (Accuracy@10) for retrieval
task, respectively over unsupervised and supervised baselines. We also show
that the topic and distributed semantic features for short and long texts
improved both similarity learning and retrieval.