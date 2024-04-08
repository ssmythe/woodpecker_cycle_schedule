#!/usr/bin/env python3

from datetime import datetime, timedelta
import random
import textwrap


def generate_schedule(start_date, start_problems_per_day, total_problems):
    # Convert start_date from string to datetime object
    current_date = datetime.strptime(start_date, '%Y-%m-%d')

    # Initialize variables
    problems_per_day = start_problems_per_day
    calendar = []
    cycle_number = 1
    prev_problems_per_day = 0

    while problems_per_day < total_problems:
        # Ceiling division
        days_for_cycle = -(-total_problems // problems_per_day)
        problems_list = list(range(1, total_problems + 1))
        # Shuffle the problems for the current cycle
        random.shuffle(problems_list)
        problem_index = 0

        for day in range(1, days_for_cycle + 1):
            day_problems = problems_list[problem_index:
                                         problem_index + problems_per_day]
            day_problems = day_problems[:min(
                len(day_problems), total_problems - problem_index)]

            if prev_problems_per_day != problems_per_day and day == 1:
                calendar.append(
                    ("----------", "-----", "-----------------", "------------", "----------------------------------------------------------------"))
            problems_str = ', '.join(map(str, day_problems))

            initial_space = ' | '.join(
                [" " * width for width in [10, 5, 17, 12]]) + " | "
            max_width = 120 - len(initial_space)
            wrapped_problems = textwrap.wrap(problems_str, width=max_width)

            # Fix: Correctly handling the addition of wrapped lines to the calendar
            for i, problem_line in enumerate(wrapped_problems):
                if i == 0:
                    calendar.append((current_date.strftime(
                        '%Y-%m-%d'), str(cycle_number), str(problems_per_day), str(day), problem_line))
                else:
                    # Adding spaces only to the problem column for wrapped lines
                    calendar.append(("", "", "", "", problem_line))

            current_date += timedelta(days=1)
            problem_index += len(day_problems)

        prev_problems_per_day = problems_per_day
        problems_per_day *= 2
        cycle_number += 1

    # Final day processing
    calendar.append(
        ("----------", "-----", "-----------------", "------------", "----------------------------------------------------------------"))
    final_day_problems = list(range(1, total_problems + 1))
    random.shuffle(final_day_problems)
    final_problems_str = ', '.join(map(str, final_day_problems))
    wrapped_final_problems = textwrap.wrap(final_problems_str, width=max_width)
    for i, problem_line in enumerate(wrapped_final_problems):
        if i == 0:
            calendar.append((current_date.strftime(
                '%Y-%m-%d'), str(cycle_number), str(total_problems), '1', problem_line))
        else:
            calendar.append(("", "", "", "", problem_line))

    return calendar


# Example usage:
start_date = "2023-10-25"
start_problems_per_day = 6
total_problems = 306

schedule = generate_schedule(
    start_date, start_problems_per_day, total_problems)

# Print the table with line wrapping for problems list
print("Date       | Cycle | Problems Per Day  | Day of Cycle | Problems")
for entry in schedule:
    print(' | '.join(field.ljust(width)
          for field, width in zip(entry, [10, 5, 17, 12, 15])))
