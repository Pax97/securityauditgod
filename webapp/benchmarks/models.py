from django.db import models


class Benchmark(models.Model):
    """Model representing a CIS Benchmark."""

    benchmark_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    publication_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} v{self.version}"


class Profile(models.Model):
    """Model representing a profile within a benchmark (e.g., Level 1, Level 2)."""

    profile_id = models.CharField(primary_key=True, max_length=100)
    benchmark = models.ForeignKey(
        Benchmark, on_delete=models.CASCADE, related_name="profiles"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.benchmark.name})"


class Section(models.Model):
    """Model representing a section within a benchmark."""

    section_id = models.CharField(primary_key=True, max_length=100)
    benchmark = models.ForeignKey(
        Benchmark, on_delete=models.CASCADE, related_name="sections"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subsections",
    )
    section_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.section_number} {self.title}"


class Control(models.Model):
    """Model representing a specific control/recommendation within a benchmark."""

    ASSESSMENT_STATUS_CHOICES = (
        ("automated", "Automated"),
        ("manual", "Manual"),
    )

    control_id = models.CharField(primary_key=True, max_length=100)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="controls"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rationale = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    audit_procedure = models.TextField(blank=True)
    remediation = models.TextField(blank=True)
    default_value = models.TextField(blank=True)
    assessment_status = models.CharField(
        max_length=20, choices=ASSESSMENT_STATUS_CHOICES
    )
    control_number = models.CharField(max_length=20, blank=True)
    profiles = models.ManyToManyField(Profile, related_name="controls")

    def __str__(self):
        return f"{self.control_number} {self.title}"
