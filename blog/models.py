from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.validators import FileExtensionValidator
from datetime import date, time, datetime, timedelta

PARTNERSHIP_TYPE = (
    ("personal", "personal"),
    ('government', 'government'),
    ('corporate supply', 'corporate supply'),
    ('equipment and supply', 'equipment and supply')
)

FEELINGS_CHOICES = (
    ("Happy", "Happy"),
    ("Sad", "Sad"),
    ("Confued", "Confued"),
    ("Smiling", "Smiling"),
    ("Crying", "Crying"),
    ("Winki", "Winki"),
    ("Chilling", "Chilling"),
)

LEVEL_CHOICES = (
    ("Assessment", "Assessment"),
    ("Development", "Development"),
    ("Planning", "Planning"),
    ("Implementation", "Implementation"),
    ("Evaluation", "Evaluation"),
    ("Star", "Star")
)

GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)

COUNTRY_OF_CHOICE = (
    ("Afghanistan", "Afghanistan"),
    ("Akrotiri", "Akrotiri"),
    ("Albania", "Albania"),
    ("Algeria", "Algeria"),
    ("American Samoa", "American Samoa"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Anguilla", "Anguilla"),
    ("Antarctica", "Antarctica"),
    ("Antigua and Barbuda", "Antigua and Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Armenia"),
    ("Aruba", "Aruba"),
    ("Ashmore and Cartier Islands", "Ashmore and Cartier Islands"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Belarus", "Belarus"),
    ("Belgium", "Belgium"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bermuda", "Bermuda"),
    ("Bhutan", "Bhutan"),
    ("Bolivia", "Bolivia"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Botswana", "Botswana"),
    ("Brazil", "Brazil"),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Cambodia", "Cambodia"),
    ("Cameroon", "Cameroon"),
    ("Canada", "Canada"),
    ("Cape Verde", "Cape Verde"),
    ("Central African Republic", "Central African Republic"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Colombia", "Colombia"),
    ("Comoros", "Comoros"),
    ("Congo, Democratic Republic of the", "Congo, Democratic Republic of the"),
    ("Costa Rica", "Costa Rica"),
    ("Cote d'Ivoire", "Cote d'Ivoire"),
    ("Croatia", "Croatia"),
    ("Cuba", "Cuba"),
    ("Cyprus", "Cyprus"),
    ("Czech Republic", "Czech Republic"),
    ("Denmark", "Denmark"),
    ("Dominican Republic", "Dominican Republic"),
    ("Ecuador", "Ecuador"),
    ("Egypt", "Egypt"),
    ("El Salvador", "El Salvador"),
    ("Equatorial Guinea", "Equatorial Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Ethiopia", "Ethiopia"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("Gabon", "Gabon"),
    ("Gambia", "Gambia"),
    ("Georgia", "Georgia"),
    ("Germany", "Germany"),
    ("Ghana", "Ghana"),
    ("Gibraltar", "Gibraltar"),
    ("Greece", "Greece"),
    ("Greenland", "Greenland"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Haiti", "Haiti"),
    ("Honduras", "Honduras"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Ireland", "Ireland"),
    ("Israel", "Israel"),
    ("Italy", "Italy"),
    ("Jamaica", "Jamaica"),
    ("Japan", "Japan"),
    ("Jordan", "Jordan"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kenya", "Kenya"),
    ("Korea, North", "Korea, North"),
    ("Korea, South", "Korea, South"),
    ("Kuwait", "Kuwait"),
    ("Latvia", "Latvia"),
    ("Lebanon", "Lebanon"),
    ("Liberia", "Liberia"),
    ("Libya", "Libya"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lithuania", "Lithuania"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malaysia"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Mauritania", "Mauritania"),
    ("Mauritius", "Mauritius"),
    ("Mexico", "Mexico"),
    ("Monaco", "Monaco"),
    ("Morocco", "Morocco"),
    ("Mozambique", "Mozambique"),
    ("Namibia", "Namibia"),
    ("Netherlands", "Netherlands"),
    ("New Zealand", "New Zealand"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    ("Norway", "Norway"),
    ("Pakistan", "Pakistan"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Philippines"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Puerto Rico", "Puerto Rico"),
    ("Qatar", "Qatar"),
    ("Romania", "Romania"),
    ("Russia", "Russia"),
    ("Rwanda", "Rwanda"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Senegal", "Senegal"),
    ("Serbia and Montenegro", "Serbia and Montenegro"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapore"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Somalia", "Somalia"),
    ("South Africa", "South Africa"),
    ("Spain", "Spain"),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudan", "Sudan"),
    ("Swaziland", "Swaziland"),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Taiwan", "Taiwan"),
    ("Tanzania", "Tanzania"),
    ("Thailand", "Thailand"),
    ("Togo", "Togo"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Tunisia", "Tunisia"),
    ("Turkey", "Turkey"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukraine"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("United Kingdom", "United Kingdom"),
    ("United States", "United States"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistan"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),
    ("Other", "Other")
)


CAREPLAN_CHOICE = (
    ("Eagle","Eagle"),
    ("Kangaroo","Kangaroo"),
    ("Nested","Nested"),
)


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=100)
    country = models.CharField(max_length=50, choices=COUNTRY_OF_CHOICE, default="United States")
    photo = models.ImageField(upload_to="volunteer_photos", default="volunteer.jpg")
    phone = models.CharField(max_length=40)
    why_join_Orgeon = models.CharField(max_length=200)
    additional_message = models.CharField(max_length=200, default="To make a difference",
                                          help_text="Please press once on the button below")
    date_volunteered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} has volunteered."


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    theme = models.CharField(max_length=100)
    venue = models.CharField(max_length=150)
    date_of_event = models.DateField(default=timezone.now)
    # event_started = models.BooleanField(default=False,)
    event_poster = models.ImageField(upload_to='event_pics', blank=True,
                                     validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg'])])
    description_of_event = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.theme}"

    def get_absolute_event_url(self):
        return reverse("event_detail", args={self.id})


class JoinTrip(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} has decided to join the trip."


class Partnership(models.Model):
    partnership = models.CharField(choices=PARTNERSHIP_TYPE, max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.partnership}"


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"


class NewsUpdate(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    report = models.TextField()
    has_read = models.ManyToManyField(User, related_name="has_read_report", blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s report = {self.title}"

    def get_absolute_url(self):
        return reverse("report_detail", args={self.pk})


class Post(models.Model):
    author = author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title = models.CharField(max_length=200)
    message = models.TextField(help_text="This message would be sent to all employees")
    poster = models.ImageField(upload_to="post_posters", blank=True,
                               validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg'])],
                               help_text="Leave this field blank if message has no image.")
    views = models.IntegerField(default=0)
    has_read = models.ManyToManyField(User, related_name="has_read_post", blank=True)
    need_replies = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_post_url(self):
        return reverse("post_detail", args={self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.poster.path)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} has commented on {self.post}"


class Gallery(models.Model):
    image_caption = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="galleries")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.image_caption} "


class LoginCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_logged = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} logged in at {self.date_logged}"


class Online_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_logged_in = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} just came online"


class Message(models.Model):
    chat_id = models.IntegerField(default=1)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} sent a message to {self.receiver.username}"


class MessageD(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_message_sender')
    message = models.TextField()
    read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender.username} sent a message"


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date_contacted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class ClientInfoProgress(models.Model):
    care_plan = models.CharField(max_length=20,choices=CAREPLAN_CHOICE,default="Eagle",help_text="Choose a plan for client")
    assessment_officer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    age = models.IntegerField(default=10,blank=True)
    email = models.EmailField(unique=True, max_length=255, blank=True,
                              help_text="Leave blank if client doesn't have any.")
    phone = models.CharField(max_length=20)
    emergency_phone = models.CharField(max_length=20, blank=True, help_text="Leave blank if client doesn't have any.")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    client_image = models.ImageField(upload_to="client_images", blank=True, default="client.jpg")
    next_of_kin = models.CharField(max_length=50, blank=True, help_text="Leave blank if client doesn't have any.")
    issue = models.TextField()
    progress = models.CharField(choices=LEVEL_CHOICES, max_length=30, help_text="Choose current level for your client.",
                                default="Assessment")
    assessment_phase_details = models.TextField(help_text="Enter detailed info gathered for assessment here",
                                                blank=True)
    development_phase_details = models.TextField(help_text="Enter detailed info gathered for development here",
                                                 blank=True)
    planning_phase_details = models.TextField(help_text="Enter detailed info gathered for planning here", blank=True)
    implementation_phase_details = models.TextField(help_text="Enter detailed info gathered for implementation here",
                                                    blank=True)
    evaluation_phase_details = models.TextField(help_text="Enter detailed info gathered for evaluation here",
                                                blank=True)
    star_phase_details = models.TextField(help_text="Enter detailed info gathered for star here.", blank=True)
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolut_client_url(self):
        return reverse("client_detail", args={self.pk})
