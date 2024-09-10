---
layout: publication
title: Region-Based Image Retrieval Revisited
authors: Hinami Ryota, Matsui Yusuke, Satoh Shin'ichi
conference: "Arxiv"
year: 2017
bibkey: hinami2017region
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1709.09106"}
tags: ['ARXIV', 'CNN', 'Deep Learning', 'Image Retrieval', 'TIP']
---
Region-based image retrieval (RBIR) technique is revisited. In early attempts at RBIR in the late 90s researchers found many ways to specify region-based queries and spatial relationships; however the way to characterize the regions such as by using color histograms were very poor at that time. Here we revisit RBIR by incorporating semantic specification of objects and intuitive specification of spatial relationships. Our contributions are the following. First to support multiple aspects of semantic object specification (category instance and attribute) we propose a multitask CNN feature that allows us to use deep learning technique and to jointly handle multi-aspect object specification. Second to help users specify spatial relationships among objects in an intuitive way we propose recommendation techniques of spatial relationships. In particular by mining the search results a system can recommend feasible spatial relationships among the objects. The system also can recommend likely spatial relationships by assigned object category names based on language prior. Moreover object-level inverted indexing supports very fast shortlist generation and re-ranking based on spatial constraints provides users with instant RBIR experiences.
