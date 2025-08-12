---
layout: publication
title: Trajectory-user Linking Is Easier Than You Think
authors: Alameen Najjar, Kyle Mede
conference: 2022 IEEE International Conference on Big Data (Big Data)
year: 2022
bibkey: najjar2022trajectory
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.07081'}]
tags: []
short_authors: Alameen Najjar, Kyle Mede
---
Trajectory-User Linking (TUL) is a relatively new mobility classification
task in which anonymous trajectories are linked to the users who generated
them. With applications ranging from personalized recommendations to criminal
activity detection, TUL has received increasing attention over the past five
years. While research has focused mainly on learning deep representations that
capture complex spatio-temporal mobility patterns unique to individual users,
we demonstrate that visit patterns are highly unique among users and thus
simple heuristics applied directly to the raw data are sufficient to solve TUL.
More specifically, we demonstrate that a single check-in per trajectory is
enough to correctly predict the identity of the user up to 85% of the time.
Moreover, by using a non-parametric classifier, we scale up TUL to over 100k
users which is an increase over state-of-the-art by three orders of magnitude.
Extensive empirical analysis on four real-world datasets (Brightkite,
Foursquare, Gowalla and Weeplaces) compares our findings to state-of-the-art
results, and more importantly validates our claim that TUL is easier than
commonly believed.