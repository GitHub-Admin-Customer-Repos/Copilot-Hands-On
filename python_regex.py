# Problem:
# Given a log file with entries in the format:

# Extract the date, time, log level, module, and message from each log entry.

# Step-by-Step Plan:
# Import the re module: This module provides support for regular expressions.
# Define a function: Create a function parse_log_entry that takes a log entry as input.
# Compile a Regular Expression: Use a regex pattern to match the log entry format.
# Match the Pattern: Use the match method to extract the components.
# Return the Components: Return the extracted components as a dictionary.

#Code:
import re

def parse_log_entry(log_entry):
    # Step 3: Compile a Regular Expression
    log_pattern = re.compile(
        r'\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\] '
        r'\[(?P<log_level>[A-Z]+)\] '
        r'\[(?P<module>[^\]]+)\] - '
        r'(?P<message>.*)'
    )
    
    # Step 4: Match the Pattern
    match = log_pattern.match(log_entry)
    
    if match:
        # Step 5: Return the Components
        return match.groupdict()
    else:
        return None

# Example usage
log_entry = "[2023-10-01 12:34:56] [ERROR] [auth_module] - Failed to authenticate user"
parsed_entry = parse_log_entry(log_entry)
print(parsed_entry)

# Explanation:
# Regex Pattern:
# \[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\]: Matches the date and time in the format [YYYY-MM-DD HH:MM:SS].
# \[(?P<log_level>[A-Z]+)\]: Matches the log level (e.g., ERROR, INFO) and captures it as log_level.
# \[(?P<module>[^\]]+)\]: Matches the module name and captures it as module.
# (?P<message>.*): Matches the message and captures it as message.
# Named Groups: The (?P<name>...) syntax is used to name the capturing groups, making it easier to access the matched components.

# Output:
{
    'date': '2023-10-01',
    'time': '12:34:56',
    'log_level': 'ERROR',
    'module': 'auth_module',
    'message': 'Failed to authenticate user'
}