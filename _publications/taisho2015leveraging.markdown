---
layout: publication
title: "Leveraging Image based Prior for Visual Place Recognition"
authors: Taisho Tsukamoto, Kanji Tanaka
conference: Arxiv
year: 2015
bibkey: taisho2015leveraging
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1505.03205"}
tags: ['ARXIV']
---
In this study, we propose a novel scene descriptor for visual place recognition.
Unlike popular bag-of-words scene descriptors which rely on a library of vector
quantized visual features, our proposed descriptor is based on a library of raw
image data, such as publicly available photo collections from Google StreetView
and Flickr. The library images need not to be associated with spatial
information regarding the viewpoint and orientation of the scene. As a result,
these images are cheaper than the database images; in addition, they are readily
available. Our proposed descriptor directly mines the image library to discover
landmarks (i.e., image patches) that suitably match an input query/database
image. The discovered landmarks are then compactly described by their pose and
shape (i.e., library image ID, bounding boxes) and used as a compact
discriminative scene descriptor for the input image. We evaluate the
effectiveness of our scene description framework by comparing its performance to
that of previous approaches.
