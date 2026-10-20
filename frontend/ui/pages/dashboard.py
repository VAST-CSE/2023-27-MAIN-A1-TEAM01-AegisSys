
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        heading = QLabel("Security overview")
        heading.setObjectName("sectionTitle")
        layout.addWidget(heading)

        description = QLabel(
            "Monitor security assessments, findings, and remediation activity."
        )
        description.setObjectName("mutedText")
        description.setWordWrap(True)
        layout.addWidget(description)

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(16)

        cards = [
            ("Systems Assessed", "0", "Systems checked by AegisSys"),
            ("Open Findings", "0", "Issues awaiting review"),
            ("Critical Risks", "0", "Critical findings identified"),
        ]

        for title, value, detail in cards:
            card = self.create_stat_card(title, value, detail)
            cards_layout.addWidget(card)

        layout.addLayout(cards_layout)

        activity_card = QFrame()
        activity_card.setObjectName("panel")

        activity_layout = QVBoxLayout(activity_card)
        activity_layout.setContentsMargins(20, 20, 20, 20)
        activity_layout.setSpacing(12)

        activity_title = QLabel("Recent activity")
        activity_title.setObjectName("cardTitle")
        activity_layout.addWidget(activity_title)

        activity_text = QLabel(
            "No assessment activity yet.\n\n"
            "Run a security assessment to see findings and results here."
        )
        activity_text.setObjectName("mutedText")
        activity_text.setWordWrap(True)
        activity_layout.addWidget(activity_text)

        layout.addWidget(activity_card)
        layout.addStretch()

    @staticmethod
    def create_stat_card(title, value, detail):
        card = QFrame()
        card.setObjectName("statCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("statValue")

        detail_label = QLabel(detail)
        detail_label.setObjectName("mutedText")
        detail_label.setWordWrap(True)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(detail_label)

        return card
