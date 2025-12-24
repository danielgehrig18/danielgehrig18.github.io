---
title: "Neural Inertial Odometry from Lie Events"
authors:
- Royina Karegoudra ayanth,
- Yinshuang Xu
- Evangelos Chatzipantazis
- Kostas Daniilidis
- Daniel Gehrig
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2025-03-20T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*Robotics: Science and Systems (RSS)*"
publication_short: ""

abstract: "Neural displacement priors (NDP) can reduce the drift in inertial odometry and provide uncertainty estimates that can be readily fused with off-the-shelf filters. However, they fail to generalize to different IMU sampling rates and trajectory profiles, which limits their robustness in diverse settings. To address this challenge, we replace the traditional NDP inputs comprising raw IMU data with Lie events that are robust to input rate changes and have favorable invariances when observed under different trajectory profiles. Unlike raw IMU data sampled at fixed rates, Lie events are sampled whenever the norm of the IMU pre-integration change, mapped to the Lie algebra of the SE(3) group, exceeds a threshold. Inspired by event-based vision, we generalize the notion of level-crossing on 1D signals to level-crossings on the Lie algebra and generalize binary polarities to normalized Lie polarities within this algebra. We show that training NDPs on Lie events incorporating these polarities reduces the trajectory error of off-the-shelf downstream inertial odometry methods by up to 21% with only minimal preprocessing. We conjecture that many more sensors than IMUs or cameras can benefit from an event-based sampling paradigm and that this work makes an important first step in this direction."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://www.roboticsproceedings.org/rss21/p143.pdf
url_code: 'https://github.com/RoyinaJayanth/NIO_Lie_Events'
url_dataset: ''
url_poster: ''
url_project: 'https://www.roboticsproceedings.org/rss21/p143.html'
url_slides: ''
url_source: ''
url_video: ''

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
{{% callout note %}}
This work extended event-based sampling to IMU-based navigation opening the door to new event-based sensing paradigms!
{{% /callout %}}

