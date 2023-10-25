#!/usr/bin/env python3

from datetime import datetime, timedelta

def generate_schedule(start_date, start_problems_per_day, total_problems):
    # Convert start_date from string to datetime object
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    
    # Initialize variables
    problems_per_day = start_problems_per_day
    calendar = []
    cycle_number = 1
    prev_problems_per_day = 0
    
    while problems_per_day < total_problems:
        days_for_cycle = -(-total_problems // problems_per_day)  # Ceiling division
        for day in range(1, days_for_cycle + 1):
            # Add a divider between cycles
            if prev_problems_per_day != problems_per_day and day == 1:
                calendar.append(("----------", "-----", "-----------------", "-------------"))
            calendar.append((current_date.strftime('%Y-%m-%d'), cycle_number, problems_per_day, day))
            current_date += timedelta(days=1)
        prev_problems_per_day = problems_per_day
        problems_per_day *= 2
        cycle_number += 1
    
    # Add a divider before the final day
    calendar.append(("----------", "-----", "-----------------", "-------------"))
    # Add the final day where all problems are solved
    calendar.append((current_date.strftime('%Y-%m-%d'), cycle_number, total_problems, 1))
    
    return calendar

# Example usage:
start_date = "2023-10-25"
start_problems_per_day = 6
total_problems = 306

schedule = generate_schedule(start_date, start_problems_per_day, total_problems)

# Print the table
print("Date       | Cycle | Problems Per Day  | Day of Cycle")
for entry in schedule:
    print(f"{entry[0]} | {entry[1]:<5} | {entry[2]:<17} | {entry[3]}")

