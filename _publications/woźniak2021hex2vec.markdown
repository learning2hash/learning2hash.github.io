---
layout: publication
title: Hex2vec -- Context-aware Embedding H3 Hexagons With Openstreetmap Tags
authors: "Szymon Wo\u017Aniak, Piotr Szyma\u0144ski"
conference: 'SIGSPATIAL ''21: 29th International Conference on Advances in Geographic
  Information Systems'
year: 2021
bibkey: "wo\u017Aniak2021hex2vec"
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.00970'}]
tags: ["Evaluation"]
short_authors: "Szymon Wo\u017Aniak, Piotr Szyma\u0144ski"
---
Representation learning of spatial and geographic data is a rapidly
developing field which allows for similarity detection between areas and
high-quality inference using deep neural networks. Past approaches however
concentrated on embedding raster imagery (maps, street or satellite photos),
mobility data or road networks. In this paper we propose the first approach to
learning vector representations of OpenStreetMap regions with respect to urban
functions and land-use in a micro-region grid. We identify a subset of OSM tags
related to major characteristics of land-use, building and urban region
functions, types of water, green or other natural areas. Through manual
verification of tagging quality, we selected 36 cities were for training region
representations. Uber's H3 index was used to divide the cities into hexagons,
and OSM tags were aggregated for each hexagon. We propose the hex2vec method
based on the Skip-gram model with negative sampling. The resulting vector
representations showcase semantic structures of the map characteristics,
similar to ones found in vector-based language models. We also present insights
from region similarity detection in six Polish cities and propose a region
typology obtained through agglomerative clustering.