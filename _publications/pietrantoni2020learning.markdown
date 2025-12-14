---
layout: publication
title: Learning Synthetic To Real Transfer For Localization And Navigational Tasks
authors: Maxime Pietrantoni, Boris Chidlovskii, Tomi Silander
conference: Arxiv
year: 2020
bibkey: pietrantoni2020learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.10274'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Maxime Pietrantoni, Boris Chidlovskii, Tomi Silander
---
Autonomous navigation consists in an agent being able to navigate without
human intervention or supervision, it affects both high level planning and low
level control. Navigation is at the crossroad of multiple disciplines, it
combines notions of computer vision, robotics and control. This work aimed at
creating, in a simulation, a navigation pipeline whose transfer to the real
world could be done with as few efforts as possible. Given the limited time and
the wide range of problematic to be tackled, absolute navigation performances
while important was not the main objective. The emphasis was rather put on
studying the sim2real gap which is one the major bottlenecks of modern robotics
and autonomous navigation. To design the navigation pipeline four main
challenges arise; environment, localization, navigation and planning. The
iGibson simulator is picked for its photo-realistic textures and physics
engine. A topological approach to tackle space representation was picked over
metric approaches because they generalize better to new environments and are
less sensitive to change of conditions. The navigation pipeline is decomposed
as a localization module, a planning module and a local navigation module.
These modules utilize three different networks, an image representation
extractor, a passage detector and a local policy. The laters are trained on
specifically tailored tasks with some associated datasets created for those
specific tasks. Localization is the ability for the agent to localize itself
against a specific space representation. It must be reliable, repeatable and
robust to a wide variety of transformations. Localization is tackled as an
image retrieval task using a deep neural network trained on an auxiliary task
as a feature descriptor extractor. The local policy is trained with behavioral
cloning from expert trajectories gathered with ROS navigation stack.