---
layout: publication
title: 'Wojood: Nested Arabic Named Entity Corpus And Recognition Using BERT'
authors: Mustafa Jarrar, Mohammed Khalilia, Sana Ghanem
conference: In Proceedings of the International Conference on Language Resources and
  Evaluation (LREC 2022) Marseille France. 2022
year: 2022
bibkey: jarrar2022wojood
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.09651'}]
tags: ["Evaluation", "LREC"]
short_authors: Mustafa Jarrar, Mohammed Khalilia, Sana Ghanem
---
This paper presents Wojood, a corpus for Arabic nested Named Entity
Recognition (NER). Nested entities occur when one entity mention is embedded
inside another entity mention. Wojood consists of about 550K Modern Standard
Arabic (MSA) and dialect tokens that are manually annotated with 21 entity
types including person, organization, location, event and date. More
importantly, the corpus is annotated with nested entities instead of the more
common flat annotations. The data contains about 75K entities and 22.5% of
which are nested. The inter-annotator evaluation of the corpus demonstrated a
strong agreement with Cohen's Kappa of 0.979 and an F1-score of 0.976. To
validate our data, we used the corpus to train a nested NER model based on
multi-task learning and AraBERT (Arabic BERT). The model achieved an overall
micro F1-score of 0.884. Our corpus, the annotation guidelines, the source code
and the pre-trained model are publicly available.