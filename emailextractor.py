import re
import pyperclip

# Create the regex's
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}', re.IGNORECASE)
phoneRegex = re.compile(r'''(
        (\d{3}|\(\e{3}\))?          # area code
        (\s|-|\.)?                  # seperator
        (\d{3})                     # first 3 digits
        (\s|-|\.)?                  # seperator
        (\d{4})                     # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
        )''', re.VERBOSE)

emailRegex = re.compile(r'\w+@\w+\.com')

# Get the text from the clipboard
clippy = pyperclip.paste()

# Find all occurences of the emails and the phone numbers.
phone = phoneRegex.findall(clippy)
email = emailRegex.findall(clippy)

# Format the text to look pretty
final=""
for i in phone:
    final=final+' '+i
for i in email:
    final=final+' '+i

# Put the formatted string back on the clipboard
pyperclip.copy(final)
