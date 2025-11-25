---
layout: publication
title: 'Von Mises-fisher Loss: An Exploration Of Embedding Geometries For Supervised
  Learning'
authors: Tyler R. Scott, Andrew C. Gallagher, Michael C. Mozer
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: scott2021von
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.15718'}]
tags: ["ICCV", "Image Retrieval", "Supervised"]
short_authors: Tyler R. Scott, Andrew C. Gallagher, Michael C. Mozer
---
Recent work has argued that classification losses utilizing softmax
cross-entropy are superior not only for fixed-set classification tasks, but
also by outperforming losses developed specifically for open-set tasks
including few-shot learning and retrieval. Softmax classifiers have been
studied using different embedding geometries -- Euclidean, hyperbolic, and
spherical -- and claims have been made about the superiority of one or another,
but they have not been systematically compared with careful controls. We
conduct an empirical investigation of embedding geometry on softmax losses for
a variety of fixed-set classification and image retrieval tasks. An interesting
property observed for the spherical losses lead us to propose a probabilistic
classifier based on the von Mises-Fisher distribution, and we show that it is
competitive with state-of-the-art methods while producing improved
out-of-the-box calibration. We provide guidance regarding the trade-offs
between losses and how to choose among them.