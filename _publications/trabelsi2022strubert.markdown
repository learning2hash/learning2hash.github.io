---
layout: publication
title: 'Strubert: Structure-aware BERT For Table Search And Matching'
authors: Mohamed Trabelsi, Zhiyu Chen, Shuo Zhang, Brian D. Davison, Jeff Heflin
conference: Proceedings of the ACM Web Conference 2022
year: 2022
bibkey: trabelsi2022strubert
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14278'}]
tags: [Datasets]
short_authors: Trabelsi et al.
---
A large amount of information is stored in data tables. Users can search for
data tables using a keyword-based query. A table is composed primarily of data
values that are organized in rows and columns providing implicit structural
information. A table is usually accompanied by secondary information such as
the caption, page title, etc., that form the textual information. Understanding
the connection between the textual and structural information is an important
yet neglected aspect in table retrieval as previous methods treat each source
of information independently. In addition, users can search for data tables
that are similar to an existing table, and this setting can be seen as a
content-based table retrieval. In this paper, we propose StruBERT, a
structure-aware BERT model that fuses the textual and structural information of
a data table to produce context-aware representations for both textual and
tabular content of a data table. StruBERT features are integrated in a new
end-to-end neural ranking model to solve three table-related downstream tasks:
keyword- and content-based table retrieval, and table similarity. We evaluate
our approach using three datasets, and we demonstrate substantial improvements
in terms of retrieval and classification metrics over state-of-the-art methods.