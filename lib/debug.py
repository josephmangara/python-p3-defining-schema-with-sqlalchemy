# lib/sqlalchemy_sandbox.py
#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy_sandbox import Base, Student

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

