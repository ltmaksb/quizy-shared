from sqlalchemy import Text, Boolean, Integer, ForeignKey

from sqlalchemy.orm import DeclarativeBase
import uuid

from sqlalchemy import Column, UUID, DateTime, func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, relationship
from datetime import datetime


class Base(DeclarativeBase):
    ...

class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[str] = Column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = Column(VARCHAR(36), nullable=False)
    description: Mapped[str] = Column(VARCHAR(255), nullable=False)

    creator_id: Mapped[str] = Column(UUID, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime, nullable=False, default=func.now())

    questions: Mapped[list['Question']] = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = Column(Integer, primary_key=True)
    question: Mapped[str] = Column(Text, nullable=False)
    image: Mapped[str] = Column(Text, nullable=True)

    points: Mapped[int] = Column(Integer, nullable=False, default=10)
    time_for_answer: Mapped[int] = Column(Integer, nullable=False, default=30)
    hint: Mapped[str] = Column(Text, nullable=True)

    quiz_id: Mapped[str] = Column(UUID, ForeignKey('quiz.id'), nullable=False)

    quiz: Mapped['Quiz'] = relationship('Quiz', back_populates='questions')
    answers: Mapped[list['Answer']] = relationship('Answer', back_populates='question')

class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[str] = Column(UUID, primary_key=True, default=uuid.uuid4)
    answer: Mapped[str] = Column(Text, nullable=False)
    is_correct: bool = Column(Boolean, nullable=False, default=False)

    question_id: Mapped[int] = Column(Integer, ForeignKey('questions.id'), nullable=False)

    question: Mapped['Question'] = relationship('Question', back_populates='answers')