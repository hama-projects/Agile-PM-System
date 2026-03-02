class Task:
    def __init__(self, task_id, title, status, assignee, story_points):
        self.task_id = task_id
        self.title = title
        self.status = status
        self.assignee = assignee
        self.story_points = story_points


class Sprint:
    def __init__(self, sprint_id, name, start_date, end_date):
        self.sprint_id = sprint_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class Risk:
    def __init__(self, risk_id, description, severity, mitigation):
        self.risk_id = risk_id
        self.description = description
        self.severity = severity
        self.mitigation = mitigation


class Budget:
    def __init__(self, category, allocated, spent):
        self.category = category
        self.allocated = allocated
        self.spent = spent