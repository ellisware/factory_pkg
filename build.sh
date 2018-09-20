#!/bin/sh
echo $TRAVIS_BUILD_DIR/$TEST_DIR
cd $TRAVIS_BUILD_DIR/$TEST_DIR
ls
python test.py