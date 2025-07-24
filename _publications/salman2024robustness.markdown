---
layout: publication
title: On The Robustness Of Malware Detectors To Adversarial Samples
authors: Muhammad Salman, Benjamin Zi Hao Zhao, Hassan Jameel Asghar, Muhammad Ikram,
  Sidharth Kaushik, Mohamed Ali Kaafar
conference: Lecture Notes in Computer Science
year: 2025
bibkey: salman2024robustness
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.02310'}]
tags: ["Hashing Methods", "Locality Sensitive Hashing", "Robustness"]
short_authors: Salman et al.
---
Adversarial examples add imperceptible alterations to inputs with the
objective to induce misclassification in machine learning models. They have
been demonstrated to pose significant challenges in domains like image
classification, with results showing that an adversarially perturbed image to
evade detection against one classifier is most likely transferable to other
classifiers. Adversarial examples have also been studied in malware analysis.
Unlike images, program binaries cannot be arbitrarily perturbed without
rendering them non-functional. Due to the difficulty of crafting adversarial
program binaries, there is no consensus on the transferability of adversarially
perturbed programs to different detectors. In this work, we explore the
robustness of malware detectors against adversarially perturbed malware. We
investigate the transferability of adversarial attacks developed against one
detector, against other machine learning-based malware detectors, and code
similarity techniques, specifically, locality sensitive hashing-based
detectors. Our analysis reveals that adversarial program binaries crafted for
one detector are generally less effective against others. We also evaluate an
ensemble of detectors and show that they can potentially mitigate the impact of
adversarial program binaries. Finally, we demonstrate that substantial program
changes made to evade detection may result in the transformation technique
being identified, implying that the adversary must make minimal changes to the
program binary.