---
layout: publication
title: Short Text Classification Approach To Identify Child Sexual Exploitation Material
authors: "Mhd Wesam Al-nabki, Eduardo Fidalgo, Enrique Alegre, Roc\xEDo Alaiz-rodr\xED\
  guez"
conference: Scientific Reports
year: 2023
bibkey: alnabki2020short
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.01113'}]
tags: ["Evaluation", "Supervised"]
short_authors: Al-nabki et al.
---
Producing or sharing Child Sexual Exploitation Material (CSEM) is a serious
crime fought vigorously by Law Enforcement Agencies (LEAs). When an LEA seizes
a computer from a potential producer or consumer of CSEM, they need to analyze
the suspect's hard disk's files looking for pieces of evidence. However, a
manual inspection of the file content looking for CSEM is a time-consuming
task. In most cases, it is unfeasible in the amount of time available for the
Spanish police using a search warrant. Instead of analyzing its content,
another approach that can be used to speed up the process is to identify CSEM
by analyzing the file names and their absolute paths. The main challenge for
this task lies behind dealing with short text distorted deliberately by the
owners of this material using obfuscated words and user-defined naming
patterns. This paper presents and compares two approaches based on short text
classification to identify CSEM files. The first one employs two independent
supervised classifiers, one for the file name and the other for the path, and
their outputs are later on fused into a single score. Conversely, the second
approach uses only the file name classifier to iterate over the file's absolute
path. Both approaches operate at the character n-grams level, while binary and
orthographic features enrich the file name representation, and a binary
Logistic Regression model is used for classification. The presented file
classifier achieved an average class recall of 0.98. This solution could be
integrated into forensic tools and services to support Law Enforcement Agencies
to identify CSEM without tackling every file's visual content, which is
computationally much more highly demanding.