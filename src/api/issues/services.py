from db import (
    landlord,
    execute_query
)

def create_issue(form_data):
    try:
        execute_query(
            """
                INSERT INTO issues(
                    title,
                    description,
                    status,
                    unit,
                    issue_type,
                    submitted,
                    priority
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    NOW(),
                    %s
                )
            """,
            landlord,
            (
                form_data["title"],
                form_data["description"],
                form_data["status"],
                form_data["unit"],
                form_data["issue_type"],
                form_data["priority"],
            ),
            False
        )
        return True
    except Exception as e:
        print(e)
        return False
