# Structured Query Script

Ever wanted to do general purpose computation with SQL? Don't want to get bogged down with all that nasty data stuff? SQscript is for you!

Run sqlite3 scripts in a sensibly temporary environment. Crunch numbers, get results. That's all we ever want, right?

## Installation
```bash
uv tool install git+https://github.com/cbosoft/sqscript
```

## Usage
```bash
sqscript SCRIPT.SQL [...]
```

Pass one or more SQL scripts to be run. To provide input to the program, pass stuff in via stdin:
```bash
echo "Greetings!" | sqscript foo.sql
```
This is then available in SQL in the `StandardInput(ID, Line)` table. Output is received by reading from the table `StandardOutput(ID, Line)`. There is no `StandardError` table.


`sqscript` ignores shebang lines, so you can now make your SQL scripts executable like you always wanted:

```SQL
#!/usr/bin/env sqscript
INSERT INTO StandardOutput(Line) Values ('Hello, World!');
```

If the script is called `test.sql`, run with:
```
$ chmod +x test.sql
$ ./test.sql
> Hello, World!
```
