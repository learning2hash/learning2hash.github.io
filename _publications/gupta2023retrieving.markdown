---
layout: publication
title: Retrieving Continuous Time Event Sequences Using Neural Temporal Point Processes
  With Learnable Hashing
authors: Vinayak Gupta, Srikanta Bedathur, Abir de
conference: Arxiv
year: 2023
bibkey: gupta2023retrieving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.09613'}]
tags: ["Efficiency", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Vinayak Gupta, Srikanta Bedathur, Abir de
---
Temporal sequences have become pervasive in various real-world applications.
Consequently, the volume of data generated in the form of continuous time-event
sequence(s) or CTES(s) has increased exponentially in the past few years. Thus,
a significant fraction of the ongoing research on CTES datasets involves
designing models to address downstream tasks such as next-event prediction,
long-term forecasting, sequence classification etc. The recent developments in
predictive modeling using marked temporal point processes (MTPP) have enabled
an accurate characterization of several real-world applications involving the
CTESs. However, due to the complex nature of these CTES datasets, the task of
large-scale retrieval of temporal sequences has been overlooked by the past
literature. In detail, by CTES retrieval we mean that for an input query
sequence, a retrieval system must return a ranked list of relevant sequences
from a large corpus. To tackle this, we propose NeuroSeqRet, a
first-of-its-kind framework designed specifically for end-to-end CTES
retrieval. Specifically, NeuroSeqRet introduces multiple enhancements over
standard retrieval frameworks and first applies a trainable unwarping function
on the query sequence which makes it comparable with corpus sequences,
especially when a relevant query-corpus pair has individually different
attributes. Next, it feeds the unwarped query sequence and the corpus sequence
into MTPP-guided neural relevance models. We develop four variants of the
relevance model for different kinds of applications based on the trade-off
between accuracy and efficiency. We also propose an optimization framework to
learn binary sequence embeddings from the relevance scores, suitable for the
locality-sensitive hashing. Our experiments show the significant accuracy boost
of NeuroSeqRet as well as the efficacy of our hashing mechanism.