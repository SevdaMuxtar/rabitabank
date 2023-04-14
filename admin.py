from flask_admin.contrib.sqla import ModelView
from app import deposits_folder, campaign_folder, card_order_folder
from flask_admin import form
from flask_ckeditor import CKEditorField

class FilialAdmin(ModelView):
    can_view_detailes = True

class ServiceTypeAdmin(ModelView):
    can_view_detailes = True

class TimeAdmin(ModelView):
    can_view_detailes = True

class OnlineQueueAdmin(ModelView):
    can_view_detailes = True

class NewsCategoryAdmin(ModelView):
    can_view_detailes = True

class NewsAdmin(ModelView):
    can_view_detailes = True

class CampaignCategoryAdmin(ModelView):
    can_view_detailes = True

class CampaignAdmin(ModelView):
    can_view_detailes = True,
    def _list_thumbnail(view, model):
        if not model.image_path:
            return ''
    form_extra_fields = {
        'image_path': form.ImageUploadField(
            'Image', base_path=campaign_folder, thumbnail_size=(100, 100, True))
    }

class DepositsAdmin(ModelView):
    can_view_detailes = True,
    def _list_thumbnail(view, model):
        if not model.image_path:
            return ''
    form_extra_fields = {
        'image_path': form.ImageUploadField(
            'Image', base_path=deposits_folder, thumbnail_size=(100, 100, True))
    }

class DepositFeaturesAdmin(ModelView):
    can_view_detailes = True
    form_overrides = dict(text=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'

class DepositTypeAdmin(ModelView):
    can_view_detailes = True

class OnlineDepositAdmin(ModelView):
    can_view_detailes = True



class CardTypeAdmin(ModelView):
    can_view_detailes = True,
    def _list_thumbnail(view, model):
        if not model.image_path:
            return ''
    form_extra_fields = {
        'image_path': form.ImageUploadField(
            'Image', base_path=card_order_folder, thumbnail_size=(100, 100, True))
    }

class CardCurrencyAdmin(ModelView):
    can_view_detailes = True,
    def _list_thumbnail(view, model):
        if not model.image_path:
            return ''
    form_extra_fields = {
        'image_path': form.ImageUploadField(
            'Image', base_path=card_order_folder, thumbnail_size=(100, 100, True))
    }

class CardOrderAdmin(ModelView):
    can_view_detailes = True