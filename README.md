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
