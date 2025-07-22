---
layout: publication
title: Graph-based Non-linear Least Squares Optimization For Visual Place Recognition
  In Changing Environments
authors: Schubert Stefan, Neubert Peer, Protzel Peter
conference: IEEE Robotics and Automation Letters
year: 2021
bibkey: schubert2020graph
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.14766'}]
tags: ["Graph-Based-Ann", "Image-Retrieval", "Tools-&-Libraries", "Datasets", "Evaluation"]
short_authors: Schubert Stefan, Neubert Peer, Protzel Peter
---
Visual place recognition is an important subproblem of mobile robot
localization. Since it is a special case of image retrieval, the basic source
of information is the pairwise similarity of image descriptors. However, the
embedding of the image retrieval problem in this robotic task provides
additional structure that can be exploited, e.g. spatio-temporal consistency.
Several algorithms exist to exploit this structure, e.g., sequence processing
approaches or descriptor standardization approaches for changing environments.
In this paper, we propose a graph-based framework to systematically exploit
different types of additional structure and information. The graphical model is
used to formulate a non-linear least squares problem that can be optimized with
standard tools. Beyond sequences and standardization, we propose the usage of
intra-set similarities within the database and/or the query image set as
additional source of information. If available, our approach also allows to
seamlessly integrate additional knowledge about poses of database images. We
evaluate the system on a variety of standard place recognition datasets and
demonstrate performance improvements for a large number of different
configurations including different sources of information, different types of
constraints, and online or offline place recognition setups.