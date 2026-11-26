from .models import VisualConfig

def visual_config(request):
    config = VisualConfig.objects.first()
    if not config:
        config = VisualConfig()
    return {'config': config}
