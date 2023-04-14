from email.policy import default
from multiprocessing import context
from extensions import db, admin
from admin import *
from datetime import date

class Filial(db.Model):
    __tablename__ = 'Filial'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
class ServiceType(db.Model):
    __tablename__ = 'ServiceType'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    
    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
class Time(db.Model):
    __tablename__ ='Time'
    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.String(40), nullable=False)
    
    def __repr__(self):
        return self.hour

    def __init__(self, hour):
        self.hour = hour

    def save(self):
        db.session.add(self)
        db.session.commit()
class OnlineQueue(db.Model):
    __tablename__ ='OnlineQueue'
    id = db.Column(db.Integer, primary_key=True)

    filial_name_id = db.Column(db.Integer, db.ForeignKey('Filial.id'), nullable=False)
    filial_name = db.relationship('Filial', backref=db.backref('OnlineQueue', lazy='dynamic', cascade='all, delete-orphan'))

    service_type_id = db.Column(db.Integer, db.ForeignKey('ServiceType.id'), nullable=False)
    service_type = db.relationship('ServiceType', backref=db.backref('OnlineQueue', lazy='dynamic', cascade='all, delete-orphan'))
    
    date = db.Column(db.Date, nullable=False)
    
    time_id = db.Column(db.Integer, db.ForeignKey('Time.id'), nullable=False)
    time = db.relationship('Time', backref=db.backref('OnlineQueue', lazy='dynamic', cascade='all, delete-orphan'))

    phone_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.filial_name.name

    def __init__(self, filial_name_id, service_type_id, date, time_id, phone_number):
        self.filial_name_id = filial_name_id
        self.service_type_id = service_type_id
        self.date = date
        self.time_id = time_id
        self.phone_number = phone_number

    def save(self):
        db.session.add(self)
        db.session.commit()

class NewsCategory(db.Model):
    __tablename__ = 'NewsCategory'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return self.category_name

    def __init__(self, category_name):
        self.category_name = category_name

    def save(self):
        db.session.add(self)
        db.session.commit()
class News(db.Model):
    __tablename__ = 'News'
    id = db.Column(db.Integer, primary_key=True)
    share_time = db.Column(db.Date, nullable=False, default=date.today())
    title = db.Column(db.String(100), nullable=False)
    context = db.Column(db.Text(), nullable=True)
    img = db.Column(db.Text(), nullable=False)

    news_category_id = db.Column(db.Integer, db.ForeignKey('NewsCategory.id'), nullable=False)
    news_category = db.relationship('NewsCategory', backref=db.backref('News', lazy='dynamic', cascade='all, delete-orphan'))

    def __repr__(self):
        return self.title

    def __init__(self, share_time, title, context, img):
        self.share_time = share_time
        self.title = title
        self.context = context
        self.img = img

    def save(self):
        db.session.add(self)
        db.session.commit()



class CardType(db.Model):
    __tablename__ = "CardType"
    id = db.Column(db.Integer, primary_key=True)
    card_type = db.Column(db.String(40), nullable=False)
    image_path = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return self.card_type

    def __init__(self, card_type, image_path):
        self.card_type = card_type
        self.image_path = image_path


    def save(self):
        db.session.add(self)
        db.session.commit()
class CardCurrency(db.Model):
    __tablename__ = "CardCurrency"
    id = db.Column(db.Integer, primary_key=True)
    card_currency = db.Column(db.String(40), nullable=False)
    image_path = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return self.card_currency

    def __init__(self, card_currency, image_path):
        self.card_currency = card_currency
        self.image_path = image_path

    def save(self):
        db.session.add(self)
        db.session.commit()
class CardOrder(db.Model):
    __tablename__ = "CardOrder"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)
    fin_code = db.Column(db.String(7), nullable=False)

    card_type_id = db.Column(db.Integer, db.ForeignKey("CardType.id"), nullable=False)
    card_type = db.relationship("CardType", backref=db.backref("CardOrder", lazy='dynamic', cascade='all, delete-orphan'))

    card_currency_id = db.Column(db.Integer, db.ForeignKey("CardCurrency.id"), nullable=False)
    card_currency = db.relationship("CardCurrency", backref=db.backref("CardOrder", lazy='dynamic', cascade='all, delete-orphan'))

    def __repr__(self):
        return self.name

    def __init__(self, name, surname, phone_number, fin_code, card_type_id, card_currency_id):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.fin_code = fin_code
        self.card_type_id = card_type_id
        self.card_currency_id = card_currency_id

    def save(self):
        db.session.add(self)
        db.session.commit()
class CampaignCategory(db.Model):
    __tablename__ = "CampaignCategory"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return self.category_name

    def __init__(self, category_name):
        self.category_name = category_name

    def save(self):
        db.session.add(self)
        db.session.commit()
class Campaign(db.Model):
    __tablename__ = "Campaign"
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Text(), nullable=False)
    title = db.Column(db.Text(), nullable=False)
    context = db.Column(db.Text(), nullable=True)
    image_path = db.Column(db.String(255), unique=True)

    campaign_category_id = db.Column(db.Integer, db.ForeignKey("CampaignCategory.id"), nullable=False)
    campaign_category = db.relationship("CampaignCategory", backref=db.backref("Campaign", lazy='dynamic', cascade='all, delete-orphan'))

    def __repr__(self):
        return self.title

    def __init__(self, duration, title, context, image_path):
        self.duration = duration
        self.title = title
        self.context = context
        self.image_path = image_path
        
    def save(self):
        db.session.add(self)
        db.session.commit()
class DepositType(db.Model):
    __tablename__ = "DepositType"
    id = db.Column(db.Integer, primary_key=True)
    deposit_name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return self.deposit_name

    def __init__(self, deposit_name):
        self.deposit_name = deposit_name

    def save(self):
        db.session.add(self)
        db.session.commit()
class OnlineDeposit(db.Model):
    __tablename__ = "OnlineDeposit"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)

    deposit_name_id = db.Column(db.Integer, db.ForeignKey("DepositType.id"), nullable=False)
    deposit_name = db.relationship("DepositType", backref=db.backref("OnlineDeposit", lazy='dynamic', cascade='all, delete-orphan'))

    def __repr__(self):
        return self.name

    def __init__(self, name, surname, phone_number, deposit_name_id):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.deposit_name_id = deposit_name_id

    def save(self):
        db.session.add(self)
        db.session.commit()
class DepositFeatures(db.Model):
    __tablename__ = "DepositFeatures"
    id = db.Column(db.Integer, primary_key=True)
    min_value = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    payment_of_percent = db.Column(db.String(255), nullable=False)
    insurance = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text)

    deposit_name_id = db.Column(db.Integer, db.ForeignKey("DepositType.id"), nullable=False)
    deposit_name = db.relationship("DepositType", backref=db.backref("DepositFeatures", lazy='dynamic', cascade='all, delete-orphan'))


    def __repr__(self):
        return self.min_value

    def __init__(self, min_value, duration, payment_of_percent, insurance, deposit_name_id):
        self.min_value = min_value
        self.duration = duration
        self.payment_of_percent = payment_of_percent
        self.insurance = insurance
        self.deposit_name_id = deposit_name_id

    def save(self):
        db.session.add(self)
        db.session.commit()
class Deposits(db.Model):
    __tablename__ = "Deposits"
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.Text(), nullable=False)
    duration = db.Column(db.Text(), nullable=False)
    percent_degree = db.Column(db.Text(), nullable=False)
    currency = db.Column(db.Text(), nullable=False)
    image_path = db.Column(db.String(255), unique=True)

    deposit_name_id = db.Column(db.Integer, db.ForeignKey("DepositType.id"), nullable=False)
    deposit_name = db.relationship("DepositType", backref=db.backref("Deposits", lazy='dynamic', cascade='all, delete-orphan'))

    def __repr__(self):
        return self.deposit_name.deposit_name

    def __init__(self, context, duration, percent_degree, currency, image_path, deposit_name_id):
        self.context = context
        self.duration = duration
        self.percent_degree = percent_degree
        self.currency = currency
        self.image_path = image_path
        self.deposit_name_id = deposit_name_id

    def save(self):
        db.session.add(self)
        db.session.commit()

admin.add_view(FilialAdmin(Filial, db.session))
admin.add_view(ServiceTypeAdmin(ServiceType, db.session))
admin.add_view(TimeAdmin(Time, db.session))
admin.add_view(OnlineQueueAdmin(OnlineQueue, db.session))

admin.add_view(NewsCategoryAdmin(NewsCategory, db.session))
admin.add_view(NewsAdmin(News, db.session))


admin.add_view(CampaignCategoryAdmin(CampaignCategory, db.session))
admin.add_view(CampaignAdmin(Campaign, db.session))

admin.add_view(DepositTypeAdmin(DepositType, db.session))
admin.add_view(OnlineDepositAdmin(OnlineDeposit, db.session))
admin.add_view(DepositsAdmin(Deposits, db.session))
admin.add_view(DepositFeaturesAdmin(DepositFeatures, db.session))


admin.add_view(CardTypeAdmin(CardType, db.session))
admin.add_view(CardCurrencyAdmin(CardCurrency, db.session))
admin.add_view(CardOrderAdmin(CardOrder, db.session))
