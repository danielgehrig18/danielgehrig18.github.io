---
title: "Are High-Resolution Event Cameras Really Needed?"
authors:
- Daniel Gehrig
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-03-28T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication:  "*arXiv*"
publication_short: ""

abstract: "Due to their outstanding properties in challenging conditions, event cameras have become indispensable in a wide range of applications, ranging from automotive, computational photography, and SLAM. However, as further improvements are made to the sensor design, modern event cameras are trending toward higher and higher sensor resolutions, which result in higher bandwidth and computational requirements on downstream tasks. Despite this trend, the benefits of using high-resolution event cameras to solve standard computer vision tasks are still not clear. In this work, we report the surprising discovery that, in low-illumination conditions and at high speeds, low-resolution cameras can outperform high-resolution ones, while requiring a significantly lower bandwidth. We provide both empirical and theoretical evidence for this claim, which indicates that high-resolution event cameras exhibit higher per-pixel event rates, leading to higher temporal noise in low-illumination conditions and at high speeds. As a result, in most cases, high-resolution event cameras show a lower task performance, compared to lower resolution sensors in these conditions. We empirically validate our findings across several tasks, namely image reconstruction, optical flow estimation, and camera pose tracking, both on synthetic and real data. We believe that these findings will provide important guidelines for future trends in event camera development."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/arxiv22_Gehrig.pdf
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'https://uzh-rpg.github.io/eres/'
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/HV9_FhS-f88'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
