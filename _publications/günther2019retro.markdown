---
layout: publication
title: 'RETRO: Relation Retrofitting For In-database Machine Learning On Textual Data'
authors: "Michael G\xFCnther, Maik Thiele, Wolfgang Lehner"
conference: Arxiv
year: 2019
bibkey: "g\xFCnther2019retro"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.12674'}]
tags: ["Evaluation"]
short_authors: "Michael G\xFCnther, Maik Thiele, Wolfgang Lehner"
---
There are massive amounts of textual data residing in databases, valuable for
many machine learning (ML) tasks. Since ML techniques depend on numerical input
representations, word embeddings are increasingly utilized to convert symbolic
representations such as text into meaningful numbers. However, a naive
one-to-one mapping of each word in a database to a word embedding vector is not
sufficient and would lead to poor accuracies in ML tasks. Thus, we argue to
additionally incorporate the information given by the database schema into the
embedding, e.g. which words appear in the same column or are related to each
other. In this paper, we propose RETRO (RElational reTROfitting), a novel
approach to learn numerical representations of text values in databases,
capturing the best of both worlds, the rich information encoded by word
embeddings and the relational information encoded by database tables. We
formulate relation retrofitting as a learning problem and present an efficient
algorithm solving it. We investigate the impact of various hyperparameters on
the learning problem and derive good settings for all of them. Our evaluation
shows that the proposed embeddings are ready-to-use for many ML tasks such as
classification and regression and even outperform state-of-the-art techniques
in integration tasks such as null value imputation and link prediction.