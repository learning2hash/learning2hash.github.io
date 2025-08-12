---
layout: publication
title: 'Deart: Dataset Of European Art'
authors: Artem Reshetnikov, Maria-cristina Marinescu, Joaquim More Lopez
conference: Lecture Notes in Computer Science
year: 2023
bibkey: reshetnikov2022deart
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.01226'}]
tags: ["Datasets"]
short_authors: Artem Reshetnikov, Maria-cristina Marinescu, Joaquim More Lopez
---
Large datasets that were made publicly available to the research community
over the last 20 years have been a key enabling factor for the advances in deep
learning algorithms for NLP or computer vision. These datasets are generally
pairs of aligned image / manually annotated metadata, where images are
photographs of everyday life. Scholarly and historical content, on the other
hand, treat subjects that are not necessarily popular to a general audience,
they may not always contain a large number of data points, and new data may be
difficult or impossible to collect. Some exceptions do exist, for instance,
scientific or health data, but this is not the case for cultural heritage (CH).
The poor performance of the best models in computer vision - when tested over
artworks - coupled with the lack of extensively annotated datasets for CH, and
the fact that artwork images depict objects and actions not captured by
photographs, indicate that a CH-specific dataset would be highly valuable for
this community. We propose DEArt, at this point primarily an object detection
and pose classification dataset meant to be a reference for paintings between
the XIIth and the XVIIIth centuries. It contains more than 15000 images, about
80% non-iconic, aligned with manual annotations for the bounding boxes
identifying all instances of 69 classes as well as 12 possible poses for boxes
identifying human-like objects. Of these, more than 50 classes are CH-specific
and thus do not appear in other datasets; these reflect imaginary beings,
symbolic entities and other categories related to art. Additionally, existing
datasets do not include pose annotations. Our results show that object
detectors for the cultural heritage domain can achieve a level of precision
comparable to state-of-art models for generic images via transfer learning.