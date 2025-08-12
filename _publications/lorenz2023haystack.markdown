---
layout: publication
title: 'Haystack: A Panoptic Scene Graph Dataset To Evaluate Rare Predicate Classes'
authors: Julian Lorenz, Florian Barthel, Daniel Kienzle, Rainer Lienhart
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: lorenz2023haystack
citations: 3
additional_links: [{name: Code, url: 'https://lorjul.github.io/haystack/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.02286'}]
tags: ["Datasets", "Evaluation", "ICCV"]
short_authors: Lorenz et al.
---
Current scene graph datasets suffer from strong long-tail distributions of
their predicate classes. Due to a very low number of some predicate classes in
the test sets, no reliable metrics can be retrieved for the rarest classes. We
construct a new panoptic scene graph dataset and a set of metrics that are
designed as a benchmark for the predictive performance especially on rare
predicate classes. To construct the new dataset, we propose a model-assisted
annotation pipeline that efficiently finds rare predicate classes that are
hidden in a large set of images like needles in a haystack.
  Contrary to prior scene graph datasets, Haystack contains explicit negative
annotations, i.e. annotations that a given relation does not have a certain
predicate class. Negative annotations are helpful especially in the field of
scene graph generation and open up a whole new set of possibilities to improve
current scene graph generation models.
  Haystack is 100% compatible with existing panoptic scene graph datasets and
can easily be integrated with existing evaluation pipelines. Our dataset and
code can be found here: https://lorjul.github.io/haystack/. It includes
annotation files and simple to use scripts and utilities, to help with
integrating our dataset in existing work.