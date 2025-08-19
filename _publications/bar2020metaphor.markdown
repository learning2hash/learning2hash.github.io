---
layout: publication
title: Metaphor Interpretation Using Word Embeddings
authors: Kfir Bar, Nachum Dershowitz, Lena Dankin
conference: Arxiv
year: 2020
bibkey: bar2020metaphor
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.02665'}]
tags: [Uncategorized]
short_authors: Kfir Bar, Nachum Dershowitz, Lena Dankin
---
We suggest a model for metaphor interpretation using word embeddings trained
over a relatively large corpus. Our system handles nominal metaphors, like
"time is money". It generates a ranked list of potential interpretations of
given metaphors. Candidate meanings are drawn from collocations of the topic
("time") and vehicle ("money") components, automatically extracted from a
dependency-parsed corpus. We explore adding candidates derived from word
association norms (common human responses to cues). Our ranking procedure
considers similarity between candidate interpretations and metaphor components,
measured in a semantic vector space. Lastly, a clustering algorithm removes
semantically related duplicates, thereby allowing other candidate
interpretations to attain higher rank. We evaluate using different sets of
annotated metaphors, with encouraging preliminary results.