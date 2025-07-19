---
layout: publication
title: Quotient Space-based Keyword Retrieval In Sponsored Search
authors: Lian et al.
conference: Proceedings of the 12th ACM conference on Electronic commerce
year: 2021
bibkey: lian2021quotient
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.12371'}]
---
Synonymous keyword retrieval has become an important problem for sponsored
search ever since major search engines relax the exact match product's matching
requirement to a synonymous level. Since the synonymous relations between
queries and keywords are quite scarce, the traditional information retrieval
framework is inefficient in this scenario. In this paper, we propose a novel
quotient space-based retrieval framework to address this problem. Considering
the synonymy among keywords as a mathematical equivalence relation, we can
compress the synonymous keywords into one representative, and the corresponding
quotient space would greatly reduce the size of the keyword repository. Then an
embedding-based retrieval is directly conducted between queries and the keyword
representatives. To mitigate the semantic gap of the quotient space-based
retrieval, a single semantic siamese model is utilized to detect both the
keyword--keyword and query-keyword synonymous relations. The experiments show
that with our quotient space-based retrieval method, the synonymous keyword
retrieving performance can be greatly improved in terms of memory cost and
recall efficiency. This method has been successfully implemented in Baidu's
online sponsored search system and has yielded a significant improvement in
revenue.