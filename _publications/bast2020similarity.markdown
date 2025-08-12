---
layout: publication
title: Similarity Classification Of Public Transit Stations
authors: "Hannah Bast, Patrick Brosi, Markus N\xE4ther"
conference: Arxiv
year: 2020
bibkey: bast2020similarity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.15267'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Hannah Bast, Patrick Brosi, Markus N\xE4ther"
---
We study the following problem: given two public transit station identifiers
A and B, each with a label and a geographic coordinate, decide whether A and B
describe the same station. For example, for "St Pancras International" at
(51.5306, -0.1253) and "London St Pancras" at (51.5319, -0.1269), the answer
would be "Yes". This problem frequently arises in areas where public transit
data is used, for example in geographic information systems, schedule merging,
route planning, or map matching. We consider several baseline methods based on
geographic distance and simple string similarity measures. We also experiment
with more elaborate string similarity measures and manually created
normalization rules. Our experiments show that these baseline methods produce
good, but not fully satisfactory results. We therefore develop an approach
based on a random forest classifier which is trained on matching trigrams
between two stations, their distance, and their position on an interwoven grid.
All approaches are evaluated on extensive ground truth datasets we generated
from OpenStreetMap (OSM) data: (1) The union of Great Britain and Ireland and
(2) the union of Germany, Switzerland, and Austria. On all datasets, our
learning-based approach achieves an F1 score of over 99%, while even the most
elaborate baseline approach (based on TFIDF scores and the geographic distance)
achieves an F1 score of at most 94%, and a naive approach of using a
geographical distance threshold achieves an F1 score of only 75%. Both our
training and testing datasets are publicly available.