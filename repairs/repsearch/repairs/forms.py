from django.forms import ModelForm
from .models import Repair


class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = ['title', 'featured_image', 'description', 'demo_link',
                  'source_link', 'tags']
