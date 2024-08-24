class Bug:
    def __init__(self, title, description, status='Open'):
        self.title = title
        self.description = description
        self.status = status

class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, title, description):
        bug = Bug(title, description)
        self.bugs.append(bug)

    def get_all_bugs(self):
        return self.bugs

    def get_open_bugs(self):
        return [bug for bug in self.bugs if bug.status == 'Open']

# Example usage
tracker = BugTracker()
tracker.add_bug('Issue 1', 'This is the description of Issue 1')
tracker.add_bug('Issue 2', 'This is the description of Issue 2')
tracker.add_bug('Issue 3', 'This is the description of Issue 3')

all_bugs = tracker.get_all_bugs()
open_bugs = tracker.get_open_bugs()

for bug in all_bugs:
    print(f'Title: {bug.title}, Description: {bug.description}, Status: {bug.status}')

print('\nOpen Bugs:')
for bug in open_bugs:
    print(f'Title: {bug.title}, Description: {bug.description}, Status: {bug.status}')
