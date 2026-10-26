# Python Assignment 2: Object-Oriented Programming

**Name:** Tendai *(replace with your name)*
**Student number:** *(add yours)*
**Due:** 26 October 2026
**Language:** Python 3.8+ (no external libraries)

## Structure
| Question | Code | Written answers | Output |
|---|---|---|---|
| Q1: UniCash Wallet | [`q1_wallet/`](q1_wallet) | [`answers/Q1.md`](answers/Q1.md) | [`outputs/`](outputs) |
| Q2 | *not included in the PDF I received* | | |
| Q3: Exam alert channels | [`q3_channels/`](q3_channels) | [`answers/Q3.md`](answers/Q3.md) | [`outputs/`](outputs) |
| Q4: Connection leak | [`q4_connections/`](q4_connections) | [`answers/Q4.md`](answers/Q4.md) | [`outputs/`](outputs) |
| Q5: Diamond problem | [`q5_diamond/`](q5_diamond) | [`answers/Q5.md`](answers/Q5.md) | [`outputs/`](outputs) |

## Values used for the placeholders
`NAME = "Tendai"`, `BAL = 500`, `LIMIT = 300`, `MAXCONN = 3` (explained in Q4). Change `NAME` at the top of each file.

## How to run
```bash
./run_all.sh                          # runs everything, saves results to outputs/
# or individually:
cd q1_wallet && python3 test_wallet.py
cd q3_channels && python3 main.py && python3 main_with_push.py
cd q4_connections && python3 leaky.py && python3 fixed.py && python3 people.py
cd q5_diamond && python3 diamond.py && python3 composition.py
```
