# berkeley-stat-157

Homepage for STAT 157 at UC Berkeley

## How to build

- Local build: `bash build/build.sh`, all HTMLs will be in the folder `build/_build/html`
- CI is enabled:
  [![Status](http://ci.diveintodeeplearning.org/job/berkeley-stat-157/job/master/badge/icon)](http://ci.diveintodeeplearning.org/job/berkeley-stat-157/job/master/). Every
  commit into the master branch will be pushed into the website automatically.


## How to use it for your own class

1. Fork this repo
2. Edit the markdowns files
3. Edit the `build/conf.py` for meta data
4. Build it through `bash build/build.sh`
5. Upload HTML to a place
