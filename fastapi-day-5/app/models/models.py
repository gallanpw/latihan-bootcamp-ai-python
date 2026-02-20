from datetime import date

from sqlmodel import Field, Relationship, SQLModel


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # int | None => autoincrement()
    title: str
    author: str
    isbn: str = Field(unique=True)
    borrowing_records: list["BorrowingRecord"] = Relationship(back_populates="book")

    @property
    def is_available(self) -> bool:
        return not any([record.return_date for record in self.borrowing_records])


class Member(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)
    borrowing_records: list["BorrowingRecord"] = Relationship(back_populates="member")


class BorrowingRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="book.id")
    member_id: int = Field(foreign_key="member.id")
    borrow_date: date
    return_date: date | None = Field(default=None)
    book: Book = Relationship(back_populates="borrowing_records")
    member: Member = Relationship(back_populates="borrowing_records")
