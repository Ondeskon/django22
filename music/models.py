from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Jméno interpreta")
    bio = models.TextField(verbose_name="Biografie", blank=True)
    birth_date = models.DateField(verbose_name="Datum narození", null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name="Země původu", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizováno")

    class Meta:
        verbose_name = "Interpret"
        verbose_name_plural = "Interpreti"
        ordering = ['name']

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název alba")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Interpret")
    release_date = models.DateField(verbose_name="Datum vydání")
    cover_image = models.ImageField(upload_to='album_covers/', verbose_name="Obal alba", blank=True, null=True)
    description = models.TextField(verbose_name="Popis", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizováno")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Alba"
        ordering = ['-release_date']

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název skladby")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', verbose_name="Album")
    duration = models.DurationField(verbose_name="Délka skladby")
    track_number = models.PositiveIntegerField(verbose_name="Číslo skladby")
    lyrics = models.TextField(verbose_name="Text písně", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Aktualizováno")

    class Meta:
        verbose_name = "Skladba"
        verbose_name_plural = "Skladby"
        ordering = ['track_number']

    def __str__(self):
        return f"{self.title} - {self.album.title}"

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Jméno")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Zpráva")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Odesláno")

    class Meta:
        verbose_name = "Zpráva z formuláře"
        verbose_name_plural = "Zprávy z formuláře"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at.strftime('%d.%m.%Y %H:%M')}"
