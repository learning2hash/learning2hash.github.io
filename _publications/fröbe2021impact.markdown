---
layout: publication
title: The Impact Of Main Content Extraction On Near-duplicate Detection
authors: "Maik Fr\xF6be, Matthias Hagen, Janek Bevendorff, Michael V\xF6lske, Benno\
  \ Stein, Christopher Schr\xF6der, Robby Wagner, Lukas Gienapp, Martin Potthast"
conference: Arxiv
year: 2021
bibkey: "fr\xF6be2021impact"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.10864'}]
tags: ["Evaluation"]
short_authors: "Fr\xF6be et al."
---
Commercial web search engines employ near-duplicate detection to ensure that
users see each relevant result only once, albeit the underlying web crawls
typically include (near-)duplicates of many web pages. We revisit the risks and
potential of near-duplicates with an information retrieval focus, motivating
that current efforts toward an open and independent European web search
infrastructure should maintain metadata on duplicate and near-duplicate
documents in its index.
  Near-duplicate detection implemented in an open web search infrastructure
should provide a suitable similarity threshold, a difficult choice since
identical pages may substantially differ in parts of a page that are irrelevant
to searchers (templates, advertisements, etc.). We study this problem by
comparing the similarity of pages for five (main) content extraction methods in
two studies on the ClueWeb crawls. We find that the full content of pages
serves precision-oriented near-duplicate-detection, while main content
extraction is more recall-oriented.