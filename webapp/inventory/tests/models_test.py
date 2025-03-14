import pytest
from django.test import TestCase
from inventory.models import Asset, AssetGroup, Project


class TestProject(TestCase):
    def test_create_project(self):
        project = Project.objects.create(
            name="Test Project", description="This is a test project"
        )
        self.assertEqual(project.name, "Test Project")
        self.assertTrue(project.project_id)


class TestAsset(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project", description="This is a test project"
        )

    def test_create_asset(self):
        asset = Asset.objects.create(
            project=self.project,
            name="Test Server",
            type="linux",
            hostname="test.example.com",
            ip_address="192.168.1.100",
        )
        self.assertEqual(asset.name, "Test Server")
        self.assertEqual(asset.project, self.project)
