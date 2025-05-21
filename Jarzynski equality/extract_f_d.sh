#!/bin/bash

for i in {1..10}
do
	awk 'NR >= 27' pullf$i.xvg > output_f$i.csv
	awk 'NR >= 27' pullx$i.xvg > output_d$i.csv
done
