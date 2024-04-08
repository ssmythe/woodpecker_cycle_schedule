# Woodpecker Method Study Schedule

This program generates a study schedule based on the Woodpecker Method, a popular technique for studying chess problems. The method involves repetitive solving of a set of problems, increasing the number of problems solved each cycle until all problems are tackled in a single day.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [License](#license)

## Introduction

The Woodpecker Method is a systematic approach to studying chess problems. The idea is to solve a set of problems in cycles, where the number of problems solved each day increases with each cycle. The ultimate goal is to solve all the problems in a single day by the end of the cycles.

## Usage

1. Set the following variables in the script:
   - `start_date`: The date you want to start your study schedule (format: 'YYYY-MM-DD').
   - `start_problems_per_day`: The number of problems you want to start with on the first day.
   - `total_problems`: The total number of problems you want to study.

2. Run the script.

3. The program will output a table showing the study schedule, including the date, cycle number, number of problems to solve that day, and the day of the cycle.

## How It Works

1. The program starts with the given `start_problems_per_day` and calculates how many days it will take to solve all `total_problems` at that rate.
2. For the next cycle, the number of problems solved each day is doubled, and the program calculates the number of days for this cycle.
3. This process continues, doubling the number of problems each cycle, until all problems are solved in a single day.
4. The program then outputs a table with the study schedule, showing each day, the cycle number, the number of problems to solve, and the day of the cycle.

## Example

For a starting date of "2023-10-25", starting with 6 problems per day, and a total of 306 problems, the program might output:

```text
Date       | Cycle | Problems Per Day | Day of Cycle
-----------|-------|------------------|-------------
2023-10-25 | 1     | 6                | 1
...
2024-02-05 | 7     | 306              | 1
```

## Randomized version (wpcsr.py)

Randomizing the problem set helps prevent the learner from associating the solution of one problem with its position in a sequence, fostering deeper understanding and retention. This technique leverages the cognitive benefits of varied practice, where encountering problems in a non-fixed order encourages the brain to form more robust neural pathways and apply concepts flexibly. It counters the risk of rote memorization, prompting learners to engage with the underlying principles of each problem rather than relying on pattern recognition based on sequence. Consequently, this approach enhances problem-solving skills, promotes adaptive learning, and improves the ability to transfer knowledge to new, unfamiliar contexts.

## Spaced Repetition version (srs.py)

The spaced repetition method is a learning technique that strategically increases the time intervals between reviews of previously learned material. This approach is grounded in the psychological spacing effect, which suggests that information is more effectively remembered and internalized when study sessions are spaced out over time, rather than when massed together in a short period.

By reintroducing concepts and problems at gradually increasing intervals—often starting with a day, then expanding to several days, and eventually weeks—the learner's memory is optimally challenged just as it begins to fade. This timing encourages deeper cognitive processing and reinforces memory retention, making the material more resistant to being forgotten.

The benefits of spaced repetition include enhanced long-term retention of information, improved recall speed, and a more efficient use of study time. It is particularly effective for cumulative subjects and skills development, where foundational knowledge needs to be solidified to support more advanced learning. This method adapts well to individual learning paces and can be tailored based on personal performance, making it a versatile tool for both academic study and lifelong learning.