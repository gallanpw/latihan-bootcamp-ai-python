"""Database seeder with real data for books, members, and borrowing records."""

import sys
from pathlib import Path
from datetime import date, timedelta
from sqlmodel import Session, SQLModel

# Add parent directory to path to allow imports from app module
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.models.engine import engine
from app.models.models import Book, Member, BorrowingRecord


def seed_database():
    """Seed the database with real book, member, and borrowing record data."""

    # Create all tables
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # Check if data already exists to avoid duplicates
        existing_books = session.query(Book).first()
        if existing_books:
            print("Database already seeded. Skipping...")
            return

        # Sample real books
        books_data = [
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "978-0-06-112008-4"},
            {"title": "1984", "author": "George Orwell", "isbn": "978-0-451-52494-2"},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "978-0-14-143951-8"},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "978-0-7432-7356-5"},
            {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "978-0-316-76948-0"},
            {"title": "Brave New World", "author": "Aldous Huxley", "isbn": "978-0-06-085052-4"},
            {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "isbn": "978-0-544-00555-5"},
            {"title": "Jane Eyre", "author": "Charlotte Brontë", "isbn": "978-0-14-144206-8"},
        ]

        # Create books
        books = []
        for book_data in books_data:
            book = Book(**book_data)
            session.add(book)
            books.append(book)

        session.commit()

        # Sample real members
        members_data = [
            {"name": "John Smith", "email": "john.smith@email.com"},
            {"name": "Sarah Johnson", "email": "sarah.johnson@email.com"},
            {"name": "Michael Chen", "email": "michael.chen@email.com"},
            {"name": "Emily Davis", "email": "emily.davis@email.com"},
            {"name": "Robert Wilson", "email": "robert.wilson@email.com"},
            {"name": "Jessica Martinez", "email": "jessica.martinez@email.com"},
            {"name": "David Anderson", "email": "david.anderson@email.com"},
            {"name": "Amanda Taylor", "email": "amanda.taylor@email.com"},
        ]

        # Create members
        members = []
        for member_data in members_data:
            member = Member(**member_data)
            session.add(member)
            members.append(member)

        session.commit()

        # Refresh to get IDs
        for book in books:
            session.refresh(book)
        for member in members:
            session.refresh(member)

        # Create borrowing records
        borrowing_records = []
        base_date = date.today()

        borrowing_data = [
            (0, 0, base_date - timedelta(days=30), base_date - timedelta(days=5)),
            (1, 1, base_date - timedelta(days=20), None),  # Not returned yet
            (2, 2, base_date - timedelta(days=15), base_date - timedelta(days=3)),
            (3, 3, base_date - timedelta(days=25), base_date - timedelta(days=10)),
            (4, 4, base_date - timedelta(days=7), None),  # Not returned yet
            (5, 5, base_date - timedelta(days=12), base_date),
            (6, 6, base_date - timedelta(days=18), base_date - timedelta(days=2)),
            (0, 7, base_date - timedelta(days=10), base_date - timedelta(days=1)),
            (1, 0, base_date - timedelta(days=5), None),  # Not returned yet
            (2, 1, base_date - timedelta(days=22), base_date - timedelta(days=8)),
        ]

        for book_idx, member_idx, borrow_date, return_date in borrowing_data:
            record = BorrowingRecord(
                book_id=books[book_idx].id,
                member_id=members[member_idx].id,
                borrow_date=borrow_date,
                return_date=return_date,
            )
            session.add(record)
            borrowing_records.append(record)

        session.commit()

        print("✓ Database seeded successfully!")
        print(f"  - Added {len(books)} books")
        print(f"  - Added {len(members)} members")
        print(f"  - Added {len(borrowing_records)} borrowing records")


if __name__ == "__main__":
    seed_database()
