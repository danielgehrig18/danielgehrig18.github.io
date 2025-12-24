---
title: "Exploring Event Camera-based Odometry for Planetary Robots"
authors:
- Florian Mahlknecht
- Daniel Gehrig
- Jeremy Nash
- Friedrich M. Rockenbauer
- Benjamin Morrell
- Jeff Delaune 
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-07-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication:  "IEEE Robot. Autom. Lett. (RA-L)"
publication_short: ""

abstract: "Due to their resilience to motion blur and high robustness in low-light and high dynamic range conditions, event cameras are poised to become enabling sensors for visionbased exploration on future Mars helicopter missions. However, existing event-based visual-inertial odometry (VIO) algorithms either suffer from high tracking errors or are brittle, since they cannot cope with significant depth uncertainties caused by an unforeseen loss of tracking or other effects. In this work, we introduce EKLT-VIO, which addresses both limitations by combining a state-of-the-art event-based frontend with a filter-based backend. This makes it both accurate and robust to uncertainties, outperforming event- and frame-based VIO algorithms on challenging benchmarks by 32%. In addition, we demonstrate accurate performance in hover-like conditions (outperforming existing event-based methods) as well as high robustness in newly collected Mars-like and high-dynamic-range sequences, where existing frame-based methods fail. In doing so, we show that event-based VIO is the way forward for visionbased exploration on Mars."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/RAL22_Mahlknecht.pdf
url_code: 'https://uzh-rpg.github.io/eklt-vio/'
url_dataset: 'https://uzh-rpg.github.io/eklt-vio/'
url_poster: ''
url_project: 'https://uzh-rpg.github.io/eklt-vio/'
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/KahAhSxC9_8'

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

