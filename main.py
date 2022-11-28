#!/usr/bin/env python
import io
from bs4 import BeautifulSoup
import requests

with io.open('lpc1-plan.svg', encoding='utf-8') as svg:
    plan = BeautifulSoup(svg, 'html.parser')

allRects = []
allRects = plan.findAll('rect')


for rect in allRects:
    print(rect)