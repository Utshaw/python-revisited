#!/usr/bin/env python
import re, pyperclip
# PDF: https://cdm16039.contentdm.oclc.org/digital/collection/p266101coll7/id/25785/

phoneRegex = re.compile(r'''
# 415-555-0000,555-0000, (415) 555-0000, 555-0000 ext 123456, ext. 123456, x12345
(
((\d\d\d) | (\(\d\d\d\)))?    # area code (optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)    # extension word-part (optional)
(\d{2,5}))? # extension number-part (optional)
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
# some.+_thing@.com

[a-zA-Z0-9_.+]+      # name part
@                    # @ symbol
[a-zA-Z0-9_.+]+      # domain name part

''', re.VERBOSE)


# Get the text off the clipboard
text =  pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


results = '\n'.join(allPhoneNumbers) + '\n' +  '\n'.join(extractedEmail)
pyperclip.copy(results) # copy results to clipboard
# print(allPhoneNumbers)
# print(extractedEmail)


