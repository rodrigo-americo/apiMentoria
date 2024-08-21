from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pc  # Importe o modelo Pc
from django.core.cache import cache


class PcViewSetTests(APITestCase):
    def setUp(self):
        # Limpa todos os registros do banco de dados antes de cada teste
        Pc.objects.all().delete()
        # Limpa o cache antes de cada teste
        cache.clear()
        # Configura a URL da lista
        self.list_url = reverse('Pc-crate-list')  # Substitua pelo nome correto da sua URL

    def tearDown(self):
        # Limpa o banco de dados após cada teste
        Pc.objects.all().delete()

    def test_create_pc_with_valid_id(self):
        # Dados de exemplo com IDs válidos
        valid_data = [
            {'id': 'PC101', 'brand': 'BrandA', 'model': 'ModelA', 'classroom': 101, 'ssd': True},
            {'id': 'PC502', 'brand': 'BrandB', 'model': 'ModelB', 'classroom': 102, 'ssd': False},
            {'id': 'PC110', 'brand': 'BrandC', 'model': 'ModelC', 'classroom': 103, 'ssd': True},
        ]

        for data in valid_data:
            response = self.client.post(self.list_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Pc.objects.filter(id=data['id']).exists(), True)

    def test_create_pc_with_invalid_id(self):
        # Dados de exemplo com IDs inválidos
        invalid_data = [
            {'id': 'PC601', 'brand': 'BrandA', 'model': 'ModelA', 'classroom': 101, 'ssd': True},
            # Terceiro dígito inválido
            {'id': 'PC011', 'brand': 'BrandB', 'model': 'ModelB', 'classroom': 102, 'ssd': False},
            # Terceiro dígito inválido
            {'id': 'PC1045', 'brand': 'BrandC', 'model': 'ModelC', 'classroom': 103, 'ssd': True},
            # Últimos dois dígitos inválidos
            {'id': 'AB101', 'brand': 'BrandD', 'model': 'ModelD', 'classroom': 104, 'ssd': False},  # Prefixo inválido
        ]

        for data in invalid_data:
            response = self.client.post(self.list_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('id', response.data)  # Verifica se o erro é referente ao campo 'id'

    def test_list_pc(self):
        # Criando um objeto Pc para testar a listagem
        Pc.objects.create(id='PC101', brand='BrandA', model='ModelA', classroom=101, ssd=True)
        response = self.client.get(self.list_url, format='json')

        # Se a paginação estiver ativada, verifique dentro da chave 'results'
        results = response.data.get('results', response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['id'], 'PC101')

    def test_cache_pc_list(self):
        # Criando um objeto Pc e verificando o cache
        Pc.objects.create(id='PC101', brand='BrandA', model='ModelA', classroom=101, ssd=True)
        response1 = self.client.get(self.list_url, format='json')

        # Se a paginação estiver ativada, verifique dentro da chave 'results'
        results1 = response1.data.get('results', response1.data)

        # Verificando a resposta antes do cache
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results1), 1)

        # Adicionando outro objeto para ver se o cache persiste
        Pc.objects.create(id='PC102', brand='BrandB', model='ModelB', classroom=102, ssd=False)

        response2 = self.client.get(self.list_url, format='json')
        results2 = response2.data.get('results', response2.data)

        self.assertEqual(len(results2), 1)  # Deve ser 1 se o cache estiver funcionando

        # Limpando o cache e verificando novamente
        cache.clear()
        response3 = self.client.get(self.list_url, format='json')
        results3 = response3.data.get('results', response3.data)

        self.assertEqual(len(results3), 2)  # Agora deve mostrar 2 objetos

