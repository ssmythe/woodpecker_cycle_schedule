#!/usr/bin/env python3

from datetime import datetime, timedelta
import random


def generate_spaced_repetition_schedule(start_date, total_problems):
    # Convert start_date from string to datetime object
    current_date = datetime.strptime(start_date, '%Y-%m-%d')

    # Define spaced repetition intervals (in days)
    intervals = [1, 3, 7, 14, 28]  # Customize based on learning goals

    problems_list = list(range(1, total_problems + 1))
    random.shuffle(problems_list)  # Shuffle the problems for the initial cycle

    # Initialize schedule dictionary
    schedule = {}

    # Schedule each problem according to spaced repetition intervals
    for i, problem in enumerate(problems_list):
        for interval in intervals:
            review_date = current_date + timedelta(days=i + interval)
            if review_date not in schedule:
                schedule[review_date] = [problem]
            else:
                schedule[review_date].append(problem)

    # Convert schedule dictionary to a sorted list of tuples
    sorted_schedule = sorted(schedule.items())

    return sorted_schedule


# Example usage:
start_date = "2024-04-07"
total_problems = 306

schedule = generate_spaced_repetition_schedule(start_date, total_problems)

# Print the schedule
print("Date       | Problems")
for review_date, problems in schedule:
    problems_str = ', '.join(map(str, problems))
    print(f"{review_date.strftime('%Y-%m-%d')} | {problems_str}")
