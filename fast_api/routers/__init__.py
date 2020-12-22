from fastapi import HTTPException

def invalidUsage(message=None, status_code=None, payload=None):
    raise HTTPException(
            status_code=status_code,
            detail=message,
            headers={"X-Error": "There goes my error"},
    )