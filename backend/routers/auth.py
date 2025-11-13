from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserResponse, UserLogin
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.user import User
from backend.schemas.user import UserCreate, UserResponse, UserLogin
from backend.utils.auth import get_password_hash, verify_password, create_access_token
from datetime import timedelta

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Signup endpoint
@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    # Hash password and create user
    hashed_password = get_password_hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Login endpoint
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    # Create JWT token
    access_token_expires = timedelta(hours=1)
    token = create_access_token(data={"user_id": db_user.id}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
