---
layout: publication
title: 'EUFCC-340K: A Faceted Hierarchical Dataset For Metadata Annotation In GLAM
  Collections'
authors: Francesc Net, Marc Folia, Pep Casals, Andrew D. Bagdanov, Lluis Gomez
conference: Multimedia Tools and Applications
year: 2025
bibkey: net2024eufcc
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.02380'}]
tags: ["Datasets"]
short_authors: Net et al.
---
In this paper, we address the challenges of automatic metadata annotation in
the domain of Galleries, Libraries, Archives, and Museums (GLAMs) by
introducing a novel dataset, EUFCC340K, collected from the Europeana portal.
Comprising over 340,000 images, the EUFCC340K dataset is organized across
multiple facets: Materials, Object Types, Disciplines, and Subjects, following
a hierarchical structure based on the Art & Architecture Thesaurus (AAT). We
developed several baseline models, incorporating multiple heads on a ConvNeXT
backbone for multi-label image tagging on these facets, and fine-tuning a CLIP
model with our image text pairs. Our experiments to evaluate model robustness
and generalization capabilities in two different test scenarios demonstrate the
utility of the dataset in improving multi-label classification tools that have
the potential to alleviate cataloging tasks in the cultural heritage sector.