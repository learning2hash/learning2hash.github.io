---
layout: publication
title: Approximate Query Matching for Image Retrieval
authors: Suprem Abhijit, Chau Polo
conference: "Arxiv"
year: 2018
bibkey: suprem2018approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1803.05401"}
tags: ['ARXIV', 'Graph', 'Image Retrieval']
---
Traditional image recognition involves identifying the key object in a portrait-type image with a single object focus (ILSVRC AlexNet and VGG). More recent approaches consider dense image recognition - segmenting an image with appropriate bounding boxes and performing image recognition within these bounding boxes (Semantic segmentation). The Visual Genome dataset 5 is an attempt to bridge these various approaches to a cohesive dataset for each subtask - bounding box generation image recognition captioning and a new operation scene graph generation. Our focus is on using such scene graphs to perform graph search on image databases to holistically retrieve images based on a search criteria. We develop a method to store scene graphs and metadata in graph databases (using Neo4J) and to perform fast approximate retrieval of images based on a graph search query. We process more complex queries than single object search e.g. girl eating cake retrieves images that contain the specified relation as well as variations.
