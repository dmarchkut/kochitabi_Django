from django.db import models


WEATHER_CHOICES = (("晴れ", "晴れ"),("曇り", "曇り"),("雨", "雨"),("雪", "雪"),("雷雲", "雷雲"),("霧雨", "霧雨"),("霧", "霧"),)
WEATHER_CONDITION_CHOICES = (("晴天", "晴天"),("雨天", "雨天"))
#weather_condition

# Create your models here.
class Message(models.Model):
    """メッセージ"""
    message_id   = models.CharField('メッセージID', primary_key=True, max_length = 6, null=False)
    text_data = models.TextField('テキストデータ',  null=False)
    created_at   = models.DateTimeField('作成日時', null=False)
    update_at    = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.message_id


class Coordinate(models.Model):
    """座標"""
    coordinate_id   = models.CharField('座標ID', primary_key=True, max_length = 6, null=False)
    place_name      = models.TextField('地名', max_length = 50, null=False)
    latitude        = models.FloatField('緯度', max_length = 10, null = False)
    longitude       = models.FloatField('経度', max_length = 11, null=False)
    created_at      = models.DateTimeField('作成日時', null=False)
    update_at       = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.coordinate_id



class Photo_path(models.Model):
    """写真ファイルパス"""
    photo_path_id   = models.CharField('写真ファイルパスID', primary_key=True, max_length = 6, null=False)
    photo_file_path = models.TextField('写真ファイルパス', max_length = 50, null=False)
    photo_index     = models.IntegerField("写真索引番号", max_length = 2, null=False)
    created_at      = models.DateTimeField('作成日時', null=False)
    update_at       = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.photo_path_id


class Spot(models.Model):
    """観光スポット"""
    spot_id        = models.CharField('観光地ID', max_length = 6, primary_key=True, null=False)
    coordinate_id  = models.ForeignKey(Coordinate)
    message_id     = models.ForeignKey(Message)
    spot_name      = models.TextField('観光地名', max_length = 50, null=False)
    spot_phoname   = models.TextField('フリガナ', max_length = 50, null=False)
    street_address  = models.TextField('住所', max_length = 50, null=False)
    postal_code    = models.IntegerField('郵便番号', null=False)
    created_at     = models.DateTimeField('作成日時', null=False)
    update_at      = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.spot_id


class Character(models.Model):
    """キャラクターテーブル"""
    character_id   = models.CharField('キャラクターID', max_length = 6, primary_key=True, null=False)
    character_name = models.CharField('キャラクター名', max_length = 20, null=False)
    created_at     = models.DateTimeField('作成日時', null=False)
    update_at      = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.character_id


class Spot_photo(models.Model):
    """観光地写真"""
    spot_photo_id  = models.CharField('写真グループID', max_length = 6, primary_key=True, null=False)
    use_photo_path_id = models.ForeignKey(Photo_path)
    spot_id      = models.ForeignKey(Spot)
    photo_number = models.IntegerField('写真枚数', null=False)
    created_at   = models.DateTimeField('作成日時', null=False)
    update_at    = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.spot_photo_id


class Environment(models.Model):
    """環境"""
    environment_id = models.CharField('環境ID', primary_key=True, max_length = 6, null=False)
    spot_id        = models.ForeignKey(Spot)
    weather        = models.CharField('天気', choices=WEATHER_CHOICES, max_length = 10, null=True, blank=True)
    temperature    = models.CharField('気温', max_length = 5, null=True, blank=True)
    # temperature    = Integer.CharField('気温', max_length = 5, null=True)
    created_at     = models.DateTimeField('作成日時', null=False)
    update_at      = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.environment_id


class Access_point(models.Model):
    """アクセスポイント"""
    access_point_id   = models.CharField('アクセスポイントID', primary_key=True, max_length = 6, null=False)
    spot_id           = models.ForeignKey(Spot)
    coordinate_id     = models.ForeignKey(Coordinate)
    message_id          = models.ForeignKey(Message)
    raspberry_pi_number   = models.CharField('RaspberryPi識別番号', max_length = 6, null=False)
    access_point_name = models.TextField('アクセスポイント名', max_length = 50, null=False)
    created_at        = models.DateTimeField('作成日時', null=False)
    update_at         = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.access_point_id


class Character_data(models.Model):
    """キャラクターデータ"""
    character_data_id        = models.CharField('キャラクターデータID', max_length = 6, primary_key=True, null=False)
    access_point_id     = models.ForeignKey(Access_point)
    character_id        = models.ForeignKey(Character)
    weather_condition   = models.CharField('天気条件', choices = WEATHER_CONDITION_CHOICES, max_length = 2, null=False)
    character_file_pass = models.TextField('キャラクターファイルパス', max_length = 50)
    created_at          = models.DateTimeField('作成日時', null=False)
    update_at           = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.character_data_id


class Point_temperature(models.Model):
    """局所気温"""
    point_temperature_id = models.CharField('局所気温ID', primary_key=True, max_length = 6, null=False)
    environment_id       = models.ForeignKey(Environment)
    access_point_id      = models.ForeignKey(Access_point)
    point_temperature    = models.FloatField('局所気温', max_length = 5)
    acquisition_rank     = models.IntegerField('取得順位',max_length = 2)
    created_at   = models.DateTimeField('作成日時', null=False)
    update_at    = models.DateTimeField('更新日時', null=False)
    def __str__(self):
        return self.point_temperature_id
