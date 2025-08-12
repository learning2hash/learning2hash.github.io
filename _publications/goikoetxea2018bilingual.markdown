---
layout: publication
title: Bilingual Embeddings With Random Walks Over Multilingual Wordnets
authors: J. Goikoetxea, A. Soroa, E. Agirre
conference: Knowledge-Based Systems
year: 2018
bibkey: goikoetxea2018bilingual
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.08316'}]
tags: ["Datasets"]
short_authors: J. Goikoetxea, A. Soroa, E. Agirre
---
Bilingual word embeddings represent words of two languages in the same space,
and allow to transfer knowledge from one language to the other without machine
translation. The main approach is to train monolingual embeddings first and
then map them using bilingual dictionaries. In this work, we present a novel
method to learn bilingual embeddings based on multilingual knowledge bases (KB)
such as WordNet. Our method extracts bilingual information from multilingual
wordnets via random walks and learns a joint embedding space in one go. We
further reinforce cross-lingual equivalence adding bilingual con- straints in
the loss function of the popular skipgram model. Our experiments involve twelve
cross-lingual word similarity and relatedness datasets in six lan- guage pairs
covering four languages, and show that: 1) random walks over mul- tilingual
wordnets improve results over just using dictionaries; 2) multilingual wordnets
on their own improve over text-based systems in similarity datasets; 3) the
good results are consistent for large wordnets (e.g. English, Spanish), smaller
wordnets (e.g. Basque) or loosely aligned wordnets (e.g. Italian); 4) the
combination of wordnets and text yields the best results, above mapping-based
approaches. Our method can be applied to richer KBs like DBpedia or Babel- Net,
and can be easily extended to multilingual embeddings. All software and
resources are open source.