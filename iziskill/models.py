from django.db import models
from django.contrib.auth.models import AbstractUser


from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class User(AbstractUser):
    """
    Modèle personnalisé pour les utilisateurs, héritant de AbstractUser pour ajouter des champs spécifiques.
    """
    username = models.CharField(max_length=255, verbose_name="Nom d'utilisateur", unique=True)
    password = models.CharField(max_length=255, verbose_name="Mot de passe")
    status = models.CharField(
        max_length=10,
        choices=(
            ('mentor', 'Mentor'),
            ('apprenant', 'Apprenant')
        ),
        verbose_name="status")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Image de profil")
    email = models.EmailField(unique=True, verbose_name="Adresse e-mail")
    points = models.PositiveIntegerField(default=0, verbose_name="Points")  
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="Numéro de téléphone")
    occupation = models.CharField(max_length=100, blank=True, verbose_name="Profession")
    display_name = models.CharField(max_length=50, blank=True, verbose_name="Nom affiché")
    bio = models.TextField(blank=True, verbose_name="Biographie")
    facebook = models.URLField(max_length=200, blank=True, verbose_name="Profil Facebook")
    twitter = models.URLField(max_length=200, blank=True, verbose_name="Profil Twitter")
    linkedin = models.URLField(max_length=200, blank=True, verbose_name="Profil LinkedIn")
    instagram = models.URLField(max_length=200, blank=True, verbose_name="Profil Instagram")
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name="Groupes"
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set_permissions',
        blank=True,
        verbose_name="Permissions utilisateur"
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def str(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"















    





class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def str(self):
        return f"{self.user.username}'s Profile"



# Model par PRIMAEL DOHA 

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def str(self):
        return self.name



class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paniers')
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.course.title} - {self.user.username}"

    @property
    def total_price(self):
        return self.course.price * self.quantity

class Course(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('draft', 'Draft'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Statut"
    )

    # Les autres champs de votre modèle
    title = models.CharField(max_length=255, verbose_name="Titre du cours")
    description = models.TextField(verbose_name="Description")
    instructor = models.ForeignKey(User, related_name='instructed_courses', on_delete=models.SET_NULL, null=True, limit_choices_to={'status': 'mentor'})
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix du cours")
    original_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix d'origine", blank=True, null=True)
    total_points = models.PositiveIntegerField(default=0, verbose_name="Points totaux")
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    additional_info = models.TextField(verbose_name="Informations supplémentaires", blank=True)
    prerequisites = models.TextField(verbose_name="Prérequis", blank=True)
    syllabus = models.TextField(verbose_name="Syllabus", blank=True)
    duration = models.TimeField(verbose_name="Durée", blank=True, null=True)
    date = models.DateField(verbose_name="Date du cours", blank=True, null=True)
    certificat = models.BooleanField(verbose_name="Certificat", default=False)
    quiz = models.BooleanField(verbose_name="Quiz", default=False)
    language = models.CharField(max_length=100, verbose_name="Langue", blank=True)
    progress = models.IntegerField(default=0)
    lessons = models.PositiveIntegerField(default=0, verbose_name="Leçons")
    skill_level = models.CharField(
        max_length=20,
        choices=[
            ('basic', 'Basic'),
            ('intermediate', 'Intermédiaire'),
            ('advanced', 'Élevé'),
        ],
        verbose_name="Niveau de compétence",
        default='basic',
    )  # Nouveau champ avec des choix
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
    def str(self):
        return self.title
  
  
  

class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')
    order = models.PositiveIntegerField(help_text="Ordre d'affichage de la vidéo dans la playlist")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.video_file and not self.duration:
            video = VideoFileClip(self.video_file.path)
            self.duration = video.duration
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.title} ({self.course.title})"
    
class MentoringSession(models.Model):
    mentor = models.ForeignKey(User, related_name='mentoring_sessions', on_delete=models.SET_NULL, null=True, limit_choices_to={'status': 'mentor'})
    learner = models.ForeignKey(User, related_name='mentored_sessions', on_delete=models.CASCADE, limit_choices_to={'status': 'apprenant'})
    course = models.ForeignKey(Course, related_name='mentoring_sessions', on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    duration = models.DurationField(help_text="Durée de la session en heures")
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix par heure")

    def str(self):
        return f"Session de {self.mentor.username} avec {self.learner.username} pour le cours {self.course.title}"
    

class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='payments', on_delete=models.CASCADE, blank=True, null=True)
    session = models.ForeignKey(MentoringSession, related_name='payments', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)

    def str(self):
        if self.course:
            return f"Payment of {self.amount} for course {self.course.title}"
        elif self.session:
            return f"Payment of {self.amount} for mentoring session with {self.session.mentor.username}"
        return f"Payment of {self.amount} by {self.user.username}"
    


class MentoringRequest(models.Model):
    learner = models.ForeignKey(User, related_name='mentoring_requests', on_delete=models.CASCADE, limit_choices_to={'status': 'apprenant'})
    course = models.ForeignKey(Course, related_name='mentoring_requests', on_delete=models.CASCADE)
    preferred_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')

    def str(self):
        return f"Request by {self.learner.username} for mentoring in {self.course.title}"









# Modèle pour les statistiques utilisateur
class Statistic(models.Model):
    user = models.ForeignKey(User, related_name='statistics', on_delete=models.CASCADE)
    enrolled_courses = models.IntegerField(default=0)
    active_courses = models.IntegerField(default=0)
    completed_courses = models.IntegerField(default=0)
    total_students = models.PositiveIntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def update_statistics(self):
        if self.user.role == 'student':
            # Logique pour mettre à jour les statistiques des étudiants
            self.enrolled_courses = self.user.enrolled_courses.count()
            self.active_courses = self.user.enrollments.filter(active=True).count()
            self.completed_courses = self.user.certificates.count()
        elif self.user.role == 'instructor':
            # Logique pour mettre à jour les statistiques des instructeurs
            courses = self.user.instructed_courses.all()
            self.total_students = sum(course.students.count() for course in courses)
            self.total_earnings = sum(course.total_points for course in courses)
        self.save()

    def str(self):
        return f"Statistics for {self.user.username}"




# Modèle pour l'inscription aux cours
class Enrollment(models.Model):
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def str(self):
        return f"{self.user.username} enrolled in {self.course.title}"

# Modèle pour les Certificats
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='certificates', on_delete=models.CASCADE)
    issue_date = models.DateField()
    certificate_number = models.CharField(max_length=255, unique=True)

    def str(self):
        return f"Certificate {self.certificate_number} for {self.user.username}"

# Modèle pour les Commentaires et Retours sur les cours
class Feedback(models.Model):
    user = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='feedbacks', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)

    def str(self):
        return f"Feedback by {self.user.username} for {self.course.title}"

# Modèle pour les Messages
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def str(self):
        return f"Message from {self.sender.username} to {self.recipient.username}"

# Modèle pour la Liste de Souhaits (Wishlist)
class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='wishlisted_by', on_delete=models.CASCADE)

    def str(self):
        return f"{self.course.title} in wishlist of {self.user.username}"

# Modèle pour les Tentatives de Quiz
class QuizAttempt(models.Model):
    user = models.ForeignKey(User, related_name='quiz_attempts', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='quiz_attempts', on_delete=models.CASCADE)
    score = models.IntegerField()
    attempt_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Quiz attempt by {self.user.username} for {self.course.title} with score {self.score}"

# Modèle pour les Devoirs (Assignments)
class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def str(self):
        return self.title
    
    

# Modèle pour les Réglages (Settings)
class UserSetting(models.Model):
    user = models.OneToOneField(User, related_name='settings', on_delete=models.CASCADE)
    receive_notifications = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)

    def str(self):
        return f"Settings for {self.user.username}"





class InstructorDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dashboard')
    total_courses = models.PositiveIntegerField(default=0)
    active_courses = models.PositiveIntegerField(default=0)
    completed_courses = models.PositiveIntegerField(default=0)
    total_students = models.PositiveIntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def update_statistics(self):
        courses = self.user.instructed_courses.all()
        self.total_courses = courses.count()
        self.active_courses = courses.filter(status='active').count()
        self.completed_courses = courses.filter(status='completed').count()
        self.total_students = sum(course.enrolled for course in courses)
        self.total_earnings = sum(course.earnings for course in courses) if hasattr('course', 'earnings') else 0
        self.save()

    def str(self):
        return f"Dashboard for {self.user.username}"
    
    
class ClientTestimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/images/', blank=True, null=True)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.PositiveIntegerField(help_text="Note sur 5", choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.name} - {self.profession}"
    


class Award(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='awards/images/', blank=True, null=True)
    award_date = models.DateField()
    
    def str(self):
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)


    def _str_(self):
        return "Room : "+ self.name + " | Id : " + self.slug

    

class Messager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return "Message is :- "+ self.content