#!/usr/bin/env bash
# Runs every program and saves the output in outputs/
set -e
cd "$(dirname "$0")"
mkdir -p outputs
(cd q1_wallet      && python3 test_wallet.py)        | tee outputs/q1_test_wallet.txt
(cd q3_channels    && python3 main.py)               | tee outputs/q3_main.txt
(cd q3_channels    && python3 main_with_push.py)     | tee outputs/q3_main_with_push.txt
(cd q4_connections && python3 leaky.py)              | tee outputs/q4_leaky.txt
(cd q4_connections && python3 fixed.py)              | tee outputs/q4_fixed.txt
(cd q4_connections && python3 people.py)             | tee outputs/q4_people.txt
(cd q5_diamond     && python3 diamond.py)            | tee outputs/q5_diamond.txt
(cd q5_diamond     && python3 composition.py)        | tee outputs/q5_composition.txt
