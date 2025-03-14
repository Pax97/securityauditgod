import uuid

from django.db import models


class Assessment(models.Model):
    """Model representing an assessment of an asset against a benchmark."""

    assessment_id = models.CharField(
        primary_key=True, max_length=100, default=uuid.uuid4
    )
    project = models.ForeignKey(
        "inventory.Project", on_delete=models.CASCADE, related_name="assessments"
    )
    asset = models.ForeignKey(
        "inventory.Asset", on_delete=models.CASCADE, related_name="assessments"
    )
    benchmark = models.ForeignKey(
        "benchmarks.Benchmark", on_delete=models.CASCADE, related_name="assessments"
    )
    profile = models.ForeignKey(
        "benchmarks.Profile", on_delete=models.CASCADE, related_name="assessments"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField(blank=True, null=True)
    compliance_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.asset.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Result(models.Model):
    """Model representing a single control result within an assessment."""

    STATUS_CHOICES = (
        ("pass", "Pass"),
        ("fail", "Fail"),
        ("unknown", "Unknown"),
        ("not_applicable", "Not Applicable"),
    )

    result_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    assessment = models.ForeignKey(
        Assessment, on_delete=models.CASCADE, related_name="results"
    )
    control = models.ForeignKey(
        "benchmarks.Control", on_delete=models.CASCADE, related_name="results"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    actual_value = models.TextField(blank=True)
    expected_value = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.control.control_number} - {self.status}"


class CollectedData(models.Model):
    """Model storing the raw collected data from collector scripts."""

    collection_id = models.CharField(
        primary_key=True, max_length=100, default=uuid.uuid4
    )
    asset = models.ForeignKey(
        "inventory.Asset", on_delete=models.CASCADE, related_name="collected_data"
    )
    collector_type = models.CharField(max_length=20)
    collection_date = models.DateTimeField()
    raw_data = models.JSONField()

    def __str__(self):
        return f"{self.asset.name} data - {self.collection_date.strftime('%Y-%m-%d')}"
