
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PlaceholderPage(QWidget):
    def __init__(self, page_name):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel(page_name)
        title.setObjectName("sectionTitle")
        layout.addWidget(title)

        description = QLabel(
            f"The {page_name} page is under development."
        )
        description.setObjectName("mutedText")
        description.setWordWrap(True)
        layout.addWidget(description)

        layout.addStretch()
