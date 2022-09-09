from urllib import response
from django.test import TestCase
from django.urls import reverse
from api.models import CheckBox
from api.serializers import CheckBoxSerializer

class CheckBoxSerializerApiTestCase(TestCase):
    def test_serializer(self):

        checkbox_1 = CheckBox.objects.create(name='checkbox_1')
        checkbox_2 = CheckBox.objects.create(name='checkbox_2')
        serializer_data = CheckBoxSerializer([checkbox_1, checkbox_2], many = True).data
        expected_data = [
            {
                'id':1,
                'name':'checkbox_1',
                'is_cheked':False,
            },
                        {
                'id':2,
                'name':'checkbox_2',
                'is_cheked':False,
            },
        ]
        
        self.assertEqual(serializer_data, expected_data )
