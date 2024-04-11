# 0x00. Personal data

## Resources
Read or watch:

	1. [What Is PII, non-PII, and Personal Data?](https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg)
	2. [logging documentation](https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw)
	3. [bcrypt package](https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw)
	4. [Logging to Files, Setting Levels, and Formatting](https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
	1. Examples of Personally Identifiable Information (PII)
	7. How to implement a log filter that will obfuscate PII fields
	4. How to encrypt a password and check the validity of an input password
	3. How to authenticate to a database using environment variable

## Tasks
### 0. Regex-ing
Write a function called filter_datum that returns the log message obfuscated:
- Arguments:
	- fields: a list of strings representing all fields to obfuscate
	- redaction: a string representing by what the field will be obfuscated
	- message: a string representing the log line
 	- separator: a string representing by which character is separating all fields in the log line (message)
- The function should use a regex to replace occurrences of certain field values.
- filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.
