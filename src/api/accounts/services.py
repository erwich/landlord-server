from db import landlord, execute_query
import hashlib
import uuid


def authenticate(email, password):
    password = hashlib.md5(bytes(password, "utf-8")).hexdigest()
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
        True,
    )

    return False if len(user) == 0 else user


def purge_user_session(userid):
    execute_query(
        """
            DELETE FROM user_sessions
            WHERE user_id = %s
        """,
        landlord,
        (userid,),
        False,
    )


def generate_session_token(userid):
    # First, purge existing sessions (one session per user for security)
    purge_user_session(userid)
    session_id = str(uuid.uuid4())
    execute_query(
        """
            INSERT INTO user_sessions(
                id,
                user_id,
                login_time
            ) VALUES (
                %s,
                %s,
                NOW()
            )
        """,
        landlord,
        (session_id, userid),
        False,
    )
    return session_id
