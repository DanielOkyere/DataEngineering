#!/bin/zsh

black src/*.py &&
git add . &&
git commit -m "update completed" &&
git push && clear