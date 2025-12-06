import sys
from pathlib import Path
import sqlite3 as sql
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('scripts', action='append', type=Path)
    return parser.parse_args()


def main():
    args = parse_args()

    db = sql.connect(':memory:')
    db.execute('CREATE TABLE StandardInput (ID INTEGER PRIMARY KEY, Line TEXT);')
    db.execute('CREATE TABLE StandardOutput (ID INTEGER PRIMARY KEY, Line TEXT);')

    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            db.execute('INSERT INTO StandardInput (Line) VALUES (?)', (line,))

    for script in args.scripts:
        with open(script) as f:
            db.executescript(f.read())

        output = db.execute('SELECT Line FROM StandardOutput ORDER BY ID ASC;').fetchall()
        for line, in output:
            print(line)
        db.execute('DELETE FROM StandardOutput;')


if __name__ == "__main__":
    main()
