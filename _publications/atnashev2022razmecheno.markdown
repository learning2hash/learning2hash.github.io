---
layout: publication
title: 'Razmecheno: Named Entity Recognition From Digital Archive Of Diaries "prozhito"'
authors: Timofey Atnashev, Veronika Ganeeva, Roman Kazakov, Daria Matyash, Michael
  Sonkin, Ekaterina Voloshina, Oleg Serikov, Ekaterina Artemova
conference: Arxiv
year: 2022
bibkey: atnashev2022razmecheno
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.09997'}]
tags: ["Datasets", "Evaluation"]
short_authors: Atnashev et al.
---
The vast majority of existing datasets for Named Entity Recognition (NER) are
built primarily on news, research papers and Wikipedia with a few exceptions,
created from historical and literary texts. What is more, English is the main
source for data for further labelling. This paper aims to fill in multiple gaps
by creating a novel dataset "Razmecheno", gathered from the diary texts of the
project "Prozhito" in Russian. Our dataset is of interest for multiple research
lines: literary studies of diary texts, transfer learning from other domains,
low-resource or cross-lingual named entity recognition. Razmecheno comprises
1331 sentences and 14119 tokens, sampled from diaries, written during the
Perestroika. The annotation schema consists of five commonly used entity tags:
person, characteristics, location, organisation, and facility. The labelling is
carried out on the crowdsourcing platfrom Yandex.Toloka in two stages. First,
workers selected sentences, which contain an entity of particular type. Second,
they marked up entity spans. As a result 1113 entities were obtained. Empirical
evaluation of Razmecheno is carried out with off-the-shelf NER tools and by
fine-tuning pre-trained contextualized encoders. We release the annotated
dataset for open access.