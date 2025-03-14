import uuid

from django.db import models


class Project(models.Model):
    """Model representing a project."""

    project_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    """Model representing an IT asset to be assessed."""

    ASSET_TYPES = (
        ("linux", "Linux"),
        ("windows", "Windows"),
        ("mysql", "MySQL"),
        ("other", "Other"),
    )

    asset_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="assets"
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ASSET_TYPES)
    hostname = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    os_info = models.JSONField(blank=True, null=True)
    db_info = models.JSONField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.hostname})"


class AssetGroup(models.Model):
    """Model representing a group of assets."""

    group_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="groups"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assets = models.ManyToManyField(Asset, related_name="groups")

    def __str__(self):
        return f"{self.name} (in {self.project.name})"
