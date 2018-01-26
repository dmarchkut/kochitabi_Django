from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator

WEATHER_CHOICES = (("晴れ", "晴れ"),("曇り", "曇り"),("雨", "雨"),("雪", "雪"),("雷雲", "雷雲"),("霧雨", "霧雨"),("霧", "霧"),("その他", "その他"),)
WEATHER_CONDITION_CHOICES = (("晴天", "晴天"),("雨天", "雨天"))

# Create your models here.
class Message(models.Model):
    """メッセージ"""
    message_id   = models.CharField('メッセージID', primary_key=True, validators=[MinLengthValidator(6)], max_length = 6, null=False, default = 'me')
    text_data = models.TextField('テキストデータ',  null=False)
    created_at   = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at    = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        if len(self.text_data) > 30:
            return '['+self.message_id+'] '+self.text_data[:30]+'...'
        else:
            return '['+self.message_id+'] '+self.text_data[:30]


class Coordinate(models.Model):
    """座標"""
    coordinate_id   = models.CharField('座標ID', primary_key=True, validators=[MinLengthValidator(6)], max_length = 6, null=False, default = 'co')
    place_name      = models.TextField('地名', max_length = 50, null=False)

    latitude        = models.FloatField('緯度', validators=[MaxValueValidator(90),MinValueValidator(-90)], max_length = 10, null=True, blank=True)
    longitude       = models.FloatField('経度', validators=[MaxValueValidator(180),MinValueValidator(-180)], max_length = 11, null=True, blank=True)
    created_at      = models.DateTimeField('作成日時', null=False)
    update_at       = models.DateTimeField('更新日時', null=False)

    def __str__(self):
        if len(self.place_name) > 30:
            return '['+self.coordinate_id+'] '+self.place_name[:30]+'...'
        else:
            return '['+self.coordinate_id+'] '+self.place_name[:30]


class Photo_path(models.Model):
    """写真ファイルパス"""
    photo_path_id   = models.CharField('写真ファイルパスID', primary_key=True, validators=[MinLengthValidator(6)], max_length = 6, null=False, default = 'pp')
    photo_file_path = models.TextField('写真ファイルパス', max_length = 50, null=False)
    #photo_index     = models.IntegerField("写真索引番号",  null=False)
    created_at      = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at       = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        if len(self.photo_file_path) > 30:
            return '['+self.photo_path_id+'] '+self.photo_file_path[:30]+'...'
        else:
            return '['+self.photo_path_id+'] '+self.photo_file_path[:30]


class Spot(models.Model):
    """観光スポット"""
    spot_id        = models.CharField('観光地ID', max_length = 6, primary_key=True, validators=[MinLengthValidator(6)], null=False, default = 'sp')
    coordinate_id  = models.ForeignKey(Coordinate, verbose_name='座標ID')
    message_id     = models.ForeignKey(Message, verbose_name='メッセージID')
    spot_name      = models.TextField('観光地名', max_length = 50, null=False)
    spot_phoname   = models.TextField('フリガナ', max_length = 50, null=False)
    street_address  = models.TextField('住所', max_length = 50, null=False)
    postal_code    = models.CharField('郵便番号', validators=[MinLengthValidator(7)] , max_length = 7, null=False)
    created_at     = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at      = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        #return self.spot_id
        if len(self.spot_name) > 30:
            return '['+self.spot_id+'] '+self.spot_name[:30]+'...'
        else:
            return '['+self.spot_id+'] '+self.spot_name[:30]


class Character(models.Model):
    """キャラクターテーブル"""
    character_id   = models.CharField('キャラクターID', max_length = 6, primary_key=True, validators=[MinLengthValidator(6)], null=False, default = 'ch')
    character_name = models.CharField('キャラクター名', max_length = 20, null=False)
    created_at     = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at      = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        if len(self.character_name) > 30:
            return '['+self.character_id+'] '+self.character_name[:30]+'...'
        else:
            return '['+self.character_id+'] '+self.character_name[:30]


class Spot_photo(models.Model):
    """観光地写真"""
    spot_photo_id  = models.CharField('写真グループID', max_length = 6, primary_key=True, validators=[MinLengthValidator(6)], null=False, default = 'ph')
    use_photo_path_id = models.ForeignKey(Photo_path, verbose_name='使用写真パスID')
    spot_id      = models.ForeignKey(Spot, verbose_name='観光地ID')
    photo_number = models.IntegerField('写真枚数', validators=[MaxValueValidator(99)],  null=False)
    created_at   = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at    = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        spot = Spot.objects.all().filter(spot_id=self.spot_id).first()
        if spot is None:
            return '['+self.spot_photo_id+']'
        if len(spot.spot_name) > 30:
            return '['+self.spot_photo_id+'] '+spot.spot_name[:30]+'...'+'の写真テーブル'
        else:
            return '['+self.spot_photo_id+'] '+spot.spot_name[:30]+'の写真テーブル'


class Environment(models.Model):
    """環境"""
    environment_id = models.CharField('環境ID', primary_key=True, max_length = 6, validators=[MinLengthValidator(6)], null=False, default = 'en')
    spot_id        = models.ForeignKey(Spot, verbose_name='観光地ID')
    weather        = models.CharField('天気', choices=WEATHER_CHOICES, max_length = 10, null=True, blank=True)
    temperature    = models.CharField('気温', max_length = 5, null=True, blank=True)
    created_at     = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at      = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        spot = Spot.objects.all().filter(spot_id=self.spot_id).first()
        if spot is None:
            return '['+self.environment_id+']'
        if len(spot.spot_name) > 30:
            return '['+self.environment_id+'] '+spot.spot_name[:30]+'...'+'の環境テーブル'
        else:
            return '['+self.environment_id+'] '+spot.spot_name[:30]+'の環境テーブル'


class Access_point(models.Model):
    """アクセスポイント"""
    access_point_id   = models.CharField('アクセスポイントID', primary_key=True, max_length = 6, validators=[MinLengthValidator(6)], null=False, default = 'ap')
    spot_id           = models.ForeignKey(Spot, verbose_name='観光地ID')
    coordinate_id     = models.ForeignKey(Coordinate, verbose_name='座標ID')
    message_id          = models.ForeignKey(Message, verbose_name='メッセージ')
    raspberry_pi_number   = models.CharField('RaspberryPi識別番号', max_length = 6, null=False, default = 'pi')
    access_point_name = models.TextField('アクセスポイント名', max_length = 50, null=False)
    created_at        = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at         = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        if len(self.access_point_name) > 30:
            return '['+self.access_point_id+'] '+self.access_point_name[:30]+'...'
        else:
            return '['+self.access_point_id+'] '+self.access_point_name[:30]


class Character_data(models.Model):
    """キャラクターデータ"""
    character_data_id        = models.CharField('キャラクターデータID', max_length = 6, validators=[MinLengthValidator(6)], primary_key=True, null=False, default = 'ch')
    access_point_id     = models.ForeignKey(Access_point, verbose_name='アクセスポイントID')
    character_id        = models.ForeignKey(Character, verbose_name='キャラクターID')
    weather_condition   = models.CharField('天気条件', choices = WEATHER_CONDITION_CHOICES, max_length = 2, null=False)
    character_file_pass = models.TextField('キャラクターファイルパス', max_length = 50)
    created_at          = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at           = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        if len(self.character_file_pass) > 30:
            return '['+self.character_data_id+'] '+self.character_file_pass[:30]+'...'
        else:
            return '['+self.character_data_id+'] '+self.character_file_pass[:30]


class Point_temperature(models.Model):
    """局所気温"""
    point_temperature_id = models.CharField('局所気温ID', primary_key=True, validators=[MinLengthValidator(6)], max_length = 6, null=False, default = 'pt')
    environment_id       = models.ForeignKey(Environment, verbose_name='環境ID')
    access_point_id      = models.ForeignKey(Access_point, verbose_name='アクセスポイントID')
    point_temperature    = models.FloatField('局所気温', validators=[MaxValueValidator(85),MinValueValidator(-40)],  max_length = 5)
    acquisition_rank     = models.IntegerField('取得順位', validators=[MaxValueValidator(99)])
    created_at   = models.DateTimeField('作成日時', null=False, default=datetime.now())
    update_at    = models.DateTimeField('更新日時', null=False, default=datetime.now())
    def __str__(self):
        access_point = Access_point.objects.all().filter(access_point_id=self.access_point_id).first()
        if access_point is None:
            return '['+self.point_temperature_id+']'
        if len(access_point.access_point_name) > 30:
            return '['+self.point_temperature_id+'] '+access_point.access_point_name[:30]+'...'+'の局所気温テーブル'
        else:
            return '['+self.point_temperature_id+'] '+access_point.access_point_name[:30]+'の局所気温テーブル'
