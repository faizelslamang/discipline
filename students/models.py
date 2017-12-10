from django.db import models

TRANSPORT_TYPES = (
    ("Bus", "Bus"),
    ("Taxi", "Taxi"),
    ("Train", "Train",)
)


INCIDENT_TYPES = (
    ("Bullying", "Bullying"),
    ("Homework", "Homework"),
    ("Late-coming", "Late-coming"),
    ("Smoking", "Smoking"),
)


STATUS_TYPES = (
    ("O", "Open"),
    ("C", "Closed"),
)

INTERACTION_TYPES = (
    ("Telephone", "Telephone"),
    ("SMS", "SMS"),
    ("Whatsapp", "WhatsApp"),
    ("Email", "EMAIL"),
    ("Meeting", "Meeting"),
)


class Student(models.Model):
    first_names = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    guardian = models.CharField(max_length=50, blank=True)
    mode_of_transport = models.CharField(max_length=10,
                                         choices=TRANSPORT_TYPES,
                                         blank=True)

    def __str__(self):
        return self.first_names + ' ' + self.last_name

    class Meta:
        ordering = ['last_name', 'first_names', ]


class Incident(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_occurred = models.DateField()
    incident_type = models.CharField(max_length=15, choices=INCIDENT_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default="O")

    def __str__(self):
        return str(self.student) + ' ' + str(self.date_occurred) + ' ' + \
            self.get_incident_type_display() + ' ' + self.get_status_display()

    class Meta:
        ordering = ['student', '-status', '-date_occurred', ]

class Interaction(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    date_interaction = models.DateField()
    interaction_type = models.CharField(max_length=12,
                                        choices=INTERACTION_TYPES)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.incident) + ' ' + self.get_interaction_type_display()

    class Meta:
        ordering = ['incident', '-date_interaction', ]
