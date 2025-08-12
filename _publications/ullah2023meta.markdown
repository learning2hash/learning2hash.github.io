---
layout: publication
title: 'Meta-album: Multi-domain Meta-dataset For Few-shot Image Classification'
authors: "Ihsan Ullah, Dustin Carri\xF3n-Ojeda, Sergio Escalera, Isabelle Guyon, Mike\
  \ Huisman, Felix Mohr, Jan N van Rijn, Haozhe Sun, Joaquin Vanschoren, Phan Anh\
  \ Vu"
conference: 36th Conference on Neural Information Processing Systems (NeurIPS 2022)
  Track on Datasets and Benchmarks. NeurIPS Nov 2022 New Orleans United States
year: 2023
bibkey: ullah2023meta
citations: 7
additional_links: [{name: Code, url: 'https://meta-album.github.io/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2302.08909'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "NEURIPS"]
short_authors: Ullah et al.
---
We introduce Meta-Album, an image classification meta-dataset designed to
facilitate few-shot learning, transfer learning, meta-learning, among other
tasks. It includes 40 open datasets, each having at least 20 classes with 40
examples per class, with verified licences. They stem from diverse domains,
such as ecology (fauna and flora), manufacturing (textures, vehicles), human
actions, and optical character recognition, featuring various image scales
(microscopic, human scales, remote sensing). All datasets are preprocessed,
annotated, and formatted uniformly, and come in 3 versions (Micro \(\subset\)
Mini \(\subset\) Extended) to match users' computational resources. We showcase
the utility of the first 30 datasets on few-shot learning problems. The other
10 will be released shortly after. Meta-Album is already more diverse and
larger (in number of datasets) than similar efforts, and we are committed to
keep enlarging it via a series of competitions. As competitions terminate,
their test data are released, thus creating a rolling benchmark, available
through OpenML.org. Our website https://meta-album.github.io/ contains the
source code of challenge winning methods, baseline methods, data loaders, and
instructions for contributing either new datasets or algorithms to our
expandable meta-dataset.