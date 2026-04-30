from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    id: int = field(kw_only=True)
    description: str
    priority: str
    created_at: datetime = field(default_factory=datetime.now)
    completed: bool = False
    completed_at: Optional[datetime] = None

    def __post_init__(self):
        if self.priority not in ('low', 'medium', 'high'):
            self.priority = 'medium'

    def complete(self) -> None:
        self.completed = True
        self.completed_at = datetime.now()

    def days_since_creation(self, reference_date: Optional[datetime] = None) -> int:
        ref = reference_date or datetime.now()
        return (ref - self.created_at).days

    def __str__(self) -> str:
        mark = "✓" if self.completed else " "
        date = self.created_at.strftime("%Y-%m-%d")
        return f"[{mark}] {self.description} (приоритет: {self.priority}, создана: {date})"


if __name__ == "__main__":
    task = Task(id=1, description="Подготовиться к 11 классу в 'Векторе'", priority="high")
    print(task)

    task.complete()
    print(task)
    print(f"Завершено в: {task.completed_at}")
