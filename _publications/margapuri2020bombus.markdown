---
layout: publication
title: Bombus Species Image Classification
authors: Venkat Margapuri, George Lavezzi, Robert Stewart, Dan Wagner
conference: Arxiv
year: 2020
bibkey: margapuri2020bombus
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11374'}]
tags: ["Evaluation"]
short_authors: Margapuri et al.
---
Entomologists, ecologists and others struggle to rapidly and accurately
identify the species of bumble bees they encounter in their field work and
research. The current process requires the bees to be mounted, then physically
shipped to a taxonomic expert for proper categorization. We investigated
whether an image classification system derived from transfer learning can do
this task. We used Google Inception, Oxford VGG16 and VGG19 and Microsoft
ResNet 50. We found Inception and VGG classifiers were able to make some
progress at identifying bumble bee species from the available data, whereas
ResNet was not. Individual classifiers achieved accuracies of up to 23% for
single species identification and 44% top-3 labels, where a composite model
performed better, 27% and 50%. We feel the performance was most hampered by our
limited data set of 5,000-plus labeled images of 29 species, with individual
species represented by 59 -315 images.