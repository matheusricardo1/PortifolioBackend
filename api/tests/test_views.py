from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import PortifolioOwner, Service, Project
from django.core.files.uploadedfile import SimpleUploadedFile

class PortifolioOwnerViewSetTest(APITestCase):
    def setUp(self):
        self.owner1 = PortifolioOwner.objects.create(
            first_name="Alice",
            last_name="Smith",
            your_stack="Full Stack Developer",
            image=SimpleUploadedFile("owner1.jpg", b"file_content", content_type="image/jpeg"),
            linkedin="https://linkedin.com/in/alicesmith",
            github="https://github.com/alicesmith",
            whatsapp="https://wa.me/123456789",
            birth_date="1990-01-01",
            about_me="Experienced developer.",
            contact_me="https://contact.me/alicesmith"
        )
        self.owner2 = PortifolioOwner.objects.create(
            first_name="Bob",
            last_name="Johnson",
            your_stack="Backend Developer",
            image=SimpleUploadedFile("owner2.jpg", b"file_content", content_type="image/jpeg"),
            linkedin="https://linkedin.com/in/bobjohnson",
            github="https://github.com/bobjohnson",
            whatsapp="https://wa.me/987654321",
            birth_date="1985-05-05",
            about_me="Specializes in APIs.",
            contact_me="https://contact.me/bobjohnson"
        )
        self.list_url = reverse('owner-list')

    def test_get_owner_list(self):
        """
        Testa a recuperação da lista de proprietários do portfólio.
        Deverá retornar apenas o último registro.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Como retorna apenas o último proprietário, verifica se é o owner2
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], 'Bob')

    def test_get_owner_detail(self):
        """
        Testa a recuperação de detalhes de um proprietário específico.
        """
        detail_url = reverse('owner-detail', kwargs={'pk': self.owner2.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Bob')

class ServiceViewSetTest(APITestCase):
    def setUp(self):
        self.service1 = Service.objects.create(
            name="Web Design",
            image=SimpleUploadedFile("service1.jpg", b"file_content", content_type="image/jpeg"),
            description="Creating beautiful websites.",
            order=1
        )
        self.service2 = Service.objects.create(
            name="SEO Optimization",
            image=SimpleUploadedFile("service2.jpg", b"file_content", content_type="image/jpeg"),
            description="Improving search rankings.",
            order=2
        )
        self.list_url = reverse('service-list')

    def test_get_service_list(self):
        """
        Testa a recuperação da lista de serviços.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Verifica a ordem
        self.assertEqual(response.data[0]['name'], 'Web Design')
        self.assertEqual(response.data[1]['name'], 'SEO Optimization')

    def test_get_service_detail(self):
        """
        Testa a recuperação de detalhes de um serviço específico.
        """
        detail_url = reverse('service-detail', kwargs={'pk': self.service1.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Web Design')

class ProjectViewSetTest(APITestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            name="Project Alpha",
            image=SimpleUploadedFile("project1.jpg", b"file_content", content_type="image/jpeg"),
            description="First project.",
            demo="https://demo.projectalpha.com",
            github="https://github.com/projectalpha"
        )
        self.project2 = Project.objects.create(
            name="Project Beta",
            image=SimpleUploadedFile("project2.jpg", b"file_content", content_type="image/jpeg"),
            description="Second project.",
            demo="https://demo.projectbeta.com",
            github="https://github.com/projectbeta"
        )
        self.list_url = reverse('project-list')

    def test_get_project_list(self):
        """
        Testa a recuperação da lista de projetos.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        project_names = [project['name'] for project in response.data]
        self.assertIn('Project Alpha', project_names)
        self.assertIn('Project Beta', project_names)

    def test_get_project_detail(self):
        """
        Testa a recuperação de detalhes de um projeto específico.
        """
        detail_url = reverse('project-detail', kwargs={'pk': self.project1.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Project Alpha')
