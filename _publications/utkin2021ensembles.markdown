---
layout: publication
title: Ensembles Of Random Shaps
authors: Lev V. Utkin, Andrei V. Konstantinov
conference: Algorithms
year: 2022
bibkey: utkin2021ensembles
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.03302'}]
tags: ["Efficiency"]
short_authors: Lev V. Utkin, Andrei V. Konstantinov
---
Ensemble-based modifications of the well-known SHapley Additive exPlanations
(SHAP) method for the local explanation of a black-box model are proposed. The
modifications aim to simplify SHAP which is computationally expensive when
there is a large number of features. The main idea behind the proposed
modifications is to approximate SHAP by an ensemble of SHAPs with a smaller
number of features. According to the first modification, called ER-SHAP,
several features are randomly selected many times from the feature set, and
Shapley values for the features are computed by means of "small" SHAPs. The
explanation results are averaged to get the final Shapley values. According to
the second modification, called ERW-SHAP, several points are generated around
the explained instance for diversity purposes, and results of their explanation
are combined with weights depending on distances between points and the
explained instance. The third modification, called ER-SHAP-RF, uses the random
forest for preliminary explanation of instances and determining a feature
probability distribution which is applied to selection of features in the
ensemble-based procedure of ER-SHAP. Many numerical experiments illustrating
the proposed modifications demonstrate their efficiency and properties for
local explanation.