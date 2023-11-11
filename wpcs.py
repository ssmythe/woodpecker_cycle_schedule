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
    problem_start = 1  # Initialize the start problem number for each cycle
    
    while problems_per_day < total_problems:
        days_for_cycle = -(-total_problems // problems_per_day)  # Ceiling division
        for day in range(1, days_for_cycle + 1):
            # Calculate the problem range for the current day
            problem_end = problem_start + problems_per_day - 1
            # Ensure we do not go over the total number of problems
            if problem_end > total_problems:
                problem_end = total_problems
            
            # Add a divider between cycles
            if prev_problems_per_day != problems_per_day and day == 1:
                calendar.append(("----------", "-----", "-----------------", "------------", "----------"))
            calendar.append((current_date.strftime('%Y-%m-%d'), cycle_number, problems_per_day, day, f"{problem_start}-{problem_end}"))
            current_date += timedelta(days=1)
            problem_start = problem_end + 1  # Set the start for the next day
        prev_problems_per_day = problems_per_day
        problems_per_day *= 2
        cycle_number += 1
        problem_start = 1  # Reset the start problem number for the new cycle
    
    # Add a divider before the final day
    calendar.append(("----------", "-----", "-----------------", "------------", "----------"))
    # Add the final day where all problems are solved
    calendar.append((current_date.strftime('%Y-%m-%d'), cycle_number, total_problems, 1, f"{problem_start}-{total_problems}"))
    
    return calendar

# Example usage:
start_date = "2023-10-25"
start_problems_per_day = 6
total_problems = 306

schedule = generate_schedule(start_date, start_problems_per_day, total_problems)

# Print the table with the new column for problem range
print("Date       | Cycle | Problems Per Day  | Day of Cycle | Problem Range")
for entry in schedule:
    print(f"{entry[0]} | {entry[1]:<5} | {entry[2]:<17} | {entry[3]:<12} | {entry[4]}")
