#!/bin/zsh

black src/*.py &&
git add ./src &&
git commit -m "update completed" &&
git push && clear