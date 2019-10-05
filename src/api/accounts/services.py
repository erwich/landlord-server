from db import (
    landlord,
    execute_query
)
import hashlib

def authenticate(email, password):
    password = hashlib.md5(
        bytes(password, 'utf-8')
    ).hexdigest()
    user = execute_query(
        """
            SELECT 
                id,
                email,
                first_name,
                last_name,
                user_type
            FROM users
            WHERE email = %s
                AND password = %s
            LIMIT 1
        """,
        landlord,
        (email, password),
        True
    )
    
    return False if len(user) == 0 else user
