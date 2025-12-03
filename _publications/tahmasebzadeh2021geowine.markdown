---
layout: publication
title: 'Geowine: Geolocation Based Wiki, Image,news And Event Retrieval'
authors: "Golsa Tahmasebzadeh, Endri Kacupaj, Eric M\xFCller-Budack, Sherzod Hakimov,\
  \ Jens Lehmann, Ralph Ewerth"
conference: 'SIGIR ''21: The 44th International ACM SIGIR Conference on Research and
  Development in Information Retrieval'
year: 2021
bibkey: tahmasebzadeh2021geowine
citations: 8
additional_links: [{name: Other, url: 'http://cleopatra.ijs.si/geowine/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2104.14994'}]
tags: ["Datasets", "Multimodal Retrieval", "SIGIR"]
short_authors: Tahmasebzadeh et al.
---
In the context of social media, geolocation inference on news or events has
become a very important task. In this paper, we present the GeoWINE
(Geolocation-based Wiki-Image-News-Event retrieval) demonstrator, an effective
modular system for multimodal retrieval which expects only a single image as
input. The GeoWINE system consists of five modules in order to retrieve related
information from various sources. The first module is a state-of-the-art model
for geolocation estimation of images. The second module performs a
geospatial-based query for entity retrieval using the Wikidata knowledge graph.
The third module exploits four different image embedding representations, which
are used to retrieve most similar entities compared to the input image. The
embeddings are derived from the tasks of geolocation estimation, place
recognition, ImageNet-based image classification, and their combination. The
last two modules perform news and event retrieval from EventRegistry and the
Open Event Knowledge Graph (OEKG). GeoWINE provides an intuitive interface for
end-users and is insightful for experts for reconfiguration to individual
setups. The GeoWINE achieves promising results in entity label prediction for
images on Google Landmarks dataset. The demonstrator is publicly available at
http://cleopatra.ijs.si/geowine/.