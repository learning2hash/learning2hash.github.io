---
layout: publication
title: Estimating People Flows To Better Count Them In Crowded Scenes
authors: Weizhe Liu, Mathieu Salzmann, Pascal Fua
conference: Lecture Notes in Computer Science
year: 2020
bibkey: liu2019estimating
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.10782'}]
tags: ["Datasets", "Evaluation"]
short_authors: Weizhe Liu, Mathieu Salzmann, Pascal Fua
---
Modern methods for counting people in crowded scenes rely on deep networks to
estimate people densities in individual images. As such, only very few take
advantage of temporal consistency in video sequences, and those that do only
impose weak smoothness constraints across consecutive frames.
  In this paper, we advocate estimating people flows across image locations
between consecutive images and inferring the people densities from these flows
instead of directly regressing. This enables us to impose much stronger
constraints encoding the conservation of the number of people. As a result, it
significantly boosts performance without requiring a more complex architecture.
Furthermore, it also enables us to exploit the correlation between people flow
and optical flow to further improve the results.
  We will demonstrate that we consistently outperform state-of-the-art methods
on five benchmark datasets.